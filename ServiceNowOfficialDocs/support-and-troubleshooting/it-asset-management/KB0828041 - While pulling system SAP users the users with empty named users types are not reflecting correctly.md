---
title: "While pulling system SAP users the users with empty named users types are not reflecting correctly"
aliases:
  - KB0828041
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0828041
kb_number: KB0828041
last_modified: 2025-01-16
---

## Issue

We have a user who has no licenses on the SAP side when we pull the user entry into servicenow we see previously present license on the user record.

## Resolution

On the transform map record there is a field "Copy empty fields". If this field is checked then the empty records will still update the user records.

Navigate to 

1\. <<YOUR\_INSTANCE\_HERE>>.service-now.com/nav\_to.do?uri=sys\_transform\_map.do?sys\_id=69f9542773631300c9b2cb15d4f6a720

2\. check the box Copy empty fields.

3\. reprocess the import sets.
