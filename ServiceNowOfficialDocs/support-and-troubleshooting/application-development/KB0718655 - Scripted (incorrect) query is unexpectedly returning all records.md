---
title: "Scripted (incorrect) query is unexpectedly returning all records"
aliases:
  - KB0718655
tags:
  - servicenow
  - support-kb
  - GlideRecord
  - scripting
  - addQuery
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718655
kb_number: KB0718655
last_modified: 2024-12-25
---

## Issue

When executing a query from a script it is returning all records from the table when it was only expecting one record.

As an example when trying to perform an update on a single record using the following background script:   
  
var gr = new GlideRecord('u\_ci\_sample\_data');   
gr.addQuery('sysid', '01d90bd3db392b008f01fbc61d96193b'); // column name is invalid should be sys\_id   
gr.query();   
while(gr.next())   
{   
gr.u\_status = 'Live';   
gr.u\_sub\_status = 'Operational';   
gr.update();   
} 

## Resolution

1\. There is also an alternative way to find a specific record based on a sys\_id value that would avoid this situation (essentially using a correct filter):  
  
var gr = new GlideRecord('u\_ci\_sample\_data');  
if (gr.get('01d90bd3db392b008f01fbc61d96193b'))  
{  
gr.u\_status = 'Live';   
gr.u\_sub\_status = 'Operational';   
gr.update();   
}  
  
Please see documentation on the get function of the GlideRecord:   
[https://docs.servicenow.com/csh?topicname=c\_GlideRecordScopedAPI.html&version=latest](https://docs.servicenow.com/csh?topicname=c_GlideRecordScopedAPI.html&version=latest)

2\. To prevent a similar situation occurring, consider creating a new system property setting:   
  
glide.invalid\_query.returns\_no\_rows = true   
  
**Warning**:  
This property is global, so it will apply to the whole instance, test it very well on a sub-production instance as it will affect other scripted filters where an incorrect filter had gone unnoticed, not to return data any longer!

## Related

- [[KB0692550 - Why addQuery() method in Business Rule constructs incorrect query]]
- [[KB0717827 - Using a business rule to copy attachments from one record to another upon creation]]
