---
title: "Manual Upgrade instructions for MultiSSO V2 for CSE"
aliases:
  - KB0778202
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778202
kb_number: KB0778202
last_modified: 2023-09-11
---

## Manual Upgrade instructions for MultiSSO V2 for CSE

  

The MultiSSO plugin v2 is upgraded with its internal library of OpenSAML to 3.4.1, which addresses the known vulnerabilities of Open SAML Lib 2.4.1, this includes changes to the existing Script includes, Installation Exits, and other components.

Customers upgrading to later releases will get the new version of MultiSSO with Open SAML Lib V3.4.1, however pre-New York instances will have an upgrade path provided to move them to latest MultiSSO V2 if they have any customization(s) to any of the MultiSSO resources. The Upgrade path will ensure that their customizations are preserved and all the existing SAML flows function as is.

If an instance is upgraded to MultiSSO V2 or not, can be verified checking the system property '**_glide.authenticate.multissov2\_feature.enabled_**'.

If the property is not found or its value is set to false, then instance is not upgraded to MultiSSO V2.

It is recommended to go through the for [OOB available customization samples](/kb_view.do?sysparm_article=KB0778203 "OOB available customization samples"), before applying solution on customer instances.

# Customized Instances :

Customized Instances refers to those instances where there is some customization in any of the MultiSSO resources.

In order to upgrade from MultiSSO to latest MultiSSO V2, for Customized Instances, customers have to manually perform Upgrade as per the instructions in the Upgrade Doc (provided in this [KB Article](/kb?id=kb_article_view&sysparm_article=KB0756504 "KB Article")). If the customers are not able to upgrade to the MultiSSO V2 themselves, due to their customizations, they can reach out to customer support.

# Upgrade Path for Customized Instances :

1.  Navigate to the Customization List from Platform Security instance [SAML Lib Upgrade Customization Audit Results](https://platformsecurityteam.service-now.com/nav_to.do?uri=%2Fu_saml_lib_upgrade_customization_audit_results_list.do%3Fsysparm_query%3D%26sysparm_first_row%3D1%26sysparm_view%3D)
2.  Search for the Customer in the 'Instance Name' column.
3.  Open the record and Search for the 'Analysis' and 'Solution Categories' columns .  
    1.  Read through the 'Analysis' column to get information about the customization, Check If any Solution Category is mapped in 'Solution Categories' column. If No Solution is mapped, then follow the steps mentioned in the 'Analysis' column (if any) and then follow next section - [Steps to Upgrade to MultiSSO V2](#_Steps_to_Upgrade) to upgrade to MultiSSO V2.
    2.  If there are changes required per the 'Analysis' Column and/or Solution Categories are mapped to the 'Solution Categories' column, search for the each Solution provided as part of the 'Solution Categories'.
    3.  Navigate to à [MultiSSO Customization Solutions](https://platformsecurityteam.service-now.com/nav_to.do?uri=%2Fmultissov2_customization_solution_list.do%3Fsysparm_userpref_module%3D325680fddb4c3f0093039ea3db961927%26sysparm_clear_stack%3Dtrue) in the Platform Security instance and search for the category.
    4.  Open the customization solution category.
    5.  In the Request/Response solution for V2 Column, select the code changes for the specific customer (perform a customer instance name search, if the list is too big).
    6.  Pick the code changes and apply in the customer instance as stated in the top of the Solution category column.
    7.  Once you apply the code changes, then follow the next section - [Steps to Upgrade to MultiSSO V2](#_Steps_to_Upgrade) to upgrade to MultiSSO V2.

#  

# Steps to Upgrade to MultiSSO V2 :

-   Verify if the System property '**_glide.authenticate.multissov2\_feature.enabled_**' is available.  
    -   If **available,** verify if the _**property**_ is set to _**true,**_ if NOT then set it to _**true.**_
    -   If **NOT available**, then Create a New System property as specified below -  
        -   Name – **_glide.authenticate.multissov2\_feature.enabled_**
        -   Type – true | false
        -   Value – **true**
        -   Example Screenshot :

![](/sys_attachment.do?sys_id=0178a9dc47d9f110b6d8aa25126d437e)

-   Perform the below steps:  
    -   On 'Multiple Provider SSO Properties' page **Disable (or uncheck)** and Save the property  "**Enable multiple provider SSO**".
    -   On the same page **Enable (or check)** and Save the property  "**Enable multiple provider SSO**".

![](/sys_attachment.do?sys_id=0978a9dc47d9f110b6d8aa25126d436a)

-   -   Post the above two steps, MultiSSO V2 will be enabled and V2 Installation Exits will become active, please refer the screenshot :

![](/sys_attachment.do?sys_id=5178e9dc47d9f110b6d8aa25126d4304)

-   Navigate to your Identity Provider record, and perform 'Test connection'. If **Test Connection** is successful, the upgrade is done.
