---
title: "Change Request Affected CIs Related List \"Add Selected\" button is not adding CIs"
aliases:
  - KB0996596
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996596
kb_number: KB0996596
last_modified: 2024-08-23
---

## Change Request Affected CIs Related List "Add Selected" button is not adding CIs

  

### Issue

When the user is on the Change Request form, they go down to the Related Lists. Under the "Affected CIs" Related List, there is an "Add" button.

When the user clicks the "Add" button, a modal window opens and there are two UI Actions the user can select from, "Add Selected" or "Add All(number)".

The "Add All (number)" UI Action works, but the "Add Selected" UI Action does not work to add the checked Configuration Items, even though the modal window closes onClick of the "Add Selected" UI action, just as it does when the behavior adds the CIs to the Related List.

### Cause

The user did not have the Service Portfolio Management Core (com.snc.service\_portfolio\_core) plugin enabled. This caused a Script Include's script to fail, which resulted in the "Add Selected" UI Action failing to add the selected CIs.

### Resolution

As shared above, the reason the "Add Selected" UI Action was not behaving properly is that the Service Portfolio Management Core (com.snc.service\_portfolio\_core) plugin was not installed. As a result, the **AssociateCItoTask** Script Include query to the _service\_offering_ table failed. The _service\_offering_ table comes from the not-yet-installed plugin, and without it, the query cannot resolve and the selected CIs do not get added to the "Affected CIs" Related List.

Installing the plugin resolved the issue, as the Script Include could locate the _service\_offering_ table, resolve the query, and add the selected CIs.
