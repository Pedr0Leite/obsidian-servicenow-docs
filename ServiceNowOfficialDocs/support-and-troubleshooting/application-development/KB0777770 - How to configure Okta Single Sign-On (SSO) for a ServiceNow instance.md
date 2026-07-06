---
title: "How to configure Okta Single Sign-On (SSO) for a ServiceNow instance"
aliases:
  - KB0777770
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0777770
kb_number: KB0777770
last_modified: 2026-01-29
---

## How to configure Okta Single Sign-On (SSO) for a ServiceNow instance

  

### Summary

Configure Okta as a SAML 2.0 identity provider for Single Sign-On (SSO) on a ServiceNow instance. This article outlines the setup process for both the Okta and ServiceNow configurations.

**Note**: ServiceNow does not endorse any specific identity provider. Instructions for Okta configuration may change based on updates made by Okta. For current Okta documentation, refer to Okta's official support resources.

### Release

All supported releases

### Instructions

### Configure Okta

1.  Sign up for an Okta developer account at [https://developer.okta.com/signup/](https://developer.okta.com/signup/).
2.  Log in to Okta and switch to **Classic UI (Developer Console > Classic UI)**.
3.  Go to the admin dashboard: https://<okta\_account>-admin.okta.com/admin/dashboard
4.  Select **Add Application** > **ServiceNow UD**.
5.  Configure the application settings:
    -   **General** > **Base URL**: Enter https://<instance\_name>.service-now.com
    -   **Sign On**: Select SAML 2.0 (use defaults for other settings)
6.  Save the configuration.
7.  Select **Identity Provider** **metadata** and save the URL. You will need this URL when configuring ServiceNow.
8.  Create a test user in Okta:
    -   Go to **Directory** \> **People**.
    -   Create a new user with a user name and password.
9.  Assign the user to the ServiceNow application:
    -   Open the ServiceNow app you created.
    -   Go to **Assignment** \> **Assign** \> **Assign to People**.
    -   Select the user you created.

### Configure ServiceNow

#### Activate the Multi-Provider SSO plugin

1.  Go to **System Definition** > **Plugins**.
2.  Search for and activate the **Integration - Multiple Provider Single Sign-On Installer** plugin.
3.  Go to **Multi-Provider SSO** > **Properties**.
4.  Enable the following properties:
    -   Enable multiple provider SSO
    -   Enable debug logging for the multiple provider SSO integration

#### Create a matching user

Create a user in ServiceNow that matches the user you created in Okta. The email address in the User \[sys\_user\] record must match the email configured for the Okta user.

#### Import the identity provider metadata

1.  Go to **Identity Providers** > **New**.
2.  Select **SAML**.
3.  Select **Import Identity Provider Metadata**.
4.  Enter the metadata URL you saved from Okta.

### Configure Single Logout (optional)

Single Logout requires certificate configuration on both Okta and ServiceNow. Choose one of the following options:

#### Option 1: Use your own certificate

1.  Upload your certificate to Okta in the application setup.
2.  Upload the same certificate to the Certificates \[sys\_certificate\] table in ServiceNow.
3.  In Okta, select **Enable Single Logout**.

#### Option 2: Use the default ServiceNow certificate

1.  In Okta, select **Enable Single Logout**.
2.  Follow steps 1-5 in [Steps to migrate from expiring SAML 2.0 SP Keystore to new Keystore](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994948) to configure the correct SHA256 certificate in the system properties. See the KB article for currently valid certificates.
3.  On the Identity Provider record in ServiceNow, select **Sign LogoutRequest**.
4.  Enter the following values:
    -   **Signing Key Alias**: saml2sp
    -   **Signing Key Password**: saml2sp
5.  Select **Generate Metadata**.
6.  Copy the x509 certificate from the metadata screen.
7.  Format the certificate with BEGIN and END markers:  
      
    \-----BEGIN CERTIFICATE-----  
    MIIDoTCCAomgAwIBAgIERs1yFjANBgkqhkiG9w0BAQsFADCBgDELMAkGA1UEBhMCVVMxCzAJBgNV  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    \============================================================================  
    W7GRabHJ8Zv5k/9f45/9F8l/9+v8g+OaqEdQuAdymHbeFQ732vd/4MuJWHylQGcyQz7ytJUqr7j4  
    epX6Li/sQdXGaLxLM+rEKFMY7uB/  
    \-----END CERTIFICATE-----  
      
    
8.  In Okta, go to the advanced options and select **Upload Certificate**.
9.  Upload the certificate file.  
    ![](/sys_attachment.do?sys_id=e5e680f047f6fe54343d8b69736d4393 "Capture6.PNG")
10.  Select **Enable Single Logout**.

**Note**: If you receive an invalid certificate error, contact Okta Support to verify they accept the ServiceNow default certificate.

### Test the configuration

1.  On the Identity Provider record, select **Test Connection**.
2.  Verify the connection is successful.
3.  Activate the Identity Provider record.
