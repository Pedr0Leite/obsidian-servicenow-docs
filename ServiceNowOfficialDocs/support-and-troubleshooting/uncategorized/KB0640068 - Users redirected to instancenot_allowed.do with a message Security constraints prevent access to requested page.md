---
title: "Users redirected to <instance>/not_allowed.do with a message \"Security constraints prevent access to requested page\""
aliases:
  - KB0640068
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0640068
kb_number: KB0640068
last_modified: 2025-09-10
---

## Users redirected to /not\_allowed.do with a message "Security constraints prevent access to requested page"

  

### Issue

Security checks are in place to avoid redirecting to external sites, if SSO is not correctly configured, the users are not redirected to the Identity provider but to the '/not\_allowed.do' page.

### Cause

When logging in by Single Sign-on (SSO), the system checks the redirected URL is part of the defined Identity provider or IdP records on the instance. If a matching URL is not found, the instance redirects to **/not\_allowed.do**.

### Resolution

Please ensure the defined IdP contains the redirection URL as part of the IdP records.

To disable the validation, which is _not_ recommended, administrators can create or define the following system property:

<table class="MsoNormalTable" style="width: 335px; background: whitesmoke; border-collapse: collapse; border: none; height: 78px;" border="1" cellspacing="0" cellpadding="0"><tbody><tr style="height: 15.0pt;"><td style="border-top: none; border-left: none; border-bottom: 1pt solid #e0e0e0; border-right: 1pt solid #e0e0e0; padding: 6pt; width: 230.625px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 10.5pt; font-family: SourceSansPro, serif; color: #2e2e2e;">Name</span></strong></p></td><td style="border-top: none; border-left: none; border-bottom: 1pt solid #e0e0e0; border-right: 1pt solid #e0e0e0; padding: 6pt; width: 69.7188px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 10.5pt; font-family: SourceSansPro, serif; color: #2e2e2e;">Value</span></strong></p></td></tr><tr style="height: 15.0pt;"><td style="border-top: none; border-left: none; border-bottom: 1pt solid #e0e0e0; border-right: 1pt solid #e0e0e0; background: white; padding: 6pt; width: 230.625px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 10.5pt; font-family: SourceSansPro, serif; color: #2e2e2e;">glide.authenticate.auth.validate.url</span></strong></p></td><td style="border-top: none; border-left: none; border-bottom: 1pt solid #e0e0e0; border-right: 1pt solid #e0e0e0; background: white; padding: 6pt; width: 69.7188px;"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 10.5pt; font-family: SourceSansPro, serif; color: #2e2e2e;">false</span></p></td></tr></tbody></table>
