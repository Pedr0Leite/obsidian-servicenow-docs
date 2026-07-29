---
title: "[SAMP\SAP] Integrating SAP with ServiceNow throws \"SOAP function is invalid. Please verify your SAP WSDL\" error"
aliases:
  - KB0858220
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858220
kb_number: KB0858220
last_modified: 2024-01-28
---

## \[SAMP\\SAP\] Integrating SAP with ServiceNow throws "SOAP function is invalid. Please verify your SAP WSDL" error

  

### Issue

-   While trying to configure SAMP SAP publisher pack to integrate SAP system with ServiceNow it throws an error "Request failed with response: SOAP function is invalid. Please verify your SAP WSDL" when trying to test the connectivity.

![](sys_attachment.do?sys_id=5713b5161baa60103013751f034bcb3a)

-   Below are the traces observed while validating the system logs,

Error \*\*\* Script: SAPImportWorker Exception while executing the api GET\_SAP\_VERSION Error is \[object Object\]: no thrown error com.glide.ui.ServletErrorListener  
Error SAPImportWorker.getLatestSapVersion : Can not get the lastest SAP version, returned with response : {0}SOAP function is invalid. Please verify your SAP WSDL. \*\*\* Script  
Error SAPImportWorker: SOAP function is invalid, expected NOW\_SAMP.\_-now\_-sampUserDetailsWsdl \*\*\* Script  
Error \*\*\* Script: SAPImportWorker.getLatestSapVersion : Can not get the lastest SAP version, returned with response : {0}SOAP function is invalid. Please verify your SAP WSDL.: no thrown error com.glide.ui.ServletErrorListener  
Error \*\*\* Script: SAPImportWorker: SOAP function is invalid, expected NOW\_SAMP.\_-now\_-sampUserDetailsWsdl: no thrown error com.glide.ui.ServletErrorListener  
Error SAPImportWorker Exception while executing the api GET\_SAP\_VERSION Error is \[object Object\]

  

### Release

-   Instance with Software Asset Management Professional for SAP (com.sn\_samp\_sap) plugin enabled. 

### Cause

-   Preferably the WSDL URL used in the SAP connection might use Proxy connection due to which ServiceNow couldn't validate the URL using SOAP calls.

### Resolution

-   In most occasions, it is best to start with the [KB0813999](https://hi.service-now.com/kb_view.do?sysparm_article=KB0813999 "KB0813999") article and go through the "SAP technical details setup.pdf" file to validate if all roles and configurations are set right in place.
-   If still, the connection fails and in order to establish SAP connection configure the right Proxy WSDL URL in the SOAP Connection so that ServiceNow can authenticate and integrate with SAP system.

![](sys_attachment.do?sys_id=1713b5161baa60103013751f034bcb3e)

-   Once WSDL URL is set, configure SOAP Message Function with appropriate SOAP action and SOAP end-point along with MID server to use.

![](sys_attachment.do?sys_id=df13b5161baa60103013751f034bcb3c)

![](sys_attachment.do?sys_id=5b13b5161baa60103013751f034bcb3f)

-   Post all the above configurations the "Test SAP Connection and Version" should be successful and display the message as below,

![](sys_attachment.do?sys_id=9f13b5161baa60103013751f034bcb40)

  

### Related Links

Document reference related to SAMP SAP publisher pack,

-   [Establish an SAP connection](https://docs.servicenow.com/bundle/orlando-software-asset-management/page/product/software-asset-management2/task/add-sap-connection.html "Establish an SAP connection")
-   [Record publisher details for SAP](https://docs.servicenow.com/csh?topicname=add-software-model-sap.html&version=latest "Record publisher details for SAP")
-   [Record software rights for SAP](https://docs.servicenow.com/csh?topicname=create-entitlement-sap.html&version=latest "Record software rights for SAP")
