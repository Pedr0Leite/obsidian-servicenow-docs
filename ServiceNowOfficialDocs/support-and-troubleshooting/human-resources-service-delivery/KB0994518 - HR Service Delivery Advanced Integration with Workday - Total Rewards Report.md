---
title: "HR Service Delivery Advanced Integration with Workday - Total Rewards Report"
aliases:
  - KB0994518
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994518
kb_number: KB0994518
last_modified: 2025-09-08
---

## Text

# This article walks you through the various steps involved in the setup of Total Rewards Report  
  
**Prerequisites:**

1.  User should have access of custom report creation.
2.  User should have Report data source access.

# **Steps to Create Report:**

1.  Access **Create Custom Report** task.
2.  Provide the report name as you like for example **RPT total rewards.**
3.  Select report type as **Advanced**.
4.  **Uncheck** the Optimized for performance box.
5.  Select Data Source as **All Workers**.
6.  Leave temporary report box **uncheck**. Click **ok**.
7.  Please provide the values in report as given below

![](/sys_attachment.do?sys_id=3da5a335db8a3c58f21f5583ca96190e)

8.  In Group column heading section. (Group Column heading for business object will be blank).

![](/sys_attachment.do?sys_id=f5a56335db8a3c58f21f5583ca9619a4)

9.  In filter section.

![](/sys_attachment.do?sys_id=0ea5eff1db8a3c58f21f5583ca9619d4)

10.  In prompt section, click on the **Populate Undefined Prompt defaults** check box. It will populate the all built-in prompts.

**Note**\- Make sure the prompts are configured same as below

 ![](/sys_attachment.do?sys_id=8aa5a335db8a3c58f21f5583ca961976)

11.  In advanced section, please select **enable as webservice** check box. Then click ok.
12.  Once report configuration is done. Please click on three dots icon and go to web services> view URLs option  
       
     

![](/sys_attachment.do?sys_id=daa52335db8a3c58f21f5583ca961967)

13.  Please select any currency and an employee id in below parameters and click ok. 

![](/sys_attachment.do?sys_id=9ea52335db8a3c58f21f5583ca96192f)

14.  In View URLs Web Service page, click on marked icon under **CSV section.** It will open a new browser tab. 

![](/sys_attachment.do?sys_id=aea5e335db8a3c58f21f5583ca961911)

15.  You can see the RaaS Url of the report in new browser tab and can get the below details from this link.

 ![](/sys_attachment.do?sys_id=2aa5e335db8a3c58f21f5583ca96190a)

**https://wd2-impl-services1.workday.com** represents the Base URL of customer’s workday tenant. 

**Tenant\_Name** represents customer’s workday tenant.

**Report\_Owner\_user\_name** represents user name of the report’s owner. 

**RPT\_total\_rewards** Represents report name alias.
