---
title: "Changes with Software Asset Management Foundations plugin activation"
aliases:
  - KB1569810
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1569810
kb_number: KB1569810
last_modified: 2024-08-19
---

## Changes with Software Asset Management Foundations plugin activation

  

### Summary

Once you activate the plugin Software Asset Management Foundations, you may see below visible/flow changes. 

**Plugin**: Software Asset Management Foundation (**ID**: com.snc.sams)

**Dependent Plugins**:

-   Software Asset Management Core (com.snc.sam.core)
-   Normalization Data Services Client (com.glide.data\_services\_canonicalization.client)
-   GlideQuery (com.sn\_glidequery)

**Other Plugins Activated/Updated**:

-   Asset Management (com.snc.asset\_management)
-   Asset Management Workspace    (com.sn\_itam\_workspace)
-   CMDB Page Templates    (sn\_cmdb\_pg\_templts)
-   Configuration Management (CMDB)    (com.snc.cmdb)
-   Model Management (com.snc.model)
-   Natural Language Query (com.snc.nlq)

**Summary of changes**:

**Company Records**: The core\_company table will be have normalized company records added and its related normalized mappings from ServiceNow content. Once you complete the guided set-up you will be able to see only the unique companies (with normalized=TRUE) and its alias names as Normalized mappings. Please find more details of functionality as [Normalization Data Services](https://docs.servicenow.com/bundle/vancouver-platform-administration/page/administer/normalization/concept/c_NormalizationOverview.html "Normalization Data Services").

**Application/Module(s)**: As part of the above plugin you see new applications called Software Asset, Normalization Data Services applications and its related modules are added/updated. (These labels might have updated if you are already using Legacy SAM application)

**Tables**: You will see tables like Software Entitlement (alm\_license), Device Allocations (alm\_entitlement\_asset) , User Allocations (alm\_entitlement\_user), Software Installations (cmdb\_sam\_sw\_install) are updated. These tables are labeled differently in Legacy SAM plugin. Once SAMF/P is added these are renamed and the functionality also changed. If you have the legacy-SAM active already and SAMF is activated you will see the changes as below. Else these are all new additions.

| **Table** | **Change** | **Previous Label** | **New Label** |
| --- | --- | --- | --- |
| alm\_license | Label Update | Software License | Software Entitlement |
| alm\_entitlement\_user | Label Update | User Entitlement | User Allocations |
| alm\_entitlement\_asset | Label Update | Device Entitlement | Device Allocations |
| cmdb\_sam\_sw\_install | New Table | \-- | Software Installations |

**Dictionary/Column changes**:

-   Inference mandatory field - For software models that have suite components (to bundle software models), the Inference mandatory field value in the Software Suite \[cmdb\_m2m\_suite\_model\] table is transferred to a new Mandatory field
-   Rights field - The Software Entitlements (formerly Software Licenses) Rights field value in the License Entitlements \[alm\_entitlement\] table is transferred to a new Purchased rights field, and name changed from Rights to Active rights
-   The Software model field for a software entitlement allocation (Software Entitlement \[alm\_license\] table) is automatically set to the software model on the entitlement (License Entitlements \[alm\_entitlement\] table)
-   The quantity for a software entitlement allocation (License Entitlements \[alm\_entitlement\] table) is set to 1 unless there are multiple allocations.
-   If there are multiple software entitlement allocations for the same user or device, the allocations are aggregated into one record, the quantity is set to the count of aggregated records, and duplicate allocations are not allowed.

**Forms/Views**:

-   Software Models, Entitlements (formerly Software License), Discovery Models, and Software Installations form and list layouts are modified.
-   The field manufacturer on Software model is labeled as Publisher. 
-   Some of the fields are marked as mandatory and some UI policies, client scripts added on software model or software entitlement to address certain use cases like license metric, metric type, quantity etc.

**Functionality**:

-   If you do not have any SAM related plugins earlier, then you might encounter the changes related to softwares as below:
    1.  The software used to updated to cmdb\_software\_instance table. So after this plugin you may see some data missing from cmdb\_software\_instance OR the latest data not being updated to cmdb\_software\_instance. Reason for this is with any SAM related plugin the target table for softwares is changed from cmdb\_software\_instance to targeted to cmdb\_sam\_sw\_install. This applies to all OOB applications like discovery, SCCM, other SG integrations.
    2.   After the SAM is installed and if you would like to have all the softwares from older table (cmdb\_software\_instance - Software Instance) to new table (cmdb\_sam\_sw\_install - Software Installations) then you can use the OOB [Migrate software installations process](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/task/t_MigrateSWInstalls.html "Migrate software installations process").
    3.  After the SAM is installed, the table cmdb\_ci\_spkg\_list stored data might not be the latest as it didn't check SAM-related tables.
-   The license counters from legacy-SAM are disabled as we have new functionality called reconciliation introduced from SAM-F/SAMP.
-   Legacy-SAM used to match the discovery models with related software models and populate the same. This is now deactivated.

**Customizations**:

-   Any customizations to SAMF or its dependent plugins are skipped during the SAMF/SAMP activation. These customizations are supposed to be reviewed and strongly recommended to revert to OOB (_**if you wish to use SAM functionality**_). Please [refer](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726511) 

**List of file additions/updates**:

-   [URL below will give all files from the above plugin(s)](https://instance_name.service-now.com/sys_upgrade_history_log_list.do?sysparm_query=upgrade_history.to_versionINcom.snc.sam.core%2Ccom.glide.data_services_canonicalization.client%2Ccom.snc.sams%2Ccom.snc.model%2Ccom.snc.cmdb%2Ccom.snc.asset_management%2Ccom.snc.nlq%2Ccom.sn_itam_workspace%2Csn_cmdb_pg_templts&sysparm_view= "URL below will give all files from SAMF/dependent plugins")

**Deactivate or uninstall the plugin:**

-   In the platform any plugin once activated it can not be deactivated or inactivated. Please refer more details [here](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998180) for the options available.

### Related Links

-   [Software Asset Management migration](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/concept/c_SAMMigration.html#t_MigrateSAMCustom "Software Asset Management migration")
-   [Deactivating the SAM-Professional/SAM-Foundations pluins after installatins or usage](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998180 "Deactivating the SAM-Professional/SAM-Foundations pluins after installatins or usage")
-   [Where to find SAMP plugin related files (skipped, upgraded, etc) after the plugin activation and how to revert them to OOB](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726511)
-   [Migrate software installations process](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/task/t_MigrateSWInstalls.html "Migrate software installations process").
