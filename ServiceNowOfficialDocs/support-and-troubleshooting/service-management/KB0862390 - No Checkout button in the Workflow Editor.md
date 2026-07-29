---
title: "No \"Checkout\" button in the Workflow Editor"
aliases:
  - KB0862390
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862390
kb_number: KB0862390
last_modified: 2024-09-20
---

## No "Checkout" button in the Workflow Editor

  

### Issue

The user noted that there was no "Checkout" button in the contextual menu (top left, hamburger icon) within the Workflow Editor. They saw a "Submit" button which performed the same action, but no "Checkout" button. They wanted to know what was going on.

### Cause

Another member of the user's team had customized the System UI "Message" field for the "Checkout" entry.

### Resolution

As mentioned, the system UI "Message" field for the "Checkout" record was customized to reflect a value of "Submit". This change was done by user "bucky.barnes":

-   /nav\_to.do?uri=sys\_ui\_message.do?sys\_id=d7d85a8f4a36231201e558aa811ea1c0

Therefore, to have the Workflow Editor button return to a value of "Checkout", the "Message" field must be reverted from the custom value of "Submit" to the Out of Box value of "Checkout".
