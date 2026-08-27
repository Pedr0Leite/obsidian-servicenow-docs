---
title: "[CMP\Stack provision] Failed to launch stack from Cloud User Portal"
aliases:
  - KB0815339
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815339
kb_number: KB0815339
last_modified: 2025-08-25
---

## Issue

-   During the Azure VM provision, there is an error stating **“No order found for request item: RITMxxxx”** observed in the Cloud User Portal.

![](sys_attachment.do?sys_id=df14ec45dbc874d0b55f0b55ca9619e8)

-   But the respective RITM record is found in "sc\_req\_item" table and in the Request Details of Cloud User Portal the input data are visible though the values are not fetched from the form when observed in the Cloud Orchestration Trail as well.

![](sys_attachment.do?sys_id=d314ec45dbc874d0b55f0b55ca9619e6)

![](sys_attachment.do?sys_id=5f14ec45dbc874d0b55f0b55ca9619e4)

## Resolution

#### Step -1:

-   As a first step analyze how many "workflow versions" are created in the Blueprint request.
-   If there are 2 workflow versions created, check their status.

i.e.   
for v1 "Active might be set to false while Published set to true" and,  
for v1.1 "Active might be set to true while Published set to false"

-   In such cases, the workflow version for which "Active was true" and "Published set to false" will cause the provision to fail.
-   In order to successfully provision the Stack change the value of "Published to true" for that workflow version which is "Active" and post that provision will succeded.

#### Step -2:

-   As a next step if still, the workflow fails, check if there are multiple Blueprint requests exists in the multiple domain which is then tied to the same Workflow under "wf\_workflow" table.
-   i.e. only one Blueprint request should exist in the "global" domain. (because until New York releases CMP doesn't support Domain separation)
-   If there are multiple Blueprint request exist delete the one which is created in other domain apart from the "global" domain.
