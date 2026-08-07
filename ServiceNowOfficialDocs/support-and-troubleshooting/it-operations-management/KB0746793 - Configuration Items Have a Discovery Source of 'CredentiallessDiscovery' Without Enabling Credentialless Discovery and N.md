---
title: "Configuration Items Have a Discovery Source of 'CredentiallessDiscovery' Without Enabling Credentialless Discovery and Nmap"
aliases:
  - KB0746793
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746793
kb_number: KB0746793
last_modified: 2025-07-21
---

## Configuration Items Have a Discovery Source of 'CredentiallessDiscovery' Without Enabling Credentialless Discovery and Nmap

  

### Issue

Records in the 'cmdb\_ci' table may have a discovery source of 'CredentiallessDiscovery' even though you have not enabled Credential-less Discovery.

### Facts

You might find records in the 'cmdb\_ci' table with discovery source of CredentiallessDiscovery when using ServiceNow's Service Mapping.

### Release

All

### Cause

There are some identification sections within ServiceNow patterns where the Discovery Source is set to "CredentiallessDiscovery"

For example, if you navigate to Pattern Designer >> Discovery Patterns and search the list for "Apache on Windows Pattern" you will see the Identification Section. If you click "Lightweight Identification for Apache" you will see step 3 is setting the Discovery Source (below) 

![Apache On Windows Pattern screenshot](/sys_attachment.do?sys_id=be7a523a47bae210f64de825126d4356)

### Resolution

There are many such patterns which have lightweight identification sections where the discovery source is set to CredentiallessDiscovery in the Pattern.

### Related Links

[Credential-less host Discovery](https://www.servicenow.com/docs/csh?topicname=credential-less-host-discovery.html&version=latest "Credential-less host Discovery")

[How to deactivate credential-less discovery](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961909 "How to deactivate credential-less discovery")
