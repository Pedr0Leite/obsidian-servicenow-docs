---
title: "General guidelines for configuring an unsupported custom language to translate on an instance"
aliases:
  - KB0690155
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690155
kb_number: KB0690155
last_modified: 2025-01-03
---

## Issue

  
  

# Description

* * *

As per the [documentation](https://docs.servicenow.com/csh?topicname=c_SystemLocalization.html&version=latest "documentation"), "Administrators can also translate an instance into languages other than those provided in the [internationalization plugins](https://docs.servicenow.com/csh?topicname=c_I18NKMInternational.html&version=latest)."

This article will describe general guidelines on how to add an unsupported language to an instance and how it can be used to translate the instance.

**Note**: Support for these guidelines is outside of the scope of Customer Support.

# Procedure

* * *

##### Language Internationalization:

The first step in translating an instance is to install the elements required for translation, including tables to hold the translations, language pickers to allow users to switch between languages, and import set tables and transform maps to aid in importing translations. These elements are all provided in the plugin I18N: Internationalization.

1.  Install plugin "I18N: Internationalization" \[ID: com.glide.i18n\]
2.  Install a language in order to add translations in the translation tables for sample records. (Note: This is not a required step).

##### Add a custom language:

1.  System Localization > Languages
2.  Click New
    -   Name: language name
    -   ID: ID: two-character [ISO 639.2](http://www.loc.gov/standards/iso639-2/php/code_list.php "ISO 639.2") code for the language (Example: "es" for Spanish)
    -   Text Direction: direction of text in this language.
3.  Confirm that the language has been added to "sys\_language" table.

##### Add the language to Language Picker / Dropdown in System Settings:

1.  System Definition > Dictionary
2.  Table: sys\_user and Column name: preferred\_language
3.  Go down to the related lists < Choices
4.  Click "New"
    -   Label: language name
    -   Value: two-character [ISO 639.2](http://www.loc.gov/standards/iso639-2/php/code_list.php "ISO 639.2") code for the language (Example: "es" for Spanish)
    -   Save the record.
5.  Refresh the browser and go to the Homepage.
6.  Click on the Settings icon
7.  Click on Language dropdown to confirm that the language is added to the picker.

##### Add a translation:

ServiceNow stores translation information in these [Translation Tables](https://docs.servicenow.com/csh?topicname=r_TranslationTables.html&version=latest "Translation Tables").

-   Languages `[sys_language]`
-   Translated Name / Field `[sys_translated]`
-   Message `[sys_ui_message]`
-   Field label `[sys_documentation]`
-   Choice `[sys_choice]`
-   Translated Text `[sys_translated_text]`

Note: The Languages table is available only after I18N:Internationalization has been activated.

The translations can be added to any of these tables manually or they can be imported using an Excel File.

[Import a translation from an Excel spreadsheet](https://docs.servicenow.com/csh?topicname=t_ImportATranslationFromExcel.html&version=latest "Import a translation from an Excel spreadsheet")

##### Verifying if the translation worked:

1.  From the System Settings, change the language to custom language.
2.  Navigate to the record for which the translation has been added from one of the tables above. 

## Applicable Versions

* * *

All versions

# Additional Information

* * *

Documentation:

[Translate an Instance](https://docs.servicenow.com/?title=Translating_an_Instance "Translate an Instance")

[Internationalization Support](https://docs.servicenow.com/csh?topicname=p_Localization.html&version=latest "Internationalization Support")
