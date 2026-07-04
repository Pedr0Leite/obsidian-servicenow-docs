---
title: "No Preview Available for HR profile but user has read access to the HR profile record itself"
aliases:
  - KB0860685
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860685
kb_number: KB0860685
last_modified: 2025-09-03
---

## No Preview Available for HR profile but user has read access to the HR profile record itself

  

### Issue

Group members cannot preview or open the HR profile of opened for or subject person in "sn\_hr\_core\_case" table.

When user clicks the reference icon next to the name, it comes up with "No Preview Available"

### Cause

On clicking on preview field the following method is eventually called:  
Script include : sn\_hr\_core.hr\_CaseAjax  
Method : getGlideRecordSecureSetData  
  
This returns all the HR Profile fields that the logged in user has canRead access to :  
  
\_getData: function (gr) {  
var data = {};  
var elements = gr.getElements();  
for (var i = 0; i < elements.length; i++) {  
if (!elements\[i\].canRead())  
continue;  
var ed = elements\[i\].getED();  
var name = ed.getName();  
data\[name\] = gr.getValue(name);  
}  
data\['ZZ\_YY\_display\_value'\] = gr.getDisplayValue();  
return data;  
},  
  
According to the above code if any of the HR Profile fields do not pass canRead they will not be populated in the data returned.

  
  

### Resolution

There is an out-of-box (OOB) ACL such the sn\_hr\_core\_profile.\* access is given to sn\_hr\_core\_profile reader and all the OOB Assignment group members have that role and hence this issue is not seen.

This ACL could have been modified

  

Make sure to:

Create/Modify ACL with sn\_hr\_core\_profile.\* such that access is give to the intended user.

Check if the read ACL for sn\_hr\_core\_profile was customized and revert it to OOB:  
https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=3e5370019f22120047a2d126c42e7001
