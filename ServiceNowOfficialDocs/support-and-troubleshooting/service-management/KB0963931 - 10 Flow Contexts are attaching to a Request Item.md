---
title: "10 Flow Contexts are attaching to a Request Item"
aliases:
  - KB0963931
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963931
kb_number: KB0963931
last_modified: 2026-03-09
---

## 10 Flow Contexts are attaching to a Request Item

  

### Issue

When ordering a **Catalog Item** which uses a **Flow** you are finding that there is **10** **Flow Contexts** which **attach** and **execute** on the **Request Item**.

You can confirm this by performing the following:

1.  Go to **Process Automation > Flow Designer > Executions**
2.  Add a **Filter** for **Source Record = <SYS\_ID OF REQUEST ITEM>**
3.  See that there is **10** of the **Same Flow**

### Release

### Cause

This happens when the **Flow Trigger** is set to **'Run flow in foreground'** and is then using an **'Update Record' Action** as the **First Action** of the **Flow** and it is targeting the **Request Item** itself.

Since the **'Update Record' Action** will process **immediately** after the **Trigger** which causes the **"Start FlowDesigner Flow"** **Business Rule** to trigger again and attach a **new Flow** **Context**.

### Resolution

To resolve this issue you will need to add a **Short Timer** of **1 or 2 Seconds** which should be placed **before** the '**Update Record' Action**.

This will prevent the **Conditions** for the **"Start FlowDesigner Flow" Business Rule** from being **met** when the **Request Item** is updated.
