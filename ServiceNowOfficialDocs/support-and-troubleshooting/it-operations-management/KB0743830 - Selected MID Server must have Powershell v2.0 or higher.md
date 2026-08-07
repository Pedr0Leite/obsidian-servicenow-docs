---
title: "Selected MID Server must have Powershell v2.0 or higher"
aliases:
  - KB0743830
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743830
kb_number: KB0743830
last_modified: 2024-04-07
---

## Selected MID Server must have Powershell v2.0 or higher

  

### Issue

# Symptoms

When doing a Windows Credential test, it will pop up with "Selected MID Server must have Powershell v2.0 or higher" as below.

![error](sys_attachment.do?sys_id=915968eedb02b450e515c2230596198c)

# Resolution

Follow the troubleshooting steps listed:

1.  Check to make sure that Windows host, hosting the MID server does have Powershell v2.0 or higher
2.  Check on the MID server Parameter to make sure that "mid.powershell.path" is not specified, or if it is, make sure it is to the correct path.
3.  Also if "mid.powershell.path" is configured, we maybe hitting the PRB1320534
4.  If the MID server has only 1 version of Powershell and if it is in the default path then you don't need to specify the "mid.powershell.path".
5.  If you are removing the "mid.powershell.path" in step 4, please restart the MID server.  
    5\. Check to see if Windows System variables are setup correctly. ensure "C:\\Windows\\system32" is in the path.
6.  Once you verify that ensure that path are showing up correctly by running "   echo %PATH% "
