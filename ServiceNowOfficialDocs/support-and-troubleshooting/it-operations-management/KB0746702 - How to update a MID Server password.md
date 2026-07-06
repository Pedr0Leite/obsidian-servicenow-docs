---
title: "How to update a MID Server password"
aliases:
  - KB0746702
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746702
kb_number: KB0746702
last_modified: 2026-02-06
---

## How to update a MID Server password

  

### Issue

Learn how to update the password for a MID Server service account. After initial installation, changing the MID Server password is a manual process that requires careful timing to minimize downtime.

**Important**: Perform this procedure when the MID Server is not in use. Changing the password in the instance causes the MID Server to go down immediately and may cause unexpected behavior for jobs already running.

**Note**: Review this entire procedure before starting. The final two steps must be completed as quickly as possible.

### Release

All supported releases

### Resolution

#### Step 1: Identify the MID Server and service account

1.  Go to **MID Server** > **Servers**.
2.  Locate the MID Server you want to update.
3.  Note the **Logged in user**, **Host name**, and **Home directory** fields.

**Tip**: You can personalize the list layout to add the Home directory column.

#### Step 2: Update the password in the config.xml file

Complete the following steps for all MID Servers that use this service account:

1.  On the MID Server host, go to the **Home** directory.
2.  Open the config.xml file in a text editor.  
    **Note**: On Windows, use WordPad or another editor that supports Unix line feeds.
3.  Locate the **mid.instance.password** parameter.
4.  Replace the encrypted value with the new password in plain text.  
      
    **Before**:  
    <parameter name="mid.instance.password" secure="true" value="encrypted:7cHG3x8Ssx9m84qHaHlgKQ=="/>  
      
    **After**:  
    <parameter name="mid.instance.password" secure="true" value="newpassword"/>  
      
    **Important**:  
      
    -   Delete the encrypted: prefix. Authentication fails if this prefix remains.
    -   Escape special XML characters. For example, use &amp; for & and &lt; for <. For more information, see [MID Server Configuration](https://docs.servicenow.com/search?q=MID+Server+configuration+XML+password "Docs: MID Server Configuration") in product documentation.
    -   Do not accidentally delete the "/> at the end of the line. Deleting this causes an XML parser error in the MID Server agent log.
5.  Save the file.

**Note: Do not restart the MID Server yet.** The password change does not take effect until you restart, which is the final step.

#### Step 3: Verify the service account configuration

1.  Go to **System Security** > **Users and Groups** \> **Users**.
2.  Open the user record for the MID Server service account (the Logged in user from Step 1).
3.  Verify the following:
    -   The user has the **mid\_server** role.
    -   The user is active.
    -   The user is not locked out.
    -   The User ID matches the value in the config.xml file (case-sensitive).

#### Step 4: Update the password in the instance

**Warning: Complete this step and Step 5 as quickly as possible.** The MID Server goes down immediately when you save the user record.

1.  In the Password field, enter the new password.
2.  Select **Save**.

#### Step 5: Restart the MID Server

On the MID Server host, restart the MID Server service.

-   **Windows**: Use the Services control panel or MMC snap-in.
-   **Linux**: Use the appropriate service command for your distribution.

**Important**: As soon as you update the user record, the MID Server loses connectivity and stops picking up jobs. The instance eventually marks the MID Server as Down. You cannot restart the MID Server from the instance form during this time, even if it still appears as Up. After you restart the MID Server service on the host, the MID Server returns to Up status. After validation completes, the MID Server can accept new jobs.

### Related Links

[Risks of using an LDAP user for MID Server authentication](https://support.servicenow.com/kb_view.do?sysparm_article=KB0746247 "Risks of using an LDAP user for MID Server authentication")
