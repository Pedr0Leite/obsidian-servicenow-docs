---
title: "How to Customize the Card View on Visual Task Boards (VTB)"
aliases:
  - KB0656249
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656249
kb_number: KB0656249
last_modified: 2025-06-03
---

## How to Customize the Card View on Visual Task Boards (VTB)

  

### Issue

Users want to display specific fields (e.g., Priority, Assignment Group) on the card view in Visual Task Boards to enhance visibility and usability.

### Release

  Applicable to all supported ServiceNow releases with Visual Task Boards enabled.

### Resolution

  To customize the fields shown on cards in a Visual Task Board:

1.  Open the **Task Record**
    -   Navigate to the task type you want to modify (e.g., open an Incident record).
2.  Switch to **VTB View**
    -   Right-click the ☰ menu (top-left corner of the form)
    -   Select View > VTB
3.  **Configure** the VTB Form Layout
    -   Right-click on the form context header (e.g., Incident)
    -   Click Configure > **Form Layout** (or Form Builder)
    -   Add the fields you want to display on the card view (e.g., Priority, Assignment Group, Short Description)
    -   Click Save
4.  Enable Card **Info Display** on the VTB Board
    -   Open the Visual Task Board for that record type
    -   Click the Configuration gear icon
    -   Select **Show Card Info** (This setting is available only when **Compact Cards** is disabled.)
    -   This enables display of the fields added to the VTB form layout
5.  Verify the Changes
    -   The selected fields should now **appear on each card** within the VTB board.

![Create a new VTB form view](/sys_attachment.do?sys_id=b582ec6f973166140af678ce2153aff7 "Create a new VTB form view")

![Show Card Info](/sys_attachment.do?sys_id=edd2acef973166140af678ce2153af39 "Show Card Info")

* * *

### Additional Notes

-   These changes are specific to the current board and task type.
-   Ensure the fields you want are part of the task table and added to the form layout.
-   If a field doesn’t appear, try refreshing the board or **clearing browser cache**

The following card details are hard coded on the platform and cannot be customized. They are predetermined by the system to ensure consistency across the platform.

![Card Details](sys_attachment.do?sys_id=33461bd39775e2140af678ce2153af08 "Not able to edit fields in Card Details")

### Related Links

[Visual Task Boards Overview](https://www.servicenow.com/docs/csh?topicname=c_VisualTaskBoards.html&version=latest "Visual Task Boards Overview")
