---
title: "Disabling public Content Management System (CMS) access"
aliases:
  - KB0546756
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546756
kb_number: KB0546756
last_modified: 2025-01-03
---

## Issue

Disabling public Content Management System (CMS) access

Overview

* * *

The Content Management System (CMS) plugin provides customers with unauthenticated guest access to limited content within the instance. CMS security features are activated using system properties.

<table class="noteTable" style="height: 60px;" width="1208" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><b>Notes</b>:<br><ul><li><span style="font-size: 10pt;">Do not enable if you have customized the default CMS site<br><br></span></li><li><span style="font-size: 10pt;">Please follow the steps outlined in <a href="/kb_view.do?sysparm_article=KB0547450">KB0547450</a> as a pre-requisite before enabling the system property</span></li></ul></td></tr></tbody></table>

Disabling public CMS access

* * *

Use the following procedure to change the **glide.ui.cms.enforce\_public\_pages** property and disable public CMS access.  

1.  Log into the instance as an admin user.  
      
    
2.  In the **Type filter text** field (upper-left corner), type **sys\_properties.list**.     
      
    ![](/sys_attachment.do?sys_id=e7cefca2db0ab450e515c22305961963)    
3.  In the query builder, type **\*cms** and click the search icon ![](/sys_attachment.do?sys_id=7fcefca2db0ab450e515c22305961979). 
4.  Click **glide.ui.cms.enforce\_public\_pages**.  
      
    ![](/sys_attachment.do?sys_id=b3cefca2db0ab450e515c22305961981)  
      
    
5.  Change the **Value** to **true**.  
      
    
6.  Click **Update**.         
      
    ![](/sys_attachment.do?sys_id=f7cefca2db0ab450e515c223059619b3)
