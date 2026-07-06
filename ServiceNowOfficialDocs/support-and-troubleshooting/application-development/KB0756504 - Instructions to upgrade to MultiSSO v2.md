---
title: "Instructions to upgrade to MultiSSO v2"
aliases:
  - KB0756504
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756504
kb_number: KB0756504
last_modified: 2026-03-30
---

## Text

The ServiceNow Multi-SSO plugin uses the latest version of the OpenSAML library. The pre-New York version of the plugin (MultiSSO v1) is deprecated. The latest plugin enhances security and has more features, like Assertion encryption support, IDP-initiated Single Logout (SLO).

  

The existing resources like Script Includes or Installation Exits will also be updated during this upgrade. If you are upgrading after having done any customizations to these resources, these instructions will guide your upgrade to the updated Multi-SSO plugin. The resources are listed in Annexure A at the end of this article.

See [Manual upgrade instructions for MultiSSO V2 for CSE](/kb?id=kb_article_view&sysparm_article=KB0778202 "Manual upgrade instructions for MultiSSO V2 for CSE") on how to customizations them compatible with the new Multi-SSO plugin.

### Target Audience  
**Any instance administrator upgrading to later release noticing Multi-SSO not being upgraded to the latest v2.**

Plugin Name - **Integration - Multiple Provider Single Sign-On Installer (com.snc.integration.sso.multi.installer)**

To verify if you need to upgrade the plugin:

-   Navigate to **All Properties (sys\_properties.list)**.
-   Search for the Property by name – '**_glide.authenticate.multissov2\_feature.enabled_**'.

If this property is **not found** in the instance or the property value is set to **false**, then it effectively means that you have not upgraded the Multi-SSO plugin to the latest version and you need to upgrade it.

### Upgrade Path for the Multi-SSO plugin

After the instance upgrade is complete, follow the below instructions before starting the MultiSSO plugin upgrade:

1.  1.  If you have **not** made any changes to the Multi-SSO or E-signature Plugin-related files (e.g. script includes, installation exits etc), then go directly to the section - **Steps to Upgrade the Multi-SSO plugin**.  
          
        **NOTE**: If there are any PRB fixes done by ServiceNow, those will be taken care of automatically during the upgrade.
    2.  **How to check for changes:**  
        1.  Go to the Filter Navigator and search for "**Multi-Provider SSO**"
        2.  Navigate to "Administration" -> "Installation Exits".  
            ![Check for Multi provider-SSO changes](/sys_attachment.do?sys_id=39eb9040930c0318d9743f986cba10dd "Installation_exits")  
              
              
            
        3.  Click on the Update Personalized List (GEAR ICON) and add "Updated by" to the selected list.  
              
            ![Update Personalised List in Multi-provider SSO](/sys_attachment.do?sys_id=f5ebd040930c0318d9743f986cba1013 "Installation_exists_popup")  
              
            
        4.  If you only see Admin or maint under the Updated By column, then there are no customizations in Installation Exits.
        5.  Navigate to "Administration" -> "Single Sign-On Scripts".
        6.  Add the "Updated By" to the selected list similar to Step c.
        7.  If you only see Admin or maint under the Updated By column, then there are no customizations in Single Sign-On Scripts.  
              
            You are good to go if there are **no customizations** in Installation Exits and Single Sign-On Scripts. Please proceed to **Steps to Upgrade the Multi-SSO plugin.  
              
            **
    3.  If you have made any changes or customizations to either the Multi-SSO or E-signature plugin-related files, then refer to the NY release notes ([KB0778203 - Customization support of MultiSSOv2](/kb_view.do?sysparm_article=KB0778203 "KB Article")) for Out of the Box available customization samples and check if you have done similar customizations.

-   -   -   Migrate all the customization-related changes into the latest version of Installation exits and SSO scripts as specified in the KB article. After you apply these changes, go to **Steps to Upgrade the Multi-SSO plugin.** _If you are facing any issues with customizations, contact the ServiceNow support team for assistance._

### Steps to Upgrade the Multi-SSO plugin

Ensure you are logged-in as local admin user, while executing the steps below.

**Step 1:** Disable the Multiple Provider SSO Property on the Multiple Provider SSO Properties page.

-   Navigate to All properties (**sys\_properties.list**) 
-   Search the property with the name **glide.authenticate.multisso.enabled** and Update the value as **false** and stay on the properties page.  
      
    ![Steps to disable the Multiple Provider SSO Property](/sys_attachment.do?sys_id=7deb9040930c0318d9743f986cba10c8 "sys_property_1")

