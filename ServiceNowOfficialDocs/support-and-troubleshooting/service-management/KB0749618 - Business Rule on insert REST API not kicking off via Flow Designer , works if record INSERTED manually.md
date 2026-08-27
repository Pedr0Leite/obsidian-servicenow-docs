---
title: "Business Rule on insert REST API not kicking off via Flow Designer , works if record INSERTED manually"
aliases:
  - KB0749618
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749618
kb_number: KB0749618
last_modified: 2024-04-07
---

## Business Rule on insert REST API not kicking off via Flow Designer , works if record INSERTED manually

  

### Issue

# Symptoms

If Flow Designer is used to **UPDATE** or **INSERT** any records because of which if it does an External Call( From a business rule on those tables) using any of the Web Services it throw following error in the localhost logs:

  
" No IntegrationHub plugin is available, external calls from the Flow Designer requires IntegrationHub subscription "

# Release

London onwards

# Cause

IntegrationHub Licensing compliance.

Any external call from Flow Designer requires an IntegrationHub entitlement.

If any customer is doing integrations on business rules on a table that Flow Designer is touching, it requires an IntegrationHub entitlement. 

# Resolution

Paid plugin: ServiceNow IntegrationHub Installer need to be installed.

# Additional Information

[Request IntegrationHub](https://docs.servicenow.com/csh?topicname=integrationhub.html&version=latest?cshalt=yes "Request IntegrationHub")
