---
title: "Cloud Datacenter Discovery throwing error message: Unable to unmarshall error response {"
aliases:
  - KB0749926
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749926
kb_number: KB0749926
last_modified: 2024-04-07
---

## Issue

# Symptoms

  

We see the below error on the Cloud service account form view, when we click on "Discover Datacenter"

  

![](sys_attachment.do?sys_id=016c286edb42b450e515c223059619bd)

# Release

Kingston, London

# Cause

"Datacenter URL" filed on the "cloud service account" should not be populated.

# Resolution

OOB we do not need to populate "Datacenter URL" filed at the time of "Cloud Service Account" creation. So, make sure, you keep this field empty and run the discovery, you should no longer see the error.

# Additional Information

Only "AWS USGOVCLOUD" populates the "Datacenter URL" field, no other AWS account type does.
