---
title: "How to create relationship to load the S3 buckets in a related list"
aliases:
  - KB0719952
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719952
kb_number: KB0719952
last_modified: 2024-04-07
---

## How to create relationship to load the S3 buckets in a related list

  

### Issue

  

  

  

Building a relationship between the DataCenter and the Cloud object Storage to load the S3 Buckets into the related list.

#   

  

### Cause

* * *

 From the Filter navigator:

Go to the cmdb\_ci\_aws\_datacenter.LIST 

1\. Choose a Data Center

2\. Now, go to the bottom of the record and select the 'Cloud Object Storage’ near the related lists. Out of box this field is empty.

  

The related lists for the Cloud Object Storage is controlled by the following:

1. From the sys\_relationship.LIST

2\. Search for Virtual Machines: 

In the Virtual Machine record (sys\_relationship) It is using these fields:

\- Applies to this table: 'cmdb\_ci\_logical\_datacenter'  

\- Queries from this table: 'cmdb\_ci\_vm\_instance' 

**Its Using this code:**

(function refineQuery(current, parent) { 

new global.CMPGetRelatedResourcesForLDC().getHostedResources(current,parent); 

})(current, parent); 

### Resolution

# Workaround

 Create a new Relationship:

1\. From the sys\_relationship.LIST

2\. Create a new relation ‘Cloud Object Storage’

Use these fields:

\- Applies to this table: 'cmdb\_ci\_logical\_datacenter'  

\- Queries from this table: ‘cmdb\_ci\_cloud\_object\_storage'

Using the same code as above:

(function refineQuery(current, parent) { 

new global.CMPGetRelatedResourcesForLDC().getHostedResources(current,parent); 

})(current, parent);
