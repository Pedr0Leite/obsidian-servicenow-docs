---
title: "SCOM connector instance configured with Windows Authentication"
aliases:
  - KB0686745
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686745
kb_number: KB0686745
last_modified: 2024-04-07
---

## SCOM connector instance configured with Windows Authentication

  

### Issue

# Installation Docs

* * *

[Configure the SCOM connector instance (Kingston)](https://docs.servicenow.com/csh?topicname=t_EMConfigureSCOMConnector.html&version=latest "Configure the SCOM connector instance (Kingston)")

[Configure alert collection from SCOM (Kingston)](https://docs.servicenow.com/csh?topicname=t_EMConfigureSCOMConnectorInstance.html&version=latest "Configure alert collection from SCOM (Kingston)")

# Authentication

* * *

SCOM uses the MID server user to authenticate. Please make sure the MID user has access to SCOM.

If Windows authentication is used by the connector to access the SCOM database (OperationsManagerDW), the MID Server service should be running with a user having read access to the SCOM database. Ensure that the correct credentials are used:

1.  In the local services, right-click the MID Server service and select Properties.
2.  In the Log On tab, ensure that This account is selected with the details of the user in the Windows domain having read access to the SCOM database.

Example of error if the user doesn't have access:

Connection test failed: SCOM Event connector failed.  
Microsoft.EnterpriseManagement.Common.UnauthorizedAccessEnterpriseManagementException: **The user does not have sufficient permission to perform the operation**.  
System.ServiceModel.Security.SecurityNegotiationException: The caller was not authenticated by the service.  
System.ServiceModel.FaultException: The request for security token could not be satisfied because authentication failed.  
  at System.ServiceModel.Security.SecurityUtils.ThrowIfNegotiationFault(Message message, EndpointAddress target)  
  at System.ServiceModel.Security.SspiNegotiationTokenProvider.GetNextOutgoingMessageBody(Message incomingMessage, SspiNegotiationTokenProviderState sspiState)

If you encounter problems with the SCOM connectors after upgrading to Jakarta or Kingston (i.e: problems with user name, password, or hostname not found), please check that the following files are updated to the latest version (Upgrade History):

1.  MID server script file: SCOMConnector.groovy  (events connector functionality)
2.  MID server script includes: ScomJS (Metric and BI-Directional functionality)
3.  MID server script file: Invoke-UpdateAlert.ps1  (Bi-Directional functionality)

# Additional Tips

* * *

This is true only if the SCOM uses the “Windows Authentication” option (otherwise it will use user and password credentials)

Port 5724 should be open from the SCOM server ([Configuring a Firewall for Operations Manager — Microsoft docs](https://docs.microsoft.com/en-us/system-center/scom/plan-security-config-firewall?view=sc-om-1801 "Configuring a Firewall for Operations Manager Microsoft docs"))
