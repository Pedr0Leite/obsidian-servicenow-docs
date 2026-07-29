---
title: "Using the Browser Response Time as a troubleshooting tool on instance components loading"
aliases:
  - KB0724951
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724951
kb_number: KB0724951
last_modified: 2025-03-26
---

## Using the Browser Response Time as a troubleshooting tool on instance components loading

  

### Issue

This article provides information on using the Browser Response Time as a troubleshooting tool on instance components loading.

### Release

All Releases

### Resolution

The Browser Response Time tool can be used to help with troubleshooting.  
If you are ever in an situation in which a form is loading for a long time and you suspect this is browser related.

First, notice that the bar is filled mostly with green, which denotes browser time taken

![](/sys_attachment.do?sys_id=6fe37591476cee54b8a4aa25126d4397)

You can see that the Browser is hyper linked. You may click on this to see a breakdown of categories which are loading.  
See the image below for an example.

![](/sys_attachment.do?sys_id=afe37591476cee54b8a4aa25126d4399)

If you then click on an item which may take up the most time in milliseconds, you can break this down even further to know exactly which  
client side item that is taking so long to load. There are many reasons why this could take place and troubleshooting further would take loading  
the item up to troubleshoot it further.

Below is an image of the items broken out after clicking on it!

![](/sys_attachment.do?sys_id=afe37591476cee54b8a4aa25126d439b)

The name is the items actual name of the records.
