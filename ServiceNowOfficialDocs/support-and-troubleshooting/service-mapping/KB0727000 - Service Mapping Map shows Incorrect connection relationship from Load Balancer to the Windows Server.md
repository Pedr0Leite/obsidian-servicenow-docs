---
title: "Service Mapping: Map shows Incorrect connection / relationship from Load Balancer to the Windows Server"
aliases:
  - KB0727000
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727000
kb_number: KB0727000
last_modified: 2024-04-07
---

## Service Mapping: Map shows Incorrect connection / relationship from Load Balancer to the Windows Server

  

### Issue

This KB article is to show how to check why the Service Mapping maps shows incorrect connection / relationship from Load Balancer to the Windows Server given that the patterns payload / discovery returns correct connection / relationship.

### Cause

The reason why the Windows Server ends in DNS cluster of the Load Balancer is because there is a record in the DNS mapping table \[cmdb\_ci\_dns\_name\].

DNS cluster logic is to map same IP that resolved from different host names.  
If we lookup by IP xx.xxx.xx.xxx, it shows multiple records, where duplicate host names can be found. Therefore there are more than one distinct host names. These records creates the DNS cluster.

\- Query on \[cmdb\_ip\_address\_dns\_name\] table where ip\_address.ip\_address = 'xx.xxx.xx.xxx'.

Run nslookup on the hostname, check if it returns different IPs.  
  
This means that the records in 'cmdb\_ip\_address\_dns\_name' are outdated. 

### Resolution

1\. Remove the records found from the query / URL below:

-   Replace the <instance-name> with the actual instance name 
-   Replace the xx.xxx.xx.xxx with the IP Address.

https://<instance-name>.service-now.com/cmdb\_ip\_address\_dns\_name\_list.do?sysparm\_query=ip\_address.ip\_address%3Dxx.xxx.xx.xxx

2\. Run Discovery on the Application Service.

3\. Map should be updated.
