---
title: "Can Integration Hub support connection affinity - Multiple credentials check on a single alias record "
aliases:
  - KB0863181
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863181
kb_number: KB0863181
last_modified: 2025-01-02
---

## Can Integration Hub support connection affinity - Multiple credentials check on a single alias record

  

### Summary

## Credential order

Credentials can be assigned an order value in the credential form, which forces the application to try all the credentials at their disposal in a certain sequence. If you do not specify an order value, the application tries the credentials in the Credentials \[discovery\_credential\] table randomly, until it finds one that works, such as when Orchestration attempts to run a command on an SSH server (such as a Linux or UNIX machine), or when Discovery attempts to query an SNMP device (such as a printer, router, or UPS).

[Connection and Credential alias](https://docs.servicenow.com/csh?topicname=r-credentials.html&version=latest "Connection and Credential alias")

Example: If there are multiple credentials mapped to a single alias record , all of those credentials are validated until there is success.

Integration Hub will also contain steps like SSH , REST etc to connect with the end machines and run few commands. Connection alias records are used for authentication and mapped to these steps in the flow designer actions.

As of now, any execution from Integration Hub doesn't check all the credentials in the credentials table mapped to a specific alias record in the actions until it is success. It just's pick random credentials and if the authentication to the end point fails, the execution stops. We will not check for rest of the credentials mapped to the same alias or connection record. This is by design and will be a product enhancement

Ex: There many be a requirement to login to multiple linux machines to run few flows and the linux machines might have different credentials mapped to them. One machine credential might differ from other machine credential and the flow is expected to check all the credentials in the credentials table to pick a valid match. This is NOT supported in Integration Hub and the respective actions steps.

There are couple of work arounds that can be tested and implemented

   - Maintain the host(ip) to credential alias (one alias for each credential) mapping in a table and do the Look-up Record step before SSH step to fetch the right credential alias for the given hostname and use the alias data pill into the credential alias field. PLease confirm if this helps in the customer usecase.  
    - Create 2 flows with one credential in each credential alias record  
    - Trigger the SSH call based on any pattern between the linux machines having different authentication mechanism
