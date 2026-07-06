---
title: "Avoid using user credentials in a plain text in a script when making outbound API call to get OAuth token"
aliases:
  - KB0752549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752549
kb_number: KB0752549
last_modified: 2025-11-06
---

## Avoid using user credentials in a plain text in a script when making outbound API call to get OAuth token

  

### Issue

How to avoid using user credentials in a plain text in a script when making outbound API call to get OAuth token

### Release

ALL

### Resolution

The credentials can be saved in credential table and then used in the script to get OAUTH token. As the password field in credential table is of type password2, it is encrypted. 

1\. Go to [https://INSTANCE.service-now.com/basic\_auth\_credentials\_list.do?sysparm\_query=](https://INSTANCE.service-now.com/basic_auth_credentials_list.do?sysparm_query=)

2\. Click on 'new' and populate 'name' and 'User Name' and 'Password' of user making the call

3\. Click on save

  
Here is the sample code you can use in your script to retrieve the user credentials

  
var provider = new sn\_cc.StandardCredentialsProvider();   
var credential = provider.getCredentialByID("sys\_id");//sys\_id of record created in basic\_auth\_credentials table  
var userName = credential.getAttribute("user\_name");   
var password = credential.getAttribute("password"); 

gs.log("user\_name: " + userName + " password: " + password);
