#!/usr/bin/env python3
"""
Clean up TBL_src_clean Blueprint-node pages that print the node name twice: an
`## Node Name` heading immediately followed by the same text as a plain line, e.g.

    ## Add Unchecked Level Up Result
    Add Unchecked Level Up Result
    ![[../img/nd_img_AddUncheckedLevelUpResult.png]]

This removes the duplicate plain-text line (only when it exactly matches the
heading text, so it's safe and idempotent — re-running does nothing).

Usage:
    python3 scripts/clean_node_titles.py [--dir docs/TBL_src_clean] [--dry-run]
"""
import argparse
import glob
import os

DEFAULT_DIR = "docs/TBL_src_clean"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=DEFAULT_DIR)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    changed = 0
    for path in glob.glob(os.path.join(args.dir, "*", "nodes", "*.md")):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        lines = text.splitlines(keepends=True)
        # find first heading line
        hi = next((i for i, ln in enumerate(lines) if ln.lstrip().startswith("## ")), None)
        if hi is None or hi + 1 >= len(lines):
            continue
        title = lines[hi].lstrip()[3:].strip()
        if lines[hi + 1].strip() == title and title:
            del lines[hi + 1]
            if not args.dry_run:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write("".join(lines))
            changed += 1
    verb = "would clean" if args.dry_run else "cleaned"
    print(f"{verb} {changed} node pages")


if __name__ == "__main__":
    main()
