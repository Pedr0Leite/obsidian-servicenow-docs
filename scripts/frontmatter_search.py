#!/usr/bin/env python3
"""Fast keyword search over cached frontmatter (title/description/tags) for
ServiceNowOfficialDocs. NARROWING TOOL ONLY: use this to find candidate
files fast and cheap, then Read the winning file(s) in full before answering
a question — the description here is a 1-2 sentence summary, not the content.

Usage: scripts/frontmatter_search.py <query words...> [--limit N]

Rebuild the cache first if it's missing or stale:
  scripts/build_frontmatter_cache.py
"""
import os, sys, json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_PATH = os.path.join(REPO_ROOT, "scripts", ".frontmatter_cache.jsonl")

def load_cache():
    if not os.path.exists(CACHE_PATH):
        print("No cache found. Run scripts/build_frontmatter_cache.py first.")
        sys.exit(1)
    with open(CACHE_PATH, encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def score(entry, terms):
    title = entry["title"].lower()
    desc = entry["description"].lower()
    tags = " ".join(entry["tags"]).lower()
    path = entry["path"].lower()

    s = 0
    for t in terms:
        hit = 0
        if t in title:
            hit += 3
        if t in tags:
            hit += 2
        if t in desc:
            hit += 1
        if t in path:
            hit += 1
        if hit == 0:
            return 0  # AND semantics: every term must match somewhere
        s += hit
    return s

def main():
    args = sys.argv[1:]
    limit = 20
    if '--limit' in args:
        i = args.index('--limit')
        limit = int(args[i + 1])
        del args[i:i + 2]
    if not args:
        print(__doc__)
        sys.exit(1)
    terms = [a.lower() for a in args]

    entries = load_cache()
    scored = [(score(e, terms), e) for e in entries]
    scored = [x for x in scored if x[0] > 0]
    scored.sort(key=lambda x: -x[0])

    if not scored:
        print(f"No matches for: {' '.join(args)}")
        return

    for sc, e in scored[:limit]:
        print(f"[{sc}] {e['path']}")
        print(f"     {e['title']}")
        if e['description']:
            print(f"     {e['description'][:160]}")
        print()

    print(f"({len(scored)} total matches, showing top {min(limit, len(scored))}. "
          f"Read the file(s) before answering — this is title/description only.)")

if __name__ == '__main__':
    main()
