---
title: "When HR Case is created from Interaction in HR Agent Workspace, attachments and transcripts are not transferred to HR case"
aliases:
  - KB0993746
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993746
kb_number: KB0993746
last_modified: 2025-09-03
---

## Additional Information

We can customize this based on the requirement at the customer's own risk.

Customizations however are not supported by the Technical Support Department and falls outside the scope of support.

If the business requirement is to move dependencies like attachments from the interaction to HR Case record, then the below points needs to be taken care of:  
  

-   The script responsible for moving the attachment should be in the target application scope. (ie - For example the target application scope is - Advanced Work Assignment for HRSM, then the server script should be on Advanced Work Assignment for HRSM scope as well)
-   The user has necessary and access and rights to view the attachment. For this you need to check the ACLs, and before query business rules.

```
If implementing customization is a business critical requirement, and any assistance is required to implement this, you can reach out to our Customer Success Team, who can help you achieve the desired results.Bear in mind that this will be a chargeable service.
```
