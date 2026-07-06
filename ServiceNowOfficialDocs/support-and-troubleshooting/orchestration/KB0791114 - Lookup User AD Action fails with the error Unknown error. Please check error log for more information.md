---
title: "\"Lookup User\" AD Action fails with the error \"Unknown error. Please check error log for more information\""
aliases:
  - KB0791114
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791114
kb_number: KB0791114
last_modified: 2024-04-07
---

## "Lookup User" AD Action fails with the error "Unknown error. Please check error log for more information"

  

### Issue

When we use the Lookup User AD Action in sub-flow to the get the details of the user , it fails with the below error.

 "Unknown error. Please check error log for more information"

Steps to reproduce :

1.  Log in to the instance https://<instance name>.service-now.com
2.  Create a Sub-flow and include a Lookup User AD Action in the flow
3.  Pass the user information to the flow and run the sub-flow
4.  The flow fails with the error "Unknown error. Please check error log for more information"

               ![](sys_attachment.do?sys_id=9d9c133cdb0078d066e0a345ca9619d6)

  

          To view the response data you can test this action using the user name, once test is complete you can view the output data on the execution details page under the section 'Step Output Data' there will be a link that is under the text 'Runtime value',

          The link that starts with "AccountExpirationDate:" this will show you the output data received for the test in a RAW format.

              ![](sys_attachment.do?sys_id=819c133cdb0078d066e0a345ca9619d4)

  

  

### Release

ALL

### Cause

For certain users, output data is cut off and the data payload received is too large

### Resolution

We have a property that controls the max size of the output data that is received for the sub flows 

com.snc.process\_flow.reporting.serialized.val\_size\_limit

This property has a default value: 16384 but if it is changed to 0 it will allow for the entire output payload to be received. 

Steps to change the default value of the this property:

1.  Log into the instance https://<instance name>.service-now.com
2.  Go to https://<instance name>.service-now.com/sys\_properties\_list.do
3.  Search for the "com.snc.process\_flow.reporting.serialized.val\_size\_limit" property in the Name field
4.  Open the record and set the value to zero
