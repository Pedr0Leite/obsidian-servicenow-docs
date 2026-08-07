---
title: "How to fix missing QR codes on the VAM portal"
aliases:
  - KB0955797
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955797
kb_number: KB0955797
last_modified: 2025-10-24
---

## How to fix missing QR codes on the VAM portal

  

### Issue

When you view appointments on the VAM portal, QR codes may not appear. This issue occurs when the system doesn't recognize .gif files as an authorized file name extension. 

### Release

All supported releases

### Cause

You may see this warning message in the node log:

"\*\*\* WARNING \*\*\* Security restricted: gif is not an authorized file extension"

This occurs because the glide.attachment.extensions system property doesn't include the .gif file name extension. The property currently allows only .doc, .docx, .xls, .xlsx, .pdf, .jpeg, .jpg, .png, .ico, .txt, and .svg file types.

### Resolution

To resolve this, add the .gif. file name extension to the glide.attachment.extensions system property:

1.  Go to System Properties and open the glide.attachment.extensions record: https://<INSTANCE\_NAME>.service-now.com/sys\_properties.do?sys\_id=650b07dbc0a80006004f95f2c929335d.
2.  Add .gif. to the existing list of file name extensions.
3.  Clear the system cache by running cache.do.
