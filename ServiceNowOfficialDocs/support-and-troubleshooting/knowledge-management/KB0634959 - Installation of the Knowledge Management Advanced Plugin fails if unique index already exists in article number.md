---
title: "Installation of the Knowledge Management Advanced Plugin fails if unique index already exists in article number"
aliases:
  - KB0634959
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634959
kb_number: KB0634959
last_modified: 2026-01-14
---

## Installation of the Knowledge Management Advanced Plugin fails if unique index already exists in article number

  

### Issue

Installing the Knowledge Management Advanced plugin fails if a unique index on an article number field already exists. 

### Symptoms

-   Example of error message in the installed plugins activation details for "Knowledge Management Advanced Installer":

```
21-11-2025 07:41:46 Error Knowledge Advanced installation failed - Unique database index found on the number field. Please contact ServiceNow support to resolve this issue. Knowledge Management Advanced Installer
21-11-2025 07:41:46 Error Unique index on kb_knowledge found - [number]
```

![](/sys_attachment.do?sys_id=468172a3935e7e90def533527cba10ef)

-   Checking out the article shows "Invalid update" error message:

![](/sys_attachment.do?sys_id=64737e6f935e7e90def533527cba10b1)

-   The following error appears in the log:

```
Unique Key violation detected by database (ERROR: duplicate key value violates unique constraint "kb_knowledge_nunmber_key"
```

![](/sys_attachment.do?sys_id=8422be67935e7e90def533527cba10ec)

### Release

This issue has been identified in all currently supported releases

### Resolution

The following corrective steps need to be taken as corrective action:

Step 1. Open "System Definition" > "Scripts - Background" to execute the script below to remove the unique index created on the table "kb\_Knowledge" for the field "number":

```
var tableName = "kb_knowledge";
var isUniqueIndex = true;
var columnsInIndex = ["number"];
var util = new GlideIndexUtils();
var count = util. dropByExactElementSequence(tableName, isUniqueIndex, columnsInIndex);
gs.info(count + " index dropped.");
```

Step 2: Uncheck the "**unique**" field for table **kb\_knowledge** in **sys\_dictionary**

  

1.  Navigate to **System Definition > Dictionary**
2.  Search for **Table = kb\_knowledge** and **Column name = number**
3.  Open the record and uncheck **Unique** field

Only If the Unique field is not available:

1.  1.  Right click on **Form Header > Configure > Form Layout**
    2.  Move the entry **Unique** from the **Available** to **Selected** list.
    3.  Save changes. The **Unique** field is now visible.

Step 3: Now retry activating the plugin.

This can be achieved by opening "System Definition"  > "Plugin Installation History" > "Knowledge Management Advanced Installer" and running “Repair”.
