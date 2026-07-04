---
title: "Flow Designer: In Look Up Records the Order By field disappears when you publish the Flow"
aliases:
  - KB0860640
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860640
kb_number: KB0860640
last_modified: 2024-04-08
---

## Flow Designer: In Look Up Records the Order By field disappears when you publish the Flow

  

### Issue

On the Look Up Records action, the Order By field disappears when you publish the flow. This only happens when the com.em-alert-mgmt-content plugin is enabled. 

### Cause

The com.em-alert-mgmt-content plugin has a copy of the Look up Records action that is causing a conflict.Designer-UI. This has been identified as PRB1414023.

### Resolution

The PRB will be addressed. As a workaround you can import the correct version of the look-up record attached to this article.
