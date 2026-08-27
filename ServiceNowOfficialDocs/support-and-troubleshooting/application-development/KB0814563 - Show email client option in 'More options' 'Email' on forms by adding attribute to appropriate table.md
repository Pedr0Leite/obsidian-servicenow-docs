---
title: "Show email client option in 'More options' > 'Email' on forms by adding attribute to appropriate table"
aliases:
  - KB0814563
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814563
kb_number: KB0814563
last_modified: 2024-04-08
---

## Show email client option in 'More options' > 'Email' on forms by adding attribute to appropriate table

  

### Issue

As seen on the Incident form, the [Email Client](https://docs.servicenow.com/csh?topicname=c_EnableTheEmailClient.html&version=latest "Email Client") gives you the ability to send an email directly from an Incident record. This same option, found under 'More options' in a record header, can be added to any other table using the **Email client** attribute. Below, we will use the Story form and Story table as an example, which out-of-box, does _not_ include the Email client attribute

### Release

All available

### Cause

Add the 'Email client' attribute with Value=true to the required table dictionary entry

![](/sys_attachment.do?sys_id=d7a8ecc91b047414f34d33bc1d4bcb63)

### Resolution

1.  Navigate to the Story form  
    2\. Right-click header and select Configure > All (or Dictionary)  
    3\. On the Dictionary Entries tab, locate and open the record with \[Table\]\[is\]\[rm\_story\] AND \[Type\]\[is\]\[Collection\]  
    4\. In the Attributes section, click NEW  
    5\. Add Attribute: Email client (typing Email should pop up the attribute to be selectable)  
    6\. Add Value: true  
    7\. Submit  
      
      
    ![](/sys_attachment.do?sys_id=d3a8200d1b047414f34d33bc1d4bcb77)
