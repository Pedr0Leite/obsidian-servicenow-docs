---
title: " Unable to update the ID in twilio driver record. Error: <Error MessageTwilio responded with error: The requested resource /Services/MG<> NOT FOUND>"
aliases:
  - KB0785290
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785290
kb_number: KB0785290
last_modified: 2024-04-20
---

## Unable to update the ID in twilio driver record. Error: NOT FOUND>

  

### Issue

Unable to update the ID in twilio driver record after creating new messaging service. Below Error message is seen

Error: <Error MessageTwilio responded with error: The requested resource /Services/MG<> NOT FOUND>

### Cause

Twilio configuration using Message Service ID instead of the Account SID on the Twilio configuration form

### Resolution

1.  Add Messaging service id to the Twilio Config
2.  Navigate to Default Twilio Config. ( Link to the record on the instance)  
    https://<instance>.service-now.com/nav\_to.do?uri=sn\_twilio\_direct\_twilio\_config.do?sys\_id=70e5cb7087d21300b18a046787cb0bfc
3.  Add Messaging service id to the Twilio Config Form
4.  Confirm you can add the Message Service ID 

![](sys_attachment.do?sys_id=e405a9f41bd1e0101e579979b04bcb5b)
