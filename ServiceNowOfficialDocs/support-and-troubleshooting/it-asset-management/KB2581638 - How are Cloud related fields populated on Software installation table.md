---
title: "How are Cloud related fields populated on Software installation table ? "
aliases:
  - KB2581638
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2581638
kb_number: KB2581638
last_modified: 2025-10-23
---

## How are Cloud related fields populated on Software installation table ?

  

### Issue

This KB will help answer on how are Cloud related fields populated on Software installation table. These fields are as below:  
Cloud host type  
Cloud license type  
Cloud license type source  
Cloud provider   
Cloud service type 

Refer image, install on Linux host showing Cloud provider (cloud\_provider)= AWS Datacenter and Cloud service type (cloud\_service\_type) = Iaas. Some install have this value while some are empty.

![undefined](/sys_attachment.do?sys_id=ac601f8d47783e1448cb2920326d439b)

It seems these values are from SamStampCloudInstalls and SamCloudInstallUtil script owned by Software Asset Management scope. These fields are not populated by Discovery job, nor Reconciliation are not populating these values.

Details of Software Install field here : [https://www.servicenow.com/community/sam-articles/software-installations-table-attribute-review/ta-p/2318570](https://www.servicenow.com/community/sam-articles/software-installations-table-attribute-review/ta-p/2318570 "https://www.servicenow.com/community/sam-articles/software-installations-table-attribute-review/ta-p/2318570")

### Release

Yokohama and Above

### Resolution

Pre Yokohama, Cloud related fields were stamped during reconciliation run by Recon job. To improve reconciliation performance in Yokohama to create new job SAM - Stamp Cloud Installs. 

An enhancement is created on Yokohama for 'Recon performance and usability enhancement'. This added a new job "SAM - Stamp Cloud Installs" to add the Cloud related fields on SW install .

This job is expected to run weekly so this has updates install records to have cloud related fields populated.

### Related Links

Empty Cloud License type = [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB1635251](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1635251)
