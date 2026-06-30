---
title: Forms in the classic environment
description: A form displays information from one record in a data table.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/c\_UsingForms.html
release: australia
topic_type: concept
last_updated: "2026-05-11"
reading_time_minutes: 3
breadcrumb: [Working in the classic environment, Working in Core UI, Configure UIs and portals, Configure user experiences]
---

# Forms in the classic environment

A form displays information from one record in a data table.

**Note:** This content pertains to the classic environment, which refers to working in [[lists-configurable-workspace|lists]] of records and on record [[form-configurable-workspace|forms]] directly, not in the [[workspace-landing-page|Configurable Workspace interface]]. You can work in the classic environment with Next Experience active, or with it inactive, which is referred to as [[c_UI16|Core UI]] \(formerly known as UI16\).

The specific information on a form depends on the type of record displayed. Users can view and edit records in forms. Administrators can [[configure-onboarding-modals|configure]] what appears on forms.

\[Omitted image "FormElementsUI16.png"\] Alt text: Annotated diagram showing the main elements of a form, including the header, fields, sections, related links, and related lists

<table id="tbl_FormElements"><thead><tr><th>

Form element

</th><th>

Function

</th></tr></thead><tbody><tr><td>

Form header

</td><td>

Provides navigation tools and actions related to the record.

</td></tr><tr><td>

Fields

</td><td>

Stores specific data about the record.

</td></tr><tr><td>

Sections

</td><td>

Groups related information on the form. To enable or turn off form tabs, select the gear icon in the banner frame \(\[Omitted image "Gear\_icon\_Heisenberg.png"\] Alt text:\) and toggle the **Tabbed forms** option. Users can select icons to collapse \(\[Omitted image "Hide\_form\_section\_UI15.png"\] Alt text:\) or expand \(\[Omitted image "Show\_form\_section\_UI15.png"\] Alt text:\) form sections when tabbed forms are turned off. When you collapse or expand a form section, your selection is saved as a user preference. The next time you access a record that uses the same form, the same sections are collapsed or expanded.

</td></tr><tr><td>

Related links

</td><td>

Provides access to additional functions based on record type and system setup. Administrators can add related links to forms using UI actions.

</td></tr><tr><td>

Related lists

</td><td>

Displays records in other tables that have relationships to the current record.

</td></tr><tr><td>

Embedded lists

</td><td>

Users can edit related lists without navigating away from the form. Changes are saved when the form is saved.

</td></tr><tr><td>

Response time indicator

</td><td>

Appears at the bottom of some forms to indicate the processing time required to display the form.

</td></tr></tbody>
</table>-   **[[form-header-by-version|Form headers for UI versions]]**  
Core UI and UI15 each have a different form header that offers different navigation icons.
-   **[[c_FormContextMenu|Form context menu]]**  
The form context menu provides controls based on the table and user access rights. Administrators can customize some of the options available on a context menu using UI actions.
-   **[[c_FormFields|Form fields]]**  
A field represents an individual item of data on a record.
-   **[[navigate-using-url|Navigate to a record or module using a URL]]**  
Users can navigate to a record or module directly by using a URL. This topic explains the URL schema by which the system renders pages.
-   **[[configure-activity-filters|Configure the activity filter]]**  
The activity formatter contains a filter that lets users select which of the available fields to show in the activity list.
-   **[[c_EmbeddedLists|Embedded lists or Related lists]]**  
Some forms may show related lists as embedded. Changes to embedded lists are saved when the form is saved.
-   **[[c_RelatedLists|Related lists]]**  
Related lists appear on forms and show records in tables that have relationships to the current record.
-   **[[t_EditingInForms|Edit a form]]**  
You can edit a record in the form view. You can also insert a record, apply a template, and cancel changes to the record.
-   **[[t_PersonalizeAForm|Personalize a form]]**  
When the form personalization feature is activated, users can personalize fields to appear on a specific form view according to individual preferences. Form personalization is available in Core UI.
-   **[[t_UseAWatchList|Add users to a watch list]]**  
Watch lists enable you and others to subscribe to notifications of a task.
-   **[[t_AddingAnAttachment|Add and manage attachments]]**  
You can upload a file as an attachment to an incident, a knowledge article, a change request, or to another type of record.
-   **[[enable-next-experience-email-client-core-ui|Set up the Next Experience email client in the Core UI]]**  
Access email features from the Next Experience in the Core UI.
-   **[[Documentviewer|Document Viewer]]**  
Document Viewer enables you to view documents directly in the ServiceNow AI Platform rather than having to download them.
-   **[[c_Checklists|Checklists]]**  
Checklists provide a simple way to track the progress of tasks without creating additional records. Checklists can be added to the form view of any table that extends Task \[task\].

**Parent Topic:**[[working-in-classic-lists-and-forms|Working in the classic environment]]

**Related topics**  


[UI actions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_UIActions.md)

## Related

- [[workspace-landing-page|Configurable Workspace UI]]
- [[form-header-by-version|Form headers for UI versions]]
- [[c_FormContextMenu|Form context menu]]
- [[c_FormFields|Form fields]]
- [[navigate-using-url|Navigate to a record or module using a URL]]
- [[configure-activity-filters|Configure the activity filter]]
- [[c_EmbeddedLists|Embedded lists or Related lists]]
- [[c_RelatedLists|Related lists]]
- [[t_EditingInForms|Edit a form]]
- [[t_PersonalizeAForm|Personalize a form]]
- [[t_UseAWatchList|Add users to a watch list]]
- [[t_AddingAnAttachment|Add and manage attachments]]
- [[enable-next-experience-email-client-core-ui|Set up the Next Experience email client in the Core UI]]
- [[Documentviewer|Document Viewer]]
- [[c_Checklists|Checklists]]
- [[working-in-classic-lists-and-forms|Working in the classic environment]]
- [[lists-configurable-workspace|Lists]]
- [[form-configurable-workspace|Forms]]
- [[c_UI16|Core UI]]
- [[configure-onboarding-modals|Configure]]
