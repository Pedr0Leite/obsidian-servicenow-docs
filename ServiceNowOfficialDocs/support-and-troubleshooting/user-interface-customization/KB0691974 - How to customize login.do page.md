---
title: "How to customize login.do page"
aliases:
  - KB0691974
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691974
kb_number: KB0691974
last_modified: 2025-01-03
---

## Issue

  
  

# Description

* * *

While the actual login.do page cannot be customized in itself (as it's a file on the back-end of the system) customization can be done on top of it so the the look and feel of the page can be different.

# Procedure

* * *

This customization involves creating a custom UI Page and making it public.

1) Create a new UI page with the following code in the HTML field:

<?xml version="1.0" encoding="utf-8" ?>  
<j:jelly trim="false" xmlns:j="jelly:core" xmlns:g="glide" xmlns:j2="null" xmlns:g2="null">  
<div style="width:900px;text-align:left;">  
  <g:insert\_form name="login" />  
</div>  
</j:jelly>

\*\*<g:insert\_form name="login" /> is the code that loads the login box for users to input their username and password to log into the instance

\*\*The above code is just a sample. More HTML can be added to customize the look and feel of the overall page.

2) Navigate to sys\_public.list and create a new record:

Active: true

Page: <the name of the custom UI page created>

3) [http://instance\_name.service-now.com/name\_of\_the\_custom\_ui\_page.do](http://instance_name.service-now.com/name_of_the_custom_ui_page.do) can now be given to users for them to log into the instance instead of the default OOB login.do link.

# Applicable Versions

* * *

All versions

# Additional Information

* * *

Determine where users would land after logging into the instance: [Define login scenarios](https://docs.servicenow.com/csh?topicname=t_LoginScenarios.html&version=latest "Define login scenarios")
