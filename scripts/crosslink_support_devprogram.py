#!/usr/bin/env python3
"""Tag + cross-link support-and-troubleshooting/, servicenow-dev-program/, now-assist-ai/.

No LLM calls, no yaml dep (frontmatter is hand-parsed with regex).
Env vars: DRY_RUN=1, MAX_FILES=N
"""
import os
import re
import sys

VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_ROOT = os.path.join(VAULT_ROOT, "ServiceNowOfficialDocs")
ROOTS = ["support-and-troubleshooting", "servicenow-dev-program", "now-assist-ai"]

STOPLIST = {"servicenow", "support-kb", "kb", "code-snippet", "servicenow-dev-program"}

DRY_RUN = os.environ.get("DRY_RUN") == "1"
MAX_FILES = int(os.environ.get("MAX_FILES", "0")) or None

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
RELATED_RE = re.compile(r"\n## Related Notes\n.*?(?=\n## |\Z)", re.DOTALL)

NOW_ASSIST_TOPICS = {
    "AI Agents Knowledge Base.md": ["ai-agents", "react-loop", "now-assist-ai"],
    "Get Similar Records AIS Script Documentation.md": ["ai-search", "semantic-search", "now-assist-ai"],
    "ServiceNow_Local_Development_Guide.md": ["local-development", "servicenow-sdk", "now-assist-ai"],
}


