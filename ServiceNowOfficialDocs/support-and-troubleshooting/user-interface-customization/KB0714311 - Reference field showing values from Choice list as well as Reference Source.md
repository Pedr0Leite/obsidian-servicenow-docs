---
title: "Reference field showing values from Choice list as well as Reference Source"
aliases:
  - KB0714311
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714311
kb_number: KB0714311
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

A Field had been configured as a Reference type, however it was found to also be showing values from a Choice list too. The following screenshot shows the Referenced values within the purple rectangle, and the Choice list ones in the red rectangle.

![](sys_attachment.do?sys_id=1c692ceedb02b450e515c223059619f9)

It was initially identified that this was simply due to the fact that the field in question had actually both a Reference and a Choice list configured against it.

However, having removed the Choice list definition the values still persisted.

# Cause

* * *

Although the Choice list definitions had then been removed, by looking at the exported XML of the field definition, it could be seen that Choice related configuration still existed in fields not exposed on the form. That is, as shown in the top purple rectangle in the following.

![](sys_attachment.do?sys_id=94692ceedb02b450e515c223059619ff)

From this it was identified that this field had originally been configured as a Choice field, and then changed to be one of type Reference. Due to the fields showing in the XML not being exposed on the form by default, it was not noticed that they still had values set against them. Either that, or some one had altered the XML and imported it over the record, causing this corruption.

The result was that the XML was still showing it as both a Choice field pulling records from the ‘sales\_lead’ table, as well as a Reference field pulling values from the ‘sales\_lead\_source’ table.

# Resolution

* * *

To be a Choice field it was suggested that it was then changed back to type ‘Choice’, and to then configure the ‘Choice List Specification’ to point at the ‘sales\_lead\_source’ table.

For it to be a Reference field the recommendation was to either,

1) Revert to a version where it previously functioned,

2) Set it back to be a Choice type field and then expose on the form, and empty, the values in the ‘choice’, ‘choice\_field’, and ‘choice\_table’ fields, or,

3) Change the XML to,

   <choice>0</choice>

   <choice\_field></choice\_field>

   <choice\_table></choice\_table>

and re-import the record, so as to remove the definitions.
