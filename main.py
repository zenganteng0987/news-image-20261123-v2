#!/usr/bin/env python3
"""THE DAILY ATLAS -- Monday 23 November 2026.

make.fun bounty news-image-20261123, entry V2.
Entrypoint: copies the pre-rendered entry.png into the grader output
directory and verifies the copy by size and SHA-256.

Standard library only. No network access, no writes into this repo folder.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    dest = None
    for candidate in (Path(wanted), Path.cwd()):
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            target = candidate / "entry.png"
            shutil.copyfile(SRC, target)
            dest = target
            break
        except OSError:
            continue
    if dest is None:
        print("error: could not write entry.png to any output dir",
              file=sys.stderr)
        return 1
    if dest.stat().st_size != SRC.stat().st_size:
        print("error: size mismatch after copy", file=sys.stderr)
        return 1
    if sha256_of(dest) != sha256_of(SRC):
        print("error: sha256 mismatch after copy", file=sys.stderr)
        return 1
    print("OK entry.png -> %s (%d bytes, sha256=%s)"
          % (dest, dest.stat().st_size, sha256_of(dest)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
