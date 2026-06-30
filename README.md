# obsidian-servicenow-docs

Obsidian vault and AI-navigable knowledge base for ServiceNow platform development.

Combines official ServiceNow product documentation (~46,000 files) with custom curated notes from labs, support cases, and production experience.

## Getting Started

**`INDEX.md`** is the master navigation file. It maps every directory in the vault to a description and keyword set — use it to find the right area before diving into files.

**`now-assist-ai/llms.txt`** is the LLM-optimized index for the custom knowledge section.

## Structure

```
obsidian-servicenow-docs/
├── INDEX.md                        # Master navigation index
├── CLAUDE.md                       # Instructions for AI agents
├── README.md                       # This file
│
├── now-assist-ai/                  # Custom knowledge (labs, cases, production)
│   ├── llms.txt                    # LLM index for this section
│   ├── llms_template.txt           # Template for new entries
│   ├── ai-agents/                  # AI Agent debugging & best practices
│   └── ai-search/                  # AI Search (AIS) behavior & tuning
│
└── markdown/                       # Official ServiceNow documentation
    └── <50 product areas>/         # ~46k markdown files
```

## Adding Notes

1. Create a note under `now-assist-ai/<topic>/`
2. Add an entry to `now-assist-ai/llms.txt` (copy the pattern from `llms_template.txt`)
3. If a new topic area, add a row to `INDEX.md`
