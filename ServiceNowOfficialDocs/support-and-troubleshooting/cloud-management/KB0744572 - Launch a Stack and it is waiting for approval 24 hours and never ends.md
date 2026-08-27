---
title: "Launch a Stack and it is waiting for approval 24 hours and never ends"
aliases:
  - KB0744572
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744572
kb_number: KB0744572
last_modified: 2024-04-07
---

## Launch a Stack and it is waiting for approval 24 hours and never ends

  

### Issue

# Description

Cloud Management Platform, while trying to launch a stack, the VM provision doesn't work and its stuck in **'waiting for approval'** 24hours and never end the process.

# Steps to Reproduce

-   Log into the instance
-   Create credentials for AWS, VMware and Azure.
-   Create Service Account AWS, VMware and Azure.
-   Create Setup cloud account for AWS, VMware and Azure and choose the Datacenters.
-   Create compute and image profiles for AWS, VMware and Azure. 
-   Create Basic Blueprint with VM on AWS, Azure and VMware and create catalog item.
-   Go to Cloud User  portal >> Launch a Stack
-   Fill the required fields in "General Info" and "Provision" and click submit

**Expected result**: The VM provision should work without waiting for approval 

**Actual result**: The VM provision doesn't work and it's stuck in 'waiting for approval for 24hours'.

# Applicable Versions

-   From Jakarta

# Cause

-   This issue is with the Workflow is stuck in approval.

# Fix

-   Attachment: [XML file](sys_attachment.do?sys_id=de5ba86adb42b450e515c223059619f0 "XML file"), import the XML file as a Workaround, ServiceNow development team working for fixing the issue permanently.  

**Note:** Attached XML file will update the Approval Workflow "Service Catalog Request" on table "sc\_request", no update or insert to rest of the Scripts or the environment, hence safe to import XML without issues.
