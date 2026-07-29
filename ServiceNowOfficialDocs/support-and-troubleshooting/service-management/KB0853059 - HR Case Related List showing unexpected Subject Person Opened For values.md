---
title: "HR Case Related List showing unexpected Subject Person / Opened For values"
aliases:
  - KB0853059
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853059
kb_number: KB0853059
last_modified: 2024-04-08
---

## HR Case Related List showing unexpected Subject Person / Opened For values

  

### Issue

The user was facing an issue where, in their HR Case Related List "Cases for Customer", some records seem to be out of place (namely, the "Customer" field value \[subject\_person\] is aligned to user 'B', when the user was expecting cases aligned to user 'A') - e.g. seeing "Tony Stark" as the listed Customer when "Scott Lang" was expected.

### Cause

The user had customized the label for the HR Case Related List from the Out of Box (OOB) "Cases for User" and change it to "Cases for Customer" and this is what confused them (further details on why are shared below).

### Resolution

As mentioned above, the reason the user was rightly confused is that they modified the HR Case Related list name from "Cases for User" to "Cases for Customer".  
  
There is some logic behind why unexpected names like "Tony Stark" are displaying in some of these (whether subject\_person \[custom label = "Customer"\] or opened\_for \[custom label = "Requestor"\]) column values:  
  
Even though the HR Case Related list label was changed, the Platform was still checking the Related list values against the OOB configuration - e.g. for all HR Cases where "Scott Lang" was either the Customer (Subject Person) **_or_** the Requestor (Opened For):  

```
(function refineQuery(current, parent) {    var qc = current.addQuery("opened_for", parent.opened_for);    qc.addOrCondition("subject_person", parent.opened_for);    current.addQuery("sys_id", "!=", parent.sys_id);    current.orderByDesc("sys_created_on");})(current, parent);
```

  
This is per the OOB Relationship "Cases Opened for User":  

-   /nav\_to.do?uri=sys\_relationship.do?sys\_id=f6d4f37d2f031200b3c9a310c18c95a3

With that in mind, knowing that as long as "Scott Lang" is either the Customer (subject\_person) or the Requestor (opened\_for), looking at the "Cases for Customer" Related list starts to make sense. It really does work as expected, and the only reason it is currently confusing is because of the custom label put on the Related list.  
  
It was shared that if the user wanted to truly only have cases show where "Scott Lang" (or whoever) is in the Customer field, then they would need to modify the Script in the above sys\_relationship record. They were informed that this would be a customization, however, and thus would be out of scope for Support.
