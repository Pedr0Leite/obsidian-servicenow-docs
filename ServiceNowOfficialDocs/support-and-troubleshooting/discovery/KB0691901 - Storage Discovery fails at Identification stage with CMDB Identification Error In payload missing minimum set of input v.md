---
title: "Storage Discovery fails at Identification stage with \"CMDB Identification Error: In payload missing minimum set of input values for criterion (matching) attributes from identify rule for table [cmdb_ci_storage_server]\""
aliases:
  - KB0691901
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691901
kb_number: KB0691901
last_modified: 2026-05-19
---

## Storage Discovery fails at Identification stage with "CMDB Identification Error: In payload missing minimum set of input values for criterion (matching) attributes from identify rule for table \[cmdb\_ci\_storage\_server\]"

  

### Issue

Storage Server discovery fails on the CIM-Identity probe with the below error

CMDB Identification Error: In payload missing minimum set of input values for criterion (matching) attributes from identify rule for table \[cmdb\_ci\_storage\_server\]. Add these input values in payload item '{"className":"cmdb\_ci\_storage\_server","values":{"discovery\_source":"Manual Entry","sys\_class\_name":"cmdb\_ci\_storage\_server"}}'

### Facts

1.  ServiceNow Instance with Discovery plugin activated
2.  Discovery schedule created to discover an SMI-S server, which in turn discovers the Storage Server.  The setup should be designed as advised in [Storage Discovery](https://www.servicenow.com/docs/r/it-operations-management/itom-visibility/c_Storage.html "Storage Discovery")

### Release

All releases

### Cause

There can be multiple root causes for Identification and Reconciliation engine failure. These can be found in the comprehensive list of [Identification engine error messages](https://www.servicenow.com/docs/r/servicenow-platform/configuration-management-database-cmdb/id-engine-error-messages.html "Identification engine error messages").

However, in this article we will discuss a particular case which is relevant only to CIM / Storage Discovery.

By reviewing the above message we can see that there are NO Parameters passed in the payload to IRE.  The IRE is called during execution of the Sensor script using the data collected in 'cimdata'.  The script related to this is present in script include - 'CimIDSensor' and sensor 'CIM - Computer System'

### Resolution

There are several articles for resolution of common Identification and Reconciliation engine failures.  Some of these are:

[KB0535238 Troubleshooting the Identification Phase in Discovery](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535238 "Troubleshooting the Identification Phase in Discovery")

[KB0657727 CMDB Identification Engine Error Troubleshooting for Service Mapping](https://support.servicenow.com/kb_view.do?sysparm_article=KB0657727 "CMDB Identification Engine Error Troubleshooting for Service Mapping")

-   For troubleshooting the CIM-Identity Probe, the most important debug strategy is to ensure that 'CIM - Computer System' is able to populate the values correctly.  Hence, the first troubleshooting step is to collect additional information related to the execution.  For this kindly take the below steps.  
    1.  Set the system property glide.discovery.identification.log\_level to DebugObnoxious.  For more information on the debug refer [examining identification engine - run logs](https://www.servicenow.com/docs/r/servicenow-platform/configuration-management-database-cmdb/identification-simulation.html "examining identification engine - run logs").
    2.  In the script for the sensor 'CIM - Computer System' add the statement JSUtil.logObject(computer);
-   Use the dump for 'computer' object, to review the script and pin point the exact location of the failure.
-   Browse to **Configuration > Identification/Reconciliation > Identification Logs** for viewing the logs related to each run of the IRE.

Example 1 :

The 'CIM - Computer System' Sensor Script uses the 'ElementName' returned by '${instance}.\*' 

In case the value returned for 'ElementName' is null, the scripts returns prematurely and is not able to set value for many of the other parameters.

Example 2 :

The sensor script also initializes cim\_object\_path for the IRE payload.  The field is populated by 'parse()' function of Script Include 'CimInstanceToken'.  In case there are error while initializing the field, the IRE may not be able to match the Storage server with an exiting one and may end up creating duplicates or failing completely.  

Example 3 : 

Another critical field from '${instance}.\*' is 'SerialNumber'.  In case the CIM probe returns a null value for the field, IRE may not be able to identify the Storage Server correctly.
