---
title: "HR Service Delivery Integration with Workday - Pull To Do Report"
aliases:
  - KB0994522
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994522
kb_number: KB0994522
last_modified: 2025-05-13
---

## Text

# Pull to do report:

This article walks you through the process of creating a Pull to do report which is used to fetch workers inbox items like to-dos, action items, approval etc.

## Prerequisites:

1.  User who is going to create this report should have report creation access.
2.  User should have report data source **“Business process event steps”** access.

## Report Development Instructions:

-   For identification purpose, All calculated field name starts with **CF.**
-   Please create all calculated fields for this report before developing the report, so that while creating report all fields will be available (**calculated field configurations are given below)**
-   While creating the report, report name can be selected different but please make sure that the report field names or column heading override for the respective field (if given in report doc) should be same as it is in report document. **(report field label should be same as in report doc otherwise developed action will fail).**
-   **Group Column Heading** for each business object in **Group Column Heading** section should be blank.
-   While creating filter **make sure to add parenthesis on filter** as given in screenshots.
-   All **Reports must be shared or owned by ISU user** which will be used for accessing these action on ServiceNow platform.
-   In advanced section, **Enable as webservice** box should be checked.

## Calculated field configuration:

Please create all calculated fields so that these fields can be used while developing report.

**Calculated Field 1:**

-   Create increment and decrement type calculated field named **CF\_Last\_functionally\_updated\_-1** 

![](/sys_attachment.do?sys_id=e1c4edc7475b9a1048cb2920326d4316)

-   Create Lookup Value as of date type calculated field named **cf\_assigned\_to\_worker\_previous** and use **CF\_Last\_functionally\_updated\_-1**  in this field.  
      
    

![](/sys_attachment.do?sys_id=f5c4edc7475b9a1048cb2920326d434a)  
  

**Calculated Field 2:**

-   Create text constant type calculated field named **Cf\_text\_0.**

![](/sys_attachment.do?sys_id=e9c4edc7475b9a1048cb2920326d4306)

-   Create text constant type calculated field named **CF\_Text\_as\_1**.

![](/sys_attachment.do?sys_id=d9c4adc7475b9a1048cb2920326d43d9)

-   Create true/false condition type calculated field named **cf\_competed\_by\_is\_not\_equal\_old\_assignee**.

![](/sys_attachment.do?sys_id=65c4adc7475b9a1048cb2920326d43f4)

-   Create evaluate expression calculated field named **CF\_EE\_Completed\_by\_admin\_exist\_as\_old\_Assignee\_or\_not.**

![](/sys_attachment.do?sys_id=25c4edc7475b9a1048cb2920326d4319)

**Calculated Field 3:**

-   Create text constant type calculated field named **CF\_Text.**

![](/sys_attachment.do?sys_id=65c4edc7475b9a1048cb2920326d431c)

-   Create Lookup related value type calculated field named **CF\_Action\_Event**.

![](/sys_attachment.do?sys_id=31c4edc7475b9a1048cb2920326d4335)

-   Create Concatenate text type calculated field named **CF\_inbox\_Subject**.

![](/sys_attachment.do?sys_id=6dc4adc7475b9a1048cb2920326d43e3)

**Calculated Field 4:**

-   Create text constant type calculated field named **CF\_url.**

![](/sys_attachment.do?sys_id=79c4edc7475b9a1048cb2920326d434d)

-   Create Lookup related value type calculated field named **CF\_business\_pro\_transaction**

![](/sys_attachment.do?sys_id=e1c4adc7475b9a1048cb2920326d43f1)

-   Create Lookup related value type calculated field named **CF\_BP\_Wid.**

![](/sys_attachment.do?sys_id=51c4adc7475b9a1048cb2920326d43dd)

-   Create Concatenate text type calculated field named **CF\_Inbox\_url.**

![](/sys_attachment.do?sys_id=f1c4edc7475b9a1048cb2920326d433e)

**Calculated Field 5:**

-   Create Lookup related value type calculated field named **cf\_step\_id**

![](/sys_attachment.do?sys_id=b5c4edc7475b9a1048cb2920326d431f)

