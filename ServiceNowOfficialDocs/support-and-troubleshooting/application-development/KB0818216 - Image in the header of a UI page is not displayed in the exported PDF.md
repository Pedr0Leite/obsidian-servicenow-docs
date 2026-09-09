---
title: "Image in the header of a UI page is not displayed in the exported PDF"
aliases:
  - KB0818216
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818216
kb_number: KB0818216
last_modified: 2024-04-08
---

## Image in the header of a UI page is not displayed in the exported PDF

  

### Issue

When trying to download the report from the post incident report tab of the major incident management plugin, the image in the header of UI page is missing in the exported PDF

### Release

New York Patch 6

### Cause

wkhtmltopdf  is used to export a webpage to PDF. This program requires image to be stored in local and referred by absolute path. Image stored in sys\_attachment does not work since it needs to be processed by Attachment processor first .

In short, when using embedded images, make sure:  
1) Image is stored in local and referred as absolute path;  
2) Do not put it into UI macro or nest in other UI elements (UI page/UI macro, etc).  
  
As this is the limitation of wkhtmltopdf, there is no workaround on this without changing image source.

### Resolution

Make sure the source of the image in the UI page is local and referred by absolute path.

Ex: You can define the image this way on the UI page

  <img src="gam.png" width="466" height="262"/>

Note Make sure the path doesn't have the URL to the image. This doesn't work either.
