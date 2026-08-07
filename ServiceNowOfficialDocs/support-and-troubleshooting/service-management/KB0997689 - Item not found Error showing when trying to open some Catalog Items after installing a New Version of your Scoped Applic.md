---
title: "\"Item not found\" Error showing when trying to open some Catalog Items after installing a New Version of your Scoped Application"
aliases:
  - KB0997689
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997689
kb_number: KB0997689
last_modified: 2024-09-11
---

## "Item not found" Error showing when trying to open some Catalog Items after installing a New Version of your Scoped Application

  

### Issue

You have some **Catalog Items** which are using **Flows** from a **Scoped Application** and they are working normally until you **Install** a **New Version** of your **Scoped Application**.

Once the **New Version** is **installed** you are then seeing that the **"Item not found"** **Error Message** is displaying when you try to open the **Catalog Item**.

### Cause

This is happening because the **Flow** which is attached to the **Catalog Item** is **corrupt** and is not registering as being attached properly.

It is **most likely** that the **Flow** was **corrupted** in the **Source Instance** (Where the **Scoped Application** was **created**) and that the **Corrupt Files** are then being **Installed** onto the **Next Instances**.

### Resolution

1.  Open the **Catalog Item** in the **\[sc\_cat\_item\] Table**
2.  Identify the **Flow Name** which is **Corrupt**
3.  **Open** the **Flow** in the **Source Instance** (Where the **Scoped Application** was **created**)
4.  Make any **small (meaningless) modification** to the **Flow**
5.  **Save** and **Activate** the **Flow**
6.  Ensure that it **Activates** without any **Errors**
7.  Now **Repeat Steps 1 - 6** for any other **Affected Flows** and **Catalog Items**
8.  Finally you can **Publish** a **New Version** of your **Scoped Application**
9.  This can be **Installed** on the **Affected Instance** to receive the **Fixed Flows**
