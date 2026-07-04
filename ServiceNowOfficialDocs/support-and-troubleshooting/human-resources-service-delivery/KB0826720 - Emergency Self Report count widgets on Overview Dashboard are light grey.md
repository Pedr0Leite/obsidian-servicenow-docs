---
title: " Emergency Self Report count widgets on Overview Dashboard are light grey "
aliases:
  - KB0826720
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0826720
kb_number: KB0826720
last_modified: 2024-04-08
---

## Emergency Self Report count widgets on Overview Dashboard are light grey

  

### Issue

After installing the store app 'Emergency Self Report' (sn\_imt\_quarantine), the Emergency Self Report -> Overview Dashboard count widgets are grayed out.

### Cause

The Emergency dashboard count widget colors are determined by the current main Service Portal Theme Configuration. 

### Resolution

The current Service Portal theme being used might be missing the CSS code variables used by the Emergency Self Service app dashboard to generate the default widget color.

Specifically, the code from the default 'La Jolla' theme used by the widgets is below.  
  
// Grays  
$gray-base: #000000;  
$gray-dark: lighten($gray-base, 18.04%);  
$gray-darker: lighten($gray-base, 8.24%);  
$gray-light: lighten($gray-base, 40%);  
$gray-lighter: lighten($gray-base, 94.51%);  
$gray: lighten($gray-base, 29.02%);  
  
To resolve the issue, you can either revert to the default La Jolla theme for your service portal or you can add the missing CSS variables to the current theme. 

Expected View:  

![](/sys_attachment.do?sys_id=1cd2bc45db40b4d0b55f0b55ca9619e0)

Further details on the Emergency Self Report dashboard found in the docs link below.

[https://docs.servicenow.com/csh?topicname=emergency-self-report.html&version=latest](https://docs.servicenow.com/csh?topicname=emergency-self-report.html&version=latest)
