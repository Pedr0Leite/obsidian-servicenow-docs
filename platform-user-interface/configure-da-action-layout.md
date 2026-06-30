---
title: Configure a form action layout on a workspace page
description: Add a form action layout to a workspace page in UI Builder.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/configure-da-action-layout.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure action buttons, Declarative actions, Administer, Configurable Workspace UI, Configure UIs and portals, Configure user experiences]
---

# Configure a form action layout on a workspace page

Add a form action layout to a workspace page in UI Builder.

## Before you begin

Role required: admin

## About this task

A form action layout combines multiple [[configurable-workspace-glossary|form action layout items]] and [form action layout groups](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/configurable-workspace-glossary.md) into a single table-based layout that determines which actions appear on the form.

The form action layout chosen to appear on the form is determined in the following ways:

-   **Form Controller**

    If a form action layout is assigned directly to the Form Controller in UI Builder, that layout is used.

-   **Specificity**

    If a form action layout isn't assigned to the Form Controller, the layout is chosen based on specificity calculated from the layout's table and action configuration.

    When two form action layouts have identical specificity values, the layout with the lower Order field is chosen.


## Procedure

1.  Open your workspace experience in UI Builder.

    For instructions, see [[open-your-configurable-workspace-experience-in-ui-builder|Open a Configurable Workspace experience in UI Builder]].

2.  Select or create a page that contains the Form component.

    For example, select a record page.

    For instructions on creating a workspace page in UI Builder, see [[create-configurable-workspace-page-uib|Create a Configurable Workspace page]].

3.  From the Data and scripts tree, select the **Form Controller**.

4.  Select the **[[configure-onboarding-modals|Configure]]** tab and expand the **Advanced** section.

5.  In the Action layout property, select a UX Form Actions Layout record.

6.  Select **Save**.


## Result

The actions specified in the form action layout appear on the workspace page.

## Related

- [[configurable-workspace-glossary|Configurable Workspace glossary]]
- [[create-configurable-workspace-page-uib|Create a Configurable Workspace page]]
- [[open-your-configurable-workspace-experience-in-ui-builder|Open a Configurable Workspace experience in UI Builder]]
- [[configure-onboarding-modals|Configure]]
