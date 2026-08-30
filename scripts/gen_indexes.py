#!/usr/bin/env python3
"""Generate a per-file INDEX.md for every leaf directory under ServiceNowOfficialDocs
that has more than THRESHOLD markdown files. Safe to re-run any time; each run
rewrites the INDEX.md for every qualifying directory found at that moment.

Usage:
  scripts/gen_indexes.py                  # auto-discover leaf dirs with >100 .md files
  scripts/gen_indexes.py --threshold 50    # use a different threshold
"""
import os, re, sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_ROOT = os.path.join(REPO_ROOT, "ServiceNowOfficialDocs")
THRESHOLD = 100

FM_KEY_RE = re.compile(r'^([a-zA-Z_]+):\s*(.*)$')

def strip_quotes(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ('"', "'"):
        s = s[1:-1]
    return s

def humanize(filename):
    name = os.path.splitext(filename)[0]
    name = re.sub(r'[-_]+', ' ', name)
    return name.strip().capitalize()

def parse_frontmatter(path):
    title = None
    description = None
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            first = f.readline()
            if not first.startswith('---'):
                return None, None
            for line in f:
                if line.startswith('---'):
                    break
                m = FM_KEY_RE.match(line)
                if m:
                    key, val = m.group(1), m.group(2)
                    if key == 'title' and title is None:
                        title = strip_quotes(val)
                    elif key == 'description' and description is None:
                        description = strip_quotes(val)
    except Exception:
        pass
    return title, description

def truncate(text, limit=140):
    if not text:
        return ""
    text = text.replace('\n', ' ').replace('|', '/').strip()
    text = re.sub(r'\\([\[\]()])', r'\1', text)
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(' ', 1)[0]
    return cut + "…"

def build_index(dirpath):
    files = sorted(f for f in os.listdir(dirpath) if f.endswith('.md') and f != 'INDEX.md')
    rows = []
    for fname in files:
        full = os.path.join(dirpath, fname)
        title, desc = parse_frontmatter(full)
        if not title:
            title = humanize(fname)
        rows.append((fname, title, truncate(desc)))

    rel = os.path.relpath(dirpath, REPO_ROOT)
    lines = []
    lines.append(f"# {rel} — File Index\n")
    lines.append(f"Navigation index for AI agents. One row per file in this directory ({len(rows)} files). Auto-generated from frontmatter — do not hand-edit; regenerate via `scripts/gen_indexes.py` if files are added/removed.\n")
    lines.append("---\n")
    lines.append("| File | Title | Description |")
    lines.append("|------|-------|-------------|")
    for fname, title, desc in rows:
        title = title.replace('|', '/')
        lines.append(f"| `{fname}` | {title} | {desc} |")
    lines.append("")
    out_path = os.path.join(dirpath, "INDEX.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    return len(rows), out_path

def find_qualifying_dirs(threshold):
    dirs = []
    for dirpath, subdirs, filenames in os.walk(DOCS_ROOT):
        if subdirs:
            continue  # only leaf dirs
        n = sum(1 for f in filenames if f.endswith('.md') and f != 'INDEX.md')
        if n > threshold:
            dirs.append(dirpath)
    return dirs

def main():
    threshold = THRESHOLD
    if '--threshold' in sys.argv:
        threshold = int(sys.argv[sys.argv.index('--threshold') + 1])

    dirs = find_qualifying_dirs(threshold)
    total = 0
    generated = []
    for full_dir in dirs:
        n, out_path = build_index(full_dir)
        total += n
        generated.append((os.path.relpath(full_dir, REPO_ROOT), n, out_path))

    print(f"Generated {len(generated)} indexes covering {total} files (threshold: >{threshold} files)")
    for rel, n, out_path in sorted(generated, key=lambda x: -x[1]):
        print(f"{n}\t{rel}")

if __name__ == '__main__':
    main()
