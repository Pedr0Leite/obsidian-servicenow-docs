---
title: "Prevent Rejection Without Comments"
aliases:
  - Prevent Rejection Without Comments
tags:
  - servicenow-dev-program
  - code-snippet
  - prevent-rejection-without-comments
  - client-scripts
---

🧩 Readme: Prevent Rejection Without Comments – Client Script
📘 Overview

This Client Script enforces that approvers must enter comments before rejecting a record in the Approval [sysapproval_approver] table.
It ensures accountability, audit readiness, and clear justification for rejection decisions.

🧠 Use Case
Field	Details
Table	sysapproval_approver
Type	Client Script – onSubmit
Purpose	Prevent users from rejecting approvals without comments
Business Value	Ensures transparency and proper audit trail in approval workflows
⚙️ Configuration Steps

Navigate to System Definition → Client Scripts.

Click New.

Fill the form as follows:

Field	Value
Name	Prevent Rejection Without Comments
Table	sysapproval_approver
UI Type	All
Type	onSubmit
Active	✅
Applies on	Update

Paste the following script in the Script field.

💻 Script
function onSubmit() {
    // Get the current state value of the approval record
    var state = g_form.getValue('state');

    // Get the comments entered by the approver
    var comments = g_form.getValue('comments');

    // Check if the approver is trying to REJECT the record
    // The out-of-box (OOB) value for rejection in sysapproval_approver is "rejected"
    // If state is 'rejected' and comments are empty, stop the submission
    if (state == 'rejected' && !comments) {

        // Display an error message to the user
        g_form.addErrorMessage('Please provide comments before rejecting the approval.');

        // Prevent the form from being submitted (block save/update)
        return false;
    }

    // Allow the form submission if validation passes
    return true;
}

🧪 Example Scenario
Field	Value
Approver	John Doe
State	Rejected
Comments	(empty)

User Action: Clicks Update
System Response: Shows error message —

“Please provide comments before rejecting the approval.”
Record submission is blocked until comments are provided.

✅ Expected Outcome
🚫 Prevents rejection without comments
⚠️ Displays user-friendly validation message
📝 Ensures that every rejection has a reason logged for compliance

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
