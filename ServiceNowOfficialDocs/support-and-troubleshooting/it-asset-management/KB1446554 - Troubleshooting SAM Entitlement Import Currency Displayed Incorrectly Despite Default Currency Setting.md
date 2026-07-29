---
title: "Troubleshooting SAM Entitlement Import: Currency Displayed Incorrectly Despite Default Currency Setting"
aliases:
  - KB1446554
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1446554
kb_number: KB1446554
last_modified: 2026-06-04
---

## Issue

The Software Asset Management (SAM) Entitlements workspace displays currency values that differ from the default currency setting configured for your user profile. This occurs despite having a default currency configured in the system.

## Resolution

To ensure that the user's default country is set in the sys\_user table, use the following background script if the user's country code is not in the country list. For instance, if the user wants to view their software expenses and data in the Thai Bath currency in the Software Asset Workspace, run the below script only if the default country code "TH" is not in the sys\_user table's list of countries.

```
var userGR = new GlideRecord('sys_user');
userGR.addQuery('sys_id', 'XXXXXXXXXXXXXXXXXXX');
userGR.query();
if (userGR.next()) {
userGR.setValue('country', 'TH');
userGR.update();
}
```
