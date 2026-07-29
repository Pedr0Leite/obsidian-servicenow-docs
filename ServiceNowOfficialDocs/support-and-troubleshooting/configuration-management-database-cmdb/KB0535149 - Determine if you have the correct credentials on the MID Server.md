---
title: "Determine if you have the correct credentials on the MID Server"
aliases:
  - KB0535149
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535149
kb_number: KB0535149
last_modified: 2025-04-07
---

## Determine if you have the correct credentials on the MID Server

  

### Issue

Determine if you have the correct credentials on the MID Server 

# Description

* * *

This article describes how to determine if you have all the correct credentials and permissions to run a MID Server.  

# Resolution 

* * *

To determine if you have the correct credentials to run a MID Server, try to establish a ServiceNow MID user record and configure your credentials. If you are uanble to complete the steps below, you may not have the permissions needed to run a MID Server.

1\. Create a ServiceNow MID user record for the MID Server to use. This user record must have the **mid\_server** role.

2\. In your MID Server, edit the _config.xml_ file with a text editor such as WordPad:

-   Find the element <parameter name="url" value="https://YOUR\_INSTANCE.service-now.com" /> and change the value to the URL of your instance.
-   If basic authentication is enabled, as it is by default, enter the user credentials in the mid.instance.username and mid.instance.password parameters.

3\. Next, configure your MID Server credentials.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><b>Note</b>: The domain user must have enough rights to create service and complete any task required of Discovery.</td></tr></tbody></table>

To configure your credentials: 

1.  Open the Windows Services console.
2.  Double-click the **ServiceNow <MID Server name>** service for each MID Server.
3.  Select the **Log On** tab.
4.  Set **Log on as** privileges with Domain User or Local Admin credentials.
5.  In the General tab, set **Startup type** to **Automatic**.
6.  Click **OK**.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><b>Note</b>: The upgrade fails if the domain user does not have the ability to create services.</td></tr></tbody></table>
