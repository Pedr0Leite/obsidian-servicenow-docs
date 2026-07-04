---
title: "[SAMP-License Workbench] License Workbench shows non-licensable models on the page"
aliases:
  - KB0855394
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855394
kb_number: KB0855394
last_modified: 2024-04-08
---

## \[SAMP-License Workbench\] License Workbench shows non-licensable models on the page

  

### Issue

When we open the License Workbench it shows non-licensable models on the page. Some of the other flavors of the issue are shown below:

1.  Under the Software product results, there are few software installs that are normalized to non-licensable products. But still shows under the software product results. 
2.  non-licensable models showing-up on the license workbench.

### Release

Jakarta ++

### Cause

-   The Products on license workbench are dependent on product results generated during the reconciliation. In some cases, even though the product is non-licensable somehow the product results generated. And this is the reason we see Reader in License workbench.  
    
-   In some cases, the content must have updated from licensable to non-licensable. Due to this the software installs remains in older normalization where the product is licensable.
-   There might be some bad data import mechanisms that update this.

### Resolution

Step#1 Revert the normalization for all the discovery models that are associated with these software installations. By doing below:  
[https://docs.servicenow.com/csh?topicname=t\_EditASoftwareDiscModel.html&version=latest](https://docs.servicenow.com/csh?topicname=t_EditASoftwareDiscModel.html&version=latest)  
  
Step #2 Then normalize it by clicking on Normalize UI Action as below:  
[https://docs.servicenow.com/csh?topicname=t\_EditASoftwareDiscModel.html&version=latest](https://docs.servicenow.com/csh?topicname=t_EditASoftwareDiscModel.html&version=latest)
