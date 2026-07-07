---
title: "Workday - Socket timeout' errors during HR Integrations-Workday Sync jobs"
aliases:
  - KB0794032
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794032
kb_number: KB0794032
last_modified: 2025-09-30
---

## 'Workday - Socket timeout' errors during HR Integrations-Workday Sync jobs

  

### Issue

-   'Workday - Socket timeout' errors during HR Integrations-Workday Sync jobs
-   If the HR Integrations-Workday Sync jobs fails with 'Workday - Socket timeout' errors please adjust the below timeout/pagination settings . Please note that increasing the timeout value to  higher values may have performance impact on the instance . Please also work with Workday support to check if the socket timeout is due to the performance issues on the Workday server end .

### Resolution

1.  Increase the HR Integrations Web Service timeout (within the Activity Designer) from 65 to higher value. Make sure the record with the Published value is true is the record that is updated.  
    Navigate to -> Activity Designer  
    HR Integrations Web Service  
    Execution Command -> Timeout(secs) -> 300 secs (for example).Refer to the KB :  [Socket timeout error while executing Workflow Activity](https://support.servicenow.com/kb_view.do?sysparm_article=KB0756635 "Socket timeout error while executing Workflow Activity")
2.  Adjust the Pagination for the Web Service Function (ex:Get All Workers function ).Refer to KB to adjust <bsvc:Count> : [HR Integrations FAQ](https://support.servicenow.com/kb_view.do?sysparm_article=KB0678031 "HR Integrations FAQ")  
    Set property-glide.http.outbound.max\_timeout.enabled - set to 'false'  
    glide.http.connection\_timeout ,glide.http.outbound.max\_timeout,glide.http.timeout -  adjust  these system properties to higher values 
3.  Check the 'Outbound HTTP Requests' to check the outbound web service response times from work day.
