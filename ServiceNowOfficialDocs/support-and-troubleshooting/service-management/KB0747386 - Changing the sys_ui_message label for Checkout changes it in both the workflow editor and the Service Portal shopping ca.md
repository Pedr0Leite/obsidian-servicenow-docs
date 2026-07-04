---
title: "Changing the sys_ui_message label for \"Checkout\" changes it in both the workflow editor and the Service Portal shopping cart"
aliases:
  - KB0747386
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747386
kb_number: KB0747386
last_modified: 2024-09-20
---

## Changing the sys\_ui\_message label for "Checkout" changes it in both the workflow editor and the Service Portal shopping cart

  

### Issue

# Symptoms

-   Changing the sys\_ui\_message (Message) key value for "Check Out" changes the value in two locations instead of just one (in the Workflow editor and also in the Service Portal cart)

# Release

-   Kingston Patch 12

# Cause

This is working as expected (further details below).

# Resolution

After checking with the Platform's Product Owners, it was shared that this is expected behavior (the customer's expectation was that one sys\_ui\_message should only touch one location in the Platform, not two). The sys\_ui\_message table is the table from where the Platform draws static text.  
  
The sys\_ui\_message table contains the translations for informational messages, confirmation messages, error messages, and other types of system messages.  
  
Our Product Owner shared the following documentation regarding sys\_ui\_messages and concluded that this is how the system is designed:

-   [Message table](https://docs.servicenow.com/csh?topicname=r_MessageTable.html&version=latest "Message table")
