---
title: "Advanced Scripts"
aliases:
  - Advanced Scripts
tags:
  - servicenow-dev-program
  - code-snippet
  - advanced-scripts
  - inbound-actions
---

## These inbound action scripts will help you with the following:

### 1) Creation - Map values from an email to variables and create a requested item for the same.
Check with script -> create_catalog_item_from_email.js  

This script will help you map the values coming with the email body to variables of a catalog items and submit a catalog item. In this particular script we're submitting the request for user-offboarding by mapping the userID and termination date. So, in a similar way as per your requirement you can map/add variables from an email to submit an catalog item.

### 2) Updating - Check with already created requested item and update the variables and restart the workflow.
Check with script -> update_catalog_item_from_email.js

Now, Once you've successfully mapped the values and submitted an item from the email that first came into ServiceNow, there can be a case scenario where we need to update the termination date to a new value. This script will help you query the existing RITM for the user and update the value for termination date to the new values that came into the new email and restart the workflow. So, again as per your requirement in a similar way you can query the existing RITM and update variables coming in with an email and update the RITM.

### 3) Cancellation - Check with already created requested item and cancel the same also cancel the workflow.
Check with script -> cancel_catalog_item_from_email.js

Third Scenario, here is once a termination request is submitted, now we need to re-hire the candidate. So, in this case we need to cancel the RITM. 
This script will help you query the existing RITM for the user and cancel the RITM and all related tasks. So, as per your case scenario in a similar way you can query the existing RITM and cancel it with all the related catalog tasks.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Incident Creation from Case Email/README|Auto Incident Creation from Case Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Auto Reply Email/README|Auto Reply Email]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Automate creation of incidents through inbound actions/README|Automate creation of incidents through inbound actions]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Duplicate Incident Detection and Creation/README|Duplicate Incident Detection and Creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Email Text as Attachment/README|Email Text as Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Inbound Actions/Inbound Email Action to Create User and Assign Groups/Readme|Inbound Email Action to Create User and Assign Groups]]
