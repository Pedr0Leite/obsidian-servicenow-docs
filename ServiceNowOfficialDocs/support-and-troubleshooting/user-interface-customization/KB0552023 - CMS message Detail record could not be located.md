---
title: "CMS message: Detail record could not be located"
aliases:
  - KB0552023
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552023
kb_number: KB0552023
last_modified: 2024-04-07
---

## CMS message: Detail record could not be located

  

### Issue

CMS message: Detail record could not be located

  
  

# Symptoms

* * *

When navigating to a page within [CMS](https://docs.servicenow.com/csh?topicname=c_ContentManagementSystem.html&version=latest "CMS"), the user receives this message: _Detail record could not be located._  
  
  

# Cause

* * *

This message indicates that the system is accessing a detailed content block, but either the block was configured incorrectly or the specified detailed record does not exist.  
  
For example, the message can be seen just by viewing a custom CMS page called "test.do" where a detailed content block has been added:  
  
  
![](/sys_attachment.do?sys_id=b829e8aedb02b450e515c22305961908)  
  

# Resolution

* * *

In the above example, the message displays in the Employee Self-Service site (for example, /ess/) on the test.do page. To resolve the message, go to the CMS page where the message is occurring:

1.  Navigate to **Content Management > Pages.**
2.  Go to the **Test** page.  
    
3.  Under **Related Links**, select **Edit Page**.  
      
    ![](/sys_attachment.do?sys_id=f429e8aedb02b450e515c22305961922)  
      
    
4.  View the content block to see where the message is occurring:  
      
    ![](/sys_attachment.do?sys_id=8929e8aedb02b450e515c22305961931)  
      
    
5.  To prevent the message from displaying, delete this block using the **X** in the upper-right corner.  
      
    
6.  To edit the block, select the pencil icon in the upper-right corner of the content block to view detailed content:  
      
    ![](/sys_attachment.do?sys_id=c929e8aedb02b450e515c2230596193d)

  
The content block above is configured to **Show the page's current document**. This is used to display the contents of an existing document, such as a knowledge article or service catalog request, as a block on a content page. For more about this functionality, see [Detailed Content Blocks](https://docs.servicenow.com/csh?topicname=t_DetailedContentBlock.html&version=latest "Detailed Content Blocks").  
  
This detailed content block type cannot be used alone. The CMS page on which the detailed block is embedded must be specified in the [Content Types](https://docs.servicenow.com/csh?topicname=c_ContentTypes.html&version=latest "Content Types") record in the **Default detail page** field.  

To view the content types and detailed pages:

1.  Navigate to **Content Management > Content Types** to see a list of content types and specified default detail pages:  
      
    ![](/sys_attachment.do?sys_id=0929e8aedb02b450e515c22305961948)

2.  To create a CMS page that contains a custom detailed content block, ensure there is a corresponding Content Types record configured.  
      
    

To see an example of a base-system content type in CMS and how to customize it, see this community post:  
[https://community.servicenow.com/thread/206370](https://community.servicenow.com/thread/206370)