**  
Step 2:** Search for MultiSSO v2 Property (**glide.authenticate.multissov2\_feature.enabled**). If this system property **glide.authenticate.multissov2\_feature.enabled** is not present in the instance, create the property with the following details. If the property is already present, then enable the property and stay on the properties page.

-   Name – _glide.authenticate.multissov2\_feature.enabled_
-   Type – true | false
-   Value – true  
      
    ![Search for MultiSSO v2 Property](/sys_attachment.do?sys_id=c6ebd040930c0318d9743f986cba103c "sys_property_2")

**  
Step 3:** Re-Enable the Multiple Provider SSO Property.

-   Navigate to All properties (**sys\_properties.list**) 
-   Search the property with the name **glide.authenticate.multisso.enabled** and Update the value as **true**.  
      
      
    

**  
Step 4:** Test the SSO Login in the Incognito browser window to test the IDP Configuration. If the login is successful, then your instance is upgraded successfully. If the login fails, then check the steps below.

![Test the SSO Login in the Incognito browser window to test the IDP Configuration](/sys_attachment.do?sys_id=bdeb9040930c0318d9743f986cba10ab "sys_property_3")

**Step 5:** **Test the Connection** to verify the IDP Configuration.

-   Enter the IDP user login credentials in the Test Connection popup.

**Note** - Please ensure your Identity Provider record which you are testing has the correct configuration settings before clicking Test Connection. For example, if your IDP endpoint recently changed its connection requirements please confirm whether the **Encrypt Assertion** box needs to be enabled.

![Test the Connection to verify the IDP Configuration](/sys_attachment.do?sys_id=86ebd040930c0318d9743f986cba1069 "sys_property_4")

**Step 6:** If **Test Connection** is successful, then save the Identity Provider form. **You have successfully upgraded to MultiSSO v2.** If the Test Connection still fails, then check the **Troubleshooting** section below.

-   A successful test connection means the IDP configuration in ServiceNow is able to successfully connect with the given IDP and both Login and Logout operations are working properly. Please note that you cannot activate the IdP configuration until you have a successful test connection. If the test fails, you can update to save your configuration information, but you cannot activate this configuration.
-   The Successful Test Output should look like the screenshot given below :  
      
    ![SSO login test results](/sys_attachment.do?sys_id=f5ebd040930c0318d9743f986cba1034 "sso_test_1")

**Note** - This disabling and re-enabling step is performed to automatically correct the status of MultiSSO Installation Exits (IEs) according to the current version of the MultiSSO.  
  
  

### Troubleshooting

-   Please follow the below steps to verify the IDP configuration.  
    -   For each Identity Provider record listed, verify that the configuration is up-to-date and contains the required settings to connect to the Identity Provider. For example, if required, ensure that "Auto Redirect IdP" is enabled."
    -   Verify the Multi-SSO Installation Exits status:  
        -   Once the Multi-SSO plugin is re-enabled, the new Installation Exits will be active.
        -   Navigate to **Multi-Provider SSO -> Administration -> Installation Exits**.
        -   Your instance should reflect the MultiSSO Installation Exits status similar to the one given below:  
              
            

-   -   ![Troubleshooting steps to verify the IDP configuration](/sys_attachment.do?sys_id=f1ebd040930c0318d9743f986cba100b "installation_exits_1")
    -   -   Navigate to **Multi-Provider SSO -> Identity Providers.**
        -   Verify that the script name corresponding to **Single Sign-On** Column for all your SAML Identity Provider configurations record is '_**MultiSSOv2\_SAML2\_custom**'_ similar to the below screenshot.  
              
            ![Verifying that the script name corresponding to Single Sign-On Column](/sys_attachment.do?sys_id=79eb9040930c0318d9743f986cba10c0 "idp_1")
        -   If the instance has a different configuration, then please contact ServiceNow customer support indicating the above issue.Verify the Single Sign-On Script Name:

### Annexure A

#### List of Installation Exits that can be checked for customization:

-   MultiSSO
-   MultiSSOLogout

#### List of Script Includes that can be checked for customization:

-   MultiSSO\_ClientHelper
-   MultiSSO\_ClientHelperUI
-   MultiSSO\_SAML2\_Update1
-   MultiSSO\_SAML2\_UserProvisioning
-   MultiSSO\_SAMLMetaDataHelper
-   SSO\_Helper
-   SAML2\_update1
-   ESignatureUtils
-   SAML2\_update1\_esig
