---
title: "OOTB SaaS License Management reclamation workflow fails with plugin inactive message due to outdated plugin check in workflow script"
aliases:
  - KB2732850
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2732850
kb_number: KB2732850
last_modified: 2026-01-22
---

## Issue

→ When enabling or running the OOTB reclamation workflow, the workflow stops with a message stating the SAM SaaS License Management Integrations plugin is inactive even though the plugin is installed and active

## Resolution

→ Check upgrade history for the workflow sys id 07d41b57671222007d59cbb35685ef8b  
→ Use sys\_update\_version to locate the update record for 07d41b57671222007d59cbb35685ef8b  
→ Revert the workflow script update back to the OOB version  
→ Re-enable and re-test the OOTB reclamation workflow and confirm the plugin inactive message no longer appears
