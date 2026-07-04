---
title: "What needs to be in place for entitlements and contracts to appear on the renewals calendar in SAM Workspace?"
aliases:
  - KB1646540
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1646540
kb_number: KB1646540
last_modified: 2024-07-11
---

## Additional Information

If you have created a Maintenance entitlement and associated it with the relevant perpetual entitlements, the scheduled job SAM - Subscription Maintenance (https://\[instance-name\].service-now.com/nav\_to.do?uri=sysauto\_script.do?sys\_id=05b5faa2e73003004c6f07d8d2f6a91a) must be ran, this runs daily by default but can be executed on-demand by navigating to the linked record and using the 'Execute Now' UI action. This job populates the 'Maintenance Expiration Date' field that the renewal calendar uses to query for entitlements.

**Q:** Is there reason to use a maintenance entitlement instead of a maintenance contract to track support agreements on perpetual entitlements?  
Answer: This question is out-of-scope for ServiceNow Support  
Reason: The answer depends on understanding of customer's contract landscape, advice on this can be provided by a partner or ServiceNow Professional Services.  
What ServiceNow Support can advise on: How the renewal calendar feature works on a technical level
