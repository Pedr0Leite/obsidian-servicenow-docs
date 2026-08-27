---
title: "Known reasons for \"Installs requiring action\" with an \"Undetermined\" reason arising from software asset reconciliation"
aliases:
  - KB1793130
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1793130
kb_number: KB1793130
last_modified: 2025-11-12
---

## Text

**Context**  
  
Software installs that are unlicensed are reported on the Software Asset Workspace's publisher summary section. Installs may either be "Unlicensed installs" (meaning there are insufficient software entitlement rights) or "Installs requiring action" (meaning there is a configuration/data setup issue to fix).  
  
![](/sys_attachment.do?sys_id=cec3b31793c53214f538fb2d6cba1085)  
  
You may view the installs requiring action and the reason by clicking on the progress indicator.  
  
![](/sys_attachment.do?sys_id=8ec3b31793c53214f538fb2d6cba1089)  
  
Clicking on the reason also gives you details and instructions on how to fix the issue.  
  
![](/sys_attachment.do?sys_id=0ac3b31793c53214f538fb2d6cba108d)  
  
Sometimes, however, the reason may say "Undetermined."  
  
 ![](/sys_attachment.do?sys_id=42c3b31793c53214f538fb2d6cba1091)  
  
**Root causes**  
  
An unlicensed reason usually cannot be determined if the install was processed through an unexpected code path due to unpredictable data corruption, misguided entitlement or data setup, or a bug in the reconciliation code. Below is a list of known reasons why some of these installs may unlicensed:  
  
**Unsupported virtualization technology**

-   For example, Nutanix virtualization technology is only available starting in [Xanadu](https://www.servicenow.com/docs/bundle/xanadu-release-notes/page/release-notes/it-asset-management/software-asset-management-rn.html).  
    
-   Other supported virtualization technologies are:
    -   VMWare
    -   HyperV
    -   Red Hat Virtualization
    -   Nutanix

  
**Unsupported license metric**

-   Please refer to ServiceNow documentation for supported license metrics per product.
-   For example, here are the [license metrics for Microsoft products](https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/reference/mapping-ms-license-metrics.html).

  
**Cloud licensing not supported for some publishers**

-   For example, cloud licensing for Red Hat Enterprise Linux Server is only available starting in [Xanadu](https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/reference/byol-license-rules.html#d172058e1087).
-   Supported cloud providers are:
    -   Azure
    -   AWS
    -   Google  
        

**A subscription is unlicensed due to insufficient rights, but the corresponding installs have reason 'undetermined'**

-   **[PRB1716581](/nav_to.do?uri=%2Fproblem.do%3Fsys_id%3Dc66ea44e97ae35901a7bbfa11153afe4%26sysparm_stack%3D%26sysparm_view%3D)** (fixed in Xanadu)
-   This can be verified by searching if a subscription record exists for the 'assigned\_to' user on the unlicensed install. Verify that the subscription is unlicensed.

**Installs not tied to any subscription are inferred to a subscription-only suite**

-   [**PRB1813322**](/nav_to.do?uri=%2Fproblem.do%3Fsys_id%3D797f82629301da50d6d8fdb86cba10dd%26sysparm_stack%3D%26sysparm_view%3D) (fixed in Yokohoma)  
    
-   You may be facing this PRB if installs are inferred to a software model (i.e. Windows Server is inferred to Visual Studio) that has only User Subscription entitlements, and there are no subscriptions for the software model in samp\_sw\_subscription.

  
**Subscription installs are tied to a different software model than the corresponding subscription record**

-   The Licensable software on a subscription record may not match the Inferred suite or Minimum viable software model on the corresponding install records.
-   [**PRB1663950**](/problem.do?sys_id=aa46d2a693aee954666cb66d6cba10c1) (fixed in Vancouver) - A subscription install is tied to a suite but the subscription record is not
-   [**PRB1845229**](/nav_to.do?uri=%2Fproblem.do%3Fsys_id%3D7ecd3d4393cf9a90666cb66d6cba1016%26sysparm_stack%3D%26sysparm_view%3D) (targeted to Zurich) - For duplicate software models. The solution is to move all entitlements under the same software model or to distinguish the software models (i.e. through install conditions).

**An install on VM is missing VM relationship to host, but the corresponding install has reason 'undetermined'**

-   [PRB1855067](/problem.do?sys_id=a8d841e193b35e50f538fb2d6cba1082) (targeted to Zurich) - Per processor license calculator does not give proper reason to install on VM missing relationship to host.

**An install on Windows Host that runs on a Hyper-V server with no VM**

-   [PRB1898290](/problem.do?sys_id=53b3049a9775a6d010c633f11153aff1) impacts Xanadu and Yokohama, fixed in Zurich

**A Windows Server or SQL server install (on-prem) with invalid installed on reference**

-   If a Windows Server or SQL server install has a corrupted installed on, it will not be processed by per core or per core with cal metrics, and shows with undetermined reason

**A suite install using Per User or Per Device license**

-   PRB1897823
-   We are not inserting "insufficient rights" reasons for Per User or Per Device suite installs; which is causing those installs to show up as "undetermined"

  
**Misc. data corruption**

-   If a product is not licensable, ensure that the 'norm\_publisher' and 'norm\_product' fields on the install records are cleared
-   Check that 'BYOL' and 'License included' installs have 'cloud\_provider' set

**Multiple unlicensed reasons** 

-   If a product is not licensable and we have multiple reasons for it being unlicensed. Currently we are not recording all the possible reasons. For example,   Oracle DB Products licensing we have an NUP entitlement but no CAL records created. The corresponding install is unlicensed due to missing CAL entry or possibly due to missing Per processor entitlement. 
-   [PRB1878560](/problem.do?sys_id=cfca9be1c3f0ee109c9971dc7a0131d8) - Tracking enhancement defect to evaluate internally with our PM team to see if health check is the best place to record this configuration issue or showing multiple unlicensed reasons in LWB better.

**Host class classification incorrect**

-   As part of discovery, we see the hosts tied to specific Virrtualization technology are not classified to expected classes. Example, VMware Cluster Host should be classified as ESX server but instead we see its Windows Server class. Due to this the corresponding installs are unlicensed and shows up as unlicensed with 'Undetermined' reason.
-   [PRB1878560](/problem.do?sys_id=cfca9be1c3f0ee109c9971dc7a0131d8) - Tracking enhancement defect to evaluate internally with our PM team to find all possible such scenarios across different virutalization technologies.

## Wiki

Software installs that are unlicensed from software asset reconciliation are reported on the software asset workspace publisher summary page as either "installs requiring action" or "unlicensed," meaning there are insufficient rights.
