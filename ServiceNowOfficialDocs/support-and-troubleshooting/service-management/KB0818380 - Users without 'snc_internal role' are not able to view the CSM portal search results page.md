---
title: "Users without 'snc_internal role' are not able to view the CSM portal search results page"
aliases:
  - KB0818380
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818380
kb_number: KB0818380
last_modified: 2026-05-18
---

## Users without 'snc\_internal role' are not able to view the CSM portal search results page

  

### Issue

When a user without the `snc_internal` role uses any search bar on the CSM portal, a 404 error page appears instead of the expected search results page. When the `snc_internal` role is assigned to the user, the results page displays correctly. This article explains how to make the search results page visible to users with the `snc_external` role.

Steps to Reproduce

1.  Impersonate a CSM portal user who does not have the `snc_internal` role.
2.  Navigate to `https://<instance-name>.service-now.com/csm/`.
3.  Use the search option.
4.  Result: A 404 error appears on the results page at `https://<instance-name>.service-now.com/csm/?id=search&spa=1&q=outlook`.

### Release

### Cause

The Service Portal page `sp_search` was not set to Public on the instance. This page includes the _Faceted Search_ widget, which is called when search results are displayed. In the default base system configuration, the `sp_search` page is set to Public.

To locate the page, navigate to Service Portal > Pages and search for `sp_search`.

### Resolution

1.  Navigate to Service Portal > Pages.
2.  Search for and open the `sp_search` page record.
3.  Select the Public check box.
4.  Select Save or Update.

After setting the `sp_search` page to Public, the search results page becomes accessible to users without the `snc_internal` role and the 404 error is resolved.
