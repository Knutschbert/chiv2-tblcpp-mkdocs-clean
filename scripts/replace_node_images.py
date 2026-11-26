#!/usr/bin/env python3
"""
Replace the TBL_src_clean Blueprint-node images with higher-quality ones from a
KantanDocGen export. Both trees use the same layout (<Class>/img/nd_img_*.png) and
identical filenames, so this mirrors every PNG from --src into docs/TBL_src_clean,
overwriting existing images and adding any that were missing.

Re-runnable: safe to run again after a fresh export.

Usage:
    python3 scripts/replace_node_images.py \
        [--src /mnt/u/Unchained/SDK/ArgonSDK/Intermediate_/KantanDocGen/TBL_Base_Cpp] \
        [--dst docs/TBL_src_clean]
"""
import argparse
import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor

DEFAULT_SRC = "/mnt/u/Unchained/SDK/ArgonSDK/Intermediate_/KantanDocGen/TBL_Base_Cpp"
DEFAULT_DST = "docs/TBL_src_clean"


def _copy_one(job):
    src, dst = job
    existed = os.path.exists(dst)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    return existed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=DEFAULT_SRC)
    ap.add_argument("--dst", default=DEFAULT_DST)
    ap.add_argument("--workers", type=int, default=32,
                    help="parallel copy threads (I/O-bound cross-mount copy benefits from a high count)")
    args = ap.parse_args()

    if not os.path.isdir(args.src):
        sys.exit(f"source image dir not found: {args.src}")
    if not os.path.isdir(args.dst):
        sys.exit(f"destination dir not found: {args.dst}")

    jobs = []
    for root, _dirs, files in os.walk(args.src):
        for fn in files:
            if fn.lower().endswith(".png"):
                src = os.path.join(root, fn)
                rel = os.path.relpath(src, args.src)
                jobs.append((src, os.path.join(args.dst, rel)))

    # I/O-bound: copyfile releases the GIL during the read/write, so threads
    # overlap the per-file latency of the cross-filesystem mount.
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        results = list(ex.map(_copy_one, jobs))
    replaced = sum(1 for r in results if r)
    added = len(results) - replaced
    print(f"images replaced: {replaced}, added (were missing): {added} "
          f"({len(jobs)} total, {args.workers} threads)")


if __name__ == "__main__":
    main()
