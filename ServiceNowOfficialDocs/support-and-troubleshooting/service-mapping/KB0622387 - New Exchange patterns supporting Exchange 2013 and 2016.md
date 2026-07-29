---
title: "New Exchange patterns supporting Exchange 2013 and 2016"
aliases:
  - KB0622387
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622387
kb_number: KB0622387
last_modified: 2025-01-03
---

## New Exchange patterns supporting Exchange 2013 and 2016

  

### Issue

New Exchange patterns supporting Exchange 2013 and 2016

Overview

* * *

This article is relevant for the Helsinki and Istanbul releases.

Support for Exchange 2013 and 2016 was added to the Exchange patterns in Jakarta release. Customers who haven’t upgraded to Jakarta can add the support for Exchange 2013 and 2016 by performing the following procedure.

Procedure

* * *

1.  Download four files attached to this KB article onto your computer from the Internet.
2.  For the file getExchangeServer.txt, change the file type from **txt** to **ps1**.
3.  On the ServiceNow platform, navigate to Discovery Patterns.
4.  Right-click on the table header, and select **Import XML**.
5.  Upload pattern files in xml format one by one.
6.  To upload the Powershell script, navigate to **Service Mapping > Uploaded Files**. Create new record, upload the script setting, and use the Logical name **GetExchangeServers**.
7.  On the Operating Systems tab:
    -   From OS Types, select **Windows**.
    -   From OS Architectures, select **32** and **64**.

Prerequisites for discovering exchange 2013 and 2016

* * *

1.  Provide an OS user with the rights to run Powershell commands against the Exchange servers: on the ServiceNow platform, configure applicative credentials for Service Mapping, and setting the CI type to Exchange Mailbox.
    -   Note: Do not confuse the Exchange Mailbox CI type with the Exchange Mailbox server CI type.
2.  On the ServiceNow platform, configure a domain user for accessing the Windows OS.
3.  Make sure that the **Microsoft.Exchange.Management.PowerShell** module is installed on the server that the customer wants to discover.
4.  On the Windows Server, ensure that the winRM service is running and enable Powershell remoting. (You can run **winrm quickconfig** from cmd or **enable-psremoting -force** from a Powershell session on the Exchange Server.)
