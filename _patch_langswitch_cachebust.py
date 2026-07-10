"""Replaces old lang-switch script tag with cache-busted version in all HTML files."""
import os

BASE = r"C:\Users\Saber\mentAImage-website-deploy"
SKIP_DIRS = {'.git', 'stories', '__pycache__'}
OLD = '<script src="/lang-switch.js"></script>'
NEW = '<script src="/lang-switch.js?v=2"></script>'

patched = 0
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, encoding='utf-8') as f:
            content = f.read()
        if OLD in content:
            content = content.replace(OLD, NEW)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Patched: {os.path.relpath(fpath, BASE)}")
            patched += 1

print(f"\nDone. {patched} files patched.")
