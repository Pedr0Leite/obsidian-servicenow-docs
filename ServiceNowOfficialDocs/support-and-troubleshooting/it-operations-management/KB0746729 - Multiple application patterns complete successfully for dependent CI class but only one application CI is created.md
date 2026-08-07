---
title: "Multiple application patterns complete successfully for dependent CI class but only one application CI is created"
aliases:
  - KB0746729
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746729
kb_number: KB0746729
last_modified: 2024-04-07
---

## Multiple application patterns complete successfully for dependent CI class but only one application CI is created

  

### Issue

# Symptoms

Multiple application patterns complete successfully for dependent CI class, however only one application CI is created.

# Release

All currently supported releases.

# Cause

Application CIs depend on a parent CI, the main CI which is independent. Dependent CIs are identified using dependent identifiers. The parent identifier for different application classes is the "Application Rule" identifier. An identifier may be configured to fallback to a parent identifier before attempting to insert a new CI. The OOB "Application Rule" uses fields "Running process command", "Running process key parameters", and "Class" to find matches. It is possible that multiple applications on the same host have the same "Running process command", "Running process key parameters", and "Class". The OOB "Application Rule" therefore would not be a good identifier to fallback to if this is acceptable or expected for such application being discovered. This would lead to only one such application being created per parent CI. 

To confirm the "Application Rule" is being used: 

1.  Collect the input payload passed to the identification engine, will be available in the ecc\_queue input used by the pattern.
2.  Navigate to "Configuration > Identification/Reconciliation > Identification Simulation".
3.  Select "Start with Existing Payload".
4.  Select "ServiceNow" source, paste payload, and click execute.
5.  Review "Output" section to see rules used by the identification engine.

Example output:

```
Output Payload :{ "items": [ { "className": "cmdb_ci_linux_server", "operation": "UPDATE", "sysId": "edb652ca133837403ece70404244b085", "identifierEntrySysId": "Unknown", "identificationAttempts": [] }, { "className": "cmdb_ci_db_db2_instance", "operation": "UPDATE", "sysId": "789a52ce133837403ece70404244b045", "identifierEntrySysId": "8985a23ec3f00200d8d4bea192d3ae08", "identificationAttempts": [ { "attemptResult": "NO_MATCH", "identifierName": "DB2", "attributes": [ "db_name", "installed_dir", "sys_class_name", "tcp_port" ], "searchOnTable": "cmdb_ci_db_db2_instance" }, { "attemptResult": "SKIPPED", "identifierName": "Database instance rule", "attributes": [ "serial_number" ], "searchOnTable": "cmdb_ci_db_instance" }, { "attemptResult": "SKIPPED", "identifierName": "Database instance rule", "attributes": [ "edition", "name", "tcp_port" ], "searchOnTable": "cmdb_ci_db_instance" }, { "attemptResult": "SKIPPED", "identifierName": "Application Rule", "attributes": [ "cl_port", "sys_class_name" ], "searchOnTable": "cmdb_ci_appl" }, { "attemptResult": "MATCHED", "identifierName": "Application Rule", "attributes": [ "running_process_command", "running_process_key_parameters", "sys_class_name" ], "searchOnTable": "cmdb_ci_appl" } ] } ], "relations": [ { "className": "cmdb_rel_ci", "operation": "NO_CHANGE", "sysId": "7c9a52ce133837403ece70404244b049", "identifierEntrySysId": "Unknown" } ]}
```

# Resolution

1.  Create a dependent identifier for the CI class if there isn't already one.
2.  Set the "Allow fallback to parent's rules" to false for the identifier/identifier rules being used for such CI, in the previous example identifier for cmdb\_ci\_db\_db2\_instance.

# Additional Information

Helpful documentation:

-   [Effective usage of CMDB Identification](https://docs.servicenow.com/csh?topicname=best-practices-id-reconcile.html&version=latest "Effective usage of CMDB Identification")
-   [Identification and reconciliation components and process](https://docs.servicenow.com/csh?topicname=c_CompsandProcessIDandReconcil.html&version=latest "Identification and reconciliation components and process")
-   [IdentificationEngineScriptableApi - Global](https://docs.servicenow.com/csh?topicname=c_IdentEngineScriptAPI.html&version=latesttAPI.html "IdentificationEngineScriptableApi - Global")
