---
title: "Configuring dictionary overrides to change default field values on extended tables"
aliases:
  - KB0538794
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538794
kb_number: KB0538794
last_modified: 2026-06-16
---

## Configuring dictionary overrides to change default field values on extended tables

  

### Issue

Dictionary Overrides allow system administrators to override field settings on extended tables. This article describes how to use this capability to change the initial state values for the incident and problem tables (both extended tables from the task table).

### Facts

### Using Dictionary Overrides

In instances, information is stored in tables, organized by parent and child tables. The incident and problem tables are both extended from the parent task table. The default state on the parent task table is **New**. On the incident table, the initial state should be **Active**. On the problem table, the initial state should be **Awaiting Review**.

For extended tables, the field settings should be changed from the default state to the correct initial state. **Dictionary Overrides** enables changes to the field attributes without affecting the task tables and their extended tables. 

### Release

All Supported Releases

### Resolution

### Using Dictionary Overrides to change field settings on extended tables.

To change the initial state on incident tables:

1.  Navigate to **Incident > Create New**.
2.  In the **State** field, open the choice list.  
    The initial state is selected as **New**.
3.  Right-click **State** and select **Personalize Dictionary**.  
    The state value is specified in the **Dictionary Entry** for this field. The state field is defined on the task table, with a default value of **1**.
4.  Go to **Choices**.  
    This displays a list of choices and corresponding values on the state fields. **Active** fields have a value of **2**.
5.  Personalize the list columns to view the table and corresponding choices:  
    -   Click the gear icon.
    -   Add **Table** to the list.
    -   Click **OK**.

The initial state is **New** because it corresponds to the default task state value of **1**. The initial state for incidents should be **Active**, with a value of **2**. Use **Dictionary Overrides** to make changes only to the table specified.

To change the default value:

1.  Navigate to **Dictionary Overrides** tab in **Related Links,** Select **New**.
2.  In the **Table** field, select **Incident**.
3.  Select **Override default value**.
4.  Enter a value of **2**.
5.  Click **Submit**.

When a new incident is opened, the initial state is now **Active** with a default value of **2**.

Use the same steps to set the initial state and values for problem tables.

### Related Links

[Dictionary Overrides](https://www.servicenow.com/docs/csh?topicname=c_DictionaryOverrides.html&version=latest " Dictionary Overrides")
