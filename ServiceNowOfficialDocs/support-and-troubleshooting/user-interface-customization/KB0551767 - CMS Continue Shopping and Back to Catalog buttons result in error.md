---
title: "CMS Continue Shopping and Back to Catalog buttons result in error"
aliases:
  - KB0551767
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551767
kb_number: KB0551767
last_modified: 2024-04-07
---

## CMS Continue Shopping and Back to Catalog buttons result in error

  

### Issue

CMS Continue Shopping and Back to Catalog buttons result in error

Problem

* * *

After upgrading to Eureka and later versions, if you use CMS and Service Catalog the **Continue Shopping** and **Back to Catalog** buttons can result in a **Page not found** broken link error and the following error:  
  
![](/sys_attachment.do?sys_id=e35deca2db82b450e515c22305961968)

Cause

* * *

Eureka introduced new functionality that included support for multiple Service Catalogs. As a result, it is now necessary to associate the CMS Site with the Service Catalog in order for the **Continue Shopping** and **Continue to Homepage** buttons to redirect the user correctly.

The [Using Catalog Site Records](https://docs.servicenow.com/ "Using Catalog Site Records") section of the product documentation explains the changes introduced in Eureka and how the **Sites** related list is used to specify the CMS Site to a service catalog record.

  
Resolution

* * *

Follow these steps to populate the fields necessary to support the redirection of the buttons within CMS.

1.  To display a list of service catalog records within the instance, navigate to **Service Catalog > Catalog Definitions > Maintain Catalogs**.    
      
    
2.  Click on the service catalog record being used.  
      
    
3.  From the Service Catalog \[sc\_catalog\] record, click the **Sites** related tab.  
      
    
    <table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: In the base system, the&nbsp;default Employee Self Service (ESS) site is already associated to the base sytem&nbsp;Service Catalog record.</td></tr></tbody></table>
    
      
      
      
    ![](/sys_attachment.do?sys_id=775deca2db82b450e515c223059619a2) 
    
4.  Click the **Edit** button to display the slushbucket.  
      
    
5.  Double click your custom site on the left to add it to the right and click **Save**:  
    ![](/sys_attachment.do?sys_id=335deca2db82b450e515c223059619b4)  
      
    
6.  Now back on the Sites related list, double click on the field in the related list to populate the following for the Site record:  
    ![](/sys_attachment.do?sys_id=fb5deca2db82b450e515c223059619c0)  
    -   CMS homepage: the url suffix of the content page that is the top of your catalog
    -   CMS search page: catalog\_find\_cms
    -   CMS 'Continue Shopping' page: <the url suffix of the content page that you want users' redirected to...if nothing is specified, the default behavior is to redirect the user to the previous CMS page>  
          
        
7.  Retest the steps and verify that the **Page not found** error no longer occurs and the user is redirected to the CMS content page as expected.
