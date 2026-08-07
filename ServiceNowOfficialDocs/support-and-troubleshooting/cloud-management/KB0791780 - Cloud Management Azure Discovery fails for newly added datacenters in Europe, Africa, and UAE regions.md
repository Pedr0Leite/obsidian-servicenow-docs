---
title: "Cloud Management Azure Discovery fails for newly added datacenters in Europe, Africa, and UAE regions"
aliases:
  - KB0791780
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791780
kb_number: KB0791780
last_modified: 2024-04-08
---

## Cloud Management Azure Discovery fails for newly added datacenters in Europe, Africa, and UAE regions

  

Azure has recently added a few more data centers in Europe, Africa, and UAE regions. These new regions appear while discovering regions/datacenters for an Azure Service Account or from Cloud Management's Cloud Account screen.

These newly added data centres:

1.  Europe (France Central, France South)
2.  AFRICA(South Africa North, South Africa West)
3.  UAE(UAE North, UAE Central)

![](sys_attachment.do?sys_id=43b95c8ddbc474d0b55f0b55ca961992)

The resources in these data centers are currently not accessible by default - some of these do not have API endpoints while some require access request to be raised with Azure Support explicitly in order to use them.As a result,  if discovering resources under these datacenters - discovery fails.

**Recommendation**

-   Select only those LDC's/Regions where your infrastructure resources are present. If you don't have any resources under these new data centers, please exclude them while you run the full discovery.

**Azure Support Document** : 

-   [https://azure.microsoft.com/en-in/global-infrastructure/geographies/](https://azure.microsoft.com/en-in/global-infrastructure/geographies/)
