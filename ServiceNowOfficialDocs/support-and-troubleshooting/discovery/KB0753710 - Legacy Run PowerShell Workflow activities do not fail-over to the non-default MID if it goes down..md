---
title: "Legacy \"Run PowerShell\" Workflow activities do not fail-over to the non-default MID if it goes down."
aliases:
  - KB0753710
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753710
kb_number: KB0753710
last_modified: 2024-04-07
---

## Legacy "Run PowerShell" Workflow activities do not fail-over to the non-default MID if it goes down.

  

### Issue

The Legacy "Run PowerShell" Workflow activities do not automatically fail-over to the non-default MID if it goes down.

  

### Resolution

This is due to the logic in the MIDServerSelector Script Include:  
https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=97e984500a0006786e9c7e86128249a8

var defaultMidServer = GlideProperties.get("mid.server.rba\_default");

if (!JSUtil.nil(defaultMidServer)) {  
     var gr = new GlideRecord('ecc\_agent');  
     gr.addQuery('name', defaultMidServer);  
     gr.query();

     if (!gr.next()) {  
          this.errorMsg = 'The configured default MID server (' + defaultMidServer + ') is not valid';  
          defaultMidServer = "";  
     }  
} else

this.errorMsg = 'There is no MID server configured to run this activity';

  

This "Run PowerShell" activity is deprecated and is unavailable for new workflows. To replace the functionality of this activity, use the Powershell activity template  
to create a custom, scoped activity.

#   

### Related Links

[Powershell Activities](https://docs.servicenow.com/csh?topicname=c_OrchestrPowerShellActivities.html&version=latest#c_UseHResultCodes "Powershell Activities")
