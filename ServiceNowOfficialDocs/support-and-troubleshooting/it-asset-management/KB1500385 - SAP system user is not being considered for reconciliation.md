---
title: "SAP system user is not being considered for reconciliation "
aliases:
  - KB1500385
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1500385
kb_number: KB1500385
last_modified: 2026-03-27
---

## Issue

We have an SAP system user who is not being considered for reconciliation, because of this we are not able to see the user under the License required by.

## Resolution

![](/sys_attachment.do?sys_id=0631a5879377f2dcf538fb2d6cba10d0)

In this case, the SAP Client's" environment is testing, so it will not be considered for reconciliation.

SAP client's environment should be of type "Development" (C) or "Production" (P), so in order to consume users, we need to change either of the types. This is part of the reconciliation code.

The condition that checks the SAP Client Environment is part of the Script Include "SamPublisherCalculatorSAP", in the function "ignoreUnlicensableUsers".

https://<instance>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=ae1120b987712300923aa75fe5cb0b70
