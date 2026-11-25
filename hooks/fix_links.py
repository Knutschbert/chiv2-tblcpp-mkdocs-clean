"""
MkDocs build-time hook: fix links that are valid in the Obsidian vault but break
in the MkDocs/web build. Source files are left untouched (they must stay
Obsidian-correct); everything here runs only at build time, before the roamlinks
plugin.

Fixes three things that generated the bulk of the build warnings:

1. Obsidian image embeds  ![[../img/foo.png]]  ->  ![](../img/foo.png)
   (roamlinks mangles the relative path inside [[...]]; a plain Markdown image
   resolves correctly and roamlinks ignores it).

2. Absolute vault links   [x](/docs/SDK/.../classFoo.md)  ->  relative link
   (the leading /docs is the Obsidian vault root; on the site it 404s).

3. Prefix-omitted cross-refs  [[ATBLCharacter]]  ->  link to classATBLCharacter.md
   (doxygen refs drop the class/struct/namespace filename prefix, so roamlinks
   can't match them). Resolved via a one-time filename index.

Truly page-less cross-refs (engine symbols with no page here) remain; their
roamlinks "unable to find" warnings are filtered out, since they are inherent to
generated API docs and not fixable in this doc set.
"""
import logging
import os
import re

import mkdocs.plugins

log = logging.getLogger("mkdocs.hooks.fix_links")

# --- suppress roamlinks "unable to find" noise (generated, page-less refs) ----
class _DropUnableToFind(logging.Filter):
    def filter(self, record):
        return "unable to find" not in record.getMessage()

_f = _DropUnableToFind()
for _n in ("mkdocs.plugins.mkdocs_roamlinks_plugin.plugin",
           "mkdocs.plugins.mkdocs_roamlinks_plugin"):
    logging.getLogger(_n).addFilter(_f)
for _h in logging.getLogger("mkdocs").handlers:
    _h.addFilter(_f)

# --- filename index for prefix-aware cross-ref resolution ---------------------
_FILE_PREFIXES = ("class", "struct", "namespace", "interface", "union", "group", "dir")
_UE_PREFIX = re.compile(r"^[AUFEIST](?=[A-Z])")

_index = None          # simplified-key -> docs-relative posix path
_ambiguous = set()


def _simplify(name):
    return re.sub(r"[\-_ ]", "", name.lower()).replace(".md", "")


def _add(key, path):
    k = _simplify(key)
    if not k:
        return
    if k in _index and _index[k] != path:
        _ambiguous.add(k)
    else:
        _index[k] = path


def _build_index(docs_dir):
    global _index, _ambiguous
    _index, _ambiguous = {}, set()
    for root, _dirs, files in os.walk(docs_dir):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), docs_dir).replace(os.sep, "/")
            stem = fn[:-3]
            _add(stem, rel)
            sym = stem
            for p in _FILE_PREFIXES:
                if stem.startswith(p) and len(stem) > len(p) and stem[len(p)].isupper():
                    sym = stem[len(p):]
                    break
            if sym != stem:
                _add(sym, rel)                       # ATBLCharacter -> classATBLCharacter.md
                stripped = _UE_PREFIX.sub("", sym)
                if stripped != sym:
                    _add(stripped, rel)              # TBLCharacter  -> classATBLCharacter.md
    for k in _ambiguous:
        _index.pop(k, None)
    log.info("fix_links: indexed %d reference pages (%d ambiguous dropped)",
             len(_index), len(_ambiguous))


def on_config(config, **kwargs):
    _build_index(config["docs_dir"])
    return config


# --- transforms ---------------------------------------------------------------
_CODE_RE = re.compile(r"(```.*?```|~~~.*?~~~|``.+?``|`[^`\n]*`)", re.S)
_IMG_EMBED_RE = re.compile(r"!\[\[\s*([^\]|]+?\.(?:png|jpe?g|gif|svg|webp))\s*\]\]", re.I)
_ABS_LINK_RE = re.compile(r"\]\(\s*/docs/([^)\s]+?)\s*\)")
_WIKI_RE = re.compile(
    r"(?<!!)\[\[\s*(?P<name>[^\]|#]+?)\s*"
    r"(?:#(?P<frag>[^\]|]+?))?\s*"
    r"(?:\|\s*(?P<alias>[^\]]+?)\s*)?\]\]"
)


def _rel(from_src, to_src):
    rel = os.path.relpath(to_src, os.path.dirname(from_src)).replace(os.sep, "/")
    return rel


def _transform(md, page_src):
    # 1) image embeds -> markdown images
    md = _IMG_EMBED_RE.sub(lambda m: "![](" + m.group(1).strip() + ")", md)

    # 2) absolute /docs/... links -> relative to this page
    def abs_repl(m):
        target = m.group(1)
        return "](" + _rel(page_src, target) + ")"
    md = _ABS_LINK_RE.sub(abs_repl, md)

    # 3) prefix-omitted [[Symbol]] cross-refs -> relative link (only if resolvable)
    def wiki_repl(m):
        name = m.group("name").strip()
        if "/" in name or "." in name:        # a path/file wikilink: leave for roamlinks
            return m.group(0)
        target = _index.get(_simplify(name)) if _index else None
        if not target:
            return m.group(0)                  # unresolved: leave (roamlinks warns, filtered)
        link = _rel(page_src, target)
        if m.group("frag"):
            anchor = re.sub(r"[^\w一-鿿\- ]", "", m.group("frag").strip().lower())
            anchor = re.sub(r" +", "-", anchor)
            link += "#" + anchor
        text = m.group("alias") or name
        return f"[{text}](<{link}>)"
    md = _WIKI_RE.sub(wiki_repl, md)
    return md


@mkdocs.plugins.event_priority(100)  # before roamlinks (priority 0)
def on_page_markdown(markdown, page=None, config=None, files=None, **kwargs):
    page_src = page.file.src_path.replace(os.sep, "/")
    parts = _CODE_RE.split(markdown)
    for i in range(0, len(parts), 2):          # skip code regions (odd indices)
        parts[i] = _transform(parts[i], page_src)
    return "".join(parts)
