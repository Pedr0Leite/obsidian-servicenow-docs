---
title: "Root-Cause Predictor"
aliases:
  - Root-Cause Predictor
tags:
  - servicenow-dev-program
  - code-snippet
  - root-cause-predictor
  - script-includes
---

## Incident Root-Cause Predictor

### Overview
The **Incident Root-Cause Predictor** automatically classifies incoming Incidents into categories like *Network, Hardware, Application,* or *Security* based on keywords in the description.  
This helps in faster triaging and routing tickets to the right support teams.

---

## How It Works
1. A user submits an Incident.
2. A **Business Rule** runs on insert.
3. It calls the **Script Include – `RootCausePredictor`**.
4. The predictor scans the description and returns a probable root-cause category.

---
## Business Rule Script (How to call Script Include on BR)
    var util = new global.RootCausePredictor();
    
(function executeRule(current) {
    var util = new global.RootCausePredictor();
    var cat = util.predict(current.description);
    current.u_root_cause = cat;
    current.work_notes = "Auto-classified as: " + cat.toUpperCase();
})(current);

--------------
## Sample Input and Output
Input : A user logs a ticket:
“Wi-Fi keeps disconnecting every few minutes.”

The Script Include scans for the word “Wi-Fi”, which matches the Network keyword list.
OutPut: 

System automatically sets field u_root_cause = "Network"
Work note added: “Auto-classified as: NETWORK”

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
