---
title: "Flow Designer Activation & Testing Errors: \"Invalid values passed to the API\"
aliases:
  - KB0745336
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745336
kb_number: KB0745336
last_modified: 2026-02-02
---

## Flow Designer Activation & Testing Errors: "Invalid values passed to the API"

  

### Issue

When working with Flow Designer, users may encounter errors that prevent a Flow or Subflow from being tested, saved, or activated. Common error messages include:

-   “Invalid values passed to the API, details: Record is mandatory and must be filled in”
-   “Invalid values passed to the API, details: Only one Trigger instance can be part of a flow”
-   “Only one Trigger instance can be part of a flow”

These errors typically occur during testing, saving, or activating a Flow.

### Release

-   Flow Designer
-   All releases

### Cause

These errors are usually caused by one of the following:

1.  Mandatory fields in one or more actions are not populated
2.  Multiple Trigger instances exist in the same Flow
3.  Trigger configuration is incomplete or corrupted after recent changes

### Resolution

**Scenario 1: Mandatory Fields Not Populated**

If the error states that a Record is mandatory and must be filled in, one or more actions in the Flow or Subflow are missing required inputs.

Steps to resolve:

1.  If the Flow is not yet activated, attempt to activate it.
2.  The activation error will indicate the action number where the issue occurs.
3.  Open the Flow or Subflow in Flow Designer.
4.  Review each action in the Flow.
5.  Verify that all mandatory fields are populated.
6.  Populate any missing required values.
7.  Save and activate the Flow again.

**Scenario 2: Multiple or Invalid Trigger Configuration**

If the error indicates “Only one Trigger instance can be part of a flow”, the Flow contains more than one Trigger or an invalid Trigger setup.

Steps to resolve:

1.  Open the Flow in Flow Designer.
2.  Review the Trigger configuration.
3.  Ensure the Flow has only one Trigger.
4.  Make a small update to the existing Trigger (for example, reselect a field or condition).
5.  Save the Flow.
6.  Activate the Flow.

After updating the Trigger, the Flow should activate successfully.
