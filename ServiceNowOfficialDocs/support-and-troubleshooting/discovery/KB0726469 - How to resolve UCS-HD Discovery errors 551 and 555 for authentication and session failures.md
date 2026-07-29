---
title: "How to resolve UCS-HD Discovery errors 551 and 555 for authentication and session failures"
aliases:
  - KB0726469
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726469
kb_number: KB0726469
last_modified: 2026-02-17
---

## How to resolve UCS-HD Discovery errors 551 and 555 for authentication and session failures

  

### Issue

Resolve UCS-HD Discovery pattern step failures that return error "551 - Authentication failed" or "555 - Session not found."

### Release

All supported releases

### Cause

The errors are caused by an incorrect user name and password combination or an unavailable API URL path.

The pattern communicates with the UCS device using HTTPS requests. The API URL should be:

https://<ip\_of\_UCS\_device>/nuova

If this URL is not available, communication fails. Per the Cisco UCS Manager XML API Programmer's Guide, this URL must be present for the API to function.

### Resolution

#### **Verify the credential using a POST tool**

You can test the user name and password against the target using a POST tool. Pass the following values to the tool, replacing userName, password, and ip\_of\_UCS\_device with the correct values:

-   **Content/Body:** <aaaLogin inName="userName" inPassword="password" />
-   **ContentType:** application/xml
-   **Charset:** UTF-8
-   **Target:** https://<ip\_of\_UCS\_device>/nuova

#### **Verify the credential using Windows PowerShell**

Open a PowerShell session and run the following command, replacing userName, password, and ip\_of\_UCS\_device with the correct values:

\[System.Net.ServicePointManager\]::ServerCertificateValidationCallback = {$true} Invoke-WebRequest -Uri "https://<ip\_of\_UCS\_device>/nuova" -ContentType "application/json" -Method POST -Body '<aaaLogin inName="userName" inPassword="password" />' 

#### **Verify the credential using UNIX or Linux curl**

Run the following command, replacing userName, password, and ip\_of\_UCS\_device with the correct values:

curl -d '<aaaLogin inName="userName" inPassword="password" />' -H "Content-Type: application/json" -X POST https://<ip\_of\_UCS\_device>/nuova 

After verifying the credential:

1.  Create a credential with the correct user name and password combination. User names and passwords are case sensitive.
2.  Run Discovery again.
3.  If the API URL is not available, contact the UCS administrator or Cisco support to complete setup of the target UCS device.

### Related Links

[Cisco Unified Computing System (UCS)-HD device discovery](https://docs.servicenow.com/csh?topicname=r-CiscoUCSHD.html&version=latest "Cisco Unified Computing System (UCS)-HD device discovery")
