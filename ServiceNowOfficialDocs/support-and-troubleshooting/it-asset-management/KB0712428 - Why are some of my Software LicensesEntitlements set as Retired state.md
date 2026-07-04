---
title: "Why are some of my Software Licenses/Entitlements set as Retired state?"
aliases:
  - KB0712428
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712428
kb_number: KB0712428
last_modified: 2024-04-07
---

## Why are some of my Software Licenses/Entitlements set as Retired state?

  

### Issue

# Symptoms

* * *

When looking at your Software Entitlements table \[alm\_license\], you may see some with State=Retired \[install\_status=7\].

**Asset -> Software Entitlement** (or **License Assets** for older versions)  
or**  
Software Asset -> Software Entitlements** (or **Software Licenses** for older versions)

# Release

* * *

All releases with with a Software Asset Management plugin installed.

# Cause

* * *

One cause is that these licences were merged into a new licence by someone clicking the 'Merge with Similar Records' related link on one of those licenses' forms.

That process takes all the Rights from all the alm\_license records that share the same Model, and creates a new record that now has the sum of all those rights.

The records that were merged now have State=Retired, and will have the 'Merged into' field set with a reference to the new licence.

![](sys_attachment.do?sys_id=a97a6866db42b450e515c223059619a0)

# Resolution

* * *

Don't use the retired record, and instead use the new merged record.

# Additional Information

* * *

For full details of this Merge feature, please refer to the documentation - [Merge a software license](https://docs.servicenow.com/search?q=Merge+a+software+license "Merge a software license").
