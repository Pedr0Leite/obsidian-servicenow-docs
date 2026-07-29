---
title: "Invoking the OOTB Now Assist – Summarize feature from a custom UI Action button, or through a Flow Designer action"
aliases:
  - KB2920682
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2920682
kb_number: KB2920682
last_modified: 2026-03-27
---

## Invoking the OOTB Now Assist – Summarize feature from a custom UI Action button, or through a Flow Designer action

  

### Summary

**Query**: ServiceNow Now Assist provides an out-of-the-box (OOTB) “Summarize” feature on the Incident form that automatically generates a summary of incident details.Is it possible to invoke the OOTB Now Assist – Summarize feature from a custom UI Action button, or trigger it through a Flow Designer action?

  
The OOTB Now Assist – Summarize button itself cannot be directly invoked from a custom UI Action or called as an API. However, the same summarization capability can be triggered in a supported way by invoking the underlying Now Assist summarization skill.

You can do this using Flow Designer with the "Call Now Assist Skill" action, or through supported UI Builder patterns, to generate the incident summary and store or display the output as needed.

### Release

Yokohama
