---
title: Schedule a meeting from a lead
description: Schedule a client meeting directly from a lead record to associate it with the lead.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/order-management/schedule-meeting-lead.html
release: australia
topic_type: task
last_updated: "2026-06-11"
reading_time_minutes: 1
breadcrumb: [Lead Management, Lead and opportunity apps, Use, Sales Customer Relationship Management]
tags:
  - order-management
  - fulfillment
  - catalog
  - orchestration
  - type-task
---

# Schedule a meeting from a lead

Schedule a client meeting directly from a lead record to associate it with the lead.

## Before you begin

Verify that the Meetings plugin \(sn\_meeting\_mgmt\) is activated.

The lead must be in a non-closed state.

Role required: sn\_meeting\_mgmt.meeting\_creator

## About this task

When you schedule a meeting from a lead, the system automatically associates the meeting with that lead. The meeting then appears in the lead **Meetings** tab.

## Procedure

1.  In the CSM Configurable Workspace, select the **List** \[Omitted image "list-outline-24.svg"\] Alt text: view.

2.  Navigate to **Leads** &gt; **All** and open the lead record.

3.  In the lead header, select **Create** &gt; **Meeting**.

    The **Meeting** option appears only when you have permission to create meetings. The option is hidden when the lead is in a closed state.

4.  Complete the meeting form.

    The meeting form includes tabs for occurrences, participants, and summary. The meeting is automatically associated with the lead.

5.  Select **Save**.


## Result

The meeting is created and linked to the lead. It appears in the **Meetings** tab of the lead record and in the **Upcoming meetings** section of the Priority Activity panel.

## What to do next

To view all meetings for the lead, select the **Meetings** tab.

**Note:** The **Meetings** tab displays both meetings linked directly to the lead and meetings linked to the lead's touchpoints.

**Parent Topic:**[[lead-management-using|Using Lead Management]]

**Related topics**  


[[schedule-meeting-touchpoint|Schedule a meeting from a touchpoint]]

[[manage-touchpoints-lead|Manage touchpoints on a lead]]

[[create-meeting-touchpoints-form|Create new meeting form]]

[[explore-activity-management|Activity Management]]

## Related

- [[lead-management-using|Using Lead Management]]
- [[schedule-meeting-touchpoint|Schedule a meeting from a touchpoint]]
- [[manage-touchpoints-lead|Manage touchpoints on a lead]]
- [[create-meeting-touchpoints-form|Create new meeting form]]
- [[explore-activity-management|Activity Management]]
