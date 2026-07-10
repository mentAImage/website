"""
Adds favicon link + lang-switch.js to all HTML pages.
Also adds id="francais" to the lang-section div in story pages.
Safe to re-run (skips if already patched).
"""
import os, re

BASE = r"C:\Users\Saber\mentAImage-website-deploy"

FAVICON = '<link rel="icon" href="/favicon.svg" type="image/svg+xml" />'
LANG_SCRIPT = '  <script src="/lang-switch.js"></script>'

# Directories to skip
SKIP_DIRS = {'.git', 'stories', '__pycache__'}

# Story slug dirs (need id="francais" on lang-section)
STORY_SLUGS = {
    "the-heart-of-advocacy-stevens-story-of-faith-resilience-and-inclusion",
    "special-in-the-best-possible-way-amrritas-story",
    "finding-clarity-turning-a-dyslexia-journey-into-a-blueprint-for-change",
    "listening-for-the-voices-we-miss-deborahs-journey",
    "shifting-the-default-gillian-on-disability-justice-and-workplace-change",
    "respecting-limits-hannelores-journey-toward-sustainable-work",
    "balancing-innovation-and-burnout-jons-story",
    "from-burnout-to-belonging-kellys-journey-with-neurodivergence",
    "it-was-just-too-much-louises-journey-to-finding-a-workplace-that-works",
    "a-diagnosis-in-progress-manshuk-on-neurodiversity-and-entrepreneurship",
    "they-finally-saw-me-marisas-journey-with-neurodivergence",
    "beyond-equality-nat-on-neurodiversity-and-equity-at-work",
    "from-rigidity-to-realization-pauls-path-as-a-late-diagnosed-autistic-professional",
    "from-burnout-to-advocacy-for-neuroinclusion-rogers-story",
    "meeting-people-where-they-are-roberts-journey-as-a-neurodivergent-therapist",
    "living-through-passion-sydneys-journey-toward-authenticity-and-inclusion",
    "vs-path-to-leadership-courage-community-and-change",
}

patched = 0

for root, dirs, files in os.walk(BASE):
    # Prune skip dirs
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, encoding='utf-8') as f:
            content = f.read()

        changed = False

        # 1. Add favicon if missing
        if FAVICON not in content:
            content = content.replace(
                '<link rel="stylesheet" href="/shared.css" />',
                f'{FAVICON}\n  <link rel="stylesheet" href="/shared.css" />'
            )
            # Fallback: insert before </head>
            if FAVICON not in content:
                content = content.replace('</head>', f'  {FAVICON}\n</head>')
            changed = True

        # 2. Add lang-switch script if missing
        if 'lang-switch.js' not in content:
            content = content.replace('</body>', f'{LANG_SCRIPT}\n</body>')
            changed = True

        # 3. Add id="francais" to lang-section in story pages
        rel = os.path.relpath(root, BASE)
        top_dir = rel.split(os.sep)[0]
        if top_dir in STORY_SLUGS:
            if 'id="francais"' not in content:
                content = content.replace(
                    '<div class="lang-section">',
                    '<div class="lang-section" id="francais">'
                )
                changed = True

        if changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Patched: {os.path.relpath(fpath, BASE)}")
            patched += 1

print(f"\nDone. {patched} files patched.")
