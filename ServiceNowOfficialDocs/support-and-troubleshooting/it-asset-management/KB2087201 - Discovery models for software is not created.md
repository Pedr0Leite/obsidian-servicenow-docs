---
title: "Discovery models for software is not created"
aliases:
  - KB2087201
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2087201
kb_number: KB2087201
last_modified: 2025-04-30
---

## Discovery models for software is not created

  

### Issue

Discovery models for software are not created or not mapped

### Facts

1.  OOB, When a software record is added to the cmdb\_sam\_sw\_install table, the discovery model is created or linked by the business rule "Create a Software Normalization." This rule considers the software record's primary key.
2.  The primary key is the mandatory attribute for the software installations and software usage.
3.  The primary key is created in two ways: either by the discovery source or by a business rule "Build Primary Key" which runs before "Create a Software Normalization". 
4.  This script takes into consideration the value of property "com.snc.samp.exclude\_device\_flag" which is set to "u\_exclude\_from\_sam". This value is set on the corresponding CI record the software is on.
    1.  Build Primary Key:  
        https://<instance>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=efd6bb4d37101000deeabfc8bcbe5d44   
          
        
    2.  Create a Software Normalization:  
        https://<instance>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=9ec2b34d37101000deeabfc8bcbe5d43 

### Release

All releases

### Cause

1.  Go to the system property com.snc.samp.exclude\_device\_flag and verify if this property is available or not; if this property is available, verify if there is a value to the property.
    1.  https://<instance>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=79e091db93b22300d40d14f1b47ffb51
2.  While investigating, it has been observed the above property has a value "exclude\_sam". So, any software installation record with this value will be excluded 
3.  When this value, "exclude\_sam," is true, no primary key is created, and "Create a Software Normalization" does not run. As a result, the discovery model is not associated. 

### Resolution

1.  The field "exclude\_sam" is a custom field. the purpose of this field shpuld be verified, source of update and make necessary changes in the property com.snc.samp.exclude\_device\_flag.
2.  The system property "com.snc.samp.exclude\_device\_flag" should be OOB and an empty value. Then, the Discovery models should be created for the Software.
