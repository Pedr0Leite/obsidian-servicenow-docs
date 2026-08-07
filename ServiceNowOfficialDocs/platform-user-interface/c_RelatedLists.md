---
title: Related lists
description: Related lists appear on forms and show records in tables that have relationships to the current record.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/c\_RelatedLists.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Forms in the classic environment, Working in the classic environment, Working in Core UI, Configure UIs and portals, Configure user experiences]
tags:
  - platform-user-interface
  - type-concept
---

# Related lists

Related lists appear on [[form-configurable-workspace|forms]] and show records in tables that have relationships to the current record.

Users can view and modify information in related lists like any other list. Administrators can [[configure-onboarding-modals|configure]] related lists to appear on forms and in hierarchical [[lists-configurable-workspace|lists]] by [configuring a form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/configure-form-layout.md). Related lists do not have a size limit.

**Note:**

Creating a record using a related list applies the list filter to the record and auto-populates the related field. This behavior applies to [[onboarding-modals-reference|reference]], string, Boolean, and menu fields when the criteria in the filter is set to **is** or **=**.

-   **[[t_SelectRelatedRecords|Select or create records in a related list]]**  
When a form contains a related list, such as the **Incidents** related list in the problem form, you can select existing records or add new ones in the related list.
-   **[[t_ConfigureWhenARelatedListLoads|Configure when a related list loads]]**  
If there are many related lists on a form or many records in the related lists, the form may load slowly. You can improve form response times by configuring related lists to load manually, on demand, or automatically, after the rest of the form loads.
-   **[[t_CreateADefaultFilter|Create a default filter for a related list]]**  
Create a default filter for the records that load when your related list displays.
-   **[[t_ConfigureTheEditOption|Configure the edit option]]**  
You can configure the edit option that allows users to add records to related lists in forms.
-   **[[t_CreateDefinedRelatedLists|Create defined related lists]]**  
You can add default related lists to the form for all users to see when viewing records.
-   **[[t_AddingFieldsToARelatedList|Add fields to selections in a related list]]**  
When you click **Edit** in a related list and select an item, information about the item appears below the list. You can expand the fields that appear for the item to provide more information.
-   **[[t_CreateDefaultRelatedRecSecFilter|Create a default filter for list selector records]]**  
You can set a default filter to restrict which related records users can select when editing a reference field. Default [[c_Filters|filters]] are simple to set up but lack a dynamic filtering element, which prevents the end user from changing the default filter.

**Parent Topic:**[[c_UsingForms|Forms in the classic environment]]

**Related topics**  


[Configure form layout](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/configure-form-layout.md)

[[c_UseLists|Lists in the classic environment]]

## Related

- [[t_SelectRelatedRecords|Select or create records in a related list]]
- [[t_ConfigureWhenARelatedListLoads|Configure when a related list loads]]
- [[t_CreateADefaultFilter|Create a default filter for a related list]]
- [[t_ConfigureTheEditOption|Configure the edit option]]
- [[t_CreateDefinedRelatedLists|Create defined related lists]]
- [[t_AddingFieldsToARelatedList|Add fields to selections in a related list]]
- [[t_CreateDefaultRelatedRecSecFilter|Create a default filter for list selector records]]
- [[c_UsingForms|Forms in the classic environment]]
- [[c_UseLists|Lists in the classic environment]]
- [[form-configurable-workspace|Forms]]
- [[configure-onboarding-modals|Configure]]
- [[lists-configurable-workspace|Lists]]
- [[onboarding-modals-reference|Reference]]
- [[c_Filters|Filters]]
