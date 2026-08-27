---
title: "Discovery fails at insertion into CMDB but crosses lookup for the identifiers."
aliases:
  - KB0781924
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781924
kb_number: KB0781924
last_modified: 2024-04-08
---

## Issue

When discovery tries to insert a CI into CMDB as no identifiers match, we get an insertion failure. The discovery log just shows "insertion failed due to unknown reason".

Enabling identification engine logging does not show the issue. Use the payload and run a background script using createOrUpdateCI, then you will see the error:

FAILED TRYING TO EXECUTE ON CONNECTION glide.15 (connpid=xxx): INSERT INTO cmdb (<<PAYLOAD>>),INSERT INTO cmdb$par1 (\`operational\_status\`,\`sys\_updated\_on\`,\`sys\_class\_name\`,\`sys\_id\`,\`sys\_updated\_by\`,\`sys\_class\_path\`,\`sys\_created\_on\`,\`sys\_domain\`,\`sys\_created\_by\`,\`sys\_mod\_count\`,\`sys\_domain\_path\`,\`install\_status\`,\`name\`) VALUES(xxx,'xxx','cmdb\_ci\_win\_server','xxx','xxx','xxx','xxx,'xxx','xxx',xxx,'xxx',xxx,'xxx')  
java.sql.BatchUpdateException: Duplicate entry '<<SYS\_ID>>' for key 'PRIMARY'

## Resolution

Inactivate custom business rules that have an update operation on tables  where we perform an insert before the main CI is inserted.
