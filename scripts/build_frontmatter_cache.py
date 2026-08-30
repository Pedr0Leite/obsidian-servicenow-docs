#!/usr/bin/env python3
"""Build a cache of (path, title, description, tags) for every markdown file
under ServiceNowOfficialDocs, for use by frontmatter_search.py.

This is a NARROWING tool only: it tells you which files might be relevant.
It is not a substitute for reading the file body — always Read the winning
candidate(s) in full before answering a question from their content.

Usage: scripts/build_frontmatter_cache.py
Output: scripts/.frontmatter_cache.jsonl (one JSON object per line)
"""
import os, re, json, time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_ROOT = os.path.join(REPO_ROOT, "ServiceNowOfficialDocs")
CACHE_PATH = os.path.join(REPO_ROOT, "scripts", ".frontmatter_cache.jsonl")

FM_KEY_RE = re.compile(r'^([a-zA-Z_]+):\s*(.*)$')

def strip_quotes(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ('"', "'"):
        s = s[1:-1]
    return s

def parse_frontmatter(path):
    title = description = None
    tags = []
    in_tags = False
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            first = f.readline()
            if not first.startswith('---'):
                return None
            for line in f:
                if line.startswith('---'):
                    break
                if in_tags:
                    m = re.match(r'^\s*-\s*(.+)$', line)
                    if m:
                        tags.append(m.group(1).strip())
                        continue
                    else:
                        in_tags = False
                m = FM_KEY_RE.match(line)
                if m:
                    key, val = m.group(1), m.group(2)
                    if key == 'title' and title is None:
                        title = strip_quotes(val)
                    elif key == 'description' and description is None:
                        description = strip_quotes(val)
                    elif key == 'tags' and not val.strip():
                        in_tags = True
    except Exception:
        return None
    return title, description, tags

def main():
    start = time.time()
    count = 0
    with open(CACHE_PATH, 'w', encoding='utf-8') as out:
        for dirpath, subdirs, filenames in os.walk(DOCS_ROOT):
            for fname in filenames:
                if not fname.endswith('.md') or fname == 'INDEX.md':
                    continue
                full = os.path.join(dirpath, fname)
                parsed = parse_frontmatter(full)
                if parsed is None:
                    continue
                title, description, tags = parsed
                rel = os.path.relpath(full, REPO_ROOT)
                out.write(json.dumps({
                    "path": rel,
                    "title": title or "",
                    "description": description or "",
                    "tags": tags,
                }) + "\n")
                count += 1
    elapsed = time.time() - start
    print(f"Cached {count} files in {elapsed:.1f}s -> {CACHE_PATH}")

if __name__ == '__main__':
    main()
