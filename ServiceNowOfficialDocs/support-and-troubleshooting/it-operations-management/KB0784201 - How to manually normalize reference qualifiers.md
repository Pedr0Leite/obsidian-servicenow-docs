---
title: "How to manually normalize reference qualifiers"
aliases:
  - KB0784201
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784201
kb_number: KB0784201
last_modified: 2026-06-10
---

## How to manually normalize reference qualifiers

  

### Issue

After running the "Update Reference Qualifiers" step for "Normalization Data Services" guided setup, there are records need to manually update

![](sys_attachment.do?sys_id=f094c6a04750751011eaf24c736d43cb)

How do you manually normalize reference qualifier after running the "Normalization Data Services" guided setup?

### Resolution

"Note that a lot of these dictionary entries are cloned descendent (belongs to the base table). Therefore, you don't require updating 1400+ odd dictionaries. Most of the cloned descendent belong to CMDB tables, start with those first. Use the link in 2. to find remaining dictionary entries"

1\. For records that need a manual update:

Link:  
https://<INSTANCE\_NAME>.service-now.com/sys\_dictionary\_list.do?sysparm\_query=reference%3Dcore\_company%5Edynamic\_ref\_qual%3DNULL  
  
a) For "Use reference qualifier" = Simple,  
Edit "reference\_qual\_condition" field to "Normalized" is true as per screenshot "after\_manual\_ref\_qual\_condition.png".

![](sys_attachment.do?sys_id=b894c6a04750751011eaf24c736d43c5)  
  
b) For "Use reference qualifier" =Advanced,  
For example,

![](sys_attachment.do?sys_id=f494c6a04750751011eaf24c736d43cd)  
Edit field "reference\_qual"   
the one with "javascript:" tag, prefix it with "canonical=true^" or suffix with "^canonical=true" to add "canonical=true" condition.   
ie: Change   
_javascript:'sys\_idIN' + current.assignment\_group.vendors_ 

TO (prefix way)

**javascript:'canonical=true^' + 'sys\_idIN' + current.assignment\_group.vendors** 

OR (suffix way)

**javascript:'sys\_idIN' + current.assignment\_group.vendors + '^canonical=true'**   
  
c) For "Use reference qualifier" =Dynamic,   
\- Go to the 'Dynamic ref qual' record being used (sys\_filter\_option\_dynamic).   
\- Edit the Script field to add 'canonical=true' condition. (suffix "^canonical=true" or prefix "canonical=true^" same as Advanced)

2\. After manually updating all reference qualifier in step 1, run the following query to get the remaining reference qualifiers:

https://<INSTANCE\_NAME>.service-now.com/sys\_dictionary\_list.do?sysparm\_query=reference%3Dcore\_company%5Edynamic\_ref\_qual!%3D1b3dae2c0b911200f0f04696a6673ab7%5EORdynamic\_ref\_qualISEMPTY%5Ereference\_qualNOT%20LIKEcanonical%3Dtrue%5EORreference\_qualISEMPTY

![](sys_attachment.do?sys_id=fc94c6a04750751011eaf24c736d43c8)

If there are records returned, update the reference qualifiers as suggested in step 1.

3\. After performing the above manual steps, re-run "Normalize Configuration Items (CMDB)" step in the guided setup to normalize 'core\_company' records.
