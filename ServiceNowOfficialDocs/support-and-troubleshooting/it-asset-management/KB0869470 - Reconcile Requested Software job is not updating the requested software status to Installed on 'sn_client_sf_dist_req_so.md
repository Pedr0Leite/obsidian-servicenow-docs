---
title: "\"Reconcile Requested Software\" job is not updating the requested software status to Installed on 'sn_client_sf_dist_req_software' table."
aliases:
  - KB0869470
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869470
kb_number: KB0869470
last_modified: 2023-11-30
---

## Issue

"Reconcile Requested Software" Job is not updating the requested software status to Installed even though the software was installed successfully.

![](sys_attachment.do?sys_id=17f9299fdb9da090fa192183ca96197b)

## Resolution

1.Login to the instance.

2.Navigate to 'sn\_client\_sf\_dist\_req\_software' table and remediate all the records with Application name as Empty and with status "Not Installed".

3.Run the "Reconcile Requested Software" scheduled job and now it will update the "status" field to Installed for all the devices which are successfully installed.
