---
title: "[SAMP]Importing Software Entitlement with Custom Fields"
aliases:
  - KB0854431
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0854431
kb_number: KB0854431
last_modified: 2024-04-08
---

## \[SAMP\]Importing Software Entitlement with Custom Fields

  

## Table of Contents

-     
    
-   [Overview](#mcetoc_1eg4ea5u090)
-   [Example: The Form Contains a Custom Field "Notes"](#mcetoc_1eg4ea5u091)
-   [Other Field Validations](#mcetoc_1eg4ea5u092)

# Overview

* * *

  

If you have added additional fields to the software entitlement table; and customized the entitlement form to display those fields, you can also import values for such fields using the import template. The default template downloaded from the instance will not contain the custom columns. You are required to add those custom columns in the excel template. The column name on template should exactly match the field label on the entitlement table.

# Example: The Form Contains a Custom Field "Notes"

* * *

  

<table class="internaltable" style="height: 1208px;" border="0"><tbody><tr style="height: 10px;"><td style="height: 10px; width: 704px;"><ul style="list-style-position: inside;"><li>This form contains a custom field called “Notes”.</li></ul></td><td style="height: 10px; width: 818px;"><img style="align: baseline;" title="" src="sys_attachment.do?sys_id=8c4ffc89db4cb890dc2beeb5ca9619d0" alt="" width="734" height="322" align="baseline" border="" hspace="" vspace=""></td></tr><tr style="height: 13px;"><td style="height: 13px; width: 1533px;" colspan="2"><br></td></tr><tr style="height: 13px;"><td style="height: 13px; width: 704px;"><ul style="list-style-position: inside;"><li>To import data in this field, you must add a column in the excel template making sure the name of this column is exactly same as the field label on entitlement form</li></ul></td><td style="height: 13px; width: 818px;"><img style="align: baseline;" title="" src="sys_attachment.do?sys_id=004ffc89db4cb890dc2beeb5ca9619fa" alt="" width="737" height="229" align="baseline" border="" hspace="" vspace=""></td></tr><tr style="height: 13px;"><td style="height: 13px; width: 1533px;" colspan="2"><br></td></tr><tr style="height: 13px;"><td style="height: 13px; width: 704px;"><ul style="list-style-position: inside;"><li>Once you import this template, the entitlement should get created with ‘notes’ field populated.</li></ul></td><td style="height: 13px; width: 818px;"><img style="align: baseline;" title="" src="sys_attachment.do?sys_id=4c4ffc89db4cb890dc2beeb5ca9619fc" alt="" width="760" height="237" align="baseline" border="" hspace="" vspace=""></td></tr><tr style="height: 13px;"><td style="width: 1533px; height: 13px;" colspan="2"><br></td></tr><tr style="height: 166px;"><td style="width: 704px; height: 166px;"><ul style="list-style-position: inside;"><li>If the column name in the excel does not match the field name on the form, the entitlement will not be created and an import error will get generated. You can fix the error on the import error record itself and create the entitlement right from there instead of attempting to import the excel again.</li></ul><p><br></p><ul style="list-style-position: inside;"><li>For example – in this case there is a typo in the field. Instead of “Notes”, it is misspelt as “Nots”</li></ul></td><td style="width: 818px; height: 166px;"><img style="align: baseline;" title="" src="sys_attachment.do?sys_id=884ffc89db4cb890dc2beeb5ca9619ff" alt="" width="710" height="164" align="baseline" border="" hspace="" vspace=""></td></tr><tr style="height: 13px;"><td style="width: 704px; height: 13px;"><br></td><td style="width: 818px; height: 13px;"><br></td></tr><tr style="height: 366px;"><td style="width: 704px; height: 366px;"><ul style="list-style-position: inside;"><li>While importing this sheet, an error is generated</li></ul></td><td style="width: 818px; height: 366px;"><img style="align: baseline;" title="" src="sys_attachment.do?sys_id=d44f30c9db4cb890dc2beeb5ca961902" alt="" width="756" height="364" align="baseline" border="" hspace="" vspace=""></td></tr><tr style="height: 10px;"><td style="width: 1533px; height: 10px;" colspan="2"><br></td></tr><tr style="height: 354px;"><td style="width: 704px; height: 354px;"><ul style="list-style-position: inside;"><li>The error description specifically tells you which custom column was not found and a new related list will appear with the list of custom columns you were trying to import with their corresponding values</li></ul></td><td style="width: 818px; height: 354px;"><img style="align: baseline;" title="" src="sys_attachment.do?sys_id=144f30c9db4cb890dc2beeb5ca961905" alt="" width="712" height="352" align="baseline" border="" hspace="" vspace=""></td></tr><tr style="height: 13px;"><td style="width: 1533px; height: 13px;" colspan="2"><br></td></tr><tr style="height: 120px;"><td style="width: 704px; height: 120px;"><ul style="list-style-position: inside;"><li>You can fix the error right here by entering the correct column name.</li></ul></td><td style="width: 818px; height: 120px;"><img style="align: baseline;" title="" src="sys_attachment.do?sys_id=dc4f30c9db4cb890dc2beeb5ca961920" alt="" width="672" height="118" align="baseline" border="" hspace="" vspace=""></td></tr></tbody></table>

# Other Field Validations

* * *

  

<table class="internaltable" style="height: 52px;" border="0"><tbody><tr style="height: 13px;"><td style="height: 13px; width: 1533px;"><p>There are other field validations performed while importing custom fields to ensure data integrity. Below are some of the other errors that you may see –</p></td></tr><tr style="height: 13px;"><td style="height: 13px; width: 1533px;"><ul style="list-style-type: circle; list-style-position: inside;"><li>The custom field '&lt;field name&gt;' must be a number</li><li>The custom field '&lt;field_name&gt;' has an unsupported type: '&lt;field type&gt;'</li><li>The custom column field '&lt;field_name&gt;' contains an invalid reference to the '&lt;table_name&gt;' table</li><li>The custom column field '&lt;field_name&gt;' is mandatory but was blank</li><li>The custom column field '&lt;field_name&gt;' is mandatory but was not present</li><li>The custom column field '&lt;field_name&gt;' is not a valid formatted date</li><li>The custom field '&lt;field_name&gt;' contains an invalid currency value. Currency values are expected to be formatted with the currency code followed by a semicolon followed by the value. eg: USD;123.45"<br></li></ul></td></tr></tbody></table>
