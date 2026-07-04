---
title: "NowSupport KB Article Typesetting Conventions"
aliases:
  - KB0623104
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623104
kb_number: KB0623104
last_modified: 2026-06-24
---

## NowSupport KB Article Typesetting Conventions

  

These are general rules that we recommend using when creating KB articles on NowSupport.

 **Note:** Do not apply these typesetting conventions to section headers or to table columns that are dedicated to a specific type of term, such as field names or property names.

### When to Use Bold

Bold these items in the text:

-   Key names, such as **Enter**, **Tab**, and **Shift**.
-   Menus: **Service portal > Widget Instances**
-   Field names (Do not use bold for the word sys\_id in general text. Do bold sys\_id when it is specifically called out as a field.)
-   Button names: **Save**, **Update**
-   Message text, such as error messages: "**Number of rows removed from this list by Security constraints: #**"
-   Business rule names
-   Scheduled job names
-   Related list names
-   UI macro names
-   Workflow activity names
-   Workflow activity input variables  
    -   **Note**: When showing the selections that define a specific condition, use square brackets to enclose each element.
-   Conditions selected in a condition builder, for example **\[Incident state\] \[is\] \[Resolved\]**.
-   Sample URLs that should not be live links (for example, **http://10.0.103.202/users**)
-   Values entered or selected. For example:  
    -   In the **Priority** field, select **4 - Low**.
    -   However, for text that is _typed_ rather than _selected_, use monospace font:
    -   In the **Date** field, enter April 1.
-   Paths in the GUI. For example, **LDAP > LDAP Servers**. (Use a space before and after the > in paths, include section labels.)

### When to Use Italic

Use _italic_ for these items:

-   File extensions such as _.jpg_
-   Folder names
-   Directory paths
-   Script names, script include names

### When to Use a Fixed-Width (monospace) Font

Use a fixed-width font (such as Andale mono) for these items:

-   Brief code snippets in text
-   Class names
-   Attribute names
-   Method names and function names
-   Variables
-   Event names
-   Script macros
-   Database views
-   Configuration parameters used in XML files
-   Other code-like elements that are not listed specifically for other typesetting conventions
-   Property names, for example, mid.version or glide.workflow.long
-   Values entered or typed in

 **Note:** To apply the "Andale Mono" fixed-width font in the HI HTML editor, select the text and choose "Andale Mono" from the **Font Family** drop-down menu.

### When to Use Plain Text

Use plain text for these items, but note the related standards.

-   Table names. Generally, use the table label (common name) whenever identifying a table. If the internal table name is not needed for understanding, omit it. If the internal table name is needed for understanding, present the label and name as they appear in the system: Table Label \[table\_name\] (for example, Configuration Item \[cmdb\_ci\] table).  
      
    If the same table is mentioned multiple times in an article, be sure to give the full table name first (Label \[internal name\] table). Subsequent references can use just the label if the article is intended for administrators or less technical users. If the article is intended for developers or very technical administrators, the table name can be shortened to just the internal table name, in plain text.  
      
    
-   Role names. Capitalize role names as they appear in the system, and always include the word role (for example, itil\_admin role).
-   Form names, List names. View names. Capitalize the form or list name as it appears in the system, but do not capitalize the word "form" or "list" or "view."
-   Form section names. Capitalize the name as it appears on the form, but use plain text. These are different from related list names, which are bold.
-   Application names and module names (except when they appear in a GUI path).
-   Icon names, regardless of whether there is a picture of the icon (for example, reference lookup icon, knowledge search icon).
-   User preference names (for example, glide.ui.javascript\_editor).
-   Discovery probes and classifiers.
-   Server names.
-   Plugin names.
-   Workflow names (capitalize them as they appear in the UI).
-   Workflow condition names (capitalize them as they appear in the UI).
-   sys\_id (the word used in general text; bold if used to reflect the UI).
-   Relationships between CIs, such as "Connected to::Connected by".
-   Window names.
-   Dialog box names.
