---
title: "Requested by (requested_by) and Requested for (u_requested_for) are not copying correctly to the SCTASK record"
aliases:
  - KB0819357
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819357
kb_number: KB0819357
last_modified: 2024-04-08
---

## Requested by (requested\_by) and Requested for (u\_requested\_for) are not copying correctly to the SCTASK record

  

### Issue

The user's Requested By and Requested For values weren't transferring correctly to SCTASK records.

### Resolution

It was found that there were custom Business Rules which were populating the "requested\_for" and "u\_requested\_by" fields on both the Request (REQ) and Requested Item (RITM), but there was no custom Business Rule which was applied to the Catalog Task (SCTASK) table to perform the same functionality there. What the user was doing was taking the value stored in a variable, entered by an end-user when they ordered an item, and copying the value to the appropriate fields. Again, the user had the customization in place for Requests (sc\_request) and Requested Items (sc\_req\_item), but not for Catalog Tasks (sc\_task).

To remedy this, the user created a similar custom Business Rule on the sc\_task table. Doing this resolved the issue.
