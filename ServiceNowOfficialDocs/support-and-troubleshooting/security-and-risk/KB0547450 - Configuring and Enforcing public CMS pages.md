---
title: "Configuring and Enforcing public CMS pages"
aliases:
  - KB0547450
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547450
kb_number: KB0547450
last_modified: 2025-01-03
---

## Issue

# Overview

* * *

The Content Management System (CMS) plugin is a default ServiceNow application designed to allow administrators to create a custom interface for the ServiceNow platform and ServiceNow applications. When the custom interface is created, a customer may potentially induce a partial CMS outage to the instance if the property glide.ui.cms.enforce\_public\_pages is set to **true** as described in [KB0546756](/kb_view.do?sysparm_article=KB0546756). The following instructions will walk you through how to correctly activate the property without accidentally revoking public access to your CMS pages.

# Identification of potentially problematic CMS pages

* * *

Use the procedure below to identify the existing custom CMS pages on the instance that need to be altered to ensure the correct access is available after the property is enabled.

1\. Log in using the admin role.

2\. In the navigation filter, enter **Content Management.**

3\. Click **Pages**.

4\. Filter the table results as follows:

![](/sys_attachment.do?sys_id=c49a60a6db42b450e515c223059619c3)

5\. Click **Run.**

6\. If any custom CMS pages without a “Content site” exist, they should be found on this page as a result of the previous step. For demonstration purposes, the screenshot below shows a custom page named “Demo\_Custom\_CMS\_Page” with no “Content site”.

![](/sys_attachment.do?sys_id=449a60a6db42b450e515c223059619cf)

7\. Take note of the **Name** and **URL suffix** field values for all the entries identified on the previous step.

8\. Please ignore the **"Clean Login"** entry from the filter results, as this entry does NOT have to be added to the Public pages table as described in the next section.

9\. In addition to the above entries, the **pages** and **references** included in the custom CMS pages have to be added to the **Public Pages** table. Click **View Page** to view the current page and associated pages/references.

![](/3.pngx)

![](/4.pngx)

10\. The above example shows the pages that are included in the custom CMS page: Demo\_Custom\_CMS\_Page. As shown above, all the links/pages shown represent the same table \[kb\_view\], and thus simply adding the table name \[kb\_view\] to the Public Pages module should be sufficient. 

![](/5.pngx)

  

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note: </strong>Once the page is&nbsp;Public, it can be viewed by any unauthenticated individual on the internet. Be certain the public pages do not contain any sensitive data or enable read/write operations by the guest users.&nbsp;</td></tr></tbody></table>

For identified pages that you want to be private

* * *

The previous step showed you how to identify the CMS pages that do not have the “Content Site” field filled in. If you have already advertised these pages as being available and you do not want to associate them with a Content Site then you need to take some actions to appropriately lock them down.

If you do not want to associate these pages with a Content Site but you do want these pages to be private (i.e. not accessible by un-authenticated users) then you should populate the entries in the **“Read roles”** field in the Content page entry, such that only authorized individuals will have access.

The following steps provide an example of a **Private page setup** scenario : A content page with NO content\_site has been advertised as a part of the CMS. Customer admin authorizes only **ITIL** to have access to that page, so the “Read roles” should say **“itil”**.

1\. Log in as a user with the admin role.

2\. In the navigation filter, enter **Content Management.**

3\. Click **Pages**.

4\. Filter the table results as follows:

![](/sys_attachment.do?sys_id=9c9a60a6db42b450e515c223059619dc)

5\. Click **Run.**

6\. If any custom CMS pages without a **Content site** exist, they should be found on this page as a result of the previous step. For demonstration purposes, the screenshot below shows a custom page named “Demo\_Custom\_CMS\_Page” with no “Content site”.

![](/sys_attachment.do?sys_id=589a60a6db42b450e515c223059619e6)

7\. Click the **Demo\_Custom\_CMS\_Page** record. 

8\. Once you are in the page as follows, click on **pencil marker tab** highlighted to expand the selection box.

![](/sys_attachment.do?sys_id=d49aa0a6db42b450e515c22305961902)

9\. Per example above, only **itil** role has to be authorized to view this page. Scroll down to select the **itil** role from the Available section, and add to the Selected section.

10\. Save the record.

For more information, see [Content\_Management\_Security](https://docs.servicenow.com/csh?topicname=c_ContentManagementSecurity.html&version=latest) in the product documentation.

  

Adding a Public Page 

* * *

Use the procedure below to create Public Page entries for CMS pages that were identified as having no “Content Site” field value.

1\. Log in as a user with the admin role.

2\. In the navigation filter, enter **Public Pages.**

![](/11.pngx)  
  

<table class="noteTable" style="height: 42px;" width="741" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note: </strong>If the Public Pages module is not enabled, follow&nbsp;step 2 in the product documentation page named <a href="https://docs.servicenow.com/csh?topicname=t_MakeAPagePublic.html&amp;version=latest" target="_blank" rel="noopener noreferrer">Making_a_Page_Public</a>.</td></tr></tbody></table>

  

3\. Click **Public Pages**.

4\. Add all the **Public CMS pages** identified in the previous section to the **Public Pages** table. Make sure that for every CMS page identified, both **Name** and **URL suffix** are added to the table in separate entries (unless, of course, they have the same value then only one entry is needed).

![](/22.pngx)  

**Example:** A content page containing a self-service portal should be ideally accessible without logging into the instance. Therefore, this content page has to be added in the public pages table. Example content page available by default: Portal - Common Answers.
