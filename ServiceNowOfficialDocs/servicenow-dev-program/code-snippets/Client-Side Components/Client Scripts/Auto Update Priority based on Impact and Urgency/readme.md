---
title: "Auto Update Priority based on Impact and Urgency"
aliases:
  - Auto Update Priority based on Impact and Urgency
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-update-priority-based-on-impact-and-urgency
  - client-scripts
---

🧩 Readme : Client Script: Auto Priority Update Based on Impact and Urgency
📘 Overview

This client script automatically updates the Priority field on the Incident form whenever the Impact or Urgency value changes.
It follows the ITIL standard mapping to ensure the correct priority is always set automatically, improving data accuracy and efficiency for service desk agents.

⚙️ Script Details
Field	Value
Name	Auto Priority Update based on Impact and Urgency
Type	onChange
Applies to Table	Incident
Applies on Fields	impact, urgency
UI Type	All (Classic, Mobile, Workspace)
Active	✅ Yes
Condition	Leave blank
💻 Script Code
// ==========================================================================
// Script Name: Auto Priority Update based on Impact and Urgency
// Table: Incident
// Type: onChange | Fields: impact, urgency
// UI Type: All
// Version: 2025 Production Ready
// ==========================================================================

function onChange(control, oldValue, newValue, isLoading, isTemplate) {
    // Skip execution if form is loading or field is empty
    if (isLoading || newValue == '') {
        return;
    }

    // Get Impact and Urgency values
    var impact = g_form.getValue('impact');
    var urgency = g_form.getValue('urgency');

    // Define Priority Matrix (ITIL standard)
    var priorityMatrix = {
        '1': { '1': '1', '2': '2', '3': '3' },
        '2': { '1': '2', '2': '3', '3': '4' },
        '3': { '1': '3', '2': '4', '3': '5' }
    };

    // Find the new Priority
    var newPriority = priorityMatrix[impact]?.[urgency];

    // Update the Priority field if valid
    if (newPriority) {
        if (g_form.getValue('priority') != newPriority) {
            g_form.setValue('priority', newPriority);
            g_form.showFieldMsg('priority', 'Priority auto-updated based on Impact and Urgency', 'info');
        }
    } else {
        // Optional: Clear Priority if invalid combination is selected
        g_form.clearValue('priority');
        g_form.showFieldMsg('priority', 'Invalid Impact/Urgency combination — priority cleared', 'error');
    }
}

🧠 How It Works

The script runs automatically when Impact or Urgency changes.
It checks the ITIL-based matrix to determine the correct Priority.
If a valid combination is found, the Priority field updates automatically.
A small info message appears to confirm the update.

🔢 ITIL Mapping Table
Impact	Urgency	Resulting Priority
1 (High)	1 (High)	1 (Critical)
1	2	2
1	3	3
2	1	2
2	2	3
2	3	4
3	1	3
3	2	4
3	3	5
✅ Benefits

Automatically enforces ITIL priority standards
Reduces manual effort and user errors
Ensures consistency in priority calculation
Compatible with Classic UI, Next Experience, and Agent Workspace

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto-Populate Planned End Date/README|Auto-Populate Planned End Date]]
