---
title: "[Agentic workflow troubleshooting] OOTB Agentic workflow \"Resolve noncritical HR cases\" doesn't update the Case work note"
aliases:
  - KB2948484
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2948484
kb_number: KB2948484
last_modified: 2026-04-09
---

## \[Agentic workflow troubleshooting\] OOTB Agentic workflow "Resolve noncritical HR cases" doesn't update the Case work note

  

### Issue

\[Agentic workflow troubleshooting\] OOTB Agentic workflow "Resolve noncritical HR cases" doesn't update the Case work note.

### Symptoms

Trigger the Agentic workflow, it fires an event but doesn't update the case work note.

![](/sys_attachment.do?sys_id=aeaf4f1793cc0f18f538fb2d6cba103e "c1.png")

### Release

Zurich

### Cause

**Agentic workflow details:**

\- There are two AI Agents in the Agentic Workflow "Resolve noncritical HR cases" which are "HR criticality detection AI agent" and "HR search and notify AI agent".

\- In AI Agent "HR criticality detection AI agent", it will update the case work note when The case has been classified as 'Critical' by this agent, AND The caller/task explicitly requests a work note update.

![](/sys_attachment.do?sys_id=f8acc31b930c0f18f538fb2d6cba102b "c2.png")

\- In AI Agent "HR search and notify AI agent", it will update the case work note when there is no related Catalog Items and KBs.

![](/sys_attachment.do?sys_id=e73d4b13934c0f18f538fb2d6cba105a "c3.png")

**Agentic workflow execution plan:**

\- Checking the execution plan, the case is identified as noncritical by Agent. It goes to the next AI Agent "HR search and notify AI agent" directly.

![](/sys_attachment.do?sys_id=13ddcb1b934c0f18f538fb2d6cba100f "c4.png")

\- In the AI Agent "HR search and notify AI agent", there are related Catalog Items and KBs, the Agent fires an event to send out this information to the case requester according to the AI Agent steps.

![](/sys_attachment.do?sys_id=acfe8f9b938c0f18f538fb2d6cba10a1 "c5.png")

\- Case requester can use related Catalog Items and KBs for the case resolution. 

### Resolution

It is working as expected.

The same can be found in the document [Resolve noncritical HR cases agentic workflow](https://www.servicenow.com/docs/r/zurich/employee-service-management/now-assist-for-hrsd/employee-issue-resolver-na.html)

![](/sys_attachment.do?sys_id=b06f4b1393cc0f18f538fb2d6cba10f0 "c6.png")
