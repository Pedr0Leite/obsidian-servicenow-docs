---
title: Customizing fields on the ServiceNow AI Platform
description: Administrators can add and customize fields in a table, as well as make fields mandatory, highlight list fields, specify default values, and assign record numbering.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/customize-fields-now-platform-landing.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Field administration, Forms, fields, and lists, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Customizing fields on the ServiceNow AI Platform

Administrators can add and customize fields in a table, as well as make fields mandatory, highlight list fields, specify default values, and assign record numbering.

-   **[[t_CreatingNewFields|Add and customize a field in a table]]**  
Administrators can add new fields to a table to store and display data.
-   **[[t_MakingAFieldMandatory|Make a field mandatory]]**  
Fields can be marked as mandatory, meaning they must contain a value before the record can be saved. Mandatory fields are marked with a field status indicator before the label.
-   **[[t_ChangeFieldLabelOrHint|Change the field label or hint]]**  
You can change a field's label or the text that appears as a hint when you point your mouse device to the field.
-   **[[t_DeleteFields|Delete a field from a table]]**  
You can delete custom fields that you created. Custom fields begin with **u\_**. It is recommended that you remove the field from forms and lists instead of deleting it.
-   **[[highlight-list-fields-platform|Highlight list fields]]**  
Color fields in lists to call an agent's attention to them.
-   **[[t_ModifyingStringFieldLength|Modify string field length]]**  
You can modify the maximum character limit for a string field.
-   **[[t_SpecifyingADefaultValue|Specify a default field value]]**  
A default value populates a value in a field when a new record is created.
-   **[[t_MakingAFieldDependent|Make a field dependent]]**  
A choice or [[reference-email-admin|reference]] field can be declared dependent on another field on the same table to limit the values available to select based on the value of the dependent field.
-   **[[t_RequiringUniqueValuesForAField|Require unique values for a field]]**  
The system allows you to require that a field's values be unique. When this is done, the system will not let two records have the same value for that field.
-   **[[t_DefineFieldStyles|Define field styles]]**  
Field styles enable you to declare individual CSS styles for a field in a list or form.
-   **[[c_ManagingRecordNumbering|Record numbering]]**  
In the base system, several tables are numbered, including Incident, Problem, Change Request, and Knowledge. You can also use these numbers anywhere that script is present, for example to generate watermarks for emails. Records in tables can be numbered automatically.

**Parent Topic:**[[now-platform-forms-fields-lists|ServiceNow AI Platform forms, fields, and lists]]

## Related

- [[t_CreatingNewFields|Add and customize a field in a table]]
- [[t_MakingAFieldMandatory|Make a field mandatory]]
- [[t_ChangeFieldLabelOrHint|Change the field label or hint]]
- [[t_DeleteFields|Delete a field from a table]]
- [[highlight-list-fields-platform|Highlight list fields]]
- [[t_ModifyingStringFieldLength|Modify string field length]]
- [[t_SpecifyingADefaultValue|Specify a default field value]]
- [[t_MakingAFieldDependent|Make a field dependent]]
- [[t_RequiringUniqueValuesForAField|Require unique values for a field]]
- [[t_DefineFieldStyles|Define field styles]]
- [[c_ManagingRecordNumbering|Record numbering]]
- [[now-platform-forms-fields-lists|ServiceNow AI Platform forms, fields, and lists]]
- [[reference-email-admin|Reference]]
