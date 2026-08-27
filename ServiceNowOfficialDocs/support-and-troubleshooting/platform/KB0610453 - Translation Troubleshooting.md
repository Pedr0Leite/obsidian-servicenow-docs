---
title: "Translation Troubleshooting"
aliases:
  - KB0610453
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0610453
kb_number: KB0610453
last_modified: 2026-03-11
---

## Issue

This article will provide an overview of how translations work within the platform and how to troubleshoot issues that arise when translating in the ServiceNow platform.

## Resolution

## Installation procedure

**Where to find the Internationalization Plugins**

All the plugins can be found by navigating to **System Definition > Plugins** and searching for **i18n** in the plugin name.

**The I18N: Internationalization Plugin (com.glide.i18n)**

This plugin provides the elements necessary for translating an instance, but it does not contain any pre-loaded translations. Those are covered by the additional components mentioned below. Note that instances can have all the required individual language plugins installed after the main com.glide.i18n has been installed.

**Individual Language Plugins (com.glide.i18n.\*)**

These plugins provide data for individual languages and have the **I18N: Internationalization** plugin as a dependency. Translations are provided for the majority of base system elements, though, as with any change to an instance, evaluation and testing in a sub-prod is recommended to ensure all elements are translated. (More information is provided below.)

**Tables installed with I18n**

-   Language (sys\_language)
-   Translated Name / Field (sys\_translated)
-   Messages (sys\_ui\_message)
-   Field Label (sys\_documentation)
-   Translated Text (sys\_translated\_text)

## Translating an Instance

**Choices (sys\_choice table)**

Choice records can be found by navigating to **System Localization > Choices**. These records store all choices that appear in choice fields, or string fields with choices assigned to them.

Below is an example of a translated choice. It is the Critical Priority choice on the task table. As you can see, there are four records with the same value, however, each one has a:

-   Language field represented with 2 character abbreviations (as defined by the iso639-2 standard)
-   Label field containing the translated text for that language  

<table border="1" align="center"><tbody><tr><td><img id="pasted_img_1999d1801998dd401998411019985870" style="border-width: 1px; border-image-width: 1;" title="Choice field translation on the Label values" src="https://support.servicenow.com/sys_attachment.do?sys_id=e0fa1d4a47fc2250b8a4aa25126d432b" alt="language translations on the on Choice Field Label values" width="773" height="206" align="bottom" border="1"></td></tr></tbody></table>

