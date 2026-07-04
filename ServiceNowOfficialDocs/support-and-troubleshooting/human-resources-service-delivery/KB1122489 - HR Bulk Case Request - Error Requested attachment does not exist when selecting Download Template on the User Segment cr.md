---
title: "HR Bulk Case Request - Error \"Requested attachment does not exist\" when selecting \"Download Template\" on the User Segment creation page"
aliases:
  - KB1122489
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1122489
kb_number: KB1122489
last_modified: 2025-11-13
---

## Issue

Steps to Reproduce:

1\. In the filter navigator, select "Bulk Case Requests"

2\. Click New, fill in the relevant fields and save the record

3\. Click New on the "User Segments" related list

4\. Under "User selection" ensure that the "Upload file" option is selected

5\. Select either the "user\_name template" or "email template"

6\. Click on "Download Template"

![](/sys_attachment.do?sys_id=c92512c497edc61024a7739c1253af10 "update file.png")

Expected behaviour: The template XLS file is downloaded

Actual behaviour: You will be presented with the error **Requested attachment does not exist**

**![](/sys_attachment.do?sys_id=573552c497edc61024a7739c1253afcf "error.png")**

## Resolution

1\. In Prod (or any other instance where the attachments still exist), open and Export XML and the following two records:

**Document Revision "HR Excel Upload Sample - user\_name\_0.1"**  
https://instance\_name.service-now.com/dms\_document\_revision.do?sys\_id=3983b6f8db81720085ea54c0cf961918

**Document Revision "HR Excel Upload Sample - user\_email\_0.1"**  
https://instance\_name.service-now.com/dms\_document\_revision.do?sys\_id=80e4f6f8db81720085ea54c0cf961941

2\. Import XML the records downloaded in step 1 on the affected instance. This will bring over the associated attachments.

Alternatively, clone prod over the affected sub-prod **with attachments**.
