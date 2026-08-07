---
title: "IntegrationHub action fails with error \"failed because no valid MID is available,Please check System Logs\"."
aliases:
  - KB0786254
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786254
kb_number: KB0786254
last_modified: 2024-04-07
---

## IntegrationHub action fails with error "failed because no valid MID is available,Please check System Logs".

  

### Issue

IntegrationHub action fails with error "failed because no valid MID is available,Please check System Logs".

### Release

All currently supported releases.

### Cause

IntegrationHub lets you build reusable integrations with third-party systems and call them from anywhere in the platform. For example, request IntegrationHub to call external systems using integration APIs from the Action Designer Script step, run the Script step on the Mid Server, and activate protocol steps like REST, SOAP, and PowerShell.

The integration will need to determine what MID server to use, if the integration is set to use a MID server. If based on the configuration a MID server cannot be found, the error "failed because no valid MID is available,Please check System Logs" will be returned.

### Resolution

1.  Review the integration configuration. If for example a http request, review the connection configured.
2.  Update the action criteria for the MID server. Alternatively, update the MID server capability, application, and ip range so that it can be found by the action.

### Related Links

-   [IntegrationHub](https://docs.servicenow.com/csh?topicname=integrationhub.html&version=latest "IntegrationHub")
-   [Introduction to credentials, connections, and aliases](https://docs.servicenow.com/csh?topicname=credentials-connections-alias.html&version=latest "Introduction to credentials, connections, and aliases")
-   [MID Server selection](https://docs.servicenow.com/csh?topicname=c_MIDServerConfiguration.html&version=latest#c_MIDServerConfiguration "MID Server selection")
