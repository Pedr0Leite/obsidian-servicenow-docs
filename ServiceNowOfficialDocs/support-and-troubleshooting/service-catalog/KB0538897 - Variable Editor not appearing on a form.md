---
title: "Variable Editor not appearing on a form"
aliases:
  - KB0538897
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538897
kb_number: KB0538897
last_modified: 2026-06-29
---

## Variable Editor not appearing on a form

  

### Issue

The Variable Editor field does not appear on a target record form, or variables within the editor do not behave as expected.

### Symptoms

-   No variables appear on the form
-   Variable is not visible
-   Variable cannot be updated on the form
-   Variable values are wiped out
-   A variable marked as required does not enforce that behavior
-   A variable not marked as required is behaving as required
-   Variable is read-only when it should not be
-   Variable is not read-only when it should be

### Release

All supported releases

### Cause

The Variable Editor may be missing from the form layout, or the UI Formatter records that control it may be inactive or misconfigured. Variables that do not behave as expected are often affected by conflicting configuration across multiple settings points, including the variable itself, client scripts, and UI policies.

### Resolution

**Check the form layout**

1\. Navigate to the target record.  
2\. Select Personalize Form Layout.

![Interface for customizing fields on an Incident form, showing available and selected options.](/sys_attachment.do?sys_id=521ce51d97f1cbd40ed83bbe2153af6b "Interface for customizing fields on an Incident form, showing available and selected options.")  
3\. Confirm that the Variable Editor field is added to the form. The exact name of the list item may vary depending on the target record.

If you do not see the Variable Editor option in the list, the UI Formatter records may be misconfigured. Continue to the next section.

**Check UI Formatter records**

1\. Navigate to System UI > Formatters.

![UI Formatters list showing variable editors for different tables and their active status.](/sys_attachment.do?sys_id=ca1c251d97f1cbd40ed83bbe2153afcc "UI Formatters list showing variable editors for different tables and their active status.")  
2\. Confirm that the following four records are present, active, and unmodified:

-   Change Variable Editor (change\_request: com\_glideapp\_questionset\_default\_question\_editor)
-   Incident Variable Editor (incident: com\_glideapp\_questionset\_default\_question\_editor)
-   Variable Editor (sc\_req\_item: com\_glideapp\_servicecatalog\_veditor)
-   Variable Editor (sc\_task: com\_glideapp\_servicecatalog\_veditor)

If any of these records are missing, inactive, or modified, the Variable Editor may not appear in the Personalize Form list.

In the base system, the Variable Editor is only available for Incident, Change, Request Item, and Service Catalog Task. To use the Variable Editor on any other form, create a custom formatter.

**Create a custom formatter for other tables**

1\. Navigate to System UI > Formatters.  
2\. Select New.  
3\. Enter the following values:

   For Fuji and later releases:

<table style="border-collapse: collapse; width: 41.2115%;" border="1"><colgroup><col style="width: 21.385%;"><col style="width: 78.5486%;"></colgroup><tbody><tr><td><span style="font-family: lato;">Field</span></td><td><span style="font-family: lato;">Value</span></td></tr><tr><td><span style="font-family: lato;">Name</span></td><td><span style="font-family: lato;">Variable Editor</span></td></tr><tr><td><span style="font-family: lato;">Formatter</span></td><td><span style="font-family: lato;">com_glideapp_questionset_default_question_editor</span></td></tr><tr><td><span style="font-family: lato;">Table</span></td><td><span style="font-family: lato;">Select the table whose form you want the formatter available on</span></td></tr><tr><td><span style="font-family: lato;">Type</span></td><td><span style="font-family: lato;">Formatter</span></td></tr><tr><td><span style="font-family: lato;">Active</span></td><td><span style="font-family: lato;">True</span></td></tr></tbody></table>

   For pre-Fuji releases:

<table style="border-collapse: collapse; width: 41.3737%;" border="1"><colgroup><col style="width: 25.924%;"><col style="width: 74.0121%;"></colgroup><tbody><tr><td><span style="font-family: lato;">Field</span></td><td><span style="font-family: lato;">Value</span></td></tr><tr><td><span style="font-family: lato;">Name</span></td><td><span style="font-family: lato;">Variable Editor</span></td></tr><tr><td><span style="font-family: lato;">Formatter</span></td><td><span style="font-family: lato;">com.glideapp.questionset.DefaultQuestionEditor</span></td></tr><tr><td><span style="font-family: lato;">Table</span></td><td><span style="font-family: lato;">Select the table whose form you want the formatter available on</span></td></tr><tr><td><span style="font-family: lato;">Type</span></td><td><span style="font-family: lato;">Component</span></td></tr><tr><td><span style="font-family: lato;">Active</span></td><td><span style="font-family: lato;">True</span></td></tr></tbody></table>

4\. Select Submit.  
5\. Navigate to the form, personalize the layout, and confirm the Variable Editor appears.

**Check for conflicting client scripts or UI policies**

If the form layout is correct and all formatter settings are configured correctly but the Variable Editor still does not appear, a client script or UI policy may be hiding it.

This can occur when a variable has the same name as a field on the form. For example, if a variable and a field are both named Impact, a client script that hides the Impact field may also hide the variable, making it appear as though the Variable Editor is not present.

Review your client scripts and UI policies to ensure none of them apply logic to variables that share names with fields on the target record.

**Check variable configuration on the catalog item**

If variables are visible but not behaving as expected, the issue is likely in the variable's own configuration. Variables can be configured at multiple points, and conflicting settings cause unexpected behavior.

To review variable configuration:

1\. Navigate to Service Catalog > Maintain Items.  
2\. Select the item that is causing the issue.  
3\. Open the catalog item form and scroll to the Variables related list at the bottom.  
4\. Open the variable that is causing the issue.  
5\. Review the following settings:

   Required behavior  
   Required behavior can be set in the Mandatory field, in a client script, or in a UI policy. Confirm that these settings do not conflict with each other. Conflicting configurations produce unpredictable required behavior.

   Read-only behavior  
   Read-only behavior can also be set in multiple places. Using more than one method for the same variable causes unexpected behavior. Confirm only one mechanism controls the read-only state.

   Default value  
   The Default value and Dynamic default value fields support scripting. These can cause confusion when fields appear to populate without user input. Review these settings if values appear or change unexpectedly.

   Active  
   Confirm the Active field is set to true. An inactive variable does not appear on the form.

  Read roles  
   If the variable is correctly configured for all the above settings but is still not visible, check the Read roles field. If no roles are assigned, the variable is visible to everyone. If roles are assigned, only users with those roles see the variable.
