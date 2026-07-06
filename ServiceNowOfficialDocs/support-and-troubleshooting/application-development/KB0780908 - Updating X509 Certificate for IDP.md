---
title: "Updating X509 Certificate for IDP"
aliases:
  - KB0780908
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780908
kb_number: KB0780908
last_modified: 2025-09-12
---

## Updating X509 Certificate for IDP

  

### Issue

Process to safely update the X509 Certificate for IDP.

### Cause

When IDP changes the certificate and if the same certificate is not added in the Servicenow instance under X509 certificate, User authentication stops working and in logs we can see errors like - SAML2: Could not validate SAMLResponse: no thrown error.

### Resolution

1.  Make Sure the debug logging of Multi provider SSO is enabled in your instance.  
      
    
2.  Under System Logs search the latest created log statement containing SAML  
      
    
3.  Copy the SAML Response received in the logs in notepad or any editor. You will find updated certificate from IdP in <ds:X509Certificate>...</ds:X509Certificate> tags.  
      
    
4.  From Log Statements find the statement - IdP found based on SAML response: . This statement will give you sys ID of the IdP for which the certificate mismatch has been detected and authentication failure is happening. The statement IdP found based on SAML response: will appear after system has received SAML Response.  
      
    
5.  Open the IdP record -   
    https://<instance\_name>.service-now.com/sso\_properties\_list.do?sysparm\_query=sys\_id%3D<sys\_id copied from the SAML response>
6.  Under X.509 Certificate section click New.  
      
    7\. Provide Desired name to the certificate, Keep the Format as PEM.  
      
    8\. Under PEM Certificate add the certificate copied from the SAML response in Step3 as -   
    \-----BEGIN CERTIFICATE-----  
    <Paste the certificate here>  
    \-----END CERTIFICATE-----  
      
      
    9\. Save the record.  
      
    10\. From the related links on the Certificate, click on Validate Stores/Certificates

  

Alternatively you can automate the process of renewing the SAML Certificate by

1\. Scheduled Script Execution - Refresh SSO Metadata

https://<instance\_name>.service-now.com/sysauto\_script\_list.do?sysparm\_query=nameLIKERefresh%5Ename%3DRefresh%20SSO%20Metadata

2\. Make Sure that the Scheduled Script Metadata job is Active.

3\. On IdP record, under Advanced Section, Update Metadata URL in field - idp\_metadata\_url (Field Label - Metadata URL from which IDP properties are imported)

4\. Customers can take help from respective IdP team to provide you valid Metadata URL which is accessible from instance.

5\. This job runs every 30 minutes and updates any change done at IdP metadata level, which also contains certificates.
