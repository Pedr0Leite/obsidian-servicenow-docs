---
title: "Service Mapping License Usage tracking."
aliases:
  - KB0812211
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812211
kb_number: KB0812211
last_modified: 2026-06-19
---

## Service Mapping License Usage tracking.

  

### Issue

Service Mapping consumed License Usage details not visible in the instance.

### Release

-   Instance enabled with the Service Mapping.

### Resolution

-   From the Application Navigator Go to >> Subscription Management > Subscriptions > Service Mapping node, it would show you the consumed license count.

  
![](sys_attachment.do?sys_id=6a6ef778db40f0d016d2a345ca961909)  
  

-   Service Mapping licensing logic distinctively counts the number of servers (CIs whose sys\_class\_name is an instance of cmdb\_ci\_server) which are associated with discovered services. (Application Services of type Discovered).
-   To check the Service mapping consumed license details(nodes information)in the instance, follow the below steps.

-   -   Navigate to the svc\_ci\_assoc table, filter for all Configuration Items whose class is an instance of Server and group by the Configuration Item Id field.
    -   Apply the filter on svc\_ci\_assoc as follows"

a. Configuration Item Id "is a" Server  
b. Service Id class "is" Application Service

[Query](https://instance_name.service-now.com/svc_ci_assoc_list.do?sysparm_query=ci_id.sys_class_nameINSTANCEOFcmdb_ci_server%5Eservice_id.sys_class_name%3Dcmdb_ci_service_discovered%5EGROUPBYci_id&sysparm_first_row=1&sysparm_view= "Query")

![](sys_attachment.do?sys_id=666ef778db40f0d016d2a345ca961907)

-   Group by Configuration Item Id and it will get the list of servers that are used for Service Mapping license count.
