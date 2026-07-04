---
title: "How to change the stats.do Tag \"DEMO Server\""
aliases:
  - KB0634930
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634930
kb_number: KB0634930
last_modified: 2025-04-08
---

## How to change the stats.do Tag "DEMO Server"

  

### Issue

The stats.do page's top line is almost always tagged **DEMO Server**. This is the default value for all instances. However, sometimes admins want to change to this **DEV Server**, **TEST Server**, or **PROD Server**. This can be done easily with one property change and is only a cosmetic change.

![TAG: DEMO Server](/sys_attachment.do?sys_id=edf4e06947b4ea10c4e1a325126d43ea "stats.do.jpg")

### Release

All releases

### Resolution

### Steps to Change

* * *

1.  Log in an an admin.
2.  Navigate to **System Properties > All Properties**.
3.  Do one of the following:
    -   Search and open the property **glide.installation.name** 
    -   Navigate to https://<INSTANCENAME>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=4fad0bf4c611228e01d9e895a86316c3
4.  Change the value to **DEV Server**, **TEST Server**, or **PROD Server**.
5.  Save the record.
6.  To confirm that the change worked, navigate to **/stats.do**.

![](/Note_25x.pngx "Note") **Note**: The name can be changed as needed, but ensure that the value is short and does not contain special characters
