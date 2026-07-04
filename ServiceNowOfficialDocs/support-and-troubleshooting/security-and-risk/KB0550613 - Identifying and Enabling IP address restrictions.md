---
title: "Identifying and Enabling IP address restrictions "
aliases:
  - KB0550613
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550613
kb_number: KB0550613
last_modified: 2026-06-17
---

## Issue

IP address restrictions are designed to block any and all HTTP/S access to the instance unless the user is coming from an inclusion listed IP address. Depending on the nature of the vulnerability, the current configuration acts as mitigation or compensating control for the vulnerabilities identified on the platform.

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Note</strong>: or customers who need to understand the broader scope of the instance consumer IP address space, section 1 should be followed before section 2.</td></tr></tbody></table>

### Identifying the IP addresses accessing the ServiceNow instance

Use the following steps to identify IP addresses.

1.  Log in using the admin role.
2.  Navigate to **System Logs >** **Transactions (All user)**.
3.  Edit the filters as necessary.
4.  Click the gear symbol ![](/sys_attachment.do?sys_id=4359e8eedb02b450e515c223059619c1).
5.  In the slushbucket, add the column **IP address** from the **Available** column on the left side to the **Selected** column on the right side.
6.  Click **OK**.
7.  Click **Run**.  
    You should now be able to see the **IP address** for each of the associated actions for each time period.  
      
    For more information, see [Viewing System Logs - Transactions](https://docs.servicenow.com/csh?topicname=transaction-logs-2.html&version=latest "Viewing System Logs - Transactions") in the product documentation.

### Enabling the IP address restrictions on the ServiceNow instance

Use the following steps to enable IP address restrictions.

1.  Log in using the admin role.
2.  Navigate to **System Security >** **IP Address Access Control**.
3.  Click **New**.
4.  In **Type**, select **Allow**.
5.  Enter the **static IP address** or **IP address range** based on the results in the section above ("Identifying the IP addresses accessing the ServiceNow instance").
6.  Click **Submit**.
7.  Click **New**.
8.  In **Type**, select **Deny**.
9.  Enter the IP addresses to deny (for example, from 0.0.0.0 to 255.255.255.255).
10.  Click **Submit**.

For more information, see [IP Range Based Authentication](https://docs.servicenow.com/csh?topicname=c_IPRangeBasedAuthentication.html&version=latest "IP Range Based Authentication") in the product documentation.

### Verify the IP address control setup on the ServiceNow instance

Use the following steps to verify the IP address controls.

1.  Do one of the following:  
    -   use your smartphone to connect via carrier data network  
        or
    -   connect to a network that is not included in the **Allow** list of IP addresses
2.  Open a browser
3.  Enter the instance URL (for example, https://<instance-name>.service-now.com).
4.  Click **Enter**.  
    -   If the page shows an error report with the status: **HTTP Status 403**, the configuration is now complete and the mitigation control has been enabled appropriately
    -   If the page displays anything other than **HTTP Status 403**, such as a Login page or SSO page, then ensure that the **DENY** record is added to the end of the IP address restriction table (as explained in the section above, "Enabling the IP address restrictions on the ServiceNow instance").
