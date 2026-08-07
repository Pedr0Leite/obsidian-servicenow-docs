---
title: "Manual MID server upgrade issue due to NTLM authentication "
aliases:
  - KB0743614
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743614
kb_number: KB0743614
last_modified: 2024-04-07
---

## Issue

# Symptoms

During MID server upgrade (any version) especially manual, while configuring instance connectivity setup process with Proxy server enabled and when clicking on "Test your connection" it'll throw an error "Unable to connect to instance".

![](sys_attachment.do?sys_id=88bce0eedb42b450e515c2230596192e)

# Release

-   All versions

# Cause

-   During MID server manual upgrade, post providing Proxy details and clicking "Test your connection", an error message pops-up stating "Unable to connect to instance".
-   When analyzing the mid\_installer.log file, the below error will be logged.

![](sys_attachment.do?sys_id=4cbce0eedb42b450e515c22305961933)

# Resolution

-   The error states that the Proxy server is enabled with "NTLM Authentication".
-   In order to avoid this error and proceed with upgrade/installation, Proxy team has to disable "NTLM Authentication".

# Additional Information

-   By default, ServiceNow supports only Basic Authentication against the Proxy server. 
-   If the installation has to be successful, Customer has to either disable "NTLM Authentication" or create an exception for the MID host.
