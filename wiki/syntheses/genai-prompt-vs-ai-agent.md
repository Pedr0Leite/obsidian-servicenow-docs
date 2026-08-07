---
aliases: [GenAI Prompt vs AI Agent, Flat Prompt vs ReAct]
area: synthesis
tags: [synthesis, genai, ai-agents, architecture]
---
Non-obvious architectural decision: when a GenAI call should stay a flat single prompt rather than escalating to a ReAct AI Agent loop.

Seen in: `obsidian-servicenow-docs` (design of [[sn-instance-scan]], 2026-07-14)

## The pattern
| Flat GenAI prompt | ReAct AI Agent |
|---|---|
| Single call, structured output | Multi-step loop with tool calls |
| Simpler, predictable latency | Autonomous investigation across steps |
| Sufficient for analysis/summarization of already-fetched data | Needed when the AI must decide what to fetch next |

## The decision rule
Default to a flat prompt. Escalate to an AI Agent only if the task genuinely requires the model to autonomously plan and execute multi-step investigation — i.e., when you can't pre-fetch the relevant data before the prompt.

In [[sn-instance-scan]]: the scanner fetches instance data first (Script Includes), then passes a structured payload to GenAI for analysis. The AI never needs to call tools mid-reasoning, so a flat prompt is correct.

## Sources
- [[raw/sessions/2026-07-14#Session 12:02 — obsidian-servicenow-docs]]
- [[ai-agents]] — ReAct loop mechanics and when it's warranted

## Related
- [[ai-agents]]
- [[sn-instance-scan]]
- [[wiki/index|Wiki Index]]
