---
title: "Displaying an Order Guide from CMS"
aliases:
  - KB0551838
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551838
kb_number: KB0551838
last_modified: 2024-04-07
---

## Displaying an Order Guide from CMS

  

### Issue

Displaying an Order Guide from CMS

  
Overview  

* * *

Order guides allow customers to make a single service catalog request that generates several items.

This article provides an example of how an Order Guide can be added to an IFrame on a content page and launched from a CMS navigational menu.

![](/sys_attachment.do?sys_id=701d2462db82b450e515c223059619e0)

High-level explanation  

* * *

This solution includes steps to create a new content page within a CMS site, how to add a new IFrame block of content to that page, and specify the page from a navigational menu. This article assumes there is an existing Order Guide. However, if this is not the case, use the steps in the product documentation page named [Create an Order Guide](https://docs.servicenow.com/csh?topicname=t_CreateAnOrderGuide.html&version=latest "Create an Order Guide").

The high level steps are:

1.  Create a new content page associated with a CMS site.
2.  Create a new IFrame associated to the new content page.
3.  Add any other content (for example, a header) to the new content page.
4.  Update the CMS navigational link to point to the new content page.
5.  Test the results.

Steps to implement  

* * *

**Create new content page associated with a CMS site**

1.  Navigate to **Content Management > Pages**.
2.  Click **New**.
3.  Enter a unique **Name** for the page.  
    As a best practice, prefix each page name with the name of the site followed by a dash and then the function of the page in the site. For example, ESS - Catalog Detail, ESS - Search Results, and ESS - Site Entry are all clear names for pages within the ESS site.
4.  Enter the **URL suffix** for the page.  
    The suffix is incorporated into the URL as follows: http://instance.service-now.com/site/url\_suffix.do.
5.  Select the **Content site** associated with the content page.  
    If you created this page from the site's related list, this information is automatically provided. The content site also determines part of the page URL as follows: http://instance.service-now.com/site\_suffix/page\_suffix.do.  
      
    [![](/sys_attachment.do?sys_id=b41d2462db82b450e515c223059619ff)  
      
    ](http://instance.service-now.com/site_suffix/page_suffix.do)For more information, see [Creating a Content](https://docs.servicenow.com/csh?topicname=t_CreateAContentPage.html&version=latest "Creating a Content") in the product documentation. 

**Create new iFrame associated to the new content page (created in preceding section)**

1.  Open the new content page.
2.  Scroll down to **Related Links** and click **Edit Page**.  
      
    ![](/sys_attachment.do?sys_id=f41d6462db82b450e515c22305961909)  
      
    
3.  In the upper right, click the **Add content** link.
4.  Within the **Sections** window, select **Content Blocks > \*New IFrame**.
5.  Click **Add here** to specify where the IFrame should be added.  
      
    ![](/sys_attachment.do?sys_id=0d1d6462db82b450e515c2230596190f)  
      
    
6.  Close the **Sections** window.
7.  Click the **Click here** link to display a new IFrame record.  
      
    ![](/sys_attachment.do?sys_id=451d6462db82b450e515c22305961921)  
      
    
8.  Configure the IFrame by entering values. The following was used for this example:
    -   **Name:** order\_guide\_iframe
    -   **Frame Name:** gsft\_main
    -   **Sizing:** Expand to Fit content
    -   **URL:**  com.glideapp.servicecatalog\_cat\_item\_guide\_view.do?v=1&sysparm\_initial=true&sysparm\_guide=cbc54e8c4fc9020096d31fb5f110c7d9&sysparm\_link\_parent=e4bf58092b97b4002fce294119da15de&sysparm\_catalog=e0d08b13c3330100c8b837659bba8fb4&sysparm\_catalog\_view=catalog\_default
        
        where:  
          
        \-sysparm\_guide is the sys\_id of the Order Guide \[sc\_cat\_item\_guide\] record  
        \-sysparm\_link\_parent is the sys\_id of the Category \[sc\_category\] specified within the Order Guide  
        \-sysparm\_catalog is the sys\_id of the Service Catalog \[sc\_catalog\] Order Guide is associated to 
        
          
        ![](/sys_attachment.do?sys_id=891d6462db82b450e515c2230596192c)  
          
        For more information, see [iFrames](https://docs.servicenow.com/csh?topicname=t_IFrame.html&version=latest "iFrames") in the product documentation.  

**Add any other content (for example, a header) to the new content page**

1.  Navigate to **Content Management > Pages**.
2.  Select the content page created earlier.
3.  Scroll down to **Related Links**.
4.  Select **Edit Page**.
5.  Select **Add content** link.
6.  Within the **Sections** window, select the additional content blocks to add.  
    For example, **Content Blocks > Portal - Header**.
7.  Click **Add here** to specify where it should be added.

![](/sys_attachment.do?sys_id=0d1d6462db82b450e515c22305961948)

**Update CMS navigational link to point to new content page**

1.  Navigate to **Content Management > Sites**.
2.  Select a site.  
    For example, Employee Self-Service.
3.  Click on the Homepage (for example, Portal) to open that record.
4.  Scroll down to **Related Links** and click **Edit Page**.
5.  On the **Portal Menu** block, click the pencil icon to edit that navigational menu.
6.  Scroll down to the **Menu Sections** related list (for example, **Order Things**).
7.  Scroll down to the **Menu Items** related list.
8.  Select **New**.
9.  Populate the record:
    -   **Name:** Enter a unique name for the menu item.
    -   **Menu Section:** Select the menu section in which this item will appear.
    -   **Detail page:** Select the content page (created earlier) to open when a user clicks the name or icon. This field is available only if **Redirect To** is set to **A content page**.

![](/sys_attachment.do?sys_id=d91d6462db82b450e515c2230596195e)  
  
For more information, see [Creating Menu Items](https://docs.servicenow.com/csh?topicname=t_ConfigureMenuItems.html&version=latest "Creating Menu Items") in the product documentation. 

**Test the results**

1.  Launch the CMS site (for example, http://instance.service-now.com/site/url\_suffix.do).  
    The Order Guide displays on the homepage:  
      
    ![](/sys_attachment.do?sys_id=151d6462db82b450e515c2230596196b)  
      
    
2.  Selecting the **Order Guide** link displays the new page and content.  
      
    ![](/sys_attachment.do?sys_id=151d6462db82b450e515c223059619a3)
