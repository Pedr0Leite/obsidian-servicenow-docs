---
title: "Determining that you are referencing the correct field"
aliases:
  - KB0547222
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547222
kb_number: KB0547222
last_modified: 2025-01-26
---

## Determining that you are referencing the correct field

  

### Issue

  
  

# Description

* * *

In some cases fields have very similar labels and the field that you are adding to a form is not actually the desired one. You can correct this by simply personalizing the form to have the desired field. For example, you may have a field with the label Timecard and another field with the label Time Card. In such situation it might be easy to make a mistake.

# Procedure

* * *

To confirm and correct that the desired field is being used on the form take the following actions:

1.  Go to System Definition > Dictionary.
2.  Search for the column name of your field. This is the actual database column name as opposed to the label such as u\_timecard (rather than Time Card).
3.  If you do not know the column name then just list all the fields in your table in the dictionary and locate your field that way.
4.  Identify the label value of your field.
5.  Personalize your form and confirm that the value displayed on the form does match your label name exactly. If it does not, then choose the exact matching name from the field.

# Applicable Versions

* * *

ALL
