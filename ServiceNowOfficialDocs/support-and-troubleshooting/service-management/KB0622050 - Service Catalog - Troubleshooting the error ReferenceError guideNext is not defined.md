---
title: "Service Catalog - Troubleshooting the error \"ReferenceError: guideNext is not defined\""
aliases:
  - KB0622050
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622050
kb_number: KB0622050
last_modified: 2024-04-07
---

## Service Catalog - Troubleshooting the error "ReferenceError: guideNext is not defined"

  

### Issue

Service Catalog - Troubleshooting the error "ReferenceError: guideNext is not defined"

Problem

* * *

In the Service Catalog Order Guide, the user receives the following error in the Google Chrome or Mozilla Firefox browser developer tools when they click the **Next** UI button: **ReferenceError: guideNext is not defined**

This happens when an instance is upgraded from Eureka (or earlier) to Fuji or later releases.

Symptoms

* * *

The following symptoms are seen on the Service Catalog when replicating the issue:

-   Order Guide not going to the Choose Options page after clicking **Next**
-   Order Guide showing the **Next** button instead of the Choose Options page
-   **ReferenceError: guideNext is not defined** shown in the Developer Tools on Google Chrome and Mozilla Firefox

Cause

* * *

The cause of the issue is with the UI page **com.glideapp.servicecatalog\_cat\_item\_guide\_view** being modified in Eureka, or a previous release.

When the instance is upgraded to Fuji, or later, release, this causes the code within the UI page above to be skipped during the upgrade to maintain the customization. However this causes the updated code to not be applied to the UI page and therefore causes the error to be thrown.

Resolution

* * *

<table class="noteTable" style="width: 712px;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>:&nbsp;The following change involves modifying the functionality of the Order Guide checkout process. Therefore as a caution, please ensure that the resolution is applied to a sub-production instance and ensure that testing is in progress before applying the change to a production instance.</td></tr></tbody></table>

To provide resolution to the problem, the UI page **com.glideapp.servicecatalog\_cat\_item\_guide\_view** needs to be reverted to Base System. To do this, please perform the following step :

1.  On the ServiceNow instance, find the navigation filter, and select **System UI > UI Pages** 
2.  Search for the UI page name **com.glideapp.servicecatalog\_cat\_item\_guide\_view**
3.  Open up the UI page **com.glideapp.servicecatalog\_cat\_item\_guide\_view**
4.  Ensure that the Versions related list is shown. If not, right-click the header, select **Configure > Related List**, then select **Versions** and click **Save**.
5.  On the Versions Related List, click the record where the source contains the upgraded instance version
6.  On the Version record, select **Related Links > Revert to this version**
7.  Click **OK**
