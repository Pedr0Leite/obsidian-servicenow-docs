---
title: "cmdb_ci_database table usage in Azure Database discovery"
aliases:
  - KB0749657
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749657
kb_number: KB0749657
last_modified: 2024-04-07
---

## cmdb\_ci\_database table usage in Azure Database discovery

  

### Issue

-   cmdb\_ci\_database table is used to store Azure MSSQL databases.  
      
    
-   Azure database discovery is done using the pattern "Azure Database".  
      
    
-   This would load the data under cmdb\_ci\_cloud\_database ( database instances ) and also cmdb\_ci\_database ( these are the actual databases running on the instance).  
        This process would also build a "Contains:: Contained by" relationship between these two tables.

### Related Links

Please refer to docs below

[https://docs.servicenow.com/bundle/paris-it-operations-management/page/product/discovery/reference/cloud-discovery-collected-data.html](https://docs.servicenow.com/bundle/paris-it-operations-management/page/product/discovery/reference/cloud-discovery-collected-data.html)
