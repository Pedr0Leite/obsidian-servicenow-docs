---
title: "Software Asset Management [sn_itam_samp] Store App Update Not Available in Production"
aliases:
  - KB3015123
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3015123
kb_number: KB3015123
last_modified: 2026-05-12
---

## Software Asset Management \[sn\_itam\_samp\] Store App Update Not Available in Production

  

### Issue

 

The Software Asset Management store app \[`sn_itam_samp`\] shows no option to update to the latest version in Application Manager on a production instance, even though an update is available and can be applied on sub-production instances.

### Symptoms

 

-   Navigating to **Application Manager** and searching for `sn_itam_samp` shows the app is on an earlier version, but no option to upgrade to the latest compatible release is present.
-   The upgrade option is available on sub-production instances but not on the production instance.
-   The latest compatible version of `sn_itam_samp` can be confirmed on the ServiceNow Store.

### Facts

 

-   Software Asset Management \[`sn_itam_samp`\] is a free app in the ServiceNow Store, but it must still be explicitly claimed by clicking the **Get** button on its store page to obtain the entitlement required for upgrades.
-   Without this entitlement, the upgrade option does not appear in Application Manager on the production instance.

### Release

All Releases

### Cause

 

The **Get** button on the Software Asset Management \[`sn_itam_samp`\] application page in the ServiceNow Store has not been clicked for the production account. Until the entitlement is claimed through the Store, the upgrade option does not appear in Application Manager on the production instance.

### Resolution

 

Claim the entitlement for `sn_itam_samp` in the ServiceNow Store, then sync Application Manager on the production instance.

1.  Log in to the [ServiceNow Store](https://store.servicenow.com) with the account associated with your production instance.
    
2.  Navigate to the [Software Asset Management application page](https://store.servicenow.com/store/app/d4d92f621b246a50a85b16db234bcb25) in the Store.
    
3.  Click the **Get** button and follow any prompts to claim the entitlement.
    
4.  Return to Application Manager on your production instance. If the upgrade option is still not visible, click **Sync now** from the Application Manager home page, then check again.
    

**Note:** This entitlement step is required even though `sn_itam_samp` is a free app. Sub-production instances may show the upgrade option without it, which is why the behavior differs between environments.

### Related Links

 

[Software Asset Management — ServiceNow Documentation](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/software-asset-management2/concept/sam-landing-page.html)

[Software Asset Management — ServiceNow Store](https://store.servicenow.com/store/app/d4d92f621b246a50a85b16db234bcb25)
