---
title: "KB Service Portal Review of User Criteria "
aliases:
  - KB0824691
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824691
kb_number: KB0824691
last_modified: 2025-03-26
---

## Text

### Audience

Instance Administrators

### Overview

To ensure knowledge base and customer portal pages are visible to the intended audience, use this article to review **Can Read** and **Can Contribute** user criteria configuration for your instances.

ServiceNow has identified a potential configuration issue relating to knowledge base articles and portal pages. Knowledge administrators can configure one or more knowledge bases, articles and portal pages for public access by setting up user criteria in a way that grants public viewing.

This article provides links to these main configuration options  

-   Frequently Asked Questions (noted below)
-   Service Portal Page configuration 
-   Review Knowledge Base configuration documentation
-   Set User Criteria for Knowledge Bases

  

### Details

How do I check my configurations to make sure they meet our business requirements?

  

**Part A:**

_**Step 1**_ – Does your company need to make some Knowledge articles or Portal pages available to the public?

If yes, go to Step 2 below.

If no, go to Part B2.

  

_**Step 2**_ – Confirm the Knowledge Bases and/or portal pages you expect the public to access are the only Knowledge Bases and Pages that are publicly visible. If yes, then no further action is required by you.

If there are any Knowledge Bases that are unintentionally publicly visible, please continue to Part B1 or Part B2 for options on how to modify your current configurations.

  

**Part B1:**

If your instances are NOT currently on one of the following versions, your only option is to review Part B2.

-   -   Madrid Patch 10 or above
    -   New York Patch 5 or above
    -   Orlando (All versions) 

For customers who are on one of these versions, please reference [KB0793403](/kb_view.do?sysparm_article=KB0793403) to quickly modify the configuration of your public portal pages to make them private by using an available plugin option.

  

**Part B2:**

_**Step 1**_ – Refer to [Create and Edit Service Portal pages](https://docs.servicenow.com/bundle/newyork-servicenow-platform/page/build/service-portal/task/t_ConfigureAPage.html#t_CustomizeAPage) to review your settings-> this document will show you how to review and edit your page properties. (See step 8a for the property called ‘Public’.) Be sure to mark both ServiceNow Out of the Box Portal pages as well as any custom Knowledge-related Service Portal pages as private. Then go to Step 2.

  

![](/sys_attachment.do?sys_id=a094edf8dbc57410dc2beeb5ca961920)

  

_**Step 2**_ – Next, refer to [Making UI pages public or private](https://docs.servicenow.com/bundle/newyork-platform-administration/page/administer/general/task/t_MakeAPagePublic.html). Then go to Step 3.

  

_**Step 3**_ – Review your Knowledge Base access controls by referring to [Select User Criteria for Knowledge Bases](https://docs.servicenow.com/bundle/newyork-servicenow-platform/page/product/knowledge-management/task/t_SelectUserCriteria.html#t_SelectUserCriteria). Ensure you are securing access to specific internal users using the Can Read user criteria.

  

### FAQs

**Q: Why was I directed to this KB article?**

**A:** ServiceNow is providing guidance for your existing or future configuration of the Knowledge Management modules that you may be using or may be developing in the future.

  

**Q: Does this affect non-prod instances, prod instances, or both?**

**A**: Both

  

**Q: Which instances should I review?**

**A:** If your instance is actively using Knowledge Management, you should check to make sure your articles are set according to your business requirements.

**Q: How do I determine if one of our articles/KBs is configured according to our business needs?**

**A:** The product documents we have listed in the Additional Information section below can help you review your articles in light of your specific business usage. The two main items to review are whether user criteria are defined, and how your portal has been configured. If you have specific needs to ensure public access to articles, you can do so through this configuration. If you have a need to make articles internal, these features will help you do so, along with your regular ACL and role configurations.

  

**Q: How do I install the plugin?**

**A:** Please review [KB0793403](/kb_view.do?sysparm_article=KB0793403 "KB0793403") for the versions which contain the plugin and confirm your instance supports the plugin.

-   -   If you are on a supported version, search for the plugin using the Plugin Id - com.glide.service-portal.pages.restricted. Select the plugin and install it.
    -   If your instance is not on a supported version, please upgrade to a version which contains the out of the box plugin, and then follow the instructions (above/noted in [KB0793403](/kb_view.do?sysparm_article=KB0793403 "KB0793403").)  
          
        

**Q: How do I get a list of kb articles which might have been accessed by non-authenticated users in my instance?**

**A:** For the list of articles accessed by non-authenticated users, you can check the kb\_use table. Whenever an article is viewed, this table captures the article that was viewed and the user that viewed the article. Look for records that have Viewed set to true and the user as Guest.

Example:

-   https://<instance-name>.service-now.com//kb\_use\_list.do?sysparm\_query=user.nameSTARTSWITHguest%5Eviewed%3Dtrue (Commercial)
-   https://<instance-name>.servicenowservices.com//kb\_use\_list.do?sysparm\_query=user.nameSTARTSWITHguest%5Eviewed%3Dtrue (GCC)

  

**Q: Do I need to do anything after an upgrade which contains the plugin option?**

**A:** Yes; please check the current configurations are set appropriately using the product documentation linked at the bottom of this article

   

### Additional information

Additional information can be found in our Product documentation located in the following links:

 Knowledge Management:

-   [Select User Criteria for Knowledge Bases](https://docs.servicenow.com/bundle/newyork-servicenow-platform/page/product/knowledge-management/task/t_SelectUserCriteria.html#t_SelectUserCriteria)
-   [Select User Criteria for Knowledge Articles](https://docs.servicenow.com/bundle/newyork-servicenow-platform/page/product/knowledge-management/task/t_SelectUCArticle.html)

User Interface:

-   [Making UI pages public or private](https://docs.servicenow.com/bundle/newyork-platform-administration/page/administer/general/task/t_MakeAPagePublic.html)

Portal Pages:

-   [Create and Edit Service Portal pages](https://docs.servicenow.com/bundle/newyork-servicenow-platform/page/build/service-portal/task/t_ConfigureAPage.html#t_CustomizeAPage)
