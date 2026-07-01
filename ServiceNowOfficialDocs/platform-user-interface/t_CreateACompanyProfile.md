---
title: Create a company profile
description: To customize the ServiceNow instance for your company, you can enter information such as contact phone numbers, street address, and additional notes. You can also customize the company logo and banner text your end users see at the top of each page.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/t\_CreateACompanyProfile.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [User interface configuration, Working in Core UI, Configure UIs and portals, Configure user experiences]
---

# Create a company profile

To customize the ServiceNow instance for your company, you can enter information such as contact phone numbers, street address, and additional notes. You can also customize the company logo and banner text your end users see at the top of each page.

## Before you begin

Role required: admin

## About this task

Much of the company information that you enter is [[onboarding-modals-reference|reference]] information that administrators can view. All users see the company logo and banner text. To see all company information, verify that you are in the **My Company** view.

\[Omitted image "MyCompanyView.png"\] Alt text: Select the My Company view

## Procedure

1.  Navigate to **All** &gt; **System Properties** &gt; **My Company**.

2.  To change the banner text, update the **Banner text** field.

3.  Select the **Primary** check box to indicate if this company is the primary company.

    If needed, [configure the form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/configure-form-layout.md) to add the **Primary** check box. Designate only one company in your system as the primary company.

4.  To upload your company logo, select **Click to add** or **Update** beside **UI16 Banner Image**.

    If you leave the banner image blank in [[c_UI16|Core UI]] \(UI16\), the system uses the image used in **System Properties** &gt; **Basic Configuration** &gt; **Banner image** \[glide.product.image\] as the default.

5.  Click **Choose file** and select the file, and then click **OK**.

    To use an image URL instead of a file on your hard drive, enter the URL in the file upload window.

6.  Complete the form with remaining company information.

7.  Click **Update**.


-   **[[c_CustomizeTheBannerLogoLink|Banner logo link]]**  
Properties are available to control the URL and target frame used when clicking the banner logo.
-   **[[t_CustomizeTheLogoInSysProps|Customize the banner logo in Core UI]]**  
Use the **glide.product.image** and **glide.product.description** properties to change the banner logo and description in Core UI.
-   **[[customize-favicon|Customize the favicon]]**  
Use the **glide.product.icon** property to change the icon that appears in bookmarks and the browser address bar.
-   **[[c_ExamplesOfHowToModifyTheBanner|Examples of how to modify the banner]]**  
There are various ways that you can modify the banner on your instances.
-   **[[c_ModifyTheBanner|Modify the banner]]**  
The banner is displayed at the top of the page and is rendered using certain system properties.

**Parent Topic:**[[p_NavigationAndUIConfiguration|User interface configuration]]

## Related

- [[c_CustomizeTheBannerLogoLink|Banner logo link]]
- [[t_CustomizeTheLogoInSysProps|Customize the banner logo in Core UI]]
- [[customize-favicon|Customize the favicon]]
- [[c_ExamplesOfHowToModifyTheBanner|Examples of how to modify the banner]]
- [[c_ModifyTheBanner|Modify the banner]]
- [[p_NavigationAndUIConfiguration|User interface configuration]]
- [[onboarding-modals-reference|Reference]]
- [[c_UI16|Core UI]]
