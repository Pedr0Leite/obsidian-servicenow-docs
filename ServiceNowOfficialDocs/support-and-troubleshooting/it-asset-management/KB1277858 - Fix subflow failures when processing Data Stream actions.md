---
title: "Fix subflow failures when processing Data Stream actions"
aliases:
  - KB1277858
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1277858
kb_number: KB1277858
last_modified: 2025-08-14
---

## Fix subflow failures when processing Data Stream actions

  

### Issue

Subflows with Data Stream actions fail and display an error message, "Cannot pause the flow while processing Data Stream action", when connections are incorrectly configured to use a MID Server. This occurs when the Data Stream action, which is not intended to use the MID server, is routed through it anyway. 

### Release

Any supported release

### Cause

The **Use MID Server** check box is selected in the connection record used by the action. This option should only be enabled when API calls must route through a MID server. 

### Resolution

1.  Go to **Connection and Credential Aliases**.
2.   Locate the alias record used by the action in the subflow.
3.  Open the alias record.
4.  In the Connections related list, open the Connection record.
5.  Clear the **Use MID Server** checkbox.  
    4\. Save the record.  
    5\. Run the affected flow or subflow again.

### Related Links

[Data Stream action design considerations](https://www.servicenow.com/docs/bundle/zurich-integrate-applications/page/administer/integrationhub/concept/data-stream-design.html)
