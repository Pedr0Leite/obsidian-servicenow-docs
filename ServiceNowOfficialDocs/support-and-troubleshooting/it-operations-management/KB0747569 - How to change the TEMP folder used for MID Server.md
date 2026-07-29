---
title: "How to change the TEMP folder used for MID Server"
aliases:
  - KB0747569
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747569
kb_number: KB0747569
last_modified: 2025-04-16
---

## Issue

In some cases execution from /tmp directory is restricted for security reasons, so it will be necessary to specify a different folder where the MID server can create temporary files. This KB covers how to change the TEMP folder used by the MID Server in such scenarios.

## Resolution

1.  Go to \[MID\_installation\_path\]/agent/conf
2.  Open wrapper-override.conf file
3.  Look for section titled "# Java Additional Parameters"
4.  Under that section there should be a commented section called "# Uncomment below to enable JDP. Change the address/port settings as needed."
5.  Under that add a uncommented line like:

wrapper.java.additional.2=-Djava.io.tmpdir=\[PATH\_TO\_DIFFERENT\_DIRECTORY\_FILE\]

**Note:** the "2" after "additional." above. That number will depend on if there are other properties already there. For example if there is a property using "wrapper.java.additional.1=" and "wrapper.java.additional.2=" already, then the next one that should be used is "wrapper.java.additional.3=" and so on

It should look something like:

\# Java Additional Parameters  
wrapper.java.additional.1=-Djava.util.logging.config.file=properties/glide.properties  
\# Uncomment below to enable JDP. Change the address/port settings as needed.  
wrapper.java.additional.2=-Djava.io.tmpdir=\[PATH\_TO\_DIFFERENT\_DIRECTORY\]

**Note:** If the temp folder path on Windows includes a space in any of the folders, you may have a problem. **Avoid temp folders with space characters in the path**. See [PRB1422003/KB0861154](https://support.servicenow.com/kb_view.do?sysparm_article=KB0861154), which is fixed by [PRB1396562/KB0861153](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861153 "KB0861153") in Rome.

## Additional Information

-   [ServiceNow Discovery 101: Virus Scanners And MID Server Performance](https://community.servicenow.com/community?id=community_blog&sys_id=fbdcaa65dbd0dbc01dcaf3231f961918 "ServiceNow Discovery 101: Virus Scanners And MID Server Performance")
-   [MID Server pre-upgrade check](https://docs.servicenow.com/csh?topicname=c_UpgradeAndTestMIDServer.html&version=latest "MID Server pre-upgrade check")
