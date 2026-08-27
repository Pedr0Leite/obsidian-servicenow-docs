---
title: "HR Service Delivery Advanced Integration with Workday - Payslip Report"
aliases:
  - KB0994511
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994511
kb_number: KB0994511
last_modified: 2025-09-08
---

## Text

# Payslip report:  
  

This report is used to fetch worker’s payslip data based on time range and employee ID.  
  

## Prerequisites**:**

1.  User who is going to create this report should have **Custom Report Creation** domain access.
2.  User should have report data source **“Payroll Results”** access.
3.  User should have **Copy Standard Report to Custom Report** Task access.

## Report Development Instructions:

-   While creating the report, report name can be selected different but please make sure that the report field names or column heading override for the respective field (if given in report doc) should be same as it is in report document. **(report field label should be same as in report doc otherwise developed action will fail).**
-   **Group Column Heading** for each business object in **Group Column Heading** section should be blank.
-   All **Reports must be shared or owned by ISU user** which will be used for accessing these action on ServiceNow platform.
-   In advanced section,  **Enable as webservice** box should be checked.

## Steps to Create Report:

1.  Access **Copy Standard Report to Custom Report** task.
2.  Search for **Payslip to Print - Report Design** in Standard Report name box and select it. Then click ok.

![](/sys_attachment.do?sys_id=e3a7e7bddb8a3c58f21f5583ca9619ed)

3.  Please provide the desired name of the report such as **Payslip to Print - Report Design – Copy.** Click ok.  
      
    

![](/sys_attachment.do?sys_id=53a7e7bddb8a3c58f21f5583ca9619da)  
  

4.  In Data Source box, search for Payroll results and select it.

![](/sys_attachment.do?sys_id=a7a7e7bddb8a3c58f21f5583ca9619fa)  

5.  Once you select **Payroll Results** as data source, Report will automatically populate the

Data source filter.

![](/sys_attachment.do?sys_id=bfa76bbddb8a3c58f21f5583ca9619cf)

6.  Add **Sub Period (if different from Pay Period)** report field in column section in report as shown below.

![](/sys_attachment.do?sys_id=08b72bbddb8a3c58f21f5583ca96191e)

7.  In **Columns** section, Please Remove fields which are not in screenshots given below.(**make sure all field are in same order as it is in screenshots**)

![](/sys_attachment.do?sys_id=84b7a7bddb8a3c58f21f5583ca9619f7)

![](/sys_attachment.do?sys_id=c8b7abbddb8a3c58f21f5583ca961970)

![](/sys_attachment.do?sys_id=dcb7ebbddb8a3c58f21f5583ca96194e)

![](/sys_attachment.do?sys_id=54b7abbddb8a3c58f21f5583ca96197a)

![](/sys_attachment.do?sys_id=68b7ebbddb8a3c58f21f5583ca961958) 

8.  In **Group Column Headings** section, remove business objects which are not in below screenshots. **(Group column heading for all business objects should be blank).**

![](/sys_attachment.do?sys_id=28b76bbddb8a3c58f21f5583ca9619b7)

![](/sys_attachment.do?sys_id=b8b7ebbddb8a3c58f21f5583ca96199c)

9.  In Prompt section, remove the pre-existing prompt.

![](/sys_attachment.do?sys_id=70b7ebbddb8a3c58f21f5583ca961983)

10.  Once pre-existing prompt got removed, click on the **Populate Undefined Prompt defaults** check box. It will populate the all built-in prompts.

**Note**\- Make sure the prompts are configured same as below.  
  

![](/sys_attachment.do?sys_id=81b72fbddb8a3c58f21f5583ca961916)

11.   In Advanced section, please check if **Enabled as Web Service** check box is selected?(most probably it would be already selected)if not then please select.

![](/sys_attachment.do?sys_id=c9b7ebbddb8a3c58f21f5583ca96197d)

12.  Click ok, then done.
13.  Once report configuration is done. Please click on three dots icon and go to web services> view URLs option  
       
     

 ![](/sys_attachment.do?sys_id=d1b72fbddb8a3c58f21f5583ca961931)

14.  Please select any time range in below parameters and select any user in **worker** box and click ok. 

![](/sys_attachment.do?sys_id=55b72fbddb8a3c58f21f5583ca961904)

15.  In View URLs Web Service page, click on marked icon under **CSV section.** It will open a new browser tab. 

![](/sys_attachment.do?sys_id=25b72fbddb8a3c58f21f5583ca96190d)

16.  You can see the RaaS Url of the report in new browser tab and can get the below details from this link. 

![](/sys_attachment.do?sys_id=6db72fbddb8a3c58f21f5583ca9619ed)

**https://wd2-impl-services1.workday.com** represents the Base URL of customer’s workday tenant. 

**Tenant\_Name** represents customer’s workday tenant. 

**Report\_Owner\_user\_name** represents user name of the report’s owner. 

**Payslip\_to\_Print\_-\_Report\_Design\_-\_Copy** Represents report name alias.
