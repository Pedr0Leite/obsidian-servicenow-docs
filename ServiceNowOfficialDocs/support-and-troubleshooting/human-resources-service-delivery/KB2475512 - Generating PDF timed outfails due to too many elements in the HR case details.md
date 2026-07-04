---
title: "Generating PDF timed out/fails due to too many elements in the HR case details"
aliases:
  - KB2475512
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2475512
kb_number: KB2475512
last_modified: 2025-11-13
---

## Generating PDF timed out/fails due to too many elements in the HR case details

  

### Issue

Generating PDF in an HR case timed out/fails and the pdf report is not attached to the case work notes. 

### Facts

\- Open HR case and click 'Summary report'

\- Choose a template and notice the pdf preview is a very long document with many elements and is dense in details

\- Click on 'Generate PDF', the pop-up disappears and there is no pdf attachment in the work notes. 

\- Log will be as followed: 

```
SEVERE *** ERROR *** Request : *** failed with ' Conversion failed. HTML to PDF conversion has failed with exception : null'
```

### Release

Xanadu and newer

### Resolution

Workaround:

Since the current page size of the pdf can not fit all the elements of the HR case, one workaround is to change the page size to fit all the elements. 

1.  Find the template being used in "**sn\_doc\_html\_template"** table and open the record. 
2.  In the page tab, change the page size from 'Letter' to 'Legal'. 

Note: if the pdf generating fails in the HR case, it will fail when generating pdf document in "**sn\_doc\_html\_template"** record. Hence after changing the page size in the template record, you can generate the pdf document right at the template as a good indicator for HR case pdf generating.
