---
title: "Unable to resolve a collision in Team development"
aliases:
  - KB0750821
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750821
kb_number: KB0750821
last_modified: 2024-11-02
---

## Issue

Unable to resolve a collision in Team development due to error - "Not authorized to update this record"

Steps to Reproduce:

1\. Go to Team dashboard  
2\. Try to resolve collision  
3\. Normal admin user gets Insufficient access error - "Not authorized to update this record"

## Resolution

You can export to xml the files that you are unable to skip and alter the below:

From

<state>collision</state>

To

<state>skipped</state>

You can than import the altered XML back into the instance and this will update the state field.

Push Pull versions can be found sys\_sync\_history\_version
