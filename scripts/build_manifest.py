#!/usr/bin/env python3
"""Build the top-level SHA-256 manifest without hashing the manifest itself."""
from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "MANIFEST.sha256"


def main() -> None:
    files = sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path != OUTPUT
        and ".git" not in path.relative_to(ROOT).parts
        and "__pycache__" not in path.relative_to(ROOT).parts
    )
    lines = [
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}"
        for path in files
    ]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="ascii")
    print(f"WROTE {OUTPUT.name} ({len(lines)} files)")


if __name__ == "__main__":
    main()
