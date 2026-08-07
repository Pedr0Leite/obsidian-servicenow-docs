---
title: "How to link an ECC Queue record back to a specific Feature or Job"
aliases:
  - KB0727132
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727132
kb_number: KB0727132
last_modified: 2026-03-23
---

## How to link an ECC Queue record back to a specific Feature or Job

  

### Issue

All jobs that run via a MID Server, and some that don't, pass messages via the ECC Queue table \[ecc\_queue\]. The Agent Correlator field \[agent\_correlator\] is used by code to keep track of the originating job.

Although this list is in no way comprehensive, it should help you link an ECC Queue record back to the job it came from, to understand the code responsible. The code involved in launching the probe, the Probe code that runs in the MID Server , and Sensor code back in the instance, is usually owned by the particular feature, and the MID Server platform is simply running it in a java thread. 

Note: By the Zurich release, most out-of-box legacy Orchestration workflows have been ported over to IntegrationHub flows. This document has not been updated yet for all of those changes.

## Table of Contents

-   [IT Operations Management](#mcetoc_1g24h52d325)
    -   [ITOM Visibility - Cloud License Estimator](#mcetoc_1g24h52d326)
    -   [ITOM Visibility - Discovery / Service Mapping](#mcetoc_1j99khn2o1j)
    -   [ITOM Visibility - Help The Helpdesk (HTHD)](#mcetoc_1g24h52d326)
    -   [ITOM Visibility - Test Credential](#mcetoc_1g24h52d326)
    -   [ITOM Visibility - Agent Client Collector - Visibility Content (ACC-VC)](#mcetoc_1g24h52d326)
    -   [ITOM Visibility - Kubernetes Visibility Agent](#mcetoc_1j6dg8iokii)
    -   [ITOM Optimization - Cloud Discovery - Direct from Instance](#mcetoc_1g24h52d327)
    -   [ITOM Optimization - Cloud Management](#mcetoc_1g24h52d327)
    -   [ITOM Health - Event Management](#mcetoc_1g24h52d328)
    -   [ITOM Health - Synthetic Monitoring](#mcetoc_1j77bissp6)
    -   [ITOM Health/Visibility - Agent Client Collector framework (ACC-F) / Visibility (ACC-V) / Monitoring (ACC-M)](#mcetoc_1g24h52d328)
    -   [ITOM Health - Health Log Analytics](#mcetoc_1g24h52d328)
    -   [ITOM Health - Operational Intelligence](#mcetoc_1g24h52d328)
-   [Integrations](#mcetoc_1g24h52d329)
    -   [AttachmentCreator SOAP web service](#mcetoc_1g24h52d32h)
    -   [Command probe](#mcetoc_1g24h52d32i)
    -   [DevOps Change Velocity](#mcetoc_1j7hjdsr0e)
    -   [Export Sets](#mcetoc_1j7e959v46)
    -   [Import Set / JDBC](#mcetoc_1j0r90kv092)
    -   [IntegrationHub](#mcetoc_1g24h52d32f)
    -   [JavascriptProbe](#mcetoc_1g24h52d32e)
    -   [LDAP](#mcetoc_1g24h52d32c)
    -   [OAuth2 Credential Token refresh](#mcetoc_1j608ophg7p)
    -   [Orchestration](#mcetoc_1g24h52d32a)
    -   [Outbound REST / SOAP](#mcetoc_1g24h52d32b)
    -   [Syslog Integration](#mcetoc_1g24h52d32g)
    -   [3rd party:](#mcetoc_1g24h52d32j)
-   [IT Service Management](#mcetoc_1g24h52d32k)
    -   [Agent Client Collector for Security Incident Response](#mcetoc_1g24h52d32n)
    -   [Digital End-User Experience (DEX)](#mcetoc_1j742pac85j)
    -   [Employee Document Management](#mcetoc_1g24h52d32o)
    -   [Microsoft Exchange Online for Security Operations](#mcetoc_1g24h52d32m)
    -   [Security Incident Response](#mcetoc_1g24h52d32l)
-   [Now Platform](#mcetoc_1g24h52d32p)
    -   [Source Control](#mcetoc_1g24h52d32q)
    -   [MID Server](#mcetoc_1g24h52d32r)

## IT Operations Management

### ITOM Visibility - Cloud License Estimator

This uses RESTMessageV2, synchronously, direct from the instance, so does not work via the ECC Queue. You will find requests logged in the Outbound HTTP Logs \[sys\_outbound\_http\_log\].

### ITOM Visibility - Discovery / Service Mapping

ECC Queue Topics:

-   ADMEPowershell  
    -   a Windows PowerShell based probe specifically for Application Dependency Mapping.
-   APIProxyProbe
-   CimProbe
-   Command  
    -   Runs the command in the 'Name' field from the shell (Linux) or Command Prompt (Windows) of the MID Server host.
-   CommandPipeline
-   DNS
-   DNSLookupProbe
-   DNSNameResolver
-   HorizontalDiscoveryProbe  
    -   Runs the Discovery or Service Mapping Pattern specified the name field, on the MID Server, for the target server in the source field
-   HTTPClassyProbe
-   JavascriptProbe  
    -   Runs the Javascript from the 'script' parameter of the payload. Usually calls a MID Server Script Include \[ecc\_agent\_script\_include\]'
-   MultiProbe  
    -   A probe containing multiple other Discovery probes
-   PatternDebuggerProbe
-   Powershell  
    -   Run a Powershell script on the MID Server, which may in turn do things to a target
-   RCASmcPurgeProbe
-   ServiceDiscoveryProbe
-   ServiceWatchTraceRouteProbe
    -   Runs ping then traceroute from target host to IP as part of network path determination process.
-   Shazzam  
    -   The Port scanner for Discovery
-   SNMP
-   SSHCommand
-   TrafficBasedDataCollectionUnix
-   URLCertificateScanProbe  
    -   Certificate Discovery. Name is "URL Certificate Scan"
-   VMWareProbe
-   WindowsCommand  
    -   Runs a command on the command line, of the target server in the source field.
-   WMIRunner  
    -   Retrieves data from Windows Management Instrumentation (WMI) namespaces given in the parameters, of the target server in the source field.

Agent Correlator:

-   Sys ID of the Discovery Status record \[discovery Status\]

Source:

-   Varies according to Probe. An IP Address can be linked to a specific Discovery Device History \[discovery\_device\_history\] record within the Discovery Status to find the CMDB CI.

Sensors:

-   Discovery - Sensors

Priority:

-   Interactive: Pattern Designer debug mode, Cancel Discovery, XMLStats
-   Expedited: Service Mapping, Discover Now, Quick Discovery, Shazzam port scan probes of Standard priority schedules.
-   Standard: Scheduled Horizontal Discoveries, except Shazzam

### ITOM Visibility - Help The Helpdesk (HTHD)

Although officially deprecated for almost a decade, this plugin does still get installed automatically as part of Discovery.

ECC Queue Topics:

-   WMILoader (input only)

Agent:

-   wmi

Name:

-   wmi.script

Source:

-   Hostname of the Windows computer that sent the record to the ECC Queue

Sensor Business Rule:

-   ECC Queue Reader - Async business rule which uses GlideappWMILoader in WMILoader.java.

### ITOM Visibility - Test Credential

Note: This is  Discovery feature, for testing credentials in the context of how they would be used by Discovery scans. Without fully understanding exactly what the test is testing, the test results are often misleading. e.g. When testing a windows credential, the WMI port 135 entered by default is actually  ignored, and what really happens is an attempt to create a remote PowerShell connection, using New-CimSession, making it useless in most other use cases.

ECC Queue Topics:

-   CommandPipeline

Source:

-   IP Address of the host that the credential is being tested against

Payload

-   Will contain "type="TestCredentialCommand""

### ITOM Visibility - Agent Client Collector - Visibility Content (ACC-VC)

See ACC-F in general. Except for...

#### Discovery Pattern via ACC

Docs: [Application patterns for the Agent Client Collector](https://www.servicenow.com/docs/csh?topicname=application-patterns-acc.html&version=latest)

When ACC-V gets lists of Running Processes from the Enhanced Discovery check, it will compare those against Discovery's Process Classifiers, and can trigger the Application Pattern. Discovery Patterns execute on a MID Server, and that is also the case with ACC-V. The ECC Queue records look very similar. For most Operations that would usually have the MID connec to the target's management interfaces, the Agent is told to run the command on itself directly. The main record difference is there is no agent\_correlator, because there is no discovery\_status, and the payload will contain a parameter for the Agent ID.

Topic:

-   HorizontalDiscoveryProbe

Name:

-   Pattern Launcher: <pattern name>

Payload:

-   There is a parameter for agent\_id. This tells the MID which Agent install to execute the steps on.

Source:

-   One of the IP addresses of the Agent. 

Agent correlator:

-   Blank (there is no discovery\_schedule to reference in this scenario)

From host:

-   Blank. (However it would be nice if it contained the agent\_id, or some other clue to clearly indicate it is for a specific Agent, and be listed when Show ECC queues is clicked on an agent form - enhancement TBC.)

Sensor:

-   'Discovery - Sensors' business rule, reused from Discovery.

Notes: There will be a Pattern Log \[sa\_pattern\_log\] generated as usual, which can be seen in the related lists of an Agent form, in Discovery view. That related list works from the Source IP (which might not be the IP in the agent record - TBC)

### ITOM Visibility - Kubernetes Visibility Agent

Queue Topics:

-   k8s\_informer

For further information, see:  
[KB2717556 Understanding Kubernetes Visibility Agent ECC Queue records, and Sensor business rules](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2717556)  
[KB1580241 Controlling the number of "Kubernetes Visibility Agent" (formerly CNO for Visibility) concurrent worker threads](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1580241)

### ITOM Optimization - Cloud Discovery - Direct from Instance

ECC Queue Topics:

-   RESTProbe
-   SigningRESTProbe
-   AWSRESTProbe

Agent:

-   mid.server.NODE\_AGENT

Agent Correlator:

-   TBC

### ITOM Optimization - Cloud Management

ECC Queue Topics:

-   TBC

Agent Correlator:

-   TBC

### ITOM Health - Event Management

ECC Queue Topics:

-   -   ConnectorProbe
    -   MIDExtension:VCenterExtension
    -   MIDExtension:TrapListenerExtension 
    -   MIDExtension:PipelineManager
    -   MIDExtension:WebServerExtension

Agent Correlator:

-   Empty

Source:

-   For Connectors, the name of the Connector Instance \[em\_connector\_instance\]

Name:

-   For MID Server Extensions, name of the Extension, and Context Name and Sys\_id \[ecc\_agent\_ext\_context\]

Sensor:

-   'Event Management - Connector' business rule handles ConnectorProbe, and 'Process MID Server Extension Status' business rule handles MIDExtension ones.

### ITOM Health - Synthetic Monitoring

[Docs: Synthetic Monitoring](https://www.servicenow.com/docs/csh?topicname=synthetic-monitoring-landing-page.html&version=latest)

Depending on the 'Location' of the Check, requests are sent either:

#### Hosted Location (direct from the instance)

'current instance' does not use the ECC Queue. You will find requests logged in the Outbound HTTP Logs \[sys\_outbound\_http\_log\].

#### MID Server

Topic:

-   JavascriptProbe

Name:

-   SyntheticMonitoringCheckRunner

Payload:

-   synthetic\_params - This is a Base64 encoded value. Once decoded, you'll have a JSON object containing values for:
    -   ci\_sys\_id
    -   location\_sys\_id
    -   headers
    -   synthetic\_check\_sys\_id
    -   httpMethod
    -   credential\_sys\_id
    -   url

Sensor:

-   'Synthetics Mid Runner Result Processor' Business Rule on ecc\_queue, where name=SyntheticMonitoringCheckRunner.  This uses function midRunnerResultProcessor from ServiceNow Fluent code scripts.

#### Agent Client Collector

These probes are triggered by sn\_sow\_synthetics\_check\_single\_api\_sysauto\_script scheduled scripts, via sys\_trigger, with name '<check name>-synthetics bg job'.

ECC Queue Topics:

-   MonitoringProbe

Payload:

-   The check is 'sow-synthetic.monitoring'.  
    This check is used to run synthetic api requests against a URL and write both metrics and events based on the synthetic definition. Note that since each instance of this check is created and managed by the synthetic application with different command args, the command on the definition is empty.

Sensor:

-   MID Server: SnytheticMonitoringHTTPResultParser. Parses JSON results from the ACC synthetic plugin's synthetic-monitoring HTTP check into metrics, events, and result records.
-   Instance: AgentNowResponseProcessor business rule, using AgentNowHandler script include,  processEccRecord function.  
    The 'SOW Synthetic Monitoring' sn\_agent\_check\_type uses checkTypeHandleBatchUpdate from ServiceNow Fluent code scripts.

### ITOM Health/Visibility - Agent Client Collector framework (ACC-F) / Visibility (ACC-V) / Monitoring (ACC-M)

Agent:

-   mid.server.<A MID Server Name> - ACC is connecting via an on-premise MID Server. See:
    -   [Agent Client Collector architecture](https://www.servicenow.com/docs/csh?topicname=acc-concept.html&version=latest)
-   mid.server.acc-cnc  - ACC is MID-less, and connecting via a regional ITOM Cloud Services Gateway in ServiceNow's datacenter (ACC CnC). See:
    -   [Configure MID-less Agent Client Collector for DEX](https://www.servicenow.com/docs/csh?topicname=config-midless-acc.html&version=latest)
    -   [DEX Architecture](https://www.servicenow.com/docs/csh?topicname=dex-architecture.html&version=latest)

ECC Queue Topics:

-   MonitoringProbe  
    -   Name/Source=on\_demand\_request  
        -   Payload will contain the name of the Check to run on the ACC, and the Agent ID(s) to run the check on. Payload is the only field with information on which feature, check, Agent is involved.
        -   Inputs are often too big for the payload field so end up in a payload.txt attachment, meaning payload contains filter on ecc queue lists will miss out records. The attachment needs opening to see what the input was for.
    -   Name/Source =config\_publish/policy\_deleted  
        -   Updates running\_checks\_num in sn\_agent\_ci\_extended\_info record.
        -   Sensor business rule: MonitoringProbeSensor
    -   Name/Source = auto\_mid\_selection  
        -   "Try redistributing connected agents" UI Action on MID Server form.
    -   Sensor
        -   Instance: AgentNowResponseProcessor business rule, using AgentNowHandler script include,  processEccRecord function. sn\_agent\_check\_type records map the Check Type specified in the payload to the Script Include that is run as the sensor for that check type. e.g. "EnhancedDiscovery" type uses EnhancedDiscoveryHandler script include. "ACC Spoke" just updates a record in sn\_acc\_spoke\_action\_response.
-   DataInputMarkerProbe / DataInputExamplesProbe /DataInputConnectorPortCheckProbe  
    -   Used by Log Analytics
-   MIDExtension:MonitoringExtension  
    -   Stop and start extensions

Sensor:

-   All MonitoringProbe inputs, for any feature, are initially handled by the AgentNowResponseProcessor business rule. sn\_agent\_check\_type records map the Check Type specified in the payload to the Script Include that is run as the sensor for that check type.

### ITOM Health - Health Log Analytics

ECC Queue Topics:

-   queue.log\_streaming.stats  
    -   collects streaming sources stats data on the MID and reports to the instance. This data will be available in the instance sn\_occ\_log\_streaming\_sources table.
-   queue.log\_analytics.stats  
    -   collects metrics from the log analytics services on the MID and reports to the instance. Those metrics will be reflected in the instance xmlstats.do
-   MIDExtension:DataInputWrapperExtension  
    -   Stop/Start/etc. of the MID Server extension
-   DataInputTestConnectionProbe
    -   Tests a Data Input.
-   DataInputMarkerUpdate  
    -   Periodic Inputs from the Marker Service

For ACC-L, see the ACC section.

### ITOM Health - Operational Intelligence

ECC Queue Topics:

-   MetricConfigProbe  - Synchronizes Metric Configuration Rules to MID Server ([Docs link)](https://docs.servicenow.com/bundle/quebec-it-operations-management/page/product/event-management/task/synch-config-settings-rules.html "Docs link")

TBC

## Integrations

### AttachmentCreator SOAP web service

[AttachmentCreator SOAP web service](https://docs.servicenow.com/bundle/sandiego-application-development/page/integrate/inbound-soap/reference/r_AttachmentCreatorSOAPWebService.html "AttachmentCreator SOAP web service")

ECC Queue Topics:

-   AttachmentCreator

Name:

-   The name of the file being attached, and its content-type.

Source:

-   "<table>:<sys\_id>" of the record the attachment is to go on.

Payload:

-   A base64 encoded string, representing the binary object to be attached.

Sensor business rule:

-   AttachmentCreatorSensor

### Command probe

Note: This should generally only be used for debugging, and not be used for production integrations. Instead, IntegrationHub actions, or Powershell probes should be used, which support passing of encrypted parameters to avoid any usernames and passwords needed for the script or command appearing in plaintext.

-   Topic
    -   Command
-   Name
    -   Runs the command in the 'Name' field from the shell (Linux) or Command Prompt (Windows) of the MID Server host.
-   Payload
    -   Used for a 'name' parameter, to override the Name field, when the command is too long for the field. In this case any html entities would need encoding, as parameter values need escaping for XML format. e.g. &quot; 

[KB2909424 Should 'Command' topic probes be used to run Powershell scripts on MID Servers?](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2909424)

### DevOps Change Velocity

Docs: [Integrating DevOps Change Velocity with third party tools](https://www.servicenow.com/docs/csh?topicname=integrating-devops-change-with-third-party-tools.html&version=latest)

Most of these integrations would need to be configured to work via a MID Server if the system they integration with (Rally, Split IO, Argo, SonarQube, Harness, Bitbucket, GitHub, Jenkins, GitLab, Jira, Bitbucket, JFrog, Azure, etc.) is on-premise, and behind a firewall.

These seem to be RESTMessageV2 based integrations, and are waiting for the ecc\_queue input response. Function \_setUpRESTMessage in script include DevOpsConnector is reused a lot.

See the Outbound REST / SOAP section below. - TBC

### Export Sets

ECC Queue Topics:

-   StreamPipeline (output)
-   ExportSetResult (input)

Payload parameters:

-   stream\_relay\_response\_topic=ExportSetResult
-   stream\_relay\_source  
    -   attachment\_sys\_id = sys\_id of the sys\_attachment record being exported
-   stream\_relay\_transform  
    -   attachment.table\_sys\_id = sys\_id of the ecc\_agent\_attachment record. The source field of that record references the Export Set \[sys\_export\_set\] record.
-   stream\_relay\_sink  
    -   path = file name/path

Priority:

-   Standard - This is set in Java and so is not customisable. (BaseStreamRelay.java/submitToEccQueue)

Sensor Business Rule:

-   Doesn't have a sensor. These are run synchronously, blocking an instance thread while it waits for the MID Server to execute and return the ecc\_queue input.  This is not a best practice implementation for running jobs via a MID Server, and has led to worker thread/semaphore exhaustion in the instance, when you may see threads blocked with this sort of stack trace from the Scheduled Data Export \[scheduled\_data\_export\] job. When MID Servers are busy, you may also see timeouts after 300 seconds, because the MID Server was not able to run the job within the instance-side timeout.

java.base@17.0.14/java.lang.Thread.sleep(Native Method)  
com.glide.ecc.ECCResponsePoller.poll(ECCResponsePoller.java:57)  
com.glide.export\_set.MIDServerResponsePoller.poll(MIDServerResponsePoller.java:31)  
com.glide.export\_set.MIDServerExportTargetWorker.getMidServerExportSetResponse(MIDServerExportTargetWorker.java:216)  
com.glide.export\_set.MIDServerExportTargetWorker.pollForExportSetResponse(MIDServerExportTargetWorker.java:106)  
com.glide.export\_set.MIDServerExportTargetWorker.runExport(MIDServerExportTargetWorker.java:93)  
com.glide.export\_set.ExportTargetWorker.export(ExportTargetWorker.java:53)  
com.glide.export\_set.ExportSetHandler.processExport(ExportSetHandler.java:89)  
com.snc.automation.ScheduledExportSetJob.runExport(ScheduledExportSetJob.java:92)  
com.snc.automation.ScheduledExportSetJob.execute(ScheduledExportSetJob.java:54) ...

Note: This community post gives a way of leveraging the feature's code to export any attachment (not just PDFs of reports), and do it asynchronously.  
[Community post: Export a record attachment to a mid server's export folder](https://www.servicenow.com/community/developer-articles/export-a-record-attachment-to-a-mid-server-s-export-folder/ta-p/2298652)

### Import Set / JDBC

ECC Queue Topics:

-   JDBCProbe - expect 1 output, but 1 or more inputs
-   JDBCProbeCompleted
-   JDBCProbeError - Used to tell the MID Server to stop running a JDBCProbe when the Data Source times out on the instance side

Agent Correlator:

-   A random GUID, but can be used to group records from a Import Set run together

Agent:

-   This is usually the MID Server name, but JDBCProbe topic inputs will have "JDBCProbeResult" for the inputs containing the data.

Name:

-   For JDBCProbe inputs, this is the upper Row number for the batch of rows included in the input, or the last row if it is the last input. 

Source:

-   Sys ID of the Data Source record \[sys\_data\_source\]

Sensor Business Rule:

-   JDBCProbeSensor - responds to JDBCProbeCompleted topic. Runs async as "ASYNC: JDBCProbeSensor" in scheduler workers, using process() in Script Include JDBCProbeSensor. That then combines all the JDBCProbe inputs' data.

Credentials:

-   Credentials are from the Data Source \[sys\_data\_source\] record (referenced in the source field). At runtime, on the instance side, these will be decrypted from that record (KMF), and re-encrypted for the MID Server (GlideAutomationEncrypter), before being put in the ECC Queue output payload parameters. 

### IntegrationHub

[Integration Hub](https://docs.servicenow.com/bundle/utah-integrate-applications/page/administer/integrationhub/concept/integrationhub.html)  
[Flow Designer - Retry Policy](https://docs.servicenow.com/bundle/utah-build-workflows/page/administer/flow-designer/concept/retry-policy.html)

The ecc-queue records don't contain any data/results. When the IPaaSActionProbe runs, it will use instance Flow Engine REST APIs for instructions on what to do, and for updating the flow context with the results/data. To debug issues with this probe's execution may need instance-side appnode localhost logs for the API\_INT semaphore transactions made during the execution.

ECC Queue Topics:

-   IPaaSActionProbe
-   CancelProbe  
    -   Payload contains the 'reason' for telling the MID Server to Cancel any probes for a Flow context. e.g. 'Cancelling flow context due to timeout', which would be triggered by a 'Cancel flow context on timeout' sys\_trigger job created when the flow context started.

Agent Correlator:

-   Flow Context ID \[sys\_flow\_context\]

Name:

-   The MID Server's name, when first inserted. This may not match the MID Server that actually ran it if there was any MID Cluster failover to another MID Server. (MIDSender.java legacySend)

Source:

-   Flow Context ID \[sys\_flow\_context\]

Sensor business rule:

-   IntegrationHub - Sensors
-   IntegrationHubResponder
-   Reschedule Flow

Instance APIs:

-   /api/now/hub/plan/\[sys\_flow\_context\]

Note: [Steps running PowerShell scripts](https://docs.servicenow.com/bundle/utah-integrate-applications/page/administer/flow-designer/reference/powershell-step-action-designer.html) will use the same low-level MID Server platform code for executing the script as Discovery and Orchestration. Enabling [logging for the powershell step](https://docs.servicenow.com/bundle/utah-integrate-applications/page/administer/integrationhub/tasks/configure-logging-powershell-step.html), and mid.log.level=debug mid server parameter will show exactly what PSScript.ps1 is doing.

### JavascriptProbe

Some features use JavascriptProbes, such as Cloud Discovery, however a lot of custom integrations are also implemented using them. 

ECC Queue Topics:

-   JavascriptProbe

Source:

-   Empty by default, unless overridden by setSource() API method.

Sensor Business Rule:

-   This would also be custom, and specific to the script.

Payload:

-   The payload contains a "script" parameter, which usually identifies the MID Server Script Include \[ecc\_agent\_script\_include\] used by the probe.
-   Those script includes may also use Java classes added to the MID Server platform via attachments on the JAR Files table of the instance.

### LDAP

#### Imports:

These are set up almost exactly as an Import Set would be set up, with a Schedules Data Import \[scheduled\_import\_set\], Data Source \[sys\_data\_source\] set to type=LDAP, and Transform Map \[sys\_transform\_map\].

ECC Queue Topics:

-   LDAPProbe (expect 1 output, but 1 or more inputs)
-   LDAPProbeComplete
-   LDAPProbeError

Agent Correlator:

-   A random GUID, but can be used to group records from a LDAPProbe run together

Agent:

-   Usually the MID Server name, but LDAPProbe topic inputs will have Agent = "LDAPProbeResult" for the inputs containing the data, which is misleading (and technically wrong).  
    Note: If you are filtering the ecc\_queue table by agent, you will miss these.

Name:

-   The upper Row number for the batch of rows included in the input, or the last row if it is the last input.

Source:

-   Sys ID of the Data Source \[sys\_data\_source\]

Sensor Business Rule:

-   TBC

Priority:

-   Standard

#### Listener:

ECC Queue Topics:

-   LDAPListenProbe output + LDAPListenProbeCompleted input (for stop/start commands)
-   LDAPListenProbe input (for user changes)

Agent Correlator:

-   A random GUID, but can be used to group records from a run together

Agent:

-   Usually the MID Server name, but LDAPListenProbe topic inputs will have "LDAPListenProbeResult" for the inputs containing the data, which is misleading (and technically wrong).  
    Note: If you are filtering the ecc\_queue table by agent, you will miss these.

Name:

-   For LDAPListenProbe inputs, this is the upper Row number for the batch of rows included in the input, or the last row if it is the last input.
-   LDAPListenProbe outputs, this is Stop or Start

Source:

-   Sys ID of the LDAP Server record \[ldap\_server\_config\]

Sensor Business Rule:

-   LDAPListenProbe inputs use business rule "Process LDAP Listener on MID changes", when the Listener sends user data changes to the instance.
-   LDAPListenProbeCompleted don't have sensors. These are run synchronously, blocking an instance thread while it waits for the MID Server to execute and return the ecc\_queue input.

Priority:

-   Standard

#### Test Connection:

ECC Queue Topics:

-   LDAPConnectionTesterProbe

Agent Correlator:

-   A random GUID, but can be used to group records from a LDAPConnectionTesterProbe run together

Agent:

-   The MID Server name.

Name:

-   Inputs have the value 'true' even when the test failed. (TBC)

Source:

-   Sys ID of the LDAP Server record \[ldap\_server\_config\]

Payload:

-   The result, or Error code. MID Server agent log would need checking for full details of the error.

Sensor Business Rule:

-   LDAPConnectionTesterProbe don't have a sensor. These are run synchronously, blocking an instance thread while it waits for the MID Server to execute and return the ecc\_queue input.

Priority:

-   Expedited - This is run at elevated priority to reduce the chance of a timeout (Did not get a response from the MID server after waiting for 55 seconds), which can cause false alerts when there is no actual connection issue, and also help minimise the time an instance thread is blocked waiting for the response from the MID Server. (PRB1331240)

#### Browse:

 ECC Queue Topics:

-   LDAPBrowseProbe

Agent Correlator:

-   A random GUID, but can be used to group records from a LDAPBrowseProbe run together

Agent:

-   MID Server name

Source:

-   Sys ID of the LDAP Server record \[ldap\_server\_config\]

Sensor Business Rule:

-   Doesn't have a sensor. These are run synchronously, blocking an instance thread while it waits for the MID Server to execute and return the ecc\_queue input.

Priority:

-   Expedited - This is run at elevated priority to reduce the chance of a timeout, to help minimise the time an instance thread is blocked waiting for the response from the MID Server. (PRB1331240)

#### Detail:

Issues a LDAP query to get details for an element.

ECC Queue Topics:

-   LDAPDetailProbe 

### OAuth2 Credential Token refresh

Since Zanadu, depending on the Grant Type, it is possible (maybe necessary - TBC) to refresh OAuth2.0 credential tokens via MID Servers, rather than making the request to the token URL directly from the instance. This happens when the field 'Connect to Auth Server via MID Server' \[use\_mid\] is selected on the credential record.

Topic:

-   RESTProbe

Name:

-   post

Source:

-   The token refresh URL. Possibly the OAuth Token URL in the OAuth Entity Profile (TBC)

Payload:

-   parameters will include transaction\_name=Refresh OAuth Tokens - system

Priority:

-   Interactive

### Orchestration

ECC Queue Topics:

-   JDBCOrchestrationProbe
-   JDBCOrchestrationProbeCompleted
-   Powershell
-   SSHCommand
-   SystemCommand
-   CommandPipeline  
    -   Used with SFTP Activity
-   Command  
    -   runs a local command on the MID server.
-   DNSNameResolver  
    -   resolves a fully qualified domain name (FQDN) into an IP address
-   SCPCommand  
    -   copies files securely from one machine to another
-   SSHCommandLong  
    -   executes long running shell scripts from a command line after logging in to a target machine via SSH

Agent Correlator:

-   The Workflow Context \[wf\_context\] record Sys ID, prefixed with "rba.".

Source:

-   Powershell: The target hostname
-   JDBCOrchestrationProbe/JDBCOrchestrationProbeCompleted: Empty

Sensor Business Rule:

-   Automation - Sensors

[Quebec documentation: Deprecated: Orchestration activities: Probes used by Orchestration](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/product/orchestration/reference/r_OrchestrationProbes.html "Quebec documentation: Deprecated: Orchestration activities: Probes used by Orchestration")

### Outbound REST / SOAP

The "RESTMessageV2: MID Server, executeAsync(), setEccParameter('skip\_sensor', 'true'), setEccCorrelator()" section at the end of the [KB0694711 Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync()](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694711) KB article is **the only correct way to implement Outbound TEST/SOAP via a MID Server**, however a lot of synchronous implementations that dangerously block instance threads have been see, including some ServiceNow features.

ECC Queue Topics:

-   RESTProbe (will run as a MIDWorker thread in the MID Server, as RESTProbe is not an actual Probe)
-   SOAPProbe

Agent Correlator:

-   By default empty, unless set using the setEccCorrelator() method of the API.

Source:

-   The REST Endpoint URL, unless overridden by the setEccParameter() method of the API.

Agent:

-   mid.server.<an actual MID Server Name> - This will be the MID Server that processes the job.  
    The following 3 values are for jobs run directly by the instance, directly to the endpoint, without going via a MID Server:-
-   RESTClient - This is processed in the instance by the "RESTClient" business rule, triggered by the insert of the output ECC Queue record.
-   SOAPClient - This is processed synchronously on ecc\_queue insert, by the instance, by the "SOAPClient" business rule, which calls SOAPMessageV2() and .execute();.  
    -   If system property glide.processor.debug.SOAPProcessor=true, then app node localhost log will give debug of the outbound request being executed by that business rule. Search for "OUTBOUND\_HTTP:" and "SOAP Msg Outbound" in the logs. You can also see the logging in the instance table System Logs --> Outbound HTTP Requests.
-   mid.server.NODE\_AGENT" also indicates a request from the instance, not via a MID Server.

Sensor business rule:

-   Generally custom, or specific to the endpoint. "Process Get Stock Quote" is an out-of-box example sensor for a SOAPClient direct-from-instance job.
-   Often missing due to non-best-practice use of waitForResponse(), or install calling methods for the response that would require having got the response first.

[KB0995097 Troubleshooting localhost logs for Outbound Web Service issues (internal)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995097 "KB0995097 Troubleshooting localhost logs for Outbound Web Service issues")

### Syslog Integration

Docs: [Syslog probe](https://www.servicenow.com/docs/csh?topicname=r_SyslogProbe.html&version=latest)  
Wikipedia: [Syslog](https://en.wikipedia.org/wiki/Syslog)

This probe implements a facility to send UNIX syslog messages using the standard UDP protocol. It implements RFC 5424 except for the optional structured data representation, and also RFC 3164 through separate log methods. 

ECC Queue Topics:

-   Syslog

Payload:

-   Contains parameters for the syslog host and message

Note: There is minimal logging and no additional debug logging that can be enabled for this probe. mid.log.level=debug will not add any additional logging.  
To investigate what this probe is actually doing may require a network packet sniffer, such as WireShark installed on the MID Server host, and target server if not localhost.  Syslog protocol is UDP, port 514.

### 3rd party:

These tools are not ServiceNow code, or ServiceNow's responsibility to support. If they turn out not to be working due to mid server platform or Java version changes, then alternatives should be sought out. Turning off important Java code security features to get unmaintained 10 year old code to run is not a proper solution.

#### [JDBC File Loader](https://developer.servicenow.com/connect.do#!/share/contents/5711173_jdbc_file_loader_via_mid_server?v=2.01&t=PRODUCT_DETAILS "JDBC File Loader")

ECC Queue Topics:

-   JavascriptProbe

Name:

-   JDBCFileLoaderProbe  
    -   This is the MID Server Script Include name.

Source:

-   sys\_id of the file source record

Sensor business rule:

-   JDBCFileLoaderSensor  
    -   Async business rule, using script include ImportSetUtilPlus

#### File Builder FTP

This was a ServiceNow Professional Services product, developed by Jason Petty in 2014, shared on ShareNow as an Update Set. As of 2024, a [Video Tutorial](https://www.youtube.com/watch?v=ipsztWHx2AM) remains on youtube explaining the definition tables and forms used to set this up. The code triggering this probe will usually be a call in a scheduled script to the FileBuilderFileCopyES script include.ECC Queue Topics:

-   JavascriptProbe

Name:

-   FileBuilderFileCopy

#### Remote File Importer

This is originally written by partner Cloud Sherpas (now Accenture), and shared on the developer site.

-   Developer site: [Remote File Importer (Import Files from a MID Server)](https://developer.servicenow.com/connect.do#!/share/contents/2271821_remote_file_importer_import_files_from_a_mid_server?v=1.0&t=RATINGS_REVIEWS&page=1)
-   Community site: [Getting Error in "Input ECC Queue" as "No sensors defined". I am getting this when trying to execute one of the "Remote file import".](https://www.servicenow.com/community/developer-forum/getting-error-in-quot-input-ecc-queue-quot-as-quot-no-sensors/m-p/1448678)
-   [KB1641779 Unable to import files from Mid Server after upgrade to Washington DC](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1641779)

ECC Queue Topics:

-   JavascriptProbe

Name:

-   CSRemoteFileImport

Payload:

-   targetImportSet - An instance table name
-   filePath - File path on MID Server disk
-   script =  
    var remoteFileImport = new CSMIDServerRemoteFileImport();  
    remoteFileImport.getRemoteFileAndUploadToInstance();

The probe code is in MID Server Script Include "CSMIDServerRemoteFileImport". The instance Script Include "CSRemoteFileImport", UI Page "run\_remote\_import" and UI Action "Import Now" are also involved.

## IT Service Management

### Agent Client Collector for Security Incident Response

This app uses Flow Designer workflows, and the Agent Client Connector Spoke app for IntegrationHub.

### Digital End-User Experience (DEX)

DEX uses MID-less Agent Client Collector agents, which connect directly to a hosted instance (via Hermes/Stream Connect/gPRC and an ITOM CnC Gateway pod). Messages from these agents do not appear in the ECC Queue.

### Employee Document Management

[KB0963986 Employee Document Management (EDM) FAQ](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963986)

ECC Queue Topics:

-   StreamPipeline (output) / EmployeeFileImport (input) - created by ef\_LocalFileCapture script include, importFileUsingMid function. Brings locals files from thee MID Server disk to the Attachment table in the instance.
    -   Agent Correlator:
        -   The sys\_id of the sn\_hr\_ef\_import\_staging record.
    -   Payload parameters:
        -   stream\_relay\_response\_topic=EmployeeFileImport
        -   stream\_relay\_source - from the sn\_hr\_ef\_import\_configuration record.  
            -   connection.host, connection.port, crdential\_tag, path, type.
        -   stream\_relay\_transform  
            -   attachment.table\_sys\_id, attachment.table\_name, attachment.file\_name, attachment.content\_type, type=AttachmentSink
        -   stream\_relay\_sink  
            -   path = file name/path - from the sn\_hr\_ef\_import\_staging record
    -   Sensor business rule:
        -   Process local file import  
            -   uses processLocalImportResult function in ef\_LocalFileCapture script include. Adds result to sn\_hr\_ef\_import\_staging record.
            -   Attachment data is not in the payload, which is inserted directly into the instance attachment table by the probe, using /now/attachment/file [REST Attachment API](https://docs.servicenow.com/bundle/quebec-application-development/page/integrate/inbound-rest/concept/c_AttachmentAPI.html "REST Attachment API").
-   SSHCommand - created by the "Stage local files" Orchestration legacy workflow to import files using the SSH protocol, to the MID server disk.  
    -   Agent Correlator: rba. + the sys\_id of the wf\_context that has the SSH Orchestration activities in.

### Microsoft Exchange Online for Security Operations

[Docs: Microsoft Exchange Online integration (Rome)](https://docs.servicenow.com/bundle/rome-security-management/page/product/secops-integration-microsoft-exchange-online/concept/ms-exchange-online-lookups.html "Microsoft Exchange Online integration (Rome)")

The integrations are implemented by Powershell Orchestration Workflow activities:

-   Diagnose Compliance Search
-   Create Search on Exchange Online
-   Check Status of Exchange Online Search
-   Search Threat Email in O365

MID Selection Criteria:

-   Capabilities: PowerShell, WinRM Basic Authentication
-   Applications: Orchestration

ECC Queue Topics:

-   Powershell

Name:

-   Windows - PowerShell

Payload:

-   MIDScriptFile parameter will give the powershell script name, that will link it back to the specific activity.

Agent Correlator:

-   The Workflow Context \[wf\_context\] record Sys ID, prefixed with "rba.".

Source:

-   The target hostname

Sensor Business Rule:

-   Automation - Sensors

### Security Incident Response

The Security Incident Response application includes third-party integrations.

ECC Queue Topics:

-   RESTProbe

Agent Correlator/Source/Payload:

-   TBC

## Now Platform

### Source Control

ECC Queue Topics:

-   ImportApplicationProbe
-   SourceControlProbe
-   RemoteCloneProbe
-   ExportApplicationProbe
-   ImportNewApplicationProbe
-   CreateTagProbe
-   ExportNewApplicationProbe
-   TestConnectionProbe
-   RefreshRepositoryProbe
-   CreateBranchProbe

Name

-   Source Control

Sensor Business Rule

-   Source Control Response  
    -   Async business rule using MIDResponse.java and GitECCProcessor.java, where invokeOperation calls a function specific to the operation.  
        .

### MID Server

#### ECC Queue

ECC Queue Topics:

-   queue.processing  
    -   inputs are used to notify the instance which outputs are 'processing', and subsequently 'cancelled' or 'processed'.
    -   Sensor business rule: "ECC Queue - mark outputs state" - Updates the state of the output records mentioned in the payload.
-   queue.stats  
    -   Each MID Server reports every 10 minutes on currently running threads, and performance metrics.
    -   Sensor business rule: "MID - Process XMLStats" - Updates ecc\_agent\_thread records, JVM version in ecc\_agent, and via AgentMetrics script include updates ecc\_agent\_counter\_metric, ecc\_agent\_scalar\_metric, ecc\_agent\_rgr\_metrice, cc\_agent\_memory\_metric.

#### Kubernetes Deployment

Agent:

This needs to be a MID Server that is set up as a Kubernetes Deployment MID Server, with the "MID Server Management" application.

ECC Queue Topic:

-   KubernetesOperationProbe

Name:

-   Name field of the request's mid\_k8s\_deployment record.

Payload:

-   deployment\_request\_id is the sys\_id of the mid\_k8s\_deployment record.
-   deployment\_request is BASE64 encoded, and then encrypted as well.

Sensor Business Rule:

-   KubernetesOperationResponder  
    -   Updates the deployment request mid\_server\_deployment record state.

#### System Commands

ECC Queue Topics:

-   SystemCommand

Source:

-   The name of the MID Server internal system command. These include:  
    -   restart  
        -   Restarts the MID Server. 
    -   restartService  
        -   Restarts the MID Server Service. This will completely stop and then start the Windows service.
    -   stop  
        -   Shuts down the MID Server service
    -   threaddump  
        -   Writes a Java Thread Dump to the wrapper.log
    -   gc
    -   grabLog  
        -   Retrieves the file in the name field.
    -   getResourceState
    -   deleteLog
    -   pause / unpause  
        -   Pauses the MID Server so it will not run jobs, however most system commands will continue to be run.
    -   upgradeNow  
        -   Prompts the MID Server to check if it needs to upgrade now, rather than wait for the hourly scheduled job to check.
    -   clear\_queue
    -   load\_properties
    -   load\_ip\_access  
        -   [IP Address Access Control](https://docs.servicenow.com/csh?topicname=t_AccessControl.html&version=latest "IP Address Access Control") Plugin. This will apply any rules that have "Enforce on MID server" checked to the MID Server.
    -   cancel\_discovery  
        -   When a Discovery Status reaches max runtime, or is manually cancelled, to notify the MID Server to cancel any remaining probes.
        -   Broadcast to all MID Servers, regardless of whether that are running Discovery.
        -   agent\_correlator=<sys\_id of discovery\_status>
    -   updateConfig  
        -   For pushing changes to parameters/properties to a MID Server. Parameters will also be written to config.xml.
    -   status
    -   invalidate\_cache
    -   script  
        -   Used by MID Server Scripts - Background page, to run any javascript in the mid server, and return the output
    -   credentials\_reload  
        -   Triggered by a change to any discovery\_credentials record. Updates the MID Server' local cache of its credentials.
    -   privileged\_command\_reload
    -   automation\_encryption\_keys\_reload
    -   probe\_cache
    -   range\_cache  
        -   Clears the Discovery IP Range Cache. Triggered by changes to discovery\_range table.
    -   delete\_mid\_keypair  
        -   Re-Key and Invalidate
    -   acls\_change
    -   mibs\_reload  
        -   Re-Synchronises all SNMP MIB files from ecc\_agent\_mib
    -   FileChange  
        -   Re-Synchronises Files to the disks of all MID Servers. The Name value is the table where a synchronized file change has occurred, e.g. JAR Files, Script Files/Includes.
    -   resetQueryWindow
    -   CitChanged
    -   CustomOperationChanged
    -   CustomParsingStrategyChanged
    -   LibsApplCategoryChanged
    -   LibsDeviceInfoCategoryChanged
    -   PatternExtensionChanged
    -   MetadataRulesChanged
    -   ExtCommandChanged
    -   pauseMid  
        -   Stops the MID Server from running any jobs except system commands.
    -   resumeMid  
        -   Allows the MID Server to run any jobs.
    -   autoUpgrade  
        -   Prompts the MID Server to check if it needs to upgrade now, rather than wait for the hourly scheduled job to check.
    -   grabNdl
    -   trackedFileDefinitionChanged
    -   clear\_cookies  
        -   Clears the cookie cache, which is used by the SOAP client for making requests to a ServiceNow instance, allowing the MID Server to connect to to a different app node.
    -   installNmap / uninstallNmap  
        -   Installs/uninstalls NMAP on the MID Server host, which is used by Credential-less Discovery.
    -   service\_account\_reload
    -   file\_discovery\_whitelist
    -   file\_discovery\_refresh
    -   connection\_cache\_update
    -   environment\_clear
    -   mid\_status\_change

### Release

All including the current release.

### Resolution

The scope of this KB article doesn't go so far as providing solutions to issues. It will guide you in the right direction though.
