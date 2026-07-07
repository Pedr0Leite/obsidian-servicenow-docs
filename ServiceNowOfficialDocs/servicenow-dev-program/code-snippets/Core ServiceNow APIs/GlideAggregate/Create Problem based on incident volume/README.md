---
title: "Create Problem based on incident volume"
aliases:
  - Create Problem based on incident volume
tags:
  - servicenow-dev-program
  - code-snippet
  - create-problem-based-on-incident-volume
  - glideaggregate
---

Key features
Automatic problem creation: The script uses a GlideAggregate query to count the number of incidents opened for a specific CI.
Time-based threshold: Problems are only created if more than five incidents are opened within a 60-minute window.
Targeted incidents: The script focuses on incidents related to the same CI, making it effective for identifying recurring infrastructure issues.
Customizable conditions: The number of incidents and the time frame are easily configurable within the script.
Efficient performance: The use of GlideAggregate ensures the database is queried efficiently, minimizing performance impact. 

How it works
The script is designed to be executed as a server-side script, typically within a Business Rule. When an incident is inserted or updated, the script performs the following actions:
Queries incidents: It executes a GlideAggregate query on the incident table.
Sets conditions: The query is filtered to count all incidents that meet the following conditions:
Same CI: The incident's cmdb_ci matches the cmdb_ci of the current record.
Within the last hour: The opened_at time is within the last 60 minutes.
Evaluates count: After the query is run, the script checks if the count of matching incidents exceeds the threshold (in this case, 5).
Creates problem: If the threshold is exceeded, a new problem record is initialized.
The short_description is automatically populated with a descriptive message.
The cmdb_ci is linked to the new problem record.
The new record is then inserted into the database. 
Implementation steps
Create a Business Rule:
Navigate to System Definition > Business Rules.
Click New.
Configure the Business Rule:
Name: Auto Create Problem from Multiple Incidents
Table: Incident [incident]
Advanced: true
When to run: Select after and check the Insert and Update checkboxes. This ensures the script runs after an incident has been saved.
Filter conditions: Optionally, you can add conditions to limit when the script runs (e.g., cmdb_ci is not empty).
Add the script:
Navigate to the Advanced tab.
Copy and paste the script into the Script field.
Customize (optional):
Number of incidents: Change the > 5 value to adjust the threshold.
Time frame: Adjust the gs.minutesAgoStart(60) value to change the time window.
Other conditions: If you need to check for specific incident statuses or categories, add more addQuery lines to the GlideAggregate call.
Save the Business Rule. 
Customization examples

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Get Incident Count by Priority/README|Get Incident Count by Priority]]
