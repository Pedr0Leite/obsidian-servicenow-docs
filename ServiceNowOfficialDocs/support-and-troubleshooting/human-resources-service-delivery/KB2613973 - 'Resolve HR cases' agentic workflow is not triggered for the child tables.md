---
title: "'Resolve HR cases' agentic workflow is not triggered for the child tables"
aliases:
  - KB2613973
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2613973
kb_number: KB2613973
last_modified: 2025-11-14
---

## Text

When using the 'Resolve HR cases' agentic workflow, the trigger activates only for the base table configured and does not trigger for child tables.

To enable the trigger for child tables, use one of the following options:

_Option 1: Update the flow trigger configuration_

1.  Open Flow Designer
2.  Under the Flow tab, search for the flow name containing 'Resolve HR cases'
3.  Open the flow
4.  Select Trigger --> Advanced options
5.  Change When to run the flow from Run only on current table to Run on current and extended tables
6.  Publish the flow

![](/sys_attachment.do?sys_id=16f7ee0893d53210057c7de86cba10d2)

            This allows the flow to trigger for both the base and child tables.

_Option 2: Create separate triggers for each table_

1.  In the _Add triggers_ section, create a new trigger configuration for each child table
2.  Use the same conditions and fields as defined for the base table trigger

These options can be used for other agentic workflows also where the requirement is the same.
