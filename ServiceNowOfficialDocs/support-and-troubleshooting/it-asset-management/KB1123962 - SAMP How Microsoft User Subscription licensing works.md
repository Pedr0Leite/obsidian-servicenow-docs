---
title: "SAMP: How Microsoft \"User Subscription\" licensing works"
aliases:
  - KB1123962
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1123962
kb_number: KB1123962
last_modified: 2024-10-08
---

## Text

Microsoft User Subscription

[Version Log. 2](#_Toc89425405)

[Prerequisites. 2](#_Toc89425406)

[User Subscription for Microsoft 2](#_Toc89425407)

[Change for Quebec. 4](#_Toc89425408)

[User Subscription – Compliant (Example 1) 6](#_Toc89425409)

[User Subscription - Not Compliant (Example 2) 8](#_Toc89425410)

[User Subscription – Subscription Suites (Example 3) 12](#_Toc89425411)

[Algorithm.. 15](#_Toc89425412)

[Allocated Pass. 15](#_Toc89425413)

[Unallocated Pass. 15](#_Toc89425414)

[Consume Rights 16](#_Toc89425415)

[Code Flow.. 16](#_Toc89425416)

[Scheduled Jobs for Subscriptions 16](#_Toc89425417)

[Plugins. 16](#_Toc89425418)

[Troubleshooting. 17](#_Toc89425419)

[Appendix. 17](#_Toc89425420)

# Version Log

<table class="MsoTableGrid" style="border-collapse: collapse; border: none;" border="1" cellspacing="0" cellpadding="0"><tbody><tr><td style="width: 104.45pt; border: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">Date</p></td><td style="width: 115.55pt; border: solid windowtext 1.0pt; border-left: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">Author</p></td><td style="width: 115.3pt; border: solid windowtext 1.0pt; border-left: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">Change</p></td><td style="width: 115.5pt; border: solid windowtext 1.0pt; border-left: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">Version</p></td></tr><tr><td style="width: 104.45pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">09-20-2021</p></td><td style="width: 115.55pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">Martin Kintana</p></td><td style="width: 115.3pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">Initial</p></td><td style="width: 115.5pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">1.1</p></td></tr><tr><td style="width: 104.45pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">07-19-2022</p></td><td style="width: 115.55pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">Martin Kintana</p></td><td style="width: 115.3pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">Optimize images for KB</p></td><td style="width: 115.5pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">1.2</p></td></tr><tr><td style="width: 104.45pt; border: solid windowtext 1.0pt; border-top: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">&nbsp;</p></td><td style="width: 115.55pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">&nbsp;</p></td><td style="width: 115.3pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">&nbsp;</p></td><td style="width: 115.5pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top"><p style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">&nbsp;</p></td></tr></tbody></table>

# Prerequisites

Knowledge of concepts detailed in KB1156740 SAMP: Reconciliation Primer (prerequisite knowledge) are required.

# User Subscription for Microsoft

Microsoft User Subscription metric licenses a user for the number of activated software subscriptions. When reconciliation is run for a Software Model that has one or more Entitlements with this License Metric, a right is consumed for each unique, active Software Subscriptions record assigned to a user.  Any software installations that correspond to the software model will also be licensed.  However, if a user has software installations but no subscription record, that user will not consume a right and the installations will be unlicensed.

#### Software Subscriptions (samp\_sw\_subscription)

Microsoft cloud applications such as Office 365, Project Online, etc, are subscription-based software associated with a specific user. The **"SAM - Import User Subscriptions"** scheduled job extracts data from the Microsoft Admin Portal and populates the Software Subscription (samp\_sw\_subscription) table.

![](/sys_attachment.do?sys_id=8a7c073693851610057c7de86cba1024)

Once the subscription data is pulled from the Microsoft portal, a query for the user record (sys\_user) is made against the User principal name.  If a match is found the User reference is stamped on the record.  The User reference to the sys\_user record is required for Reconciliation.  Additionally, the reference to the Software Model is also stamped on the record.

These subscription records are the primary input for the User Subscription metric.  As such, it contains all the suite fields and reconciliation-related fields analogous to those found on the Software Installation table:

1.  inferred\_suite
2.  inferred\_suite\_level
3.  inferred\_suite\_product
4.  is\_reconciled
5.  unlicensed\_subscription
6.  product\_result
7.  software\_model\_result
8.  license\_metric\_result

## Change for Quebec

When data is pulled from Microsoft, the unique identifier for the product is used to look up the corresponding DMAP to find the correct Software Model to reference.  Prior to Quebec, we look up subscription identifiers stored in samp\_sw\_product\_definition where the PPNs are stored.

![](/sys_attachment.do?sys_id=527c073693851610057c7de86cba10e8)

In Quebec, a new table was created to hold the subscription identifier information: Subscription Product Definition (samp\_sw\_subscription\_product\_definition).  This identifier to DMAP data comes from SAMP content.

#### Software Installations (cmdb\_sam\_sw\_install)

Microsoft cloud applications like Office 365 may have the software installed on the user's device.  For example, Microsoft Word, Excel, and PowerPoint might be installed on the device which allows for offline use. 

Software installations are licensed by a User Subscription entitlement if the install's assigned to the user has a corresponding subscription record for the software.  A software installation record will not be licensed by the User Subscription metric if:

-   the assigned\_to user does not have a corresponding subscription record
-   the subscription record exists but does not have a reference to the sys\_user record 

Microsoft Subscription and Install records are processed by Reconciliation and results are reflected in the License Usage module in the SAM Workspace (aka. License Workbench in pre-Rome instances).

#### Reserve Entitlement for Office 365

Microsoft allows customers to add extra subscriptions to their pool in the middle of the contractual term without having to pay up front. These are known as Reserved licenses.

![](/sys_attachment.do?sys_id=1e7c073693851610057c7de86cba106f)

These are modelled as Reserved entitlement in SAM. Reconciliation will consider these entitlements in the pool of available rights to license Office 365 and are counted as true-up costs. The entitlement has a reserve entitlement flag checked and a reference to the Source entitlement representing the original subscription being added to.

At annual true-up with Microsoft, customers need to pay a pro-rated cost for these licenses calculated from the date they are reserved. This feature allows customers to manage their O365 reserved licenses and accurately calculate the true-up cost. 

After the end date, the reserve entitlement expires (and true up has been paid), and a new Subscription entitlement will be automatically generated to represent the rights for the duration of the source entitlement.  This is done by the "SAM – Subscription Maintenance" scheduled job. More details on this feature can be found [here](https://trainingops.servicenow.com/detail/videos/itam___/video/6117133355001/orlando:-itam:-it-asset-management---manage-reserved-o365-licenses).

## User Subscription – Compliant (Example 1)

There are 20 subscriptions for Microsoft Office 365 Enterprise E1 and 20 User Subscription rights.  Since each user subscription requires 1 right, there are enough rights to license all subscriptions and the software is compliant.

Software Model: Microsoft Office 365 Enterprise E1

Subscriptions: 20 users

Entitlement: 20 User Subscription rights

Results:

![](/sys_attachment.do?sys_id=5e7c073693851610057c7de86cba105a)

License Metric Results show Microsoft Office 365 Enterprise E1 is compliant with 20 rights owned and 20 rights used.

![](/sys_attachment.do?sys_id=d67c073693851610057c7de86cba1052)

Licenses Required By shows each of the 20 users with subscriptions for Office 365 Enterprise E1.  User Subscription licenses each user with 1 right.

![](/sys_attachment.do?sys_id=d27c073693851610057c7de86cba1063)

All subscription records for Office 365 Enterprise E1 software model are licensed.

## User Subscription - Not Compliant (Example 2)

This example shows a Not Compliant scenario where not enough rights are available.  Remediation Options are generated to give the user ways to resolve the non-compliance.  The Purchase Rights remediation option shows how many rights should be purchased and which users need those rights. This example has software installed on the user's device(s) which are reflected in software installation records.

Software Model: Microsoft Office 365 Enterprise E3

Subscriptions: 357 users

Software Installs: 494 installs of Office 365 ProPlus

Entitlement: 300 User Subscription rights

![](/sys_attachment.do?sys_id=9a7c073693851610057c7de86cba1056)

License Metric Results show Microsoft Office 365 Enterprise E3 is not compliant. 357 rights are required but only 300 rights are owned, giving -57 licenses available. The non-compliance can be remediated by purchasing 57 rights which are shown in the Remediation Options tab.

![](/sys_attachment.do?sys_id=8e7c073693851610057c7de86cba1045)

Licenses Required By shows each of the 357 users with subscriptions for Office 365 Enterprise E3.  User Subscription licenses each user with 1 right.

![](/sys_attachment.do?sys_id=5a7c073693851610057c7de86cba106b)

The Subscriptions tab (grouped by Unlicensed Subscriptions) shows 300 licensed and 57 unlicensed subscription records.  The group can be expanded to show the specific licensed and unlicensed users.

![](/sys_attachment.do?sys_id=167c073693851610057c7de86cba10ec)

The Installs tab shows the 494 installs among all the users.  Grouping by Unlicensed install shows 75 installs licensed and 419 unlicensed installs.

![](/sys_attachment.do?sys_id=4e7c073693851610057c7de86cba1028)

In a not compliant scenario, Remediation Options are generated. Purchase Rights remediation option shows 57 rights to purchase with a true up cost of $13,680

![](/sys_attachment.do?sys_id=967c073693851610057c7de86cba1067)

Details of the Purchase Rights remediation option shows which 57 users require rights.

## User Subscription – Subscription Suites (Example 3)

This example shows how subscription suites work. This example has software installed on the user's device(s) which are reflected in software installation records.

Software Model: Microsoft Microsoft 365 Enterprise E5

Entitlement: 20,000 User Subscription rights

Subscriptions: 188 unique users.  Each user has subscription records for:

1.  Microsoft Enterprise Mobility Enterprise E5
2.  Microsoft Windows 10 Enterprise Windows

Software Installs: 486 installs of the following software on varying user devices.

1.  Microsoft Office 365 ProPlus - en-us Enterprise E5
2.  Discovery model: Microsoft Power BI Desktop (x64) Pro

Suite Information specified on the Software Model:

![](/sys_attachment.do?sys_id=167c073693851610057c7de86cba104e)

Results:

![](/sys_attachment.do?sys_id=4a7c073693851610057c7de86cba100e)

License Metric Results show Microsoft Microsoft 365 Enterprise E5 is compliant with 20,000 rights owned and 188 rights used.

![](/sys_attachment.do?sys_id=de7c073693851610057c7de86cba1073)

Licenses Required By shows each of the 188 users.  User Subscription licenses each user with 1 right.

![](/sys_attachment.do?sys_id=e67c073693851610057c7de86cba10f0)

Each user has a subscription record for:

1.  Microsoft Enterprise Mobility Enterprise E5
2.  Microsoft Windows 10 Enterprise Windows

Since Enterprise Mobility and Windows 10 are both part of the Microsoft 365 Suite, each user only requires 1 right from the Microsoft 365 Enterprise E5 entitlement.

![](/sys_attachment.do?sys_id=c67c073693851610057c7de86cba1020)

There are 486 install records representing Power BI and Office 365 on various devices owned by the users with Microsoft 365 subscription records.  All these are licensed (Unlicensed install == false) because Power BI is a suite component of Office 365 E5 which itself is a suite component of the Microsoft 365 Suite.

#### Suite fields and Recon fields

![](/sys_attachment.do?sys_id=427c073693851610057c7de86cba104a)

![](/sys_attachment.do?sys_id=127c073693851610057c7de86cba105f)

A look at the internal fields of the Software Subscription and Software Installation records gives a picture of how each record was reconciled.  The Inferred suite (inferred\_suite) field on the subscription and install records is stamped by the Suite Engine with the highest level Suite (ie. Microsoft 365).  This allows the license calculator to identify the subscriptions and installs for a specific user for which a given entitlement can be applied. 

#### Subscriptions take precedence

The user's install records for the software can only be licensed with the User Subscription metric if it the subscription exists.  In this example, Microsoft 365 subscription suite entitlement can be used to license the user's Office 365 installations because the user has subscription.

# Algorithm

## Allocated Pass

Since Microsoft User Subscription allocations are for a specific user, the allocated pass will process all allocated users first.  Each user requires one User Subscription right? 

A **"Rights used by"** (samp\_entitlement\_result) record for the user is created and the rights used are set accordingly.

1.  Run Allocated Pass
    1.  for each allocated user for the current product
        1.  traverse through all subscriptions which are related to this user and product
            1.  store these subscriptions' information into a subscription object array 'subscriptions'
                1.  subscriptions array stores (sys id, software model, assigned software and user)
        2.  consumeRights (see consumeRights details)
        3.  generateRightsUsedBy for the current subscription
        4.  create Rights Needed by and mark unlicensed subscriptions and unlicensed installs                          
        5.  markUnlicensedInstalls
        6.  markUnlicensedSubscriptions

## Unallocated Pass

Once all allocated devices are processed and accounted for, all remaining unreconciled subscription records are processed.  A **"Rights used by"** (samp\_entitlement\_result) record for the user is created (or the existing RUB record from the allocated pass is updated) and the rights used are set accordingly.

1.  Run Unallocated Pass
    1.  Get all unreconciled subscriptions for current product, and license them, user, by user
    2.  Handle current subscription. License it or store it in a subscription
        1.  Consume rights (see consumeRights details)
        2.  Create RUB
        3.  Create RNB
        4.  Mark unlicensed subscriptions
        5.  Mark unlicensed installs
        6.  Add this subscription to the subscriptions structure

## Consume Rights

            consumeRights is the main method to license the subscriptions and install records

-   Get the subscriptions grouped by software model
-   For each software model
    -   Calculate total available rights (allocated and unallocated)
    -   Calculate the total allocated rights
    -   Calculate total unallocated rights
    -   If there are not enough rights, create Rights Needed By records
    -   Mark subscriptions and installs

# Code Flow

Recon follows a general framework which has the ReconciliationEngine as the entry point.  This entry point is triggered from the Recon scheduled job (SAM - Software License Reconciliation) or via the "Run Reconciliation" module from the UI.

The flow of the Recon is outside the scope of this article but is covered here:

-   KB1156740 SAMP: Reconciliation Primer (prerequisite knowledge)
-   KB1156739 SAMP: Reconciliation (High-Level Flow). 

SamUserSubscriptionLicenseCalculator implements the most specific methods for the license calculator framework.  It extends the SamLicenseCalculator script include.  The class structure is shown below:

-   SamLicenseCalculator
    -   SamUserSubscriptionLicenseCalculator

# Scheduled Jobs for Subscriptions

-   SAM - Import User Subscriptions – pulls subscription information from Microsoft and

Adobe uses publisher-specific APIs. Populates the Software Subscription table

-   SAM - Subscription Maintenance - Manages Reserve Entitlements. Creates subscription

entitlements after reserve entitlements expire

-   Subscription - Daily Job - Used for PA

# Plugins

-   Software Asset Management Professional for Microsoft (com.snc.samp.microsoft)
-   Software Asset Management Spoke  (sn\_sam\_spoke)
-   Software Asset Management - SaaS License Management  (sn\_sam\_saas )
-   Software Asset Management - SaaS License Management Integrations  (sn\_sam\_saas\_int)

# Troubleshooting

Issue: Reconciliation results do not reflect Office 365 correctly.

Check the data:

1.  Check inferred suite columns are being stamped correctly on the subscription and install
2.  Subscription has the User reference and correct SW Model
    1.  Sys\_user - missing Sys User record.  The record must exist with a matching email/User principal name.
    2.  SW Model matching on the subscription is based on the Subscription Product Definition (samp\_sw\_subscription\_product\_definition) table.
3.  Check Suites Related list in Software Model

3.  1.  Suite relationships
    2.  Apply to subscriptions flag is checked
4.  Setup issues with the O365 Subscription profile
    1.  See steps in the doc: [Integrations - Microsoft Office 365 Subscriptions](https://servicenow.sharepoint.com/:w:/r/sites/app-itam/Shared%20Documents/Product%20Management/Roadmap/Product%20Documentation/General/License%20Metrics/Setting%20up%20Microsoft%20Office%20365%20Integration-v1.1.docx?d=w8a782d7e20cb4a2d8576e1e555b79e82&csf=1&web=1&e=VIzeG5)
5.  Check Entitlement

-   1.  O365 should use the User Subscription license metric
    2.  Verify the End date and active
    3.  Verify Active rights > 0
-   True-up costs are higher than expected.
    1.  Verify the entitlements marked as **"Reserved Entitlements."**  Reserved entitlements can license existing subscriptions but the cost is counted as true up because the licenses will not be paid until the true up at the end of the year.  So if reserved entitlements exist, higher true-up costs (equal to the cost of reserved entitlements) are expected.

# Appendix

-   [Creating a Microsoft Office 365 Integration Profile](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/task/set-up-microsoft-office-365.html)
-   [Setting Up Microsoft Office 365 Integration](https://servicenow.sharepoint.com/:w:/r/sites/app-itam/Shared%20Documents/Product%20Management/Roadmap/Product%20Documentation/General/License%20Metrics/Setting%20up%20Microsoft%20Office%20365%20Integration-v1.1.docx?d=w8a782d7e20cb4a2d8576e1e555b79e82&csf=1&web=1&e=VIzeG5)
-   [O365 Optimizations TOI for Rome (video)](https://trainingops.servicenow.com/detail/videos/itam_______/video/6262096537001/rome:-itam---servicenow-office-365-optimization-recommendations)
-   [O365 Optimizations TOI for Rome (slides)](https://servicenow.sharepoint.com/:p:/r/sites/AppPlatformReleases/Shared%20Documents/Rome%20Release/Release%20Programs/Support%20TOI/FINAL%20Content/ITAM/office%20365%20License%20Optimization%20TOI-v4.0.pptx?d=w54231b0148bb49928e56db2cdbf2832b&csf=1&web=1&e=xWbnRZ)
