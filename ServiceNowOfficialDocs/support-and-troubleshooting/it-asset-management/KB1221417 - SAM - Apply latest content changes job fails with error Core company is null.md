---
title: "\"SAM - Apply latest content changes\" job fails with error \"Core company is null\""
aliases:
  - KB1221417
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1221417
kb_number: KB1221417
last_modified: 2026-06-01
---

## "SAM - Apply latest content changes" job fails with error "Core company is null"

  

### Issue

The **"SAM - Apply latest content changes"** job fails with the following error:

Failing with the error: Core company is null

  

The **asset\_job\_log** table shows the following error for **"Processing samp\_sw\_product"**:

Error while processing record \[sys\_id\] : Core company is null

  

In the **samp\_sw\_product** table, the above sys\_id record has **"Unknown"** in Product Type, but it has a value for Publisher.

When opening the Publisher record in the **samp\_sw\_publisher** table, the Manufacturer field is empty because there is no record for that Manufacturer in the **core\_company** table.

For some reason, the company records are not been created as part of the out of the box **"SAM - Apply latest content changes"** job.

### Release

All supported versions.

### Cause

When the **"SAM - Apply latest content changes"** job is triggered, as part of the logic, it will call the script include **"SAMCoreCompan****yUtil"** to associate a company record with a publisher record. More specific, if a company can be matched with publisher name, the company record is associated with the publisher record, otherwise, a new company record is created with the publisher name and then associated with publisher record. 

If the **"SAM - Apply latest content changes"** job is out of the box (no customizations), then review if a **custom business rule** was created on the **core\_company** and is preventing the above logic to create a new company record. 

### Resolution

Inactivate or delete the faulty custom business rule. If customer needs to have their customization, they could modify the code and create a default company.  

**Additional information:**

Link to the _"SAM - Apply latest content changes"_ job:

https://\[your\_instance\_name\]service-now.com/nav\_to.do?uri=sysauto\_script.do?sys\_id=26f6310bdb8773004fbf75868c961988
