---
title: "How to use the newer iText7 for PDF generation within the HR Service Delivery application"
aliases:
  - KB1633478
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1633478
kb_number: KB1633478
last_modified: 2025-09-03
---

## How to use the newer iText7 for PDF generation within the HR Service Delivery application

  

### Summary

The ServiceNow platform uses the third-party application **iText** for generating PDFs. 

By default, the older **iText5** is being used when generating PDFs as part of the HR Service Delivery application, for example for e-signature tasks or HR documents.

Starting from the Paris release, a new OOB system property "**sn\_hr\_core.itext7.pdf\_conversion**" is installed on new instances provisioned from Paris onwards.

**The property does NOT get created on instances provisioned on any older release, even after upgrading to a new release.** 

If your instance does not have this property and you are using any PDF functionality within HR, consider importing it from this KB, to take advantage of the new PDF generation functionality included in **iText7**.

### Release

All instances that were provisioned on the Orlando release or earlier.

### Instructions

1\. Download the attached System Property "[**sn\_hr\_core.itext7.pdf\_conversion**](sys_attachment.do?sys_id=22db8d94472c8690f93138ce536d4382)" and its related Category Property "[**sn\_hr\_core.itext7.pdf\_conversion.Human Resources Scoped**](sys_attachment.do?sys_id=a6db81d4472c8690f93138ce536d4311)".

2\. Import XL the two items into your instance.

NOTE that the property is set to **true** by default.

When the property is set to **true**, **iText7** is used for PDF generation within the HR Service Delivery application; setting it to **false** would revert to using **iText5**.
