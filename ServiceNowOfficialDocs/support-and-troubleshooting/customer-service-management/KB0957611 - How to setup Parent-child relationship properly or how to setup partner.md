---
title: "How to setup Parent-child relationship properly or how to setup partner"
aliases:
  - KB0957611
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957611
kb_number: KB0957611
last_modified: 2026-04-30
---

## How to setup Parent-child relationship properly or how to setup partner

  

### Issue

How to setup Parent-child relationship properly or how to setup partner

### Release

All

### Resolution

\--If customers plan to go on parent-child route then please make sure to populate "Parent Account" field on child with correct parent. "Parent" field refers to company not account. Also, if you want all the contact to see cases related to all the child account then you will have to provide them Case Manager: customer\_case\_manager role   
\--If you take partner route then please set 'Partner' to true on partner
