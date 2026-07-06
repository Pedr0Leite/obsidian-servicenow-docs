---
title: "JDBC Data Source integration fails for clustered MID Server configuration"
aliases:
  - KB0789910
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789910
kb_number: KB0789910
last_modified: 2025-01-03
---

## JDBC Data Source integration fails for clustered MID Server configuration

  

### Summary

For performance and reliability reasons, these data sources should not be used with MID Server clusters:

\-LDAP  
\-Export sets  
\-JDBC data sources  
  
These external data sources should only be used with dedicated MID Servers.

For further information, I would like to ask you to check the below documentation.  
[ServiceNowPlatform](https://docs.servicenow.com/csh?topicname=r_ServiceNowPlatform.html&version=latest "ServiceNowPlatform")

### Related Links

There is no workaround for this limitation.
