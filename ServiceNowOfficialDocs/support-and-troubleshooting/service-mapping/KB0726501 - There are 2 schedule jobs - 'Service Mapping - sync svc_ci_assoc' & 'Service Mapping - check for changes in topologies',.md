---
title: "There are 2 schedule jobs - 'Service Mapping - sync svc_ci_assoc' & 'Service Mapping - check for changes in topologies', even though Service Mapping was never enabled"
aliases:
  - KB0726501
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726501
kb_number: KB0726501
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

There are 2 scheduled jobs on the instance which seem to be specific to Service Mapping.  However they exist on all instance even when Service Mapping plugin was never enabled.

Service Mapping - sync svc\_ci\_assoc  
Service Mapping - check for changes in topologies

# Release

* * *

London and Above

# Cause

* * *

The 2 Scheduled jobs are part of the "Application Service" Plugin - 'com.snc.cmdb.it\_service'. This plugin provides the features and functionalities for [Application Services](https://docs.servicenow.com/csh?topicname=c_ITILConfigurationManagement.html&version=latest "Application Services") Mapping. 

'Application Service' is new in London release. Most of its features have been carved out of Service Mapping, hence the naming convention for the scheduled job, still contains 'Service Mapping'. However, the plugin is completely independent and works even if neither Service Mapping not Event Management is installed.

# Resolution

* * *

'Application Service' plugin - com.snc.cmdb.it\_service is part of 'ServiceNow Core' - com.snc.core, which is a core platform plugin and is active by default on all instances.

This is a core platform feature which should not be modified.

# Additional Information

* * *

Both scheduled jobs mentioned above are part of the Application Service infrastructure and are required to allow access to services for non-SM roles. If service mapping plugin is not active, then the only type of Application Services that are available on the instance are the manually created services. Such services change only when manual change applied by human interaction with the map.

Since frequent changes are NOT expected on Application Services in manual mode, load and impact from these jobs is expected to be minimal. More information about this can be found here - [Manually update an application service with changes from the CMDB](https://docs.servicenow.com/csh?topicname=update-services-from-cmdb.html&version=latest "Manually update an application service with changes from the CMDB")
