---
title: "Microsoft AD Spoke - Lookup User Action hangs on status In Progress"
aliases:
  - KB0868220
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0868220
kb_number: KB0868220
last_modified: 2023-11-21
---

## Microsoft AD Spoke - Lookup User Action hangs on status In Progress

  

### Issue

From the flow designer action, when trying to run Lookup User AD action, every time it is hanging on "In Progress" state when we test the action.

![](sys_attachment.do?sys_id=96641cc6db89ec103daa1ea668961986)  
  

### Release

All Versions

### Cause

This could be due to below causes:

-   Communication between instance and mid server is not up or intermittent connectivity issue.
-   Powershell script is not able to resolve or detect the AD server from the mid server.
-   Credential issues which is required to authenticate to the AD server.

### Resolution

To fix the issue, verify below information:

1.  Make sure mid server is able to communicate well from the instance all nodes.
2.  If Mid Serer is unable to resolve the AD server then make sure to check the DNS configuration on the mid server.
3.  If Powershell script is not able to detect which Mid Server to connect then you can try hardcoding the AD server into the Powershell script.  
    

          For example: 

          If your powershell script contains:

          $user = Get-ADUser -Identity $userName -Credential $cred -Server $computer -Properties \* -ErrorAction Stop;;  
          Then try changing it to:  
          $user = Get-ADUser -Identity $userName -Server "<AD-Serverr-FQDN>" -Properties \* -ErrorAction Stop;

  

If above everything is fine, then check the ECC queue for "IPaaSActionProbe" probe output request and verify if Input is coming back for this. If not, coming then check the mid server agent log which might show error:

  

2020-12-14 03:33:54 (551) Worker-Expedited:IPaaSActionProbe-xxxxxxxxxxxxxxxxxxxx9ba DEBUG: No valid credential found, running script without credential

  

This comes when you do not have correct credentials configured in the instance in the "windows\_credentials" table.So, correct the credentials frorm here. Also, verify the credential & connection aliases configuration which is available in sys\_alias table.

### Related Links

AD Spoke document available [here](https://docs.servicenow.com/bundle/paris-servicenow-platform/page/administer/integrationhub/concept/microsoft-ad-spoke.html#d1828130e179 "here")
