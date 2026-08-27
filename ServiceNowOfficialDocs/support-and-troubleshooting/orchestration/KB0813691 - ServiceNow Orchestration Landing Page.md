---
title: "ServiceNow Orchestration Landing Page"
aliases:
  - KB0813691
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813691
kb_number: KB0813691
last_modified: 2026-05-22
---

## ServiceNow Orchestration Landing Page

  

### Issue

# Contents

1.  [Overview](#OVERVIEW)
2.  [Active Directory with Orchestration](#AD)
3.  [Orchestration Activities](#Activities)
4.  [Activity Designer](#Designer)
5.  [Client Software Distribution](#CDS)
6.  [Orchestration Databus](#Databus)
7.  [Domain Separation with Orchestration](#Domain)
8.  [MID Server for Orchestration](#MID)
9.  [Orchestration Probes](#Probes)
10.  [Orchestration ROI](#ROI)
11.  [Powershell for Orchestration](#Powershell)
12.  [Orchestration Workflow](#Workflow)
13.  [Dashboards](#Dashboards)
14.  [Troubleshooting](#Troubleshooting)
15.  [Additional Information](#AddInfo)

# 1\. Overview

## Product Docs

1.  1.  [Getting Started with orchestration](https://docs.servicenow.com/csh?topicname=r-orchestration.html&version=latesthttps://docs.servicenow.com/csh?topicname=r-orchestration.html&version=latest)
    2.  [Activate Orchestration](https://docs.servicenow.com/csh?topicname=t_ActivateOrchestration.html&version=latest#t_ActivateOrchestration)

# 2\. Orchestration Activities

## Product Docs

1.  1.  [Introduction to credentials, connections, and aliases for Orchestration](https://docs.servicenow.com/csh?topicname=credentials-conn-alias-orch.html&version=latest#credentials-conn-alias-orch)

## Knowledge Articles

1.  1.  [Configure the connection to an AD credential store](https://docs.servicenow.com/csh?topicname=config-ad-credential-store.html&version=latest)
    2.  [NT/ Domain credentials for JDBC orchestration activity to update SQL](https://support.servicenow.com/kb_view.do?sysparm_article=KB0787887)
    3.  [Azure AD orchestration fails with error "Access token validation failure. Invalid audience."](https://support.servicenow.com/kb_view.do?sysparm_article=KB0780220)
    4.  [Error in orchestration while creating a user: A device attached to the system is not functioning](https://support.servicenow.com/kb_view.do?sysparm_article=KB0724364)
    5.  [Custom/AD-related activities may fail with an error "input variable password is not password2 type"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0754810)
    6.   [Duplicate file name error occurs during update of Credentials.psm1 file synchronized by both Discovery and Orchestration](https://support.servicenow.com/kb_view.do?sys_kb_id=17e72d7adbf10b406015f47e0f961935)

# 3\. Active Directory(AD) for Orchestration

## Product Docs

1.  1.  [List of Orchestration activities](https://docs.servicenow.com/csh?topicname=r_ListOfOrchestrationActivities.html&version=latest)

## Knowledge Articles

1.  1.  [Orchestration activity 'Query AD' returning success when they failed to find the object](https://support.servicenow.com/kb_view.do?sysparm_article=KB0815823 "Orchestration activity 'Query AD' returning success when they failed to find the object")
    2.  [The specified directory service attribute or value does not exist error on Create Ad Object orchestration activity](https://support.servicenow.com/kb_view.do?sysparm_article=KB0790052)
    3.  [The module 'scripts' could not be loaded. For more information, run 'Import-Module scripts'. error while executing Orchestration activity](https://support.servicenow.com/kb_view.do?sysparm_article=KB0747488)
    4.  ["The attribute syntax specified to the directory service is invalid" error on Create AD Object Orchestration activity](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743774)
    5.  [The specified directory service attribute or value does not exist error on Create Ad Object orchestration activity](https://support.servicenow.com/kb_view.do?sysparm_article=KB0713097)
    6.  [Orchestration: 'Add user to group' activity fails for few users](https://support.servicenow.com/kb_view.do?sysparm_article=KB0716443)
    7.  [Orchestration activities failing with "Incorrect parameter count: procedure expecting 0"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0744395)
    8.  [Orchestration AD: Possibility of using Create and enable User account in one workflow and may see errors as "The server is unwilling to process the request."](https://support.servicenow.com/kb_view.do?sysparm_article=KB0785130)
    9.  [Orchestration activities fail with the error: "Fault description: null"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0688371)
    10.  [Orchestration Query AD Error - Unable to find any validated MID Server based on status (degraded), and application: Orchestration, and IP Range](https://support.servicenow.com/kb_view.do?sys_kb_id=51f5f2c8dbbb2b0054250b55ca96192e)
    11.  [ECCResponseTimeoutException while processing SOAP/JDBC requests through Orchestration](https://support.servicenow.com/kb_view.do?sysparm_article=KB0696865)
    12.  [Orchestration workflow input variable Object data field is limited to 254 characters when editing 'Create AD Object' workflow activity](https://support.servicenow.com/kb_view.do?sysparm_article=KB0622624)

# 4\. Activity Designer

## Product Docs

1.  1.  [Orchestration Activity Designer](https://docs.servicenow.com/csh?topicname=c_WorkflowActivityDesigner.html&version=latest#c_WorkflowActivityDesigner)
    2.  [Available activity packs](https://docs.servicenow.com/csh?topicname=t_ActivateAnActivityPack.html&version=latest#t_ActivateAnActivityPack)

## Knowledge Articles

1.  1.  [Delete the unwanted Orchestration activities with multiple versions](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864799 "Delete the unwanted Orchestration activities with multiple versions")  
        
    2.  [How to access the output returned by an Orchestration Activity](https://support.servicenow.com/kb_view.do?sysparm_article=KB0635207)
    3.  [Uploaded images cannot be selected for placement in the Orchestration Activity Designer](https://support.servicenow.com/kb_view.do?sysparm_article=KB0596203)

# 5\. Client Software Distribution(CDS)

## Product Docs

1.  1.  [Client Software Distribution](https://docs.servicenow.com/csh?topicname=c_ClientSoftwareDistribution.html&version=latest)

## Knowledge Articles

1.  1.  [Client Software Distribution - SCCM - Unable to Discover](https://support.servicenow.com/kb_view.do?sysparm_article=KB0759363)
    2.  ["Load Demo Data" with the activation of Orchestration - Client Software Distribution plugin causes Service Creator to show incomplete page](https://support.servicenow.com/kb_view.do?sysparm_article=KB0634363) 

# 6\. Orchestration DataBus

## Product Docs

1.  1.  [Orchestration Databus](https://docs.servicenow.com/csh?topicname=c_OrchestrationDatabus.html&version=latest)

## Knowledge Articles

1.  1.  [Orchestration - Workflow throwing "Unable to find an activity for databus lookup ID" error](https://support.servicenow.com/kb_view.do?sysparm_article=KB0811695)

# 7\. Domain Separation for Orchestration

## Product Docs

1.  1.  [Domain Separation in Orchestration](https://docs.servicenow.com/csh?topicname=domain-separation-orchestration.html&version=latest)

## Knowledge Articles

1.  1.  [The orchestration workflows get stuck in a domain-separated instance](https://support.servicenow.com/kb_view.do?sysparm_article=KB0694001)

# 8\. MID Server for Orchestration

## Product Docs

1.  1.  [MID Server For Orchestration](https://docs.servicenow.com/csh?topicname=c_OrchestrationMID.html&version=latest#c_OrchestrationMID)

## Knowledge Articles

1.  1.  [Orchestration activity failing with the error: "Unable to resolve hostname: \*\*\*\*\*\* and default MID Server null is down/invalid"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0748693)
    2.  [Capabilities on Orchestration activity is not routing to the correct MidSever](https://support.servicenow.com/kb_view.do?sysparm_article=KB0718055)
    3.  [AD orchestration activity in integration hub is picking wrong MID Server](https://support.servicenow.com/kb_view.do?sysparm_article=KB0792429)
    4.  [How a mid server is selected for Orchestration activities](https://support.servicenow.com/kb_view.do?sysparm_article=KB0693456)
    5.  [MID Server selection for AD Orchestration activities with different Domain Controllers for different environment](https://support.servicenow.com/kb_view.do?sysparm_article=KB0785104)
    6.  [Resolve DNS Name activity in orchestration, fails to use available MID servers when no default is set](https://support.servicenow.com/kb_view.do?sysparm_article=KB0717277)
    7.  [During an upgrade, MID Server selection fails for Orchestration](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597894)

# 9\. Orchestration Probes

## Product Docs

1.  1.  [Probes used by the orchestration](https://docs.servicenow.com/csh?topicname=r_OrchestrationProbes.html&version=latest)

# 10\. Orchestration ROI 

## Product Docs

1.  1.  [Orchestration ROI](https://docs.servicenow.com/csh?topicname=c_OrchestrationROI.html&version=latest#c_OrchestrationROI)
    2.  [Create an Orchestration ROI automation entry record](https://docs.servicenow.com/csh?topicname=t_CreateOrchROIAutoEntryRecord.html&version=latest)

# 11\. Powershell for Orchestration

## Product Docs

1.  1.  [PowerShell Activity Designer](https://docs.servicenow.com/csh?topicname=c_PowershellActivityDesigner.html&version=latest)

## Knowledge Articles

1.  1.  [PowerShell probe version 2 system property](https://docs.servicenow.com/csh?topicname=powershell-probe-v2.html&version=latest "PowerShell probe version 2 system property") 
    2.  [PowerShell log property](https://docs.servicenow.com/csh?topicname=powershell-log-property.html&version=latest)
    3.  [Orchestration Activity fails with error Access denied when running power-shell scripts](https://support.servicenow.com/kb_view.do?sysparm_article=KB0750852)
    4.  [Customer Powershell command in Orchestration activity and character limit](https://support.servicenow.com/kb_view.do?sysparm_article=KB0716371)
    5.  [Orchestration Powershell Activity timeout: "Terminated the probe because the max timeout was reached: 610 seconds"](https://support.servicenow.com/kb_view.do?sysparm_article=KB0635788)
    6.  [Powershell MID Server Script Files used by Orchestration Activity Packs are not signed, which is a requirement for some customers](https://support.servicenow.com/kb_view.do?sysparm_article=KB0752093) 

# 12\. Orchestration Workflow

## Product Docs

1.  1.  [Orchestration workflow](https://docs.servicenow.com/csh?topicname=r-orchestration-introduction.html&version=latest#d35925e325)

## Knowledge Articles

1.  1.  [Orchestration activity in the workflow will not accept Record Producer variables](https://support.servicenow.com/kb_view.do?sysparm_article=KB0713585)
    2.  [Running Orchestration workflow gives the below error: The term is not recognized as the name of a cmdlet, function\`, script file, or operable program](https://support.servicenow.com/kb_view.do?sysparm_article=KB0788356)
    3.  [New Hire Orchestration workflow will not open](https://support.servicenow.com/kb_view.do?sysparm_article=KB0743175)
    4.  [Orchestration workflow is cancelling on its own without any errors](https://support.servicenow.com/kb_view.do?sys_kb_id=7bdbc476db4ce304a8562926ca961993)

# 13\. Dashboards

## Product Docs

1.  1.  [Orchestration Usage dashboard](https://docs.servicenow.com/csh?topicname=orchestration-usage-dashboard.html&version=latest)

## Knowledge Articles

1.  1.  [Why does the Orchestration Usage Dashboard say 'No Data To Display'](https://support.servicenow.com/kb_view.do?sysparm_article=KB0693335)

# 14\. Troubleshooting

1.  [Troubleshooting Power-shell Orchestration Workflow not working with new MID Server](https://support.servicenow.com/kb_view.do?sysparm_article=KB0748533)
2.  [Orchestration Troubleshooting](https://support.servicenow.com/kb_view.do?sysparm_article=KB0789084 "Orchestration Troubleshooting")
3.  [Orchestration: Troubleshooting - SCCM Discovery Issues](https://support.servicenow.com/kb_view.do?sys_kb_id=214ee0f5dba76e804837f3231f961953)
4.  [Steps that can help troubleshooting domain controller issues when doing ActiveDirectory Orchestration](https://support.servicenow.com/kb_view.do?sys_kb_id=d866bf39db126b401089e15b8a96190c)

# 15\. Additional Information

1.  [Orchestration examples](https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/product/orchestration/concept/c_OrchExmplActiveDirUserMgmt.html#c_OrchExmplActiveDirUserMgmt)
2.  [Orchestration custom activity templates](https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/administer/orchestration-activity-designer/concept/c_ActivityDesignerComponents.html#c_ActivityDesignerComponents)
3.  [Client software distribution extension framework](https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/Chunk427796333.html#c_CSDExtensionFramework)
4.  [Orchestration Microsoft exchange activity pack support for 2016](https://support.servicenow.com/kb_view.do?sys_kb_id=bea42e58dbd60850d58ea345ca9619e4)

### Release

ANY

### Resolution

ALL
