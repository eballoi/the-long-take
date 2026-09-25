#!/usr/bin/env python3
"""Recompute the Content-Security-Policy hash of the inline script in index.html.

The CSP only lets the browser run the inline <script> whose SHA-256 matches the
policy, so run this after every edit to that script:

    python3 tools/update-csp.py
"""
import base64
import hashlib
import pathlib
import re
import sys

path = pathlib.Path(__file__).resolve().parent.parent / "index.html"
html = path.read_text(encoding="utf-8")

scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
if len(scripts) != 1:
    sys.exit(f"expected exactly one inline <script>, found {len(scripts)}")

digest = base64.b64encode(hashlib.sha256(scripts[0].encode("utf-8")).digest()).decode()
updated, count = re.subn(r"'sha256-[A-Za-z0-9+/=]+'", f"'sha256-{digest}'", html, count=1)
if count != 1:
    sys.exit("no 'sha256-...' source found in the Content-Security-Policy meta tag")

path.write_text(updated, encoding="utf-8")
print(f"CSP script hash updated: sha256-{digest}")
