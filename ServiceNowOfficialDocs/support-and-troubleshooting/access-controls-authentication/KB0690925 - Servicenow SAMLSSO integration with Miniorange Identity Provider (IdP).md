---
title: "Servicenow SAML/SSO integration with Miniorange Identity Provider (IdP)"
aliases:
  - KB0690925
tags:
  - servicenow
  - support-kb
  - saml
  - sso
  - idp
  - authentication
  - miniorange
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690925
kb_number: KB0690925
last_modified: 2026-01-06
---

## Servicenow SAML/SSO integration with Miniorange Identity Provider (IdP)

  

### Issue

This article shows steps how to set up SSO in ServiceNow with 'MiniOrange', an Identity provider (IdP).

**1 - Create a Free Trial account with MiniOrange**

  ![miniorange](sys_attachment.do?sys_id=df23e745975272d4f03d739c1253af88)

[https://www.miniorange.com/businessfreetrial](https://www.miniorange.com/businessfreetrial)

**2 - Login with the newly created user account in Miniorange**

Click on **Users** in left menu, this is where you see the newly created username. You can also add new users, either manually or else they can be imported.

![](/sys_attachment.do?sys_id=e7232b45975272d4f03d739c1253af57)

![](/sys_attachment.do?sys_id=23232b45975272d4f03d739c1253af5b)

**3 - Create an application**

Click on **Apps > Add Application** as shown in below:

 ![](/sys_attachment.do?sys_id=63232b45975272d4f03d739c1253af32)

Click on **SAML/WS-FED** among available options

![](/sys_attachment.do?sys_id=ab232b45975272d4f03d739c1253af35)

Search for **ServiceNow** and you see an app named **Servicenow (SAML)**

![](/sys_attachment.do?sys_id=ab232b45975272d4f03d739c1253af45)

Click on **Servicenow (SAML)** app:

![](/sys_attachment.do?sys_id=e3232b45975272d4f03d739c1253af49)

Fill in all below details in form which might be available in different tabs as shown in above image e.g. Basic Settings, Attribute Mapping, Login Policy, Advanced Settings etc:

**Custom Application Name :** type any name/string 

**\*SP Entity ID or Issuer :** [https://xxxxx.service-now.com](https://emprathenor5.service-now.com)

**\*ACS URL :** [https://xxxxx.service-now.com/navpage.do](https://emprathenor5.service-now.com)

**Single Logout URL :** [https://xxxxx.service-now.com](https://emprathenor5.service-now.com)/external\_logout\_complete.do

**Name ID :** Username / E-Mail Address (Field value should match sys\_user table field in ServiceNow for Authentication)

**Group Name :** select DEFAULT

**\*Policy Name :** type any name/string

**\*First Factor Type :** select PASSWORD

Click on **Save** and it might redirect you to App list

![](sys_attachment.do?sys_id=9b23e745975272d4f03d739c1253afec)

![](sys_attachment.do?sys_id=d323e745975272d4f03d739c1253aff0)

In app list, click Select (last column in app list) for **Servicenow (SAML)** app created above and select **Metadata** option as shown below**:**

![](/sys_attachment.do?sys_id=2f232b45975272d4f03d739c1253af4c)

If you see below image with a warning, it is very likely that **Show Metadata Details** and copy **Metadata URL** may or may not work here therefore, please click **Back to My Apps** and select Metadata option again as in previous step:

![](/sys_attachment.do?sys_id=67232b45975272d4f03d739c1253af50)

Please select either of **a) Copy Metadata URL** or **b) Download Metadata,** ServiceNow supports both while configuring a new IdP:

![](/sys_attachment.do?sys_id=af232b45975272d4f03d739c1253af53)

**4 - Configure MiniOrange settings in ServiceNow Instance**

**Create a new Identity Provider in ServiceNow**

Go to **Multi-Provider SSO > Identity Providers**

![](/sys_attachment.do?sys_id=23232b45975272d4f03d739c1253af6b)

Click **New** and select **SAML**

![](/sys_attachment.do?sys_id=af232b45975272d4f03d739c1253af6e)

![](/sys_attachment.do?sys_id=2b232b45975272d4f03d739c1253afd9)

Clicking on **SAML** opens below window and asks to import IdP metadata:

Please enter the **Metadata** **URL/XML** collected from Miniorange in previous steps:

![](sys_attachment.do?sys_id=9f232b45975272d4f03d739c1253af1a)

Click on **Import** and ServiceNow creates a new IdP record importing all the necessary details from given Metadata. The IdP certificate is also linked with the newly created IdP in ServiceNow and this is how it looks:

**Note** - Please use IdP metadata URL/XML only to import and avoid filling field values manually which is prone to errors.

![](sys_attachment.do?sys_id=0b23e745975272d4f03d739c1253af4d)

Click on the **Test Connection** button in the IDP form above and it opens a new window.

Enter MiniOrange **Username/Email** and **Password** as created in **Step 1**

![](sys_attachment.do?sys_id=df23e745975272d4f03d739c1253af52)

When SSO Test Connection is successful, you see a screen like below.

**NOTE -** It may requires removing **Identity Provider's SingleLogoutRequest** field value on IdP record for a successful Test Connection like belo: 

![](sys_attachment.do?sys_id=ab232b45975272d4f03d739c1253afe0)

Please click on **Activate** to activate above IdP

**5- Enable SSO in ServiceNow**

-   In the Filter navigator, Go to **Multi-Provider SSO** > **Administration** > **Properties**
-   Click on **Properties**
-   Set **Enable multiple provider SSO** property checkbox as True and click on Save.

![](/sys_attachment.do?sys_id=63232b45975272d4f03d739c1253afdd)

All the SSO configurations are complete now and user(s) should be able to login via SSO. Just in case, a user cannot login via SSO, please enable SSO debug (above screenshot) and check the logs. Make sure the login user does exist in ServiceNow as well as in MiniOrange application.

If for some reason, user still cannot login via SSO, please open a new case with ServiceNow Technical Support and an engineer will assist you accordingly.

### Release

All releases

### Resolution

None

## Related

- [[KB0539112 - Troubleshooting SAML or SSO issues in ServiceNow]] - master SAML/SSO troubleshooting checklist
- [[KB0538763 - Determining if the SAML certificate is incorrect]]
- [[t_CreateUpdateIdentityProvider]] - official docs on creating/updating an Identity Provider
- [[t_ActivateMultipleProviderSSO]] - official docs on activating Multiple Provider SSO

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538763 - Determining if the SAML certificate is incorrect|Determining if the SAML certificate is incorrect]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538765 - Determining if ADFS is receiving a signed request| Determining if ADFS is receiving a signed request]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538768 - Determining if the properties from the source were copied over a target|Determining if the properties from the source were copied over a target]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538769 - Determining if SAML issues are occurring due to customer scripts no longer working after upgrade|Determining if SAML issues are occurring due to customer scripts no longer working after upgrade]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538770 - Determining if the SAML issue is the result of a user being locked out| Determining if the SAML issue is the result of a user being locked out]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0538780 - Determining if the SAML issue is the result of the user having a duplicate record|Determining if the SAML issue is the result of the user having a duplicate record]]
