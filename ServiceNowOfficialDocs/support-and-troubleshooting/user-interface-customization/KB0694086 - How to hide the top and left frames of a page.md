---
title: "How to hide the top and left frames of a page"
aliases:
  - KB0694086
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694086
kb_number: KB0694086
last_modified: 2025-01-03
---

## How to hide the top and left frames of a page

  

### Issue

For most pages in an instance there would two frames that are displayed:

Top frame that shows the instance banner as well as the user name and other icons

Left frame that shows the filter navigator

![](sys_attachment.do?sys_id=541ae4e2db42b450e515c22305961909)

  

This article details the procedure on how to hide these two frames.

### Release

All releases

### Resolution

The frames are displayed due to the URL of the page containing the "nav\_to.do?uri=" parameter. So in order to not display these frames users can manually remove that parameter from the URL or update the processes that generate the URLs to not contain that parameter.

### Related Links

[Examples of navigating by URL](https://docs.servicenow.com/csh?topicname=r_NavigatingByURLExamples.html&version=latest "Examples of navigating by URL")