-   Create Lookup related value type calculated field named **CF\_subject\_id**

![](/sys_attachment.do?sys_id=a5c4adc7475b9a1048cb2920326d43f7)

-   Create Lookup related value type calculated field named **CF\_subject\_and\_step\_id**.

![](/sys_attachment.do?sys_id=bdc4edc7475b9a1048cb2920326d432e)

## **Calculated Field 6:**

-   Create Lookup related value type calculated field named **CF\_sent\_back**.

![](/sys_attachment.do?sys_id=69c4edc7475b9a1048cb2920326d4300)

**Calculated Field 7:**

-   Create Lookup related value type calculated field named **Business Process Definition on Action Event**

        ![](/sys_attachment.do?sys_id=51c4adc7475b9a1048cb2920326d43c3)

-   Create Lookup related value type calculated field named:  
        **Cf\_parent\_business\_process\_definition**.

![](/sys_attachment.do?sys_id=b9c4edc7475b9a1048cb2920326d4350)

## Steps to Create Report:

1.  Access **Create Custom Report** task.
2.  Provide the report name as you like for example **SNIH\_Inbox\_Items.**
3.  Select report type as **Advanced**.
4.  **Uncheck** the Optimized for performance box.
5.  Select Data Source as **Business Process Event steps**.
6.  Leave temporary report box **uncheck**. Click **ok**.  
      
    

![](/sys_attachment.do?sys_id=69c4adc7475b9a1048cb2920326d43ea)

7.  Please select the report business object and report fields as given below.

![](/sys_attachment.do?sys_id=fdc4edc7475b9a1048cb2920326d4331)

![](/sys_attachment.do?sys_id=71c4edc7475b9a1048cb2920326d4338)

8.  In Group column heading section, select all business object as below.(Group Column heading for each business object will be blank).  
      
    

![](/sys_attachment.do?sys_id=adc4adc7475b9a1048cb2920326d43ed)

9.  In Filter section, select the value as given below.(**please make sure to add parenthesis as given in below screenshots)  
      
    **

![](/sys_attachment.do?sys_id=75c4edc7475b9a1048cb2920326d4344)

![](/sys_attachment.do?sys_id=29c4adc7475b9a1048cb2920326d43fd)

![](/sys_attachment.do?sys_id=e5c4adc7475b9a1048cb2920326d43fa)

![](/sys_attachment.do?sys_id=35c4edc7475b9a1048cb2920326d4341)

![](/sys_attachment.do?sys_id=e1c4adc7475b9a1048cb2920326d43e7)

10.  In prompt section, click on **populate undefined prompt defaults** check box.  
       
     

![](/sys_attachment.do?sys_id=9dc4adc7475b9a1048cb2920326d43c9)

11.  Select the value of prompts as given below under Prompt default section. Make sure the **Label For Prompt XML Alias** of all prompt fields must be same as below screenshot.

![](/sys_attachment.do?sys_id=3dc4edc7475b9a1048cb2920326d4353)

![](/sys_attachment.do?sys_id=a9c4edc7475b9a1048cb2920326d4303)

12.  In advanced section, please select **enable as webservice** check box. Then click ok.
13.  Once report configuration is done. Please click on three dots icon and go to web services> view URLs option  
       
     

![](/sys_attachment.do?sys_id=b1c4edc7475b9a1048cb2920326d433b)

14.  Please select any time range in below parameters and click ok.  
       
     

![](/sys_attachment.do?sys_id=d5c4adc7475b9a1048cb2920326d43e0)

15.  In View URLs Web Service page, click on marked icon under **CSV section.** It will open a new browser tab.

![](/sys_attachment.do?sys_id=19c4adc7475b9a1048cb2920326d43c6)

16.  You can see the RaaS Url of the report in new browser tab and can get the below details from this link.

![](/sys_attachment.do?sys_id=b5c4edc7475b9a1048cb2920326d4347)

**https://wd2-impl-services1.workday.com** represents the Base URL of customer’s workday tenant.

**Tenant\_Name** represents customer’s workday tenant.

**Report\_Owner\_user\_name** represents user name of the report’s owner.

**SNIh\_Inbox\_Items** Represents report name.
