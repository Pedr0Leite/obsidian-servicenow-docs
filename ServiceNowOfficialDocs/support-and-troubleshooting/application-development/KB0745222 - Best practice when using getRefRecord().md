---
title: "Best practice when using getRefRecord()"
aliases:
  - KB0745222
tags:
  - servicenow
  - support-kb
  - gliderecord
  - getrefrecord
  - scripting
  - business-rules
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745222
kb_number: KB0745222
last_modified: 2023-09-07
---

## Best practice when using getRefRecord()

  

### Issue

[getRefRecord()](https://developer.servicenow.com/app.do#!/api_doc?v=madrid&id=r_GlideElement-getRefRecord "getRefRecord()") returns a GlideRecord object for a given reference element. This is used widely in business rule scripts but incorrect usage of this can cause some major issues. This article describes some issues seen and the best practice to follow to avoid these. 

# Issues

1.  Printing values from the record obtained using getRefRecord() might not print anything. 
2.  Orphan records get inserted when updating the record obtained using getRefRecord(). 
3.  Using values from record obtained using getRefRecord() in other script results in "undefined" errors.

  

### Resolution

If the reference field has an empty value, getRefRecord() doesn't throw any error but it does return a GlideRecord object. That's why it is important to check if the returned object is a valid GlideRecord object or not. 

<table><tbody><tr><td><pre style="margin: 0px; line-height: 125%;">1
2
3
4
5
6
7</pre></td><td><pre style="margin: 0px; line-height: 125%;"><span style="color: #008000; font-weight: bold;">var</span> grUser <span style="color: #666666;">=</span> current.user.getRefRecord();
<span style="color: #008000; font-weight: bold;">if</span>(grUser.isValidRecord()) { <span style="color: #408080; font-style: italic;">// &lt;&lt; only perform operations on it if it's a valid record</span>
    <span style="color: #008000; font-weight: bold;">if</span>(grUser.email <span style="color: #666666;">!=</span> current.email_address){
        grUser.email <span style="color: #666666;">=</span> current.email_address;
        grUser.update();
    }
}
</pre></td></tr></tbody></table>

getRefRecord() should always be followed by [isValidRecord()](https://developer.servicenow.com/app.do#!/api_doc?v=madrid&id=r_GlideRecord-isValidRecord "isValidRecord()") check. 

If expected field is on a child table, make sure the reference field points to the child table and not the parent table.  Otherwise the getRefRecord() returns the GlideRecord object from the parent table which will not have the field that exists on the child table resulting in "undefined" errors.

## Related

- [[KB0725708 - The API GlideDate.getDisplayValue() uses the UTC timezone instead of the user's timezone]] - other GlideRecord/Glide API scripting gotcha

