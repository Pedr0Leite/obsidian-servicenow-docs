---
title: "How to Discover Windows Services"
aliases:
  - KB0744968
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744968
kb_number: KB0744968
last_modified: 2025-08-07
---

## How to Discover Windows Services

  

### Issue

Follow the below steps if you want to discover Windows Services on Windows-based machines.

### Release

All

### Resolution

1.  Navigate to **Discovery Definitions - CI Classification - Windows**
2.  Edit the generic **Windows** entry, along with **Windows Server 2008/2012/2016** as needed
3.  **Windows Classification - Trigger Probes - Edit**
4.  Add **Windows-Services** to the right column, **Save**
5.  Open a CI of a Class you are trying to edit, such as Computer or Server
6.  Right-Click on the top gray bar when vewing the CI  - **Configure - Related Lists**
7.  Move **Windows Service -> Configuration Item** to the right column, **Save**
8.  The Windows Services tab should then appear on the CI page under **Related Links**
9.  Run a discovery on a Windows device to populate the list
