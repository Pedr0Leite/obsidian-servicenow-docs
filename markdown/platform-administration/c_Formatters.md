---
title: Using formatters
description: A formatter is a form element used to display information that is not a field in the record. Add formatters to a form by configuring the form.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/c\_Formatters.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Administer, Form administration, Forms, fields, and lists, Configure core features, Administer the ServiceNow AI Platform]
---

# Using formatters

A formatter is a form element used to display information that is not a field in the record. Add formatters to a form by configuring the form.

<table id="table_pjt_gpn_t4"><thead><tr><th>

Formatter

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Activity formatter

</td><td>

Displays the list of activities, or history, on a task form.

 For an example of an activity formatter, see [[c_ActivityFormatter|Activity formatter]].

</td></tr><tr><td>

Process flow formatter

</td><td>

Displays the different stages in a linear process flow across the top of a record.

 For an example of a process flow formatter, see [[r_ProcessFlowFormatter|Process flow formatter]].

</td></tr><tr><td>

Parent breadcrumbs formatter

</td><td>

Provides breadcrumbs to show the parent or parents of the current task.

 For an example of a parent breadcrumbs formatter, see [[t_TaskParentBreadcrumbsFormatter|Parent breadcrumbs formatter]].

</td></tr><tr><td>

[[approval-summarizer|Approval summarizer formatter]]

</td><td>

Displays dynamic summary information about the request being approved.

 For an example of an approval summarizer formatter, see [Approval summarizer formatter](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_ApprovalSummarizerFormatter.md).

</td></tr><tr><td>

CI relations formatter

</td><td>

Displays on the CI form a toolbar for viewing the relationships between the current CI and related CIs.

 For an example of CI relations formatter icons, see [CI relations formatter](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_CIRelationsFormatterNG.md).

</td></tr></tbody>
</table>**Note:** Formatter elements cannot be exported to PDF. When exporting PDF data from a form, any formatter elements added to the form are not displayed in the PDF output.

To create a custom formatter, create a UI macro to define content for the formatter, then create a formatter that refers to the UI macro. You can then add the formatter to a form.

-   **[[t_CreateAUIMacro|Create a UI macro for a formatter]]**  
Create a UI macro to define the content that the formatter displays.
-   **[[t_CreateAFormatter|Create a formatter and add it to a form]]**  
Create the formatter after creating the UI macro that defines the content.
-   **[Activity formatter](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_ActivityFormatter.md)**  
The activity formatter provides an easy way to track items not saved with a field in the record, for example, [[r_JournalFields|journal fields]] like comments and work notes.
-   **[Process flow formatter](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_ProcessFlowFormatter.md)**  
The process flow formatter provides a graphical summary of the stages in a process. The formatter is typically shown at the top of forms that are part of a process.
-   **[Parent breadcrumbs formatter](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_TaskParentBreadcrumbsFormatter.md)**  
The parent breadcrumbs formatter on the Task table provides breadcrumbs that show the parent or parents of the current task. This formatter can be used also on any table that extends Task.
-   **[Approval summarizer formatter](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_ApprovalSummarizerFormatter.md)**  
The approval summarizer formatter creates the summary at the bottom of an approval form.
-   **[[t_UIMacroOverride|Override a formatter with macros]]**  
The system uses formatters to handle complex rendering of specific form elements.
-   **[[limit-activity-stream-entries|Limit the number of activity stream entries]]**  
You can set a system property to limit the number of entries allowed in an activity stream.

**Parent Topic:**[[form-administration|Administering forms on the ServiceNow AI Platform]]

## Related

- [[c_ActivityFormatter|Activity formatter]]
- [[r_ProcessFlowFormatter|Process flow formatter]]
- [[t_TaskParentBreadcrumbsFormatter|Parent breadcrumbs formatter]]
- [[t_CreateAUIMacro|Create a UI macro for a formatter]]
- [[t_CreateAFormatter|Create a formatter and add it to a form]]
- [[t_UIMacroOverride|Override a formatter with macros]]
- [[limit-activity-stream-entries|Limit the number of activity stream entries]]
- [[form-administration|Administering forms on the ServiceNow AI Platform]]
- [[approval-summarizer|Approval summarizer formatter]]
- [[r_JournalFields|Journal fields]]
