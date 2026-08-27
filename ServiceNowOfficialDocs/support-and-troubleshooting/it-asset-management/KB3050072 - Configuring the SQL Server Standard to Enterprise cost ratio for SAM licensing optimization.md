---
title: "Configuring the SQL Server Standard to Enterprise cost ratio for SAM licensing optimization"
aliases:
  - KB3050072
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3050072
kb_number: KB3050072
last_modified: 2026-05-29
---

## Issue

The system property `com.snc.samp.sqlserver.standard_sa.to.enterprise_sa.cost.ratio` controls how Software Asset Management (SAM) compares the cost of licensing Microsoft SQL Server at the physical host level versus the individual virtual machine (VM) level.

The ratio is calculated as follows:

_Price of SQL Server Standard Edition with Software Assurance (SA)_ ÷ _Price of SQL Server Enterprise Edition with SA_

The default value is 0.25, which reflects Microsoft list pricing — meaning Standard Edition with SA licenses cost approximately one-quarter of Enterprise Edition with SA licenses.

SAM uses this ratio when evaluating SQL Server clusters. If licensing at the physical host level (which requires Enterprise Edition) would cost more than licensing the individual VMs, SAM recommends the VM-level approach, and vice versa.

  
  

## Resolution

### How to update the system property

1.  Navigate to All > Software Asset Management > Administration > Properties.
2.  Locate the property `com.snc.samp.sqlserver.standard_sa.to.enterprise_sa.cost.ratio`.
3.  Enter your recalculated ratio value in the Value field.
4.  Select Save.

* * *

### How the ratio controls the decision threshold

The ratio directly controls the threshold in the optimization calculation. The following example uses a simplified scenario:

-   Host has 16 physical cores
-   Host runs 4 VMs, each with 8 vCores, all Standard Edition

| Ratio | VM-side cost (4 × 8 × ratio) | Host-side cost | Decision |
| --- | --- | --- | --- |
| 0.25 | 8 cores | 16 cores | License VMs |
| 0.60 | 19.2 cores | 16 cores | License host |
| 0.50 | 16 cores | 16 cores | Tie |

If your contracted Standard Edition price is closer to 50% of Enterprise Edition (rather than the default 25%), and the property is not updated, SAM recommends VM-level licensing when host-level licensing would actually be cheaper. This creates a direct compliance and cost risk.

* * *

### Script include reference

For advanced users with the admin role, the script include containing the SQL Server licensing logic (`SamHostVMGridUtil`) can be accessed on your instance at:

`https://<instance-name>.service-now.com/sys_script_include_list.do?sysparm_query=scriptLIKEcom.snc.samp.sqlserver.standard_sa.to.enterprise_sa.cost.ratio&sysparm_view=`

Replace `<instance-name>` with your instance name. Admin access is required.

* * *

### Summary

The ratio is a cost normalization factor. It converts Standard Edition vCores into Enterprise-equivalent units so the optimizer can compare host-level and VM-level licensing costs on a consistent scale.

Note: An incorrect ratio does not produce an error. It silently generates a suboptimal licensing recommendation. Verify this value matches your contracted pricing whenever your Microsoft agreement is renegotiated.
