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


def candidate_dirs():
    """Layered output dirs: MAKEFUN_OUTPUT_DIR, then /output, then cwd.

    Duplicates are dropped so each directory is only tried once.
    """
    seen = set()
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    for raw in (env_dir, "/output", str(Path.cwd())):
        if not raw:
            continue
        key = os.path.normpath(raw)
        if key not in seen:
            seen.add(key)
            dirs.append(Path(raw))
    return dirs


def main():
    if not SRC.is_file():
        print("error: source entry.png is missing: %s" % SRC,
              file=sys.stderr)
        print("error: cannot produce entry.png without the source image",
              file=sys.stderr)
        return 1
    tried = []
    dest = None
    for candidate in candidate_dirs():
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            target = candidate / "entry.png"
            shutil.copyfile(SRC, target)
            dest = target
            break
        except OSError as exc:
            tried.append("%s (%s)" % (candidate, exc))
            continue
    if dest is None:
        print("error: could not write entry.png to any output dir",
              file=sys.stderr)
        print("error: tried: %s" % "; ".join(tried), file=sys.stderr)
        return 1
    expected_size = SRC.stat().st_size
    expected_sha = sha256_of(SRC)
    actual_size = dest.stat().st_size
    if actual_size != expected_size:
        print("error: size mismatch after copy to %s: got %d bytes, "
              "expected %d bytes" % (dest, actual_size, expected_size),
              file=sys.stderr)
        return 1
    actual_sha = sha256_of(dest)
    if actual_sha != expected_sha:
        print("error: sha256 mismatch after copy to %s: got %s, "
              "expected %s" % (dest, actual_sha, expected_sha),
              file=sys.stderr)
        return 1
    print("OK entry.png -> %s (%d bytes, sha256=%s)"
          % (dest, actual_size, actual_sha))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
