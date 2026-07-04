---
title: "Flow is throwing an Error for java.lang.NullPointerException near the start"
aliases:
  - KB0998462
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998462
kb_number: KB0998462
last_modified: 2024-09-25
---

## Flow is throwing an Error for java.lang.NullPointerException near the start

  

### Issue

You are finding that your **Flow Contexts** and failing in **Error State** and are showing a **java.lang.NullPointerException.**

**Example Error Code:**

Flow Designer: Operation(Flow Name.If$1.<sys\_id>.StartStage$1$request\_open) failed with error: java.lang.NullPointerException

### Cause

This is happening because the **"Start FlowDesigner Flow" Business Rule** has been **customized** and is running **Before Insert** of the **\[sc\_req\_item\] Record**.

Since the **Requested Item** has not been **saved** to the **Database** when the **Flow** **attaches** then it is causing the **Flow** to execute and try to perform actions on a **non-existent record**.

### Resolution

Please **revert** the **"Start FlowDesigner Flow" Business Rule** to **Out Of Box** to ensure the **Flow** attaches at the correct time.