_An example of translations for the “Critical” choice on the Priority field on task (English, French, Japanese, and French (Canada)_ 

**Translated Name / Field (sys\_translated)**

Translated Name records can be found by navigating to **System Localization > Translated Names / Fields**. These records store translated values for text fields where the field type is **translated\_field**.

<table align=""><tbody><tr><td><strong>Field</strong></td><td><strong>How used</strong></td></tr><tr><td>Table</td><td>The table for which the translation is used. This field can be left blank is desired and is used as a translation in any table.&nbsp;</td></tr><tr><td>Element</td><td>The element to be translated. If left blank, the translation applies to any applicable field matching the Value on the table (or any table if the table field is also blank).</td></tr><tr><td>Language</td><td>The two-character abbreviation for the language, as defined by the iso639-2 standard.</td></tr><tr><td>Value</td><td>The actual&nbsp;value contained in the record’s&nbsp;field.</td></tr><tr><td>Label (translate)</td><td>The translated value of the field.&nbsp;</td></tr></tbody></table>

**Messages (sys\_ui\_message)**

Message records can be found by navigating to **System Localization > Messages**. These records contain translations for informational messages, confirmation messages, error messages, and other types of system messages. Unlike the other translation tables, messages are only used when a script uses a gs.getMessage call.

<table align=""><tbody><tr><td><strong>Field</strong></td><td><strong>How used</strong></td></tr><tr><td>Key</td><td>The text to be translated. The value used in the getMessage call is checked against this field.</td></tr><tr><td>Language</td><td>The language for this particular translation. Unlike the other tables, this field is a choice field populated with the currently installed languages.&nbsp;</td></tr><tr><td>Message</td><td>The translated value returned by the&nbsp;gs.getMessage method.&nbsp;&nbsp;</td></tr></tbody></table>

**Field Label (sys\_documentation)**

Field labels can be found by navigating to **System Localization > Field Labels**. These records contain translations for the text of table names along with the singular and plural labels for each field in the table. This also includes the “hint” text that pops up when hovering over a field name. 

<table align=""><tbody><tr><td><strong>Field</strong></td><td><strong>How used</strong></td></tr><tr><td>Table</td><td>The table for the translation.</td></tr><tr><td>Element</td><td>The element for the translation. This is usually the field on that table.&nbsp;</td></tr><tr><td>Language</td><td>The two-character abbreviation for the language, as defined by the iso639-2 standard.&nbsp;</td></tr><tr><td>Label</td><td>The translated label for the item to be translated.</td></tr><tr><td>Plural</td><td>The pluralized translated label for the item to be translated.&nbsp;</td></tr><tr><td>Help</td><td>The translation for the help text for the field.&nbsp;</td></tr><tr><td>Hint</td><td>The translation for the hint text for the field.&nbsp;</td></tr></tbody></table>

**Translated Text (sys\_translated\_text)**

Translated Text records can be found by navigating to **System Localization > Translated Text**. These records store translations for fields with the field type **translated\_text** or **translated\_html**. These translations can be record-specific, unlike the other types, which makes it useful for knowledge articles, problems, etc. Following is a breakdown:

<table align=""><tbody><tr><td><strong>Field</strong></td><td><strong>How used</strong></td></tr><tr><td>Document</td><td>An&nbsp;internal identifier of the record to which this translation applies.</td></tr><tr><td>Field Name</td><td>The&nbsp;field this translated text appears in, for example, Close notes.&nbsp;</td></tr><tr><td>Language</td><td>The&nbsp;language to which the text is translated.&nbsp;</td></tr><tr><td>Table Name</td><td>&nbsp;The&nbsp;table to which this translation applies.</td></tr><tr><td>Value</td><td>The&nbsp;translated text that the user sees.&nbsp;</td></tr></tbody></table>

## **The I18N Debugger**

Finding which elements are translated into which tables is not always easy. Fortunately, the I18N debugger tool can be enabled by navigating to **System Localization > Enable I18N Debugging**. After the debugger is enabled, a three or four-letter code appears next to each element to let you know where this translation is being done (or should be done if it is not yet translated).

Following are the codes and the tables to which they correlate:

-   TRF = Translated Names / Fields
-   MSG = Messages
-   GMLD = Field Labels
-   TRT = Translated Text
-   CHC = Choices (Only in Eureka or higher)  

![I18N debugger enable to show 4 letter code to distinguish default and translated field labels value types](https://support.servicenow.com/sys_attachment.do?sys_id=e0fa1d4a47fc2250b8a4aa25126d4326 " I18N Debugger for Field labels and values")

_A portion of an Incident form with I18N Debugging Enabled_

## _Troubleshooting_

If a translation has been created and does not appear to be working correctly, here are a few areas to check:

**Spelling**

Are the Key fields used in the translation spelled correctly? Any difference between what is in the translation record and what is on the element to be translated causes the translation to fail. A similar issue can occur with hidden characters. This usually happens when text is pasted into the field from another source. To rule this situation out, try clearing the value and typing it back in manually. >

**Using the Wrong Translation Table**

Another possible issue is using the wrong table to handle a translation. If you are not sure if this is the situation, view the item to be translated using the I18N Debugger described earlier in this article. 

**Plugin Logs**

Plugin logs can be found on a related list on the plugin record or at sys\_plugin\_log\_list.do. If a translation seems incomplete after an installation, the logs may expose issues to look into. For example, look for log entries containing the word “skipping.”  This can happen if the instance already has a translation or if the translation was deleted from a previous install attempt.

**Exceptions  
  
**

**Welcome Page Section (sys\_home)** records contain the user/password fields on an instance login page:

<table border="1" align="center"><tbody><tr><td><img id="pasted_img_8273cc082763108272ca082744008271" style="border-width: 1px; border-image-width: 1;" title="Welcome Page Section example" src="https://support.servicenow.com/sys_attachment.do?sys_id=64fa1d4a47fc2250b8a4aa25126d432e" alt="Welcome Page Section example" width="836" height="348" align="bottom" border="1"></td></tr></tbody></table>

_  
An example Welcome Page Section from an Out of Box instance_

Welcome Page Section records have a language field that acts as a condition, preventing the content of the record from displaying when the user’s session is not using the language in this field. The best way to translate these is to insert a record with the new language and then manually translate the new record.

## Additional Information

#### Documentation

-   [Language internationalization support](https://docs.servicenow.com/csh?topicname=c_LangInternationalizationSupport.html&version=latest "Language internationalization support")
-   [Translation modes](https://docs.servicenow.com/bundle/sandiego-platform-administration/page/administer/localization-framework/concept/translation-modes.html "Translation modes")
-   [Locate translatable strings](https://docs.servicenow.com/csh?topicname=c_TranslateNewCustomizations.html&version=latest "Locate translatable strings")
-   [Translating text fields](https://docs.servicenow.com/csh?topicname=c_UseTranslatedText.html&version=latest "Translating text fields")
-   [CMS translation](https://docs.servicenow.com/csh?topicname=c_CMSTranslation.html&version=latest "CMS translation")
