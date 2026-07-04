---
title: "Following a link to a survey redirects to a null page after SSO authentication"
aliases:
  - KB0748137
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748137
kb_number: KB0748137
last_modified: 2024-04-07
---

## Following a link to a survey redirects to a null page after SSO authentication

  

### Issue

# Symptoms

When a user follows a link to a survey (for example, by clicking the link in an email) and the instance has SSO authentication enabled, after authenticating, they are redirected to a null page, Page Not Found

![](/sys_attachment.do?sys_id=f4eef0e2db0ab450e515c223059619b8)

The URL might be something like <_instanceName_\>.service-now.com/nav\_to.do?uri=%2Fnull

# Release

All releases.

# Cause

When SSO authentication is enabled, if the assessment\_take2 page is a public page, the link to the survey won't work.

# Resolution

Make the assessment\_take2 page a non-public page:

1\. In the Application Navigator, enter sys\_public.list  
2\. Filter the Page column for starts with assessment.  
3\. You should see 2 matching records, one for assessment\_take2 and another for assessment\_thanks.

![](/sys_attachment.do?sys_id=b8eef0e2db0ab450e515c223059619bd)

4\. Modify the Active value for the assessment\_take2 public page to false.  
5\. Leave the Active value true for the assessment\_thanks public page.
