---
title: "Property \"com.glide.attachment.max_size\" of 3MB causes some LDAP records not to be imported if using MID server"
aliases:
  - KB0623372
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623372
kb_number: KB0623372
last_modified: 2024-04-07
---

## Property "com.glide.attachment.max\_size" of 3MB causes some LDAP records not to be imported if using MID server

  

### Issue

Property com.glide.attachment.max\_size of 3 MB causes some LDAP records not to be imported if using MID server  

Problem

* * *

The import set related to the data load shows the **Load completed** field as empty even though the status of the import set is Processed.  

Symptoms

* * *

The system logs and testing the data source "Load all data" displays: GlideRecord not a SYS\_ATTACHMENT record.

![what is showed on the load data](sys_attachment.do?sys_id=53cc2ceedb42b450e515c223059619bd "what is showed on the load data")

The localhost logs includes the following entries:

2017-06-22 17:30:58 (166) worker.0 worker.0 SEVERE \*\*\* ERROR \*\*\* com.glide.db.impex.LDAPProbeLoader
java.lang.IllegalArgumentException: GlideRecord not a SYS\_ATTACHMENT record
   at com.glide.ui.SysAttachmentInputStream.<init>(SysAttachmentInputStream.java:73)

Cause

* * *

The MID server tried to create an attachment with the data received from the LDAP query; however, it exceeded the value set on the _**com.glide.attachment.max\_size**_ system property.  

 ![Cause of the problem](sys_attachment.do?sys_id=27cc2ceedb42b450e515c223059619db "Cause of the problem")

  
Resolution

* * *

In the short term, set the _**sys\_properties com.glide.attachment.max\_size**_ to a higher value.  
  
In the long term, consider tuning your LDAP query to return only the required attributes. For example, if the attributes field is empty on the LDAP server form, it will try to query and retrieve all of the attributes of the records from the LDAP server including binaries, which increases the amount of data. Therefore, it could exceed the attachment limit set.  
  
For tips about how to set the LDAP attribute, see the community article [Setting the attributes to reduce LDAP import times](https://community.servicenow.com/community/it-service-management/blog/2016/01/11/example-of-tips-to-reduce-ldap-import-times).
