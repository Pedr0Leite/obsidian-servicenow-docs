---
title: "Failure(s) with available Windows credentials from the instance - \"No such interface supported\""
aliases:
  - KB0787202
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787202
kb_number: KB0787202
last_modified: 2024-04-08
---

## Failure(s) with available Windows credentials from the instance - "No such interface supported"

  

### Issue

Windows Discovery Failed with Credential Failure Error Message, Indicating the issue could be due to Credential Issue. But we can see the actual error message below that states that it failed due to "No such Interface supported" error.

"Wmi - Classify" Input Probe will contain the following error below.

\---------

<result>  
<error>  
Failure(s) with available Windows credentials from the instance.  
</error>  
<error>No such interface supported</error>

\----------

### Resolution

We can verify the error by running a Powershell command below from the MID Server to the target IP. As below, we could see the "no such interface supported".

This error is usually associated with firewall issues. Ensure that there are no firewalls between the MID Server and the Target IP and re-run the command again to test it.

Once the command below returns the output without any error then you can try Discovery again from the ServiceNow Instance.

**gwmi win32\_operatingsystem -computer 10.xx.xx.xx -credential 'Domain\\User'**

![](sys_attachment.do?sys_id=d98210cddbcc78d066e0a345ca961994)
