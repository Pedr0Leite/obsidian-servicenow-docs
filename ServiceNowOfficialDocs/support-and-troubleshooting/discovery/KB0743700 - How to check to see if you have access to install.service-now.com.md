---
title: "How to check to see if you have access to install.service-now.com"
aliases:
  - KB0743700
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743700
kb_number: KB0743700
last_modified: 2024-04-26
---

## Issue

# Description

If you're in the pre-London release the mid server upgrades will be pulled from install.service-now.com.  You will need to have your network admin open your firewall this this site.

After London the mid server upgrade will go through the instance if the following properties is set to true.

  

**mid.download.through.instance=true  
**

If it set to false will will continue to be pulled from install.service-now.com

# Procedure

How to check to see if you can access install.service-now.com

1\. Open a command prompt in windows or a terminal in linux check to see if you can ping install.service-now.com

2\. Open a web browser on the mid server:

a. Type download in the text filter navigator

b. select the version of the mid server you wish to download.  If you're unable to download you do not have access to install.service-now.com.

[https://docs.servicenow.com/csh?topicname=t\_DownloadMIDServerFiles.html&version=latest](https://docs.servicenow.com/csh?topicname=t_DownloadMIDServerFiles.html&version=latest)

3.  Go to the mid sever agent logs to see if there are Warning during the hourly upgrade check.

## Additional Information

[MID Server Property - mid.download.through.instance changed from NY](https://docs.servicenow.com/bundle/newyork-release-notes/page/release-notes/now-platform-capabilities/mid-server-rn.html "MID Server Property - mid.download.through.instance")
