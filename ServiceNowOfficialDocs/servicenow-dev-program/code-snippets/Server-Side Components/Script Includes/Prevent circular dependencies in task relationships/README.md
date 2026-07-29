---
title: "Prevent circular dependencies in task relationships"
aliases:
  - Prevent circular dependencies in task relationships
tags:
  - servicenow-dev-program
  - code-snippet
  - prevent-circular-dependencies-in-task-relationships
  - script-includes
---

# Detect Circular Reference in Task Dependencies



## Overview

This Script Include helps identify **circular dependencies** in task relationships within ServiceNow. Circular references can cause workflow issues, reporting errors, and logic failures in project management or task tracking modules.

## What It Does

- Traverses task dependencies recursively.
- Detects if a task is indirectly dependent on itself.
- Returns `true` if a circular reference is found, `false` otherwise.

## Use Case

Imagine Task A depends on Task B, and Task B depends on Task A. This creates a circular loop that can break automation or cause infinite recursion. This script helps prevent such configurations.

Tables and modules it would be usefull
It is used for Table: planned_task_rel_planned_task
This table is used to define task dependencies between project tasks in ServiceNow's Strategic Portfolio Management (SPM) or Project Portfolio Management (PPM) modules. It stores relationships such as:

Predecessor Task
Successor Task
Dependency Type (e.g., Finish-to-Start)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
