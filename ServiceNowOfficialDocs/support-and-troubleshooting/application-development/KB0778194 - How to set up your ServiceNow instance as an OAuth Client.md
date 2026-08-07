---
title: "How to set up your ServiceNow instance as an OAuth Client"
aliases:
  - KB0778194
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778194
kb_number: KB0778194
last_modified: 2025-12-10
---

## How to set up your ServiceNow instance as an OAuth Client

  

### Summary

This article explains how to set up your ServiceNow Instance as an OAuth Client using the Grant Type "Resource Owner Password Credentials", so that both an Access and Refresh Token can be provided to access the instance.

### Release

All releases.

### Instructions

#### Setting up your ServiceNow Instance as an OAuth Client

1.  Navigate to Machine Identity Console > > Inbound integrations > > New integration > OAuth Resource owner password credential grant.  
      
    
2.  Fill out the form according to your requirement and click "**Submit**". If you are unsure then populating the "**Name**" field will suffice.  
    _Note: Please note down the "**Client ID**" and "**Client Secret**" as they will be used later._

#### Obtaining the Access and Refresh Token using Postman

1.  Open Postman and create a new Request.  
      
    
2.  Set the REST Method to "**POST**", and the Request URL to "**https://<instance\_name>.service-now.com/oauth\_token.do**".  
      
    
3.  Select the "**Body**" tab, and check "**x-www-form-url-encoded**".  
      
    
4.  Populate the KEY:VALUE pairs according to your confirmation. This should be done in body section only:  
    1.  grant\_type : **password**
    2.  client\_id : **<client\_id from previous section>**
    3.  client\_secret : **<client\_secret from previous section>**
    4.  username : **<username to authenticate with the instance>**
    5.  password : **<password to authenticate with the instance>  
          
        **
5.  Click "**Send**" and you should receive a response similar to below with both Access and Refresh Token.

<table style="border-collapse: collapse; width: 720px; height: 144px;"><tbody><tr style="height: 129.789px;"><td style="width: 100%; height: 129.789px;"><div><pre>{<!-- --><br>"access_token": "CH1XAvt8FU1yjsRHq-ixDB1Fct4mpcztmvlD_2Wfu_F83thGqcPVfjvHsf8HvBi_ByeMsPXz1Igd5OYdADfXFw",<br>"refresh_token": "EuoV22-H28J_frduuMUlKXcuJ-tFz9F2Pe_PSNa3Ml3H8bzG4FIn8ChCcmtLJkMeP_T4a-MBI-c6YRW_1D4Mcw",<br>"scope": "useraccount",<br>"token_type": "Bearer",<br>"expires_in": 1799<br>}</pre></div></td></tr></tbody></table>

#### Access a resource on your ServiceNow instance using the Access Token

1.  Open Postman and create a new Request.  
      
    
2.  Set the REST Method to "**GET**", and the Request URL to the resource endpoint.  
    _eg. **https://<instance\_name>.service-now.com/api/now/table/incident?sysparm\_limit=1  
      
    **_
3.  Click on the "**Auth**" tab and set the "Type" to "**No Auth**".  
      
    
4.  Click on the "**Headers**" tab and configure the below KEY:VALUE pair with the Access Token.
    1.  Authorization : **Bearer** **<access\_token from previous section>  
          
        **
5.  Click "**Send**" and you should receive the response payload for your resource.

#### Using the Refresh Token to renew the Access Token

1.  Open Postman and create a new Request.  
      
    
2.  Set the REST Method to "**POST**", and the Request URL to "**https://<instance\_name>.service-now.com/oauth\_token.do**".  
      
    
3.  Select the "**Body**" tab, and check "**x-www-form-url-encoded**".  
      
    
4.  Populate the KEY:VALUE pairs according to your confirmation.  
    1.  grant\_type : **refresh\_token**
    2.  client\_id : **<client\_id from previous section>**
    3.  client\_secret : **<client\_secret from previous section>**
    4.  refresh\_token : **<refresh\_token from previous section>**  
          
        
5.  Click "**Send**" and you should receive a response similar to below with a new Access Token.

<table style="border-collapse: collapse; width: 720px; height: 144px;"><tbody><tr style="height: 129.789px;"><td style="width: 100%; height: 129.789px;"><pre>{<!-- --><br>"access_token": "Y5KagMC8REDaILJL5Ohvg1SauPn36iCC2kV8-miwVEjy7j6AjJtY9lcsA5gvOC7EtFDBGd9Zw7PB-2XA4rs0XA",<br>"refresh_token": "EuoV22-H28J_frduuMUlKXcuJ-tFz9F2Pe_PSNa3Ml3H8bzG4FIn8ChCcmtLJkMeP_T4a-MBI-c6YRW_1D4Mcw",<br>"scope": "useraccount",<br>"token_type": "Bearer",<br>"expires_in": 1799<br>}</pre></td></tr></tbody></table>
