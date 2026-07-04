---
title: "Customer instance rename policy"
aliases:
  - KB0550841
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550841
kb_number: KB0550841
last_modified: 2026-06-18
---

## Issue

### Restrictions

-   [Our Instance Rename automation](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550695) can only be used for some hosted instances, including production and sub-production. 
-   Demonstration, developer instances, jumpstart instances, and temporary instances **cannot be renamed**.
-   If you need to rename an on-premise instance in Now Support, please follow [KB0551693 - Manage On-Premise Instance - Now Support Service Catalog](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551693). 

### Naming conventions for instances:

-   Production and/or sub-production instances **cannot** contain the word 'demo' or 'pov' or 'poc' as a suffix. 
-   Instance names **can** be alphanumeric, no capital letters (only lower-case).
-   Demonstration, self-hosted (on-premise), Developer, Jumpstart or Temp instances **cannot** be renamed
-   For the OEM instance naming convention, it requires to have “oem” in the name to differentiate from enterprise instance.
-   Instance names **cannot** contain special characters (e.g. $, %, &, -, \*).
-   If the new instance name has 3 characters or below, additional review and approval is required
-   It is recommended that the instance name should not exceed a maximum length of 30 characters.

### Actions needed after requesting rename

1.  If using SSO through the Multi-Provider SSO plugin please check each of your Identity Provider records (Multi-Provider SSO > Identity Provider) and update any URLs in those settings which point to the old instance name.
2.  If inbound WebService Integrations are present, every Inbound (to the SN instance) 3rd Party WebService (including SN ODBC) Integration will have to update the URL pointing to the new instance URL.
3.  When using a Proxy to access the instance which is mapping the instance URL, please update that accordingly pointing to the new one. The same goes for "Vanity URL" if applicable.
4.  When using Edge Encryption Proxy, we strongly advise you to update the Proxy server properties in order to have that to repoint to the right instance URL.
5.  When using MID server note that you will have to change the MID Server configuration to have the MID to point to the new Instance URL.
6.  If using "forwarding rule" on your email infrastructure to forward an email to the ServiceNow instance please change the "forward-to" email address to make it match the new email address.
7.  When using your own email infrastructure will not be affected by the instance rename.

### Rename procedure

1.  Select a valid instance that needs to be renamed and select desired change window from the available slots for Instance Rename
2.  The change window for the instance rename will appear on the change ticket as the planned start and end time.
3.  Beginning at the Planned Start Time the instance will not be available for up to 30 minutes.
4.  Do not run any clones to/from the instance once the rename has started.
5.  New instance and old instance URLs are simultaneously available for the time provided in the request.  
    1.  During this time, cloning functionality is not available.
6.  After the rename, the following settings may require updating:  
    1.  Email settings are reset to the out-of-box values and updated to reflect the new instance name. This change is made after the new instance URL becomes available. Any inbound emails sent to the old instance email may be lost after this change has been made. Customers will likely need to update the email settings in their instance to reflect any previously implemented customization.
    2.  If the customer is using Single Sign-On through the Multi-Provider SSO plugin, they will need to check each of their Identity Provider records (Multi-Provider SSO > Identity Provider) and update any URLs in those settings which point to the old instance name.

## Resolution

N/a
