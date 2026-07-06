---
title: "Application Discovery Mapping Overview"
aliases:
  - KB0717161
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717161
kb_number: KB0717161
last_modified: 2025-05-27
---

## Application Discovery Mapping Overview

  

### Issue

Application Dependency Mapping (ADM) probes collects information on the processes running on a server. The ADM (Application Dependency Mapping) probe is triggered on computers and servers. This probe collects information about the running processes on such devices. 

The script includes DiscoveryADMSensor, EnrichProcessesAndConnections, and ApplicationDependencyMapping work together to process the information returned by the probe. In particular, the ApplicationDependencyMapping script include checks each returned process to determine if such process matches the conditions described in one of the process classifiers. Processes which have a matching classifier may trigger a probe, or pattern, in order to collect more information on the process and create an application record in the CMDB.

The triggering of probes/patterns for such processes will depend on the configurations as per the process classifier(discovery\_classy\_proc) and process handlers(discovery\_proc\_handler).

More information can also be seen on:

-   [Application Dependency Mapping (ADM) for Discovery](https://docs.servicenow.com/csh?topicname=r_ApplicationDependencyMapping.html&version=latest)

### Release

All

### Resolution

## Table of Contents

-   [Application Dependency Mapping Flow](#mcetoc_1g8e6mec4k)
-   [Troubleshooting](#mcetoc_1g8e6mec4l)
-   [Common Issues](#mcetoc_1g8e6mec4m)
-   [Examples](#mcetoc_1g8e6mec4n)
-   [Input Processing Debug](#mcetoc_1g8e6mec4o)

### Application Dependency Mapping Flow

The Application Dependency Mapping probe is triggered once the Identification phase completes for a device being discovered.

The Application Dependency Mapping:

1.  Gathers the running processes and connections on a server via the ADM probe.
    -   **Note:** There are multiple ADM probes, and the ADM probe triggered will depend on the classifier, unix, windows, linux, etc.
2.  The data returned by the ADM probe is processed by the ADM sensor. The ADM sensor creates a JSON payload that is enriched by the DiscoveryJSONADMSensor script include.
3.  The DiscoveryJSONADMSensor calls the ApplicationDependencyMapping script include.
4.  Finally, the ApplicationDependencyMapping script include creates the application CI according to the "Discovery Definition > CI Classification > Processes" configuration.

#### Overall Input Flow

![Flow](https://support.servicenow.com/sys_attachment.do?sys_id=a81634c1db00f8d066e0a345ca961954 "Flow")

-   Process classifier table: discovery\_classy\_proc
-   Process handlers table: discovery\_proc\_handler

The following document highlights some of the applications discovered out of box:

-   [Software Discovery](https://docs.servicenow.com/csh?topicname=c_Software.html&version=latest "Software Discovery")

The following document goes over NGINX web server discovery and is a good example of a process classifier:

-   [NGINX web server discovery](https://docs.servicenow.com/csh?topicname=c_NGINXWebServerDiscovery.html&version=latest "NGINX web server discovery")

The following links will also be helpful in understanding ADM and process classification:

-   [Create a Discovery process classification](https://docs.servicenow.com/csh?topicname=t_CreateAProcessClassification.html&version=latest "Create a Discovery process classification")
-   [On classification script objects for Discovery](https://docs.servicenow.com/csh?topicname=r_OnClassificationScriptObjects.html&version=latest "On classification script objects for Discovery")
-   [Create a Discovery process handler](https://docs.servicenow.com/csh?topicname=t_CreateAProcessHandler.html&version=latest "Create a Discovery process handler")

### Troubleshooting

More often than not, the issue being investigated is that the pattern or probe for an application was not triggered or the application was not created. The issue of an application not created even though pattern/probe was triggered is something that happens after successful mapping of the application, troubleshooting for such would be the same as troubleshooting any other probe/pattern input processing and outside the scope of this knowledge article (KB). Probe permission issues or input errors would also be investigated like any other probe. The goal of this KB is so that the probe or pattern will be successfully triggered for an application.

Overall troubleshooting steps are to:

1.  Open ADM Probe input
2.  Confirm no errors in input processing
3.  Confirm payload contains the process which should trigger probe/pattern
4.  Check process information matches process classifier condition
5.  Check that process classifier is active and has a probe/pattern in the "Triggers probes" related list
6.  Check if the process information matches a process handler that is active and set classify = false
7.  If necessary (root cause not found in one of the steps above), debug input processing

### Common Issues

**Application Dependency Mapping probe not triggered | No application records created**

If no application CIs are created at all when discovering a server, the application dependency mapping probe may be turned off for the specific class. As a solution, check if the probe is present on the classifier and make sure it is active.

1.  Go to "Discovery Definition > CI Classification > All".
2.  Search for the classifier used when discovering the server, "table=cmdb\_ci\_win\_server" for windows servers in the following example.
3.  Open the classifier and find the probe on "Triggers Probes" related list.  
    ![](sys_attachment.do?sys_id=9bd878919779ee105ad8f6e11153af8b)

**Application Dependency Mapping probe triggered, however application is not created**

In this case, it is likely that the process information did not have a condition match under the discovery\_classy\_proc table. For such cases:

1.  Open the Application Dependency Mapping input ecc\_queue record.
2.  Find the process in the payload and check for any potential errors in the payload.
3.  Compare the process information with the process classifier which should have created the application and triggered further exploration probes.
4.  Adjust the process classifier conditions to match on the intended process if necessary.

### Examples

#### Successful MSSQL discovery

In the following example we discover test server appserver-01. We can see in the following image that a "SQL Server Analysis Service" and two "MSFT SQL Instances" were discovered and added to the CI.

![Server Discovered](sys_attachment.do?sys_id=dfd878919779ee105ad8f6e11153af58 "Server Discovered")

The following screenshot shows the ECC Queue related list for the discovery status, ordered newest to oldest. We can see that probes were triggered for each application discovered after the ADM input was processed.

![ECC Queue](sys_attachment.do?sys_id=53d878919779ee105ad8f6e11153af5c "ECC Queue")

Taking the "Windows - MSSQL" probe as an example, we can search "Discovery Definition > Probes" for "Windows - MSSQL" to find the probe. From the "Triggered by classifier" related list we can find the process classifier which triggered the probe.

![Probe To Classifier](sys_attachment.do?sys_id=1bd878919779ee105ad8f6e11153af86 "Probe To Classifier")

Next, we can see the condition in the process classifier which triggers the "Windows - MSSQL" probe.

![MSSQL Process Classifier](sys_attachment.do?sys_id=53d878919779ee105ad8f6e11153af89 "MSSQL Process Classifier")

Finally, we can see the process information in the payload returned by the "Windows - Application Dependency Mapping" probe.

![ADM Payload](sys_attachment.do?sys_id=9bd878919779ee105ad8f6e11153af5e "ADM Payload")

#### Custom "ModemManager"

In this example we will be using a custom process classifier for a process with name "ModemManager". We open the ADM Probe input, confirm no error in input processing, and checked the process is present in the payload

1.  Open the discovery status
2.  Select the "ECC Queue" related list
3.  Check that the "Error String" field is empty  
    ![Error String](https://support.servicenow.com/sys_attachment.do?sys_id=6c1634c1db00f8d066e0a345ca961951 "Error String")
4.  Click on the Application Dependency Mapping input
5.  Once opened, search for process  
    ![Payload](https://support.servicenow.com/sys_attachment.do?sys_id=e41634c1db00f8d066e0a345ca961957 "Payload")
6.  Navigate to parent CI, confirm the process was created successfully  
    ![Process](https://support.servicenow.com/sys_attachment.do?sys_id=e81634c1db00f8d066e0a345ca961966 "Process")

With the above steps, we know that the process information is collected successfully and the process was created. Next, we check the process information matches process classifier condition & is active

1.  Navigate to Discovery Definition > CI Classification > Process
2.  Search for the process classifier based on the table where the application should be created, in this case "cmdb\_ci\_modem\_manager"  
    ![Classifier List](https://support.servicenow.com/sys_attachment.do?sys_id=ec1634c1db00f8d066e0a345ca96193c "Classifier List")
3.  Open the classifier and compare the conditions with the fields in the process  
    ![Classifier Configuration](https://support.servicenow.com/sys_attachment.do?sys_id=501634c1db00f8d066e0a345ca96193a "Classifier Configuration")
4.  Check that the "Triggers probes" related list in the process classifier is not empty
5.  Check that the records in the "Triggers probes" related list have field active = true, if all are active = false no probes/patterns will be triggered
6.  Navigate to table discovery\_proc\_handler and confirm there are no matching handlers active and configured "classify" = false, if classify = false process will not be classified and probe/pattern will not be triggered

At this point, we have confirmed that the process information is collected successfully, a process classifier is present, and no handlers where "classify" = false. If the classifier uses probes, the application would be created at this point, if using patterns the application is only created when the input from the pattern is processed. 

![Related Items](https://support.servicenow.com/sys_attachment.do?sys_id=281634c1db00f8d066e0a345ca961969 "Related Items")

### Input Processing Debug

See following documents on how to use the script debugger and how to reprocess an ecc\_queue input in your session:

-   [Script Debugger](https://support.servicenow.com/kb_view.do?sysparm_article=KB0815530 "Script Debugger")
-   [Ecc Queue Processing](https://support.servicenow.com/kb_view.do?sysparm_article=KB0718653 "Ecc Queue Processing")

At this point, we checked all necessary configuration and input data. If probes/patterns are not triggered as expected, we can to debug the ADM input processing. We can use the debug to determine if perhaps the process matched another classifier, sometimes the process will match an "incorrect" classifier. It is helpful but not necessary to first edit the ADM input payload so that only the process of interest is present. Example:

![Edited Payload](https://support.servicenow.com/sys_attachment.do?sys_id=201634c1db00f8d066e0a345ca96194f "Edited Payload")

The classify function in the ApplicationDependencyMapping script is a good place to start. Click on the line to add a breakpoint.

Next, reprocess the input via script backgrounds:

var eccRecord = new GlideRecord('ecc\_queue');  
eccRecord.get('<ecc\_queue\_sys\_id>');  
var sp = new SncSensorProcessor(eccRecord);  
sp.process(); 

Processing of the input should stop in the breakpoint set in the script.

In the following screenshot, we see the sys\_id of classifier used. Next we should open the classifier by sys\_id to confirm the "correct" classifier was used.

![Debug](https://support.servicenow.com/sys_attachment.do?sys_id=2c1634c1db00f8d066e0a345ca96193f "Debug")

### Related Links

The following blog post has an example on how to configure discovery to collect information on applications not discovered out of box:

-   -   [Discovering Eugene's "Special" Application](https://community.servicenow.com/community?id=community_Article&sys_id=5764adc8db416388d58ea345ca9619fb "Discovering Eugene's ")
