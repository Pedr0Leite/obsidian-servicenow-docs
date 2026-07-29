---
title: "Execution Time Tracker"
aliases:
  - Execution Time Tracker
tags:
  - servicenow-dev-program
  - code-snippet
  - execution-time-tracker
  - script-includes
---

# Script Execution Time Tracker

This snippet helps developers measure how long their server-side scripts take to run in ServiceNow.
Useful for performance optimization and debugging slow background scripts or Script Includes.

## Example Use Case
- Measure performance of a GlideRecord query or function execution.
- Log the execution time to the system logs.

## How It Works
The script uses timestamps before and after execution to measure elapsed time.

## Usage
Wrap your logic between `start` and `stop`, or use the Script Include:

```javascript
var timer = new ExecutionTimeTracker();
// ... your code ...
timer.stop('My Script');

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
