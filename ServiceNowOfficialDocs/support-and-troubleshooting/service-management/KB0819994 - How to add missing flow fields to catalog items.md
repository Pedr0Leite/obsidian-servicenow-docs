---
title: "How to add missing flow fields to catalog items"
aliases:
  - KB0819994
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819994
kb_number: KB0819994
last_modified: 2025-08-11
---

## How to add missing flow fields to catalog items

  

### Issue

The Flow Designer support for Service Catalog plugin is installed, but users cannot attach flows to catalog items. The plugin functions correctly, but the flow\_designer\_flow field is missing from the request item.

To reproduce this issue: 

1.  Log in as an administrator who can edit items and flows.
2.  Optionally, create a flow that uses service catalog as a trigger.
3.  Go to a catalog item.
4.  Open the Process Engine tab.
5.  Notice that only the workflow field appears, with no option to add a flow.

### Release

Any supported release

### Resolution

To add the missing flow field to catalog items:

1.  Log in as an administrator or a user who can edit Service Catalog forms.
2.  Go to **Maintain Items**.
3.  Select an item, and then open the form layout.
4.  In the form context menu (the hamburger menu in the header), select **Configure**.
5.  Add the Form field from **Available** to **Selected**.
6.  In the Form view and section, select the **Process Engine** section.
7.  Add **Flow (+)** to the selected fields and place it under Workflow.

After completing these steps, the option to add flows is available for your catalog item.