def kebab(s):
    s = re.sub(r"[_\s]+", "-", s.strip())
    s = re.sub(r"[^a-zA-Z0-9-]", "", s)
    return s.lower()


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text, 0
    raw = m.group(1)
    fm = {"title": None, "aliases": [], "tags": [], "extra": []}
    lines = raw.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        km = re.match(r"^(\w+):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            if key == "title":
                fm["title"] = val.strip('"').strip("'")
                i += 1
                continue
            if key in ("aliases", "tags") and not val:
                items = []
                j = i + 1
                while j < len(lines) and re.match(r"^\s*-\s*(.+)$", lines[j]):
                    items.append(re.match(r"^\s*-\s*(.+)$", lines[j]).group(1).strip())
                    j += 1
                fm[key] = items
                i = j
                continue
            # any other scalar key (source_url, kb_number, last_modified, area, ...)
            fm["extra"].append((key, val))
            i += 1
            continue
        i += 1
    body = text[m.end():]
    return fm, body, m.end()


def find_h1(text):
    m = H1_RE.search(text)
    return m.group(1).strip() if m else None


def derive_dev_program_tags(path):
    rel = os.path.relpath(path, os.path.join(DOCS_ROOT, "servicenow-dev-program"))
    parts = rel.split(os.sep)
    tags = ["servicenow-dev-program", "code-snippet"]
    if len(parts) >= 2:
        tags.append(kebab(parts[-2]))
    if len(parts) >= 3:
        tags.append(kebab(parts[-3]))
    seen = []
    for t in tags:
        if t and t not in seen:
            seen.append(t)
    return seen


def derive_aliases(path, h1):
    base = os.path.splitext(os.path.basename(path))[0]
    if base.lower() == "readme":
        return [os.path.basename(os.path.dirname(path))]
    if h1:
        return [h1]
    return [base]


def build_frontmatter(fm):
    lines = ["---"]
    if fm.get("title"):
        lines.append(f'title: "{fm["title"]}"')
    if fm.get("aliases"):
        lines.append("aliases:")
        for a in fm["aliases"]:
            lines.append(f"  - {a}")
    if fm.get("tags"):
        lines.append("tags:")
        for t in fm["tags"]:
            lines.append(f"  - {t}")
    for k, v in fm.get("extra", []):
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def load_all_files():
    files = []
    for root_name in ROOTS:
        root_path = os.path.join(DOCS_ROOT, root_name)
        if not os.path.isdir(root_path):
            continue
        for dirpath, _, filenames in os.walk(root_path):
            for fn in filenames:
                if fn.endswith(".md"):
                    files.append(os.path.join(dirpath, fn))
    files.sort()
    if MAX_FILES:
        files = files[:MAX_FILES]
    return files


def process_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    fm, body, _ = parse_frontmatter(text)
    injected = False

    if fm is None:
        h1 = find_h1(text)
        aliases = derive_aliases(path, h1)
        rel_to_root = os.path.relpath(path, DOCS_ROOT)
        if rel_to_root.startswith("servicenow-dev-program"):
            tags = derive_dev_program_tags(path)
        elif rel_to_root.startswith("now-assist-ai"):
            tags = NOW_ASSIST_TOPICS.get(os.path.basename(path), ["now-assist-ai"])
        else:
            tags = []
        fm = {"title": aliases[0], "aliases": aliases, "tags": tags}
        body = text
        injected = True

    return fm, body, injected


def vault_rel_no_ext(path):
    rel = os.path.relpath(path, VAULT_ROOT)
    return rel[:-3] if rel.endswith(".md") else rel


def display_title(fm):
    if fm.get("title"):
        return fm["title"]
    if fm.get("aliases"):
        return fm["aliases"][0]
    return None


def main():
    files = load_all_files()
    print(f"Found {len(files)} files to process (MAX_FILES={MAX_FILES}, DRY_RUN={DRY_RUN})")

    parsed = {}
    for path in files:
        fm, body, injected = process_file(path)
        parsed[path] = {"fm": fm, "body": body, "injected": injected}

    tag_index = {}
    for path, info in parsed.items():
        for t in info["fm"].get("tags", []):
            if t in STOPLIST:
                continue
            tag_index.setdefault(t, set()).add(path)

    file_tags = {
        path: set(t for t in info["fm"].get("tags", []) if t not in STOPLIST)
        for path, info in parsed.items()
    }

    changed = 0
    updated_zero_links = 0
    total_links = 0

    for path, info in parsed.items():
        fm, body = info["fm"], info["body"]
        my_tags = file_tags[path]

        scores = {}
        if my_tags:
            for t in my_tags:
                for other in tag_index.get(t, ()):
                    if other == path:
                        continue
                    scores[other] = scores.get(other, 0) + 1

        ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
        top = [p for p, s in ranked if s >= 1][:6]

        links_md = None
        if top:
            link_lines = ["", "## Related Notes", ""]
            for other in top:
                target = vault_rel_no_ext(other)
                title = display_title(parsed[other]["fm"]) or os.path.splitext(os.path.basename(other))[0]
                link_lines.append(f"- [[{target}|{title}]]")
            links_md = "\n".join(link_lines) + "\n"
            total_links += len(top)
        else:
            updated_zero_links += 1

        new_body = RELATED_RE.sub("", body).rstrip("\n") + "\n"
        if links_md:
            new_body = new_body.rstrip("\n") + "\n" + links_md

        if fm:
            new_text = build_frontmatter(fm) + "\n" + new_body.lstrip("\n")
        else:
            new_text = new_body

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            original = f.read()

        if new_text != original:
            changed += 1
            if not DRY_RUN:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_text)

    print(f"Changed: {changed}, files with 0 related links: {updated_zero_links}, total wikilinks added: {total_links}")

    if DRY_RUN:
        sample_kb = next((p for p in files if "support-and-troubleshooting" in p), None)
        sample_dev = next((p for p in files if "servicenow-dev-program" in p and os.path.basename(p).lower() == "readme.md"), None)
        for label, p in [("KB article", sample_kb), ("dev-program readme", sample_dev)]:
            if not p:
                continue
            fm, body = parsed[p]["fm"], parsed[p]["body"]
            new_body = RELATED_RE.sub("", body).rstrip("\n") + "\n"
            print(f"\n=== {label}: {p} ===")
            print(build_frontmatter(fm) if fm else "(no frontmatter)")
            print("... body omitted ...")


if __name__ == "__main__":
    main()
