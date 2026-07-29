---
title: "Security remediation for password reset UI"
aliases:
  - KB0551031
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551031
kb_number: KB0551031
last_modified: 2025-01-03
---

## Issue

Security remediation for password reset UI 

Overview

* * *

This article is a guide for auditing and modifying the UI page(s) content intended for Password Reset functionality in ServiceNow platform.

Password reset application

* * *

The Password Reset application helps organizations implement and monitor a customizable self-service or service-desk process for resetting and changing passwords on the local ServiceNow instance. The application is introduced into the instance when the Password Reset plugin is enabled. For more information, see [Password Reset](https://docs.servicenow.com/ "Password Reset") in the ServiceNow product documentation.  

What is the reason for the system change?

* * *

ServiceNow identified an Information Disclosure vulnerability within the Password Reset application. The change remediates the vulnerability by enforcing additional validation on the system parameters.   
  

How to perform the system change

* * *

Follow the steps below to perform the system change.

1.  Log in to the instance with an account that has the **Administrator** role.
2.  In the navigation filter, enter **UI Pages**.  
      
    ![](/sys_attachment.do?sys_id=6e2aece2db42b450e515c223059619cd)  
      
    
3.  Click **UI Pages**. In the right hand pane, click **Show/Hide filter** to filter for the appropriate records.
4.  Filter the list to retrieve the Password reset record (as shown below).  
      
    
     ![](/sys_attachment.do?sys_id=ea2aece2db42b450e515c223059619d7)
    
    <table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: In the results above, you might find <strong>pwd_reset</strong> as the only result. This is due to the instance version you are running. If you fall under this category, please proceed with the <strong>pwd_reset</strong> page and ignore the <strong>$pwd_reset</strong> page, as shown above.</td></tr></tbody></table>
    
5.  Click on **pwd\_reset** record.
6.  In form view, navigate to the **HTML** field.
7.  Search for the variable **var sysparm\_url** in line 11.  
      
    ![](/sys_attachment.do?sys_id=ae2a2026db42b450e515c22305961927)   
      
    
8.  Replace the existing value **'${sysparm\_url}';** to **RP.getParameterValue('sysparm\_url');** 
9.  The final content on line 11 should be: **var sysparm\_url = RP.getParameterValue('sysparm\_url');**  
      
    ![](/sys_attachment.do?sys_id=432a2026db42b450e515c223059619b1)  
      
    
10.  **Update** the record.
11.  If there was a UI entry with name **$pwd\_reset** in the result section as mentioned in step 4, repeat steps 5-9 to modify the variable value in **$pwd\_reset** page as well.

ServiceNow product documentation references

* * *

-   [Password Reset](https://docs.servicenow.com/)
-   [UI Pages](https://docs.servicenow.com/csh?topicname=r_UIPages.html&version=latest)
-   [Using Filters and Breadcrumbs](https://docs.servicenow.com/csh?topicname=c_UsingFiltersAndBreadcrumbs.html&version=latest)
