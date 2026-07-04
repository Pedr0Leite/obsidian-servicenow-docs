---
title: "Service Mapping Incorrectly Identifies a Service Due to Run Order of the Patterns"
aliases:
  - KB0622477
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622477
kb_number: KB0622477
last_modified: 2024-04-07
---

## Service Mapping Incorrectly Identifies a Service Due to Run Order of the Patterns

  

### Issue

Service Mapping identifies a service incorrectly because the service matches the identification settings for two different service definitions. For example, both IIS and MS Exchange applications have an HTTP entry point. However, MS Exchange uses some of the components of IIS. Therefore, if the IIS pattern ran first, the discovery might incorrectly identify MS Exchange as IIS. To prevent this error, in the Run Order field in the MS Exchange pattern definition, select Before and IIS.

### Cause

The **Run order** field of a **Pattern** is not normally set. However, “before” or “after” should be used if there is any similarity or dependency between two patterns. In that case, you need to set the run order to either before or after.

### Resolution

Select the order in which this pattern always runs.

Before

After

Select the other applicable pattern.

This field is relevant only if a particular pattern might be confused with another pattern.

![](sys_attachment.do?sys_id=8e4de4a2db82b450e515c223059619d5)
