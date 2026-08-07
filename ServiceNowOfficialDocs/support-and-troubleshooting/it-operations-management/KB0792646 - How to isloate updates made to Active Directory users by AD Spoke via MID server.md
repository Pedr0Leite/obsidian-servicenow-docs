---
title: "How to isloate updates made to Active Directory users by AD Spoke via MID server"
aliases:
  - KB0792646
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792646
kb_number: KB0792646
last_modified: 2024-04-07
---

## Issue

The Active Directory Spoke for IntegrationHub plugin can be utilized to set workflows in place to update user information within your Active Directory from ServiceNow. The Spoke can work with a MID server to make changes to user data within AD.

Though the updates are made through 'outputs' via the MID Server, the output itself does not contain specific user data which is being updated, so it may not be apparent which ECC queue output is tied to a user being updated within AD.

## Resolution

To be able to map user updates to the correct ECC Queue outputs, you can correlate the correct time of user updates via the MID logs to the ECC queue updates. To get the time of the user updates., please do the following:

-   Log in to your instance as an admin
-   Navigate to MID Server > Servers
-   Open the relevant MID Server record.
-   Under Related Links, click Grab MID Logs.
-   Open the logs once downloaded
-   Search for the user\_name of the user in question who got updated.
-   Once found, it should have the date/time of the update to the milliseconds in the beginning of the line
-   Keep track of the time with the milliseconds (keep in mind that this time will be unique to the timezone of the machine which is hosting the MID server. This may differ from the timezone of your instance. Please account for the differences before moving on to the next step.
-   Find the corresponding time to the millisecond within the ECC queue. You will now have the ECC queue output which is tied to the user update within your AD.

## Additional Information

This information may be useful when troubleshooting what flows may have caused certain user updates in AD from your ServiceNow instance.
