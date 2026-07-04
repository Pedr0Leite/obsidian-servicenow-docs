---
title: "How to select or change language from CMS site"
aliases:
  - KB0552129
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552129
kb_number: KB0552129
last_modified: 2024-01-28
---

## How to select or change language from CMS site

  

### Issue

How to select or change language from CMS site

Problem

* * *

[Translation as it relates to the CMS](https://docs.servicenow.com/csh?topicname=c_CMSTranslation.html&version=latest "Translation as it relates to the CMS") is documented within product documentation. According to product documentation, when a user logs in, the [language for the instance](https://docs.servicenow.com/csh?topicname=c_LangInternationalizationSupport.html&version=latest "language for the instance") session is determined by the following logic:

-   If the language selection at login is enabled, that language is used.
-   If not, the language preference selected using the language picker in the header bar is used.
-   If not, the user's language setting in the User \[sys\_user\] table is used. 
-   If none of the above are true, the system default language is used.

An end user can be granted the ability to populate the **Language** field in their profile \[sys\_user\] record within CMS. This can be done by configuring the self-service view of the User \[sys\_user\] form and adding the **Language** field; however, this does _not_ change the language displayed in CMS for that user.

Based on the above, here are the two supported methods for allowing users to select or change their language in ServiceNow:  
  
From the login screen, select the language and log in:

![](/sys_attachment.do?sys_id=836a6466db42b450e515c223059619fb)  
  
  
Or click the gear icon in the top-right:  
  
![](/sys_attachment.do?sys_id=876aa466db42b450e515c22305961905)

Without the options above, users who get redirected to the CMS site or bypass the login page may have issues selecting or changing the language within the CMS.  
  

  
Resolution

* * *

These UI macros are created when the language plugin \[I18N: Internationalization\] is activated:

-   login\_language\_select - displays a list of available languages on the login page to the user
-   ui\_language\_select - displays a list of available languages to the user and lets them select one

There is no base system language picker for use with a CMS site; however, customers may choose to customize their CMS code to call the ui\_language\_select UI macro to meet their needs.    
  
There is no documented method for accomplishing this from the base system. In this case, customers are advised to pursue solutions through the Community. The following post ([https://community.servicenow.com/thread/166553](https://community.servicenow.com/thread/166553)) is provided as one such example:

To enable the language picker within a CMS site:

1.  Modify the UI macro **cms\_header\_login** to call the **ui\_language\_select** UI macro by adding the script above the login link:  
      
    <g:ui\_language\_select />  
    <script>  
    </script>  
      
    This macro displays the header on the ESS Portal:  
      
    ![](/sys_attachment.do?sys_id=4b6aa466db42b450e515c22305961919)  
      
    
2.  Select a different language to display the language selected in the CMS:  
      
    ![](/sys_attachment.do?sys_id=8b6aa466db42b450e515c22305961925)

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>: Altering the base system <span style="text-align: start;">cms_header_login UI macro causes it to be "customized"&nbsp;and potentially&nbsp;skipped by future ServiceNow upgrades.&nbsp; See&nbsp;<a title="Overwriting_Customizations_During_Upgrades" href="https://docs.servicenow.com/csh?topicname=t_OverwriteCustomizsDuringUpgrades.html&amp;version=latest" target="_blank" rel="noopener noreferrer">Overwriting_Customizations_During_Upgrades </a>for more information.<br></span></td></tr></tbody></table>

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp;Solutions implementation from the Community are outside the scope of Technical Support, which is a break/fix issues in the base platform. Customers may&nbsp;implement at their own risk but are responsible for maintaining the solutions.</td></tr></tbody></table>
