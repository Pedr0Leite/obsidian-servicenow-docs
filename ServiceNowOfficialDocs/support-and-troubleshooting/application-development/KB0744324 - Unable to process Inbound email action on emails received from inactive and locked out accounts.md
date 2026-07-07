---
title: "Unable to process Inbound email action on emails received from inactive and locked out accounts"
aliases:
  - KB0744324
tags:
  - servicenow
  - support-kb
  - inbound-email-actions
  - locked-out-accounts
  - inactive-users
  - system-properties
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744324
kb_number: KB0744324
last_modified: 2026-05-06
---

## Unable to process Inbound email action on emails received from inactive and locked out accounts

  

### Issue

When emails are sent to the instance from a user account which is -

a) Inactive - The syslog\_email entry for the received email indicate - 'Skipping <Inbound Action>, User <User Name> with email <User email ID> is inactive

b) Locked Out - The syslog\_email entry for the received email indicate - 'Skipping <Inbound Action>, User <User Name> with email <User email ID> is locked out

c) Inactive and Locked Out - There are syslog\_email entries for inactive and locked out user as above.

  

and therefore the inbound actions do not process the emails. 

### Release

Applicable to all releases

### Cause

This is based on how inbound actions work when emails are received and processed by the instance.

  

When an email is received by the instance, the system searches for a matching email record in the sys\_user table. If found, ServiceNow instance then impersonates as that user and runs the relevant inbound action steps. If the user is not found, then the instance uses the Guest user to complete this action.

### Resolution

**Case 1: When the user is inactive**

When the user is inactive, then the inbound email actions will NOT process for the user. The log entry will indicate inbound action getting skipped. 

**Case 2: When the user is Locked Out**

Inbound email actions can be triggered for Locked out users by enabling a system property - glide.pop3.process\_locked\_out . The user must still be active.

Note: Customers are requested to keep in mind the security implications of allowing users from untrusted domains, and why they were locked out before allowing emails from them to trigger inbound email actions.

**Case 3: When the user is Inactive and Locked Out**

Even if the system property from Case 2 above is enabled, the syslog\_email entry will still indicate that the inbound email actions could not be processed because the user is inactive and NOT process for the user. The log entry will indicate inbound action getting skipped.

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0689652 - Troubleshooting users unable to access responsive dashboards|Troubleshooting users unable to access responsive dashboards]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0759218 - Certain fields are visible to non-admin users only when the fields not empty.|Certain fields are visible to non-admin users only when the fields not empty.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0782082 - When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a f|When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a field, need to make to use of ACL script.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0816018 - Admin role does not pass an ACL when Admin Overrides is selected|Admin role does not pass an ACL when Admin Overrides is selected]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ|Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0693349 - Inbound emails received and processed display broken attached images in preview HTML body and in target record activity |Inbound emails received and processed display broken attached images in preview HTML body and in target record activity stream notes]]
