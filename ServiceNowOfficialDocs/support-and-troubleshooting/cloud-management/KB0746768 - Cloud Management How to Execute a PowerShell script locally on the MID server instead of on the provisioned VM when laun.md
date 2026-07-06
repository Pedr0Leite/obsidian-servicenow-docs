---
title: "Cloud Management: How to Execute a PowerShell script locally on the MID server instead of on the provisioned VM when launching a stack (during cloud provisioning)"
aliases:
  - KB0746768
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746768
kb_number: KB0746768
last_modified: 2024-04-07
---

## Cloud Management: How to Execute a PowerShell script locally on the MID server instead of on the provisioned VM when launching a stack (during cloud provisioning)

  

### Issue

# Description

This KB demonstrates how to execute a PowerShell script locally on the MID server instead of on the provisioned VM when launching a stack (during cloud provisioning).

# Procedure

1> Create a new Cloud API  
Open Cloud Admin Portal > Design > Cloud API > API tab > click on New button, fill in information as below:  
\-Cloud API: any name as required  
\-Interface: Node Access Interface  
\-Product: Node Access  
\-Version: 2.0  
\-Script Type: PowerShell

2> Configure your PowerShell script  
Open the Cloud API newly created, under CAPI Method Mappers > click on 2.0 link in ExecutePowershellScript row as showing in the screenshot below:

![](/sys_attachment.do?sys_id=06292caedb02b450e515c22305961989)

Then open the "Request script":

![](/sys_attachment.do?sys_id=96292caedb02b450e515c2230596198e)

This is the PowerShell script that runs locally on MID server.

You can either write PowerShell script in this file, e.g. echo 'asdf' > c:\\temp\\a0.txt

Or you can call your own script that's stored on the MID server, e.g. c:\\temp\\a1.ps1

3> In the Resource Block, add a step to call the API.

You can add the step to any resource block. In this example, we have a Test01 Blueprint,  so we will go to the resource block that's corresponding to it: **Test01 Blueprint Resource**.

Switch the resource block to Draft mode first, under Operations tab, click on Steps,

in Operations drop-down list, select Provision, then click on "Add step"

![](/sys_attachment.do?sys_id=9e292caedb02b450e515c2230596199f) 

The **Add Operation Steps** box pops up, fill in information below:

\-Operation Type: Invoke Cloud API

\-API Provider: NodeAccess

\-API Interface: Node Access Interface

\-API Method: ExecutePowershellScript

\-CAPI Version: 2.0

4> After the step is added, under Input, fill in any string value for the Parameters. For example:

\-NodeAddress: 'asdf'

\-NodeCredential: 'asdf'

\-Script: 'asdf'

\-ScriptParameters: 'asdf'

\*\*\* You can also create Input Parameters and takes values from user's input, for example, create below Step input:

\-ScriptParameters: ${parameter.PSScriptParameters}

Then under "Input Parameters", create below then save.

\-Name: 'PSScriptParameters'

\-Datasource: 'Text'

\-Create Form Parameter: tick

TIPS: You can refer to other resource blocks to check how the mapping works.

For example, check resource block **Virtual Server**, then check Input Parameters and Steps of the **ExecuteScript** operation (this is the OOB operation)

NOTE: Once new input parameters are added, please configure it on the Blueprint so it will show up on the form:

![](/sys_attachment.do?sys_id=de292caedb02b450e515c223059619a4) 

NOTE: There are four out of the box inputs of the step: NodeAddress, NodeCredential, Script, ScriptParameters

These parameters are stored as environmental variables and can be called in the script defined in step 2>.

For example, try below script:

echo $env:nodeaddress > c:\\temp\\a01.txt;  
echo $env:nodecredential > c:\\temp\\a02.txt;  
ls env: > c:\\temp\\a003.txt;

5> Switch the resource block from Draft to Published.

# Applicable Versions

Kingston, London, Madrid

# Additional Information

\> In Madrid, when adding operation steps on resource block, a new option is available: **Invoke Workflow**

This option allows you to launch an Orchestration workflow during cloud operations.

This is an alternative way to run PowerShell scripts from MID server (using Orchestration Custom PowerShell activity).

![](/sys_attachment.do?sys_id=12292caedb02b450e515c223059619aa)
