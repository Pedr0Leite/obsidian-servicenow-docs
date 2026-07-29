---
title: "HR Service Delivery Advanced Integration with Workday- Holiday Calendar Report"
aliases:
  - KB0994509
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994509
kb_number: KB0994509
last_modified: 2025-09-08
---

## Text

This article walks you through the various steps involved in the setup of Holiday Calendar Report

# Prerequisites:

1.  User should have access of custom report creation.
2.  User should have Report data source access.

## Steps to Create Report:

1.  Access **Create Custom Report** task.
2.  Provide the report name as you like for example **CRPT\_holiday\_calendar.**
3.  Select report type as **Advanced**.
4.  **Uncheck** the Optimized for performance box.
5.  Select Data Source as **All Workers**.
6.  Leave temporary report box **uncheck**. Click **ok**.
7.  Please provide the values in report as given below  
      
    

![](/sys_attachment.do?sys_id=a04d67b1db4e3c58f21f5583ca961903)

8.  In Group column heading section  
      
    

![](/sys_attachment.do?sys_id=f44d67b1db4e3c58f21f5583ca961953)

9.  In filter section.  
      
    

![](/sys_attachment.do?sys_id=304de3b1db4e3c58f21f5583ca9619fa)

10.  In prompt section, click on the **Populate Undefined Prompt defaults** check box. It will populate the all built-in prompts.

**Note**\- Make sure the prompts are configured same as below  
  

![](/sys_attachment.do?sys_id=7c4d67b1db4e3c58f21f5583ca961971)

11.  In advanced section, please select **enable as webservice** check box. Then click ok.
12.  Once report configuration is done. Please click on three dots icon and go to web services> view URLs option  
       
     

 ![](/sys_attachment.do?sys_id=c54de3b1db4e3c58f21f5583ca96193e)

13.  Please Enter an employee id in **Employee ID** box and click ok. 

![](/sys_attachment.do?sys_id=454d67b1db4e3c58f21f5583ca96197c)

14.  In View URLs Web Service page, click on marked icon under **CSV section.** It will open a new browser tab. 

![](/sys_attachment.do?sys_id=114d67b1db4e3c58f21f5583ca9619c0)

15.  You can see the RaaS Url of the report in new browser tab and can get the below details from this link. 

![](/sys_attachment.do?sys_id=6d4d67b1db4e3c58f21f5583ca9619b6)

**https://wd2-impl-services1.workday.com** represents the Base URL of customer’s workday tenant. 

**Tenant\_Name** represents customer’s workday tenant. 

**Report\_Owner\_user\_name** represents user name of the report’s owner. 

**CRPT\_holiday\_calendar** Represents report name alias.
