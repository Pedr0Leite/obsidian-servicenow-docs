---
title: "Issues with 'More Information' on Service Catalog Items"
aliases:
  - KB0547074
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547074
kb_number: KB0547074
last_modified: 2024-04-30
---

## Issue

This article intends to address the following issues:  
  

-   The "More information" link is needed to be maintained for all items displayed.
-   The "More information" link for catalog items does not behave as expected.

## Resolution

When browsing a category, the **More Information** link appears under the short description for a catalog item, showing an expanded description of that item, and a link to that item:  
  

![](/sys_attachment.do?sys_id=e8eef0e2db0ab450e515c22305961964)

  
  

-   If this link does not appear for an item, configure the number of items showing "More Information" using the system property **Number of Catalog Items to expand in browsing and search when not using pop-up icons to view details** \[glide.sc.auto\_expand\].  
    For example, set this to a high number such as 1,000 to expand the first 1000 catalog item descriptions in each category.  
      
      
    
-   Be aware that the **More Information** links to the service catalog item, not to an external link.  
      
    **Note:** Service catalog functionality also allows you to provide help links for requested items ([Add an ordered item link to an item](https://docs.servicenow.com/csh?topicname=t_AddOrderedItemLinks.html&version=latest "Add an ordered item link to an item")), and help links for variables in items ([Define help information for a service catalog variable](https://docs.servicenow.com/csh?topicname=t_DefineHelpInformation.html&version=latest "Define help information for a service catalog variable")). You may be able to achieve the required result using these alternative features.
