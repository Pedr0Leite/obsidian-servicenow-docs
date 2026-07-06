---
title: "Cancel Incident"
aliases:
  - Cancel Incident
tags:
  - servicenow-dev-program
  - code-snippet
  - cancel-incident
  - ui-actions
---

# Cancel Incident UI Action

A UI Action in ServiceNow is a script that defines an action or button within the platform's user interface. It enables users to perform specific operations on forms and lists, such as creating, updating, or deleting records, or executing custom scripts. UI Actions enhance the user experience by providing functional buttons, links, or context menus.

## Overview

This UI Action allows users to cancel incidents directly from the incident form. It provides a confirmation dialog to prevent accidental cancellations and updates the incident state to "Cancelled" (state value 8) when confirmed.

## Features

- **Confirmation Dialog**: Uses GlideModal to display a confirmation prompt before cancelling
- **State Management**: Updates incident state to "Cancelled" (value 8)
- **Client-Side Validation**: Runs client-side for better user experience
- **Conditional Display**: Only shows when incident state is "New" (state value 1)

## Configuration

Create a UI Action with the following field values:

**Name**: Cancel Incident

**Action Name**: cancel_incident

**Table**: Incident [incident]

**Client**: checked (true)

**Onclick**: cancelIncident();

**Condition**: current.state == '1'

**Script**: Use the provided script.js file

## Usage

1. Navigate to an incident record in "New" state
2. Click the "Cancel Incident" button
3. Confirm the action in the modal dialog
4. The incident state will be updated to "Cancelled"

## Technical Details

- **Client-Side Function**: `cancelIncident()` - Displays confirmation modal
- **Server-Side Function**: `serverCancel()` - Updates the incident state
- **Modal Configuration**: Uses `glide_ask_standard` modal with custom title
- **State Value**: Sets incident state to '8' (Cancelled)

## Prerequisites

- User must have write access to the incident table
- Incident must be in "New" state (state = 1) for the UI Action to be visible

## Notes

- This UI Action only appears on incident forms when the state is "New"
- The confirmation dialog helps prevent accidental cancellations
- The server-side script executes only after user confirmation

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Incident/SETUP|Setup Instructions for Cancel Incident UI Action]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
