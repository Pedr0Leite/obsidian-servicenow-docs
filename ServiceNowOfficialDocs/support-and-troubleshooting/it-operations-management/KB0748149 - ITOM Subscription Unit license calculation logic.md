---
title: "ITOM Subscription Unit license calculation logic"
aliases:
  - KB0748149
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748149
kb_number: KB0748149
last_modified: 2026-06-24
---

## Issue

## Table of Contents

-   ## Table of Contents
    
    -   [Table of Contents](#mcetoc_1j2fokuc616)
    -   [General](#mcetoc_1g9ipaat1h)
        -   [ITOM Licensing Store application](#mcetoc_1g9ipc19l3)
        -   [Determining licensable CI classes](#mcetoc_1g9ipcv281)
        -   [Exclusions framework](#mcetoc_1g9ipe1d51)
        -   [ITOM/OT Licensing Dashboards](#mcetoc_1g9ipe1d51)
    -   [ITOM Discovery, ITOM Visibility, OT Foundation, OT Visibility](#mcetoc_1evd7v6v5se)
        -   [Daily Discovery and Service Graph count logic](#mcetoc_1evd7v6v5sf)
        -   [Daily Service Mapping logic and deduplication (ITOM/OT Visibility only)](#mcetoc_1evd7v6v5sg)
        -   [Counting across both Visibility and Discovery](#mcetoc_1evd7v6v5sh)
        -   [Viewing daily counts](#mcetoc_1evd7v6v5sh)
        -   [Viewing the list of licensed CIs](#mcetoc_1fbafgi792k)
        -   [Compliance-reported consumption](#mcetoc_1evd7v6v5si)
    -   [ITOM Health](#mcetoc_1evd7v6v5sj)
        -   [Daily event count logic](#mcetoc_1evd7v6v5sk)
        -   [Daily metric logic and deduplication](#mcetoc_1evd7v6v5sl)
        -   [Daily log logic and deduplication](#mcetoc_1evd7v6v5sm)
        -   [Viewing daily counts](#mcetoc_1evd7v6v5sn)
        -   [Viewing the list of licensed CIs](#mcetoc_1fbafgi792l)
        -   [Compliance-reported consumption](#mcetoc_1evd7v6v5so)
    -   [ITOM Health Log Analytics (HLA)](#mcetoc_1evd7v6v5sp)
        -   [Daily logs count logic](#mcetoc_1evd7v6v5sq)
        -   [Viewing daily counts](#mcetoc_1evd7v6v5ss)
        -   [Viewing the list of licensed CIs](#mcetoc_1fbafgi792m)
        -   [Compliance-reported consumption](#mcetoc_1evd7v6v5st)
    -   [ITOM Observability](#mcetoc_1evd7v6v5sp)
        -   [Daily Service Observability count logic](#mcetoc_1evd7v6v5sq)
        -   [Viewing daily counts](#mcetoc_1evd7v6v5ss)
        -   [Viewing the list of licensed CIs](#mcetoc_1fbafgi792m)
        -   [Compliance-reported consumption](#mcetoc_1evd7v6v5st)
    -   [ITOM Cloud Accelerate (formerly named ITOM Governance)](#mcetoc_1evd7v6v5sp)
        -   [Daily Cloud Account Management count logic](#mcetoc_1evd7v6v5sq)
        -   [Daily Cloud Services Catalog count logic](#mcetoc_1evd7v6v5sq)
        -   [Daily Cloud Configuration Governance count logic](#mcetoc_1evd7v6v5sq)
        -   [Daily Cloud Migration Assessment count logic](#mcetoc_1evd7v6v5sq)
        -   [Daily filtering logic for deduplicated CIs](#mcetoc_1evd7v6v5sq)
        -   [Viewing daily counts](#mcetoc_1evd7v6v5ss)
        -   [Viewing the list of licensed CIs](#mcetoc_1fbafgi792m)
        -   [Compliance-reported consumption](#mcetoc_1evd7v6v5st)
    -   [ITOM Optimization](#mcetoc_1evd7v6v5sp)
        -   [Daily Cloud Provisioning and Governance count logic](#mcetoc_1evd7v6v5sq)
        -   [Daily Cloud Insights count logic](#mcetoc_1evd7v6v5sr)
        -   [Viewing daily counts](#mcetoc_1evd7v6v5ss)
        -   [Viewing the list of licensed CIs](#mcetoc_1fbafgi792m)
        -   [Compliance-reported consumption](#mcetoc_1evd7v6v5st)
    -   [Digital End-User Experience (DEX)](#mcetoc_1evd7v6v5sj)
        -   [Daily Desktop Assistant count logic](#mcetoc_1evd7v6v5sq)
        -   [Daily SaaS monitoring count logic](#mcetoc_1evd7v6v5sq)
        -   [Daily Content Playbook count logic](#mcetoc_1evd7v6v5sq)
        -   [Daily filtering logic for deduplicated CIs](#mcetoc_1evd7v6v5sq)
        -   [Viewing daily counts](#mcetoc_1evd7v6v5sn)
        -   [Viewing the list of licensed CIs](#mcetoc_1fbafgi792l)
        -   [Compliance-reported consumption](#mcetoc_1evd7v6v5so)
    -   [Bundle vs a la Carte Subscriptions](#mcetoc_1evd7v6v5st)
    

## General

### ITOM Licensing Store application

In the San Diego release, the ITOM license counting implementation moved from begin delivered via the twice-per-year family releases to being delivered via the new [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb "ITOM Licensing Store app"). This will allow for more frequent updates, which will benefit customers running on a wider range of family release and patch versions. _**It is important to keep this application updated to the latest version**_.  Updates to this application are trued up in family releases and in patch releases as follows, and some ITOM store apps may have a dependency on a minimum version of the app, but there may still be a newer version available to upgrade to:

<table style="border-collapse: collapse; width: 84.907498%; height: 150px;" border="1"><tbody><tr style="height: 15px;"><td style="width: 17.83761%; height: 15px;"><strong>Platform release</strong></td><td style="width: 12.564858%; height: 15px;"><strong>Licensing app</strong></td><td style="width: 24.68097%; height: 15px;"><strong>Patch release</strong></td><td style="width: 11.555182%; height: 15px;"><strong>Licensing app</strong></td><td style="width: 19.856963%; height: 15px;"><strong>ITOM store app</strong></td><td style="width: 13.462347%; height: 15px;"><strong>Licensing app</strong></td></tr><tr><td style="width: 17.83761%;">&nbsp;</td><td style="width: 12.564858%;">&nbsp;</td><td style="width: 24.68097%;">&nbsp;</td><td style="width: 11.555182%;">&nbsp;</td><td style="width: 19.856963%;">&nbsp;</td><td style="width: 13.462347%;">&nbsp;</td></tr><tr><td style="width: 17.83761%;">&nbsp;</td><td style="width: 12.564858%;">&nbsp;</td><td style="width: 24.68097%;">&nbsp;</td><td style="width: 11.555182%;">&nbsp;</td><td style="width: 19.856963%;">&nbsp;</td><td style="width: 13.462347%;">&nbsp;</td></tr><tr><td style="width: 17.83761%;">Yokohama family</td><td style="width: 12.564858%;">v3.7</td><td style="width: 24.68097%;">Washington patch 10, Xanadu patch 6</td><td style="width: 11.555182%;">v3.7</td><td style="width: 19.856963%;">&nbsp;</td><td style="width: 13.462347%;">&nbsp;</td></tr><tr style="height: 30px;"><td style="width: 17.83761%; height: 30px;">Xanadu family</td><td style="width: 12.564858%; height: 30px;">v3.5</td><td style="width: 24.68097%; height: 30px;">Vancouver patch 10, Washington patch 4</td><td style="width: 11.555182%; height: 30px;">v3.5</td><td style="width: 19.856963%; height: 30px;">&nbsp;</td><td style="width: 13.462347%; height: 30px;">&nbsp;</td></tr><tr style="height: 30px;"><td style="width: 17.83761%; height: 30px;">&nbsp;</td><td style="width: 12.564858%; height: 30px;">&nbsp;</td><td style="width: 24.68097%; height: 30px;">Vancouver patch 9, Washington patch 2</td><td style="width: 11.555182%; height: 30px;">v3.4</td><td style="width: 19.856963%; height: 30px;">DEX Feb 2024</td><td style="width: 13.462347%; height: 30px;">v3.4</td></tr><tr style="height: 15px;"><td style="width: 17.83761%; height: 15px;">Washington DC family</td><td style="width: 12.564858%; height: 15px;">v3.3</td><td style="width: 24.68097%; height: 15px;">Utah patch 10, Vancouver patch 5</td><td style="width: 11.555182%; height: 15px;">v3.3</td><td style="width: 19.856963%; height: 15px;">Cloud Services Catalog</td><td style="width: 13.462347%; height: 15px;">v3.3</td></tr><tr style="height: 15px;"><td style="width: 17.83761%; height: 15px;">&nbsp;</td><td style="width: 12.564858%; height: 15px;">&nbsp;</td><td style="width: 24.68097%; height: 15px;">Utah patch 7, Vancouver patch 1</td><td style="width: 11.555182%; height: 15px;">v3.1</td><td style="width: 19.856963%; height: 15px;">&nbsp;</td><td style="width: 13.462347%; height: 15px;">&nbsp;</td></tr><tr style="height: 15px;"><td style="width: 17.83761%; height: 15px;">Vancouver family</td><td style="width: 12.564858%; height: 15px;">v3.0.1</td><td style="width: 24.68097%; height: 15px;">Utah patch 5, Tokyo patch 10</td><td style="width: 11.555182%; height: 15px;">v3.0.1</td><td style="width: 19.856963%; height: 15px;">&nbsp;</td><td style="width: 13.462347%; height: 15px;">&nbsp;</td></tr><tr style="height: 15px;"><td style="width: 17.83761%; height: 15px;">Utah family</td><td style="width: 12.564858%; height: 15px;">v2.3.1</td><td style="width: 24.68097%; height: 15px;">&nbsp;</td><td style="width: 11.555182%; height: 15px;">&nbsp;</td><td style="width: 19.856963%; height: 15px;">&nbsp;</td><td style="width: 13.462347%; height: 15px;">&nbsp;</td></tr><tr style="height: 15px;"><td style="width: 17.83761%; height: 15px;">Tokyo family</td><td style="width: 12.564858%; height: 15px;">v2.0</td><td style="width: 24.68097%; height: 15px;">&nbsp;</td><td style="width: 11.555182%; height: 15px;">&nbsp;</td><td style="width: 19.856963%; height: 15px;">&nbsp;</td><td style="width: 13.462347%; height: 15px;">&nbsp;</td></tr><tr><td style="width: 17.83761%; height: 15px;">San Diego family</td><td style="width: 12.564858%; height: 15px;">v1.0.6</td><td style="width: 24.68097%;">&nbsp;</td><td style="width: 11.555182%;">&nbsp;</td><td style="width: 19.856963%;">&nbsp;</td><td style="width: 13.462347%;">&nbsp;</td></tr></tbody></table>

### Determining licensable CI classes

The [ServiceNow ITOM Subscription Unit Overview](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/legal/it-operations-management-itom-servicenow-subscription-unit-overview.pdf "ServiceNow ITOM Subscription Unit Overview") describes the current resource categories and their respective CMDB classes under which we count CIs, and the ratios for equating to Subscription Unit counts. Note that while this is the latest revision of this document, an existing customer contract may be tied to an earlier revision of this document such as [this one](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/legal/servicenow-subscription-unit-overview.pdf "this one"), and the new revision will only apply to new contracts. Other versions of this document, e.g. for Telecommunication Service Operations Management or IoT, as well as all archived versions can be found [here](https://www.servicenow.com/products/entitlements-packages.html).

To see the licensable resource category names and the associated Subscription Unit ratios in effect for a given customer instance (where an SU-based subscription is installed and active), navigate to ITOM License à License Summary (which is actually just a view of Subscription Management records with a default filter that only lists ITOM-related Subscription entries). Open the ITOM-related Subscription, scroll down and view the ITOM CI subscription unit ratio tab. The listed licensable resource categories are generated from the customer contract. The CMDB CI classes used for each listed category can be found by navigating to ITOM License à License by CI Types. The CMDB classes listed under resource category names that resolve to entries in the Subscription Unit Metadata are the _effective licensable classes_.

Note that previously instances where the ITOM Subscription records cannot be inserted would not possess the ITOM SU metadata required for the ITOM Licensing logic to generate consumption counts.  However in v2.1 of the [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb "ITOM Licensing Store app") includes default ITOM SU metadata that will be used when no available from an ITOM Subscription record.  This will allow for SU counts to be generated for on-premise instances and other situations.  In the event you prefer not to have SU counts generated in an instance without an SU-based ITOM Subscription, set the system property sn\_itom\_licensing.enable\_license\_calculation\_without\_subscription (which is set to true by default) to false.

### Exclusions framework

The various exclusion and deduplication logic described in the sections that follow are mostly implemented via a generic exclusion framework.  The itom\_license\_exclusion\_metadata table contains the exclusion/deduplication rules, and each day the license\_exclusion\_list table contains the excluded CIs.  Note that a given CI could be listed more than once if it falls under the scope of more than one exclusion rule.

### ITOM/OT Licensing Dashboards

Included in v2.1 of the [ServiceNow ITOM/OT SU Licensing Store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb "ServiceNow ITOM/OT SU Licensing Store app") is a new dashboard that visualizes daily licensable resource counts (stacked by resource category), as well as the 90-day average SU consumption, over time. Navigate to Performance Analytics à Dashboards, then search for ITOM Licensing Dashboard or  OTM Licensing Dashboard.

Note that the daily count bars are raw resource counts without the impact of SU ratios, but the 90-day average SU count line does reflect the impact of SU ratios.

The following sections describe how the individual ITOM applications calculate their counts against those effective licensable classes and all their respective child classes.

## ITOM Discovery, ITOM Visibility, OT Foundation, OT Visibility

### Daily Discovery and Service Graph count logic

In our daily counts, we filter CIs in the CMDB of the effective licensable classes meeting the following criteria at that moment:

-   Duplicate of (duplicate\_of) is empty
-   Most Recent Discovery (last\_discovered)\* is within past 90 days
    -   Note that CIs managed by the OT Service Graph Connector for OT Excel Import are included without limit by date of last import
-   Discovery Source (discovery\_source)\* is servicenow, service-now, ACC-Visibility, or Kubernetes-Visibility-Agent  
    -   As Service Graph Connectors are installed, their identifier strings are added to the ITOM Licensing Discovery Sources (itom\_lu\_discovery\_sources) and ITOM LU Discovery Source Mappings (itom\_lu\_discovery\_source\_mapping) tables, and are added to this filter
        -   Note that prior to v3.1, there was a defect in SGC installation where their identifier strings were not added to both tables, causing CIs managed by only SGCs to not be properly counted.  When upgrading to v3.1 (manually or via upgrading the platform to Utah Patch 7 or Vancouver Patch 1) or beyond, the license counts may increase due to this correction.
    -   Note that the Service Graph Connector for SCCM no longer adds its identifier to this table, as it has been made freely available, without entitlement restriction or license usage impact
    -   In order to compensate for different CMDB input sources overwriting the discovery\_source and last\_discovered fields, in practice we also measure against the sys\_object\_source table, using the CI's sys\_id, evaluating the last\_scan and name fields of any matching entries. Manual queries against the CI attribute fields as shown above are typically consistent with our actual count algorithm, unless there are other sources that are overwriting these attributes.
    -   The DEXv2 solution includes ACC-Visibility for DEX-managed End User Devices, but when DEXv2 counts are calculated, and an ITOM exclusion of all DEXv2-counted CIs is generated and those DEXv2-managed CIs are not double-counted by ITOM
-   Status (install\_status) is not retired (7), stolen (8) or absent (100)
    -   As of v3.5 of the [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb), if csdm.lifecycle.migration.activated is set to true, CIs with the following combination of Life Cycle Stage and Life Cycle Stage Status values will be excluded instead of filtering by Status (install\_status):
        -   Life Cycle Stage = End of Life and Life Cycle Stage Status = Pending Disposal, Retired, In Transit, Disposed, Donated, RMA, Sold, Pending Certificate, Vendor Credit, Buyout, Lease Return, Expired, Cancelled or Obsolete
        -   Life Cycle Stage = Missing and Life Cycle Stage Status = Lost or Stolen
        -   Life Cycle Stage = Defective and Life Cycle Stage Status = In Stock or In Transit
-   For cmdb\_ci\_vm\_instance (and child class) CIs, we filter out those with Instantiates::Instantiated By, Virtualizes::Virtualized By or (for IBM LPAR Instances) Owns::Owned by relationships with cmdb\_ci\_server (or child class) CIs (which also meet the above criteria), to avoid duplicate counting of logical virtual servers that are represented by CIs of both classes
-   For cmdb\_ci\_virtualization\_server (and child class) CIs, we filter out those with Runs On::Runs relationships with cmdb\_ci\_server (or child class) CIs (which also meet the above criteria), to avoid duplicate counting of virtualization host and operating system discovery patterns that create independent CIs for the same server
-   Desktop exclusions from the Server category  
    -   We exclude CIs of type cmdb\_ci\_vmware\_instance (which is a child of cmdb\_ci\_vm\_instance) based on Guest ID (guest\_id) values that indicate Windows desktops: win2000ProGuest, win31Guest, win95Guest, win98Guest, windows7\_64Guest, windows7Guest, windows8\_64Guest, windows8Guest, windows9\_64Guest, windows9Guest, winVista64Guest, winVistaGuest, winXPHomeGuest, winXPPro64Guest, winXPProGuest, and (as of v3.6) windows11\_64Guest and windows12\_64Guest
    -   We exclude VMs virtualizing desktops from the cmdb\_ci\_vm\_instance class based on Virtualized by ::Virtualizes relationships to Computer (cmdb\_ci\_computer) CIs 
    -   We exclude Azure VDI CIs from the cmdb\_ci\_vm\_instance class based on Provisioned From::Provisioned relationships to Image (cmdb\_ci\_os\_template) CIs with Object ID (object\_id) values that start with /microsoftwindowsdesktop
    -   When Azure creates VDIs, it creates Host pools tags, which we store in the cmdb\_key\_value table for the associated VM Instance CI.  Based on these Azure-created tag values, we exclude VM Instance CIs with cmdb\_key\_value entries with _Key = CM-Resource\_Parent_ and Value contains Microsoft.DesktopVirtualization/hostpools/
    -   We exclude Hyper-V desktop CIs from the cmdb\_ci\_hyper\_v\_instance class based on Instantiates::Instantiated By relationships to cmdb\_ci\_computer CIs
    -   Note that when upgrading from a version/patch level prior to each of these changes to a version/patch level with one of these changes, there may be a noticeable decrease in subsequent daily counts
-   ITOM vs Operational Technology (OT) counts
    -   For ITOM counts: OT Asset Details (cmdb\_ot\_entity) attribute, which links to an entry in the OT Asset (cmdb\_ot\_entity) table is blank
    -   For OT counts: OT Asset Details (cmdb\_ot\_entity) attribute, which links to an entry in the OT Asset (cmdb\_ot\_entity) table is NOT blank. Note that CMDB sources that populate CIs for OT resources automatically will create this reference to a corresponding entry in the OT Asset table
    -   Note that if only an ITOM or an OT subscription are present (rather than both), but both ITOM and OT usage exists, CIs of licensable categories that are common to both ITOM and OT will be counted by the single subscription

\* In order to compensate for different CMDB input sources overwriting the discovery\_source and last\_discovered fields, in practice we measure against the sys\_object\_source table, using the CI's sys\_id, evaluating the last\_scan and name fields of any matching entries. Manual queries against the CI attribute fields as shown above are typically consistent with our actual count algorithm, unless there are other sources that are overwriting these attributes.

### Daily Service Mapping logic and deduplication (ITOM/OT Visibility only)

In these daily counts, ITOM Visibility also factors in CIs of the effective licensable classes that are associated (via svc\_ci\_assoc) to Service CIs of type Discovered (cmdb\_ci\_service\_discovered) or any of its subclasses with Service Type (type) attribute values of Discovered (2) or Tag-based (4).  The daily list of CIs managed just by Service Mapping is updated in the svc\_model\_assoc\_ci table.These CIs are de-duplicated against the CIs returned in the Daily Discovery & Service Graph count logic above. 

Note that CIs of licensable classes are not filtered by discovery source or most recent discovery date in the daily counts. Continued association to Services as described constitutes still being under management by the Service Mapping feature.

### Counting across both Visibility and Discovery

In some cases, customers may be entitled to both ITOM Visibility (a la carte or via a bundle) and ITOM Discovery.  To assign daily counts between these overlapping packages, resources on which Visibility features beyond just discovery/ACC-V/SGC (such as Svc Mapping) is seen is applied to the Visibility subscription.  Resources on which just discovery/ACC-V/SGC features are used is applied initially to the unused of a bundle subscription containing Visibility (if present), then spill over to unused capacity of the Visibility a la carte subscription (if present), and then finally can spill over to the Discovery subscription.  Excess usage will be reflected in Discovery, putting it into an over-utilized condition.

### Viewing daily counts

See the ITOM/OT Licensing Dashboard section above for the preferred view of daily counts.

The ITOM License à License Daily Usage Count option (or the OTM License à License Daily Usage Count option for OT resources) presents today's daily count entries, i.e. using the filter "Aggregated=false" (as the Aggregated field indicates that the value is a computed 90-day average) and "Created on Today" by default (which if viewed before the daily count is performed that day will appear empty). To see earlier entries, modify the default date filter and add a filter of "Application=Visibility" or "Application=Discovery".

Alternatively, daily counts can be viewed in ITOM License à License Report by changing the default "Aggregated=true" filter to "Aggregated=false", filtering by "Application=Visibility" or "Application=Discovery", and further filtering/sorting by CI Category or Updated as desired.

### Viewing the list of licensed CIs

The list of license-counted CIs (at the current moment, which may vary from the time of the last daily count) can be [generated on-demand](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/it-operations-management/task/itom-licensing-count.html) by navigating to ITOM License à Report ITOM Licensable CIs (or OTM License à Report OTM Licensable CIs for OT resources). Check the box for the Visibility application (and optionally any others), update the Max Results limit value(s) if needed, add any desired additional filter criteria, and then click Populate licensable CIs. This initiates a job that will populate a table of CIs in the background. Refresh this page until the Status column shows Completed. Then click Show Licensable CIs to open the results table, which can be further filtered and sorted as desired.

Note that in some instances the population job has become stuck in the Running state and cannot be canceled.  See [KB1000108](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000108) for steps to correct this.

Also note that if subscriptions to both ITOM Visibility (a la carte or via a bundle) and ITOM Discovery are present, the list of licensable CIs will contain overlaps, meaning some CIs will appear in both application lists, increasing the number of entries beyond the computed daily count.

### Compliance-reported consumption

Each day, we recompute the average of daily counts from the last 90 days, in order to smooth out potential high and low swings in increasingly dynamic environments. This 90-day moving average is reported as the official consumption value each day.

## ITOM Health

### Daily event count logic

When events are received by ITOM Health, an entry will either be added or updated in the Event Management License Usage (em\_unique\_nodes) table based on the monitored target specified in the health message. We attempt to link the License Usage entry to its corresponding CMDB CI; if a corresponding CI cannot be found for a monitored target (with the same domain value as in the event, per [KB0869379](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869379)), the License Usage entry will be assigned the type Unknown.

The CI association for licensing is based on the CI ultimately bound to the Alert, which may involve additional binding logic, and therefore can reduce the number of Unknown entries. Additionally, events that do not get promoted to the Alert stage will not update the License Usage, effectively ignoring sources for licensing whose events are ignored.

Entries in the Event Management License Usage table (em\_unique\_nodes) are removed once they have not been updated for 365 days.

The DEXv2 solution includes Event Management for DEX-managed End User Devices, but when DEXv2 counts are calculated, and an ITOM exclusion of all DEXv2-counted CIs is generated and those DEXv2-managed CIs are not double-counted by ITOM.

Note that the Event Management License Usage table was originally built for the Node-based model, and is still used to support customers on that legacy model. The Is Licensable column only applies to the Node-based licensing model.

In our daily counts, we filter entries in the License Usage table (em\_unique\_nodes) by their linked CIs (if they are of an effective licensable class) meeting the following criteria at that moment:

-   Duplicate of (duplicate\_of) is empty
-   Status (install\_status) is not retired (7), stolen (8) or absent (100)
    -   As of v3.1 of the [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb), if CSDM Lifecycle attributes are in use, CIs with the following combination of Life Cycle Status and Life Cycle Stage Status values will be excluded instead of filtering by Status (install\_status):
        -   Life Cycle Status = End of Life and Life Cycle Stage Status = Pending Disposal, Retired, In Transit, Disposed, Donated, RMA, Sold, Pending Certificate, Vendor Credit, Buyout, Lease Return, Expired, Cancelled or Obsolete
        -   Life Cycle Status = Missing and Life Cycle Stage Status = Lost or Stolen
        -   Life Cycle Status = Defective and Life Cycle Stage Status = In Stock or In Transit
-   For cmdb\_ci\_vm\_instances (and child class) CIs, we filter out those with Instantiates::Instantiated By, Virtualizes::Virtualized By or (for IBM LPAR Instances) Owns::Owned by relationships with cmdb\_ci\_server (or child class) CIs (which also meet the above criteria), to avoid duplicate counting of logical virtual servers that are represented by CIs of both classes
-   Desktop exclusions from the Server category  
    -   We exclude CIs of type cmdb\_ci\_vmware\_instance (which is a child of cmdb\_ci\_vm\_instance) based on Guest ID (guest\_id) values that indicate Windows desktops: win2000ProGuest, win31Guest, win95Guest, win98Guest, windows7\_64Guest, windows7Guest, windows8\_64Guest, windows8Guest, windows9\_64Guest, windows9Guest, winVista64Guest, winVistaGuest, winXPHomeGuest, winXPPro64Guest, winXPProGuest, and (as of v3.6) windows11\_64Guest and windows12\_64Guest
    -   We exclude Azure VDI CIs from the cmdb\_ci\_vm\_instance class based on Provisioned From::Provisioned relationships to Image (cmdb\_ci\_os\_template) CIs with Object ID (object\_id) values that start with /microsoftwindowsdesktop
    -   When Azure creates VDIs, it creates Host pools tags, which we store in the cmdb\_key\_value table for the associated VM Instance CI.  Based on these Azure-created tag values, we exclude VM Instance CIs with cmdb\_key\_value entries with _Key = CM-Resource\_Parent_ and Value contains Microsoft.DesktopVirtualization/hostpools/
    -   We exclude Hyper-V desktop CIs from the cmdb\_ci\_hyper\_v\_instance class based on Instantiates::Instantiated By relationships to cmdb\_ci\_computer CIs
    -   Note that when upgrading from a version/patch level prior to each of these changes to a version/patch level with one of these changes, there may be a noticeable decrease in subsequent daily counts

Daily counts also include entries of type Unknown, which are reflected as Unresolved Monitored Objects in the ITOM License à License Report list.

Note that closed alerts that are not updated for 90 days are automatically deleted from the Alerts table, so it may not be feasible to reconcile all entries in the Event Management License Usage (em\_unique\_nodes) table to the alerts that caused them.

### Daily metric logic and deduplication

In these daily counts, ITOM Health also factors in CIs of the effective licensable classes that are associated to MetricBase metrics. These CIs are de-duplicated against the CIs returned in the Daily event count logic above.

### Daily log logic and deduplication

ITOM Health Log Analytics is an add-on feature to ITOM Health, and depends upon ITOM Health. The standard ITOM Health subscription does not directly include this feature, but rather it is provided via either

-   an add-on subscription to ITOM Health (or a bundle that includes ITOM Health)
-   the ITOM Predictive AIOps subscription (which combines ITOM Health with Log Analytics),
-   the ITOM AIOps Enterprise bundle subscription (which bundles ITOM Health and Log Analytics with ITOM Visibility and ITOM Optimization).

When logs are received by ITOM Health Log Analytics, an entry will either be added or updated in the Occultus License Node (sn\_occ\_license\_node) table based on the host value extracted from the sourcetype structure step within the processing of each log line. (Note that a given host may have multiple applications sending logs, but these will all be related to the single host on which the application logs originate.) We attempt to link the License Node entry to its corresponding CMDB CI; if a corresponding CI cannot be found for a log source, the License Node entry will be assigned the type Unknown.

Entries in the Occultus License Node table are removed once they have not been updated for 365 days.

In our daily counts, we filter the entries in the Occultus License Node table by their linked CIs (if they are of an effective licensable class) using the same criteria as is used for event CIs (shown above). These filtered CIs and the unknown node names are de-duplicated against those returned in the Daily event and metric count logic above.

### Viewing daily counts

See the ITOM Licensing Dashboard section above for the preferred view of daily counts.

The ITOM License à License Daily Usage Count option presents today's daily count entries, i.e. using the filter "Aggregated=false" (as the Aggregated field indicates that the value is a computed 90-day average) and "Created on Today" by default (which if viewed before the daily count is performed that day will appear empty). To see earlier entries, modify the default date filter and add a filter of "Application=Health".

Alternatively, daily counts can be viewed in ITOM License à License Report by changing the default "Aggregated=true" filter to "Aggregated=false", filtering by "Application=Health", and further filtering/sorting by CI Category or Updated as desired.

### Viewing the list of licensed CIs

The list of license-counted CIs (at the current moment, which may vary from the time of the last daily count) can be [generated on-demand](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/it-operations-management/task/itom-licensing-count.html) by navigating to ITOM License à Report ITOM Licensable CIs. Check the box for the Health application (and optionally any others), update the Max Results limit value(s) if needed, add any desired additional filter criteria, and then click Populate licensable CIs. This initiates a job that will populate a table of CIs in the background. Refresh this page until the Status column shows Completed. Then click Show Licensable CIs to open the results table, which can be further filtered and sorted as desired.

Note that in some instances the population job has become stuck in the Running state and cannot be canceled.  See [KB1000108](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000108) for steps to correct this.

### Compliance-reported consumption

Each day, we recompute the average of daily counts from the last 90 days, in order to smooth out potential high and low swings in increasingly dynamic environments. This 90-day moving average is reported as the official consumption value each day.

## ITOM Health Log Analytics (HLA)

### Daily logs count logic

When logs are received by ITOM Health Log Analytics (HLA), an entry will either be added or updated in the Occultus License Nodes (sn\_occ\_license\_node) table based on the monitored target specified in the log message or the host from which the log was streamed. We attempt to link the Occultus License Nodes entry to its corresponding CMDB CI; if a corresponding CI cannot be found for a monitored target, the Occultus License Nodes entry will be assigned the type Unknown.

Entries in the Occultus License Nodes table are removed once they have not been updated for 365 days.

In our daily counts, we filter entries in the Occultus License Nodes table by their linked CIs (if they are of an effective licensable class) meeting the following criteria at that moment:

-   Duplicate of (duplicate\_of) is empty
-   Status (install\_status) is not retired (7), stolen (8) or absent (100)
    -   As of v3.1 of the [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb), if CSDM Lifecycle attributes are in use, CIs with the following combination of Life Cycle Status and Life Cycle Stage Status values will be excluded instead of filtering by Status (install\_status):
        -   Life Cycle Status = End of Life and Life Cycle Stage Status = Pending Disposal, Retired, In Transit, Disposed, Donated, RMA, Sold, Pending Certificate, Vendor Credit, Buyout, Lease Return, Expired, Cancelled or Obsolete
        -   Life Cycle Status = Missing and Life Cycle Stage Status = Lost or Stolen
        -   Life Cycle Status = Defective and Life Cycle Stage Status = In Stock or In Transit
-   For cmdb\_ci\_vm\_instances (and child class) CIs, we filter out those with Instantiates::Instantiated By, Virtualizes::Virtualized By or (for IBM LPAR Instances) Owns::Owned by relationships with cmdb\_ci\_server (or child class) CIs (which also meet the above criteria), to avoid duplicate counting of logical virtual servers that are represented by CIs of both classes
-   Desktop exclusions from the Server category  
    -   We exclude CIs of type cmdb\_ci\_vmware\_instance (which is a child of cmdb\_ci\_vm\_instance) based on Guest ID (guest\_id) values that indicate Windows desktops: win2000ProGuest, win31Guest, win95Guest, win98Guest, windows7\_64Guest, windows7Guest, windows8\_64Guest, windows8Guest, windows9\_64Guest, windows9Guest, winVista64Guest, winVistaGuest, winXPHomeGuest, winXPPro64Guest, winXPProGuest, and (as of v3.6) windows11\_64Guest and windows12\_64Guest
    -   We exclude Azure VDI CIs from the cmdb\_ci\_vm\_instance class based on Provisioned From::Provisioned relationships to Image (cmdb\_ci\_os\_template) CIs with Object ID (object\_id) values that start with /microsoftwindowsdesktop
    -   When Azure creates VDIs, it creates Host pools tags, which we store in the cmdb\_key\_value table for the associated VM Instance CI.  Based on these Azure-created tag values, we exclude VM Instance CIs with cmdb\_key\_value entries with _Key = CM-Resource\_Parent_ and Value contains Microsoft.DesktopVirtualization/hostpools/
    -   We exclude Hyper-V desktop CIs from the cmdb\_ci\_hyper\_v\_instance class based on Instantiates::Instantiated By relationships to cmdb\_ci\_computer CIs
    -   Note that when upgrading from a version/patch level prior to each of these changes to a version/patch level with one of these changes, there may be a noticeable decrease in subsequent daily counts

Daily counts also include entries of type Unknown, which are reflected as Unresolved Monitored Objects in the ITOM License à License Report list.

### Viewing daily counts

See the ITOM Licensing Dashboard section above for the preferred view of daily counts.

The ITOM License à License Daily Usage Count option presents today's daily count entries, i.e. using the filter "Aggregated=false" (as the Aggregated field indicates that the value is a computed 90-day average) and "Created on Today" by default (which if viewed before the daily count is performed that day will appear empty). To see earlier entries, modify the default date filter and add a filter of "Application=HLA".  

Alternatively, daily counts can be viewed in ITOM License à License Report by changing the default "Aggregated=true" filter to "Aggregated=false", filtering by "Application=HLA", and further filtering/sorting by CI Category or Updated as desired.

### Viewing the list of licensed CIs

The list of license-counted CIs (at the current moment, which may vary from the time of the last daily count) can be [generated on-demand](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/it-operations-management/task/itom-licensing-count.html) by navigating to ITOM License à Report ITOM Licensable CIs. Check the box for the HLA application (and optionally any others), update the Max Results limit value(s) if needed, add any desired additional filter criteria, and then click Populate licensable CIs. This initiates a job that will populate a table of CIs in the background. Refresh this page until the Status column shows Completed. Then click Show Licensable CIs to open the results table, which can be further filtered and sorted as desired.

Note that in some instances the population job has become stuck in the Running state and cannot be canceled.  See [KB1000108](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000108) for steps to correct this.

### Compliance-reported consumption

Each day, we recompute the average of daily counts from the last 90 days, in order to smooth out potential high and low swings in increasingly dynamic environments. This 90-day moving average is reported as the official consumption value each day.

## ITOM Observability

### Daily Service Observability count logic

When observability metrics are retrieved by Service Observability, an entry will either be added or updated in the Service Observability Entity Records (sn\_sow\_svcobs\_entity\_records) table based on the resource type for which metrics are retrieved. We attempt to link the Service Observability Entity Records entry to its corresponding CMDB CI; if a corresponding CI cannot be found for a monitored target, the \*\*\* License Nodes entry will be assigned the type Unknown.

Entries in the Service Observability Entity Records table are removed once they have not been updated for 365 days.

In our daily counts, we filter entries in the Service Observability Entity Records table by their linked CIs (if they are of an effective licensable class) meeting the following criteria at that moment:

-   Duplicate of (duplicate\_of) is empty
-   Status (install\_status) is not retired (7), stolen (8) or absent (100)
    -   As of v3.1 of the [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb), if CSDM Lifecycle attributes are in use, CIs with the following combination of Life Cycle Status and Life Cycle Stage Status values will be excluded instead of filtering by Status (install\_status):
        -   Life Cycle Status = End of Life and Life Cycle Stage Status = Pending Disposal, Retired, In Transit, Disposed, Donated, RMA, Sold, Pending Certificate, Vendor Credit, Buyout, Lease Return, Expired, Cancelled or Obsolete
        -   Life Cycle Status = Missing and Life Cycle Stage Status = Lost or Stolen
        -   Life Cycle Status = Defective and Life Cycle Stage Status = In Stock or In Transit
-   For cmdb\_ci\_vm\_instances (and child class) CIs, we filter out those with Instantiates::Instantiated By, Virtualizes::Virtualized By or (for IBM LPAR Instances) Owns::Owned by relationships with cmdb\_ci\_server (or child class) CIs (which also meet the above criteria), to avoid duplicate counting of logical virtual servers that are represented by CIs of both classes
-   Desktop exclusions from the Server category  
    -   We exclude CIs of type cmdb\_ci\_vmware\_instance (which is a child of cmdb\_ci\_vm\_instance) based on Guest ID (guest\_id) values that indicate Windows desktops: win2000ProGuest, win31Guest, win95Guest, win98Guest, windows7\_64Guest, windows7Guest, windows8\_64Guest, windows8Guest, windows9\_64Guest, windows9Guest, winVista64Guest, winVistaGuest, winXPHomeGuest, winXPPro64Guest, winXPProGuest, and (as of v3.6) windows11\_64Guest and windows12\_64Guest
    -   Azure VDI CIs from the cmdb\_ci\_vm\_instance class are excluded based on Provisioned From::Provisioned relationships to Image (cmdb\_ci\_os\_template) CIs with Object ID (object\_id) values that start with /microsoftwindowsdesktop
    -   When Azure creates VDIs, it creates Host pools tags, which we store in the cmdb\_key\_value table for the associated VM Instance CI.  Based on these Azure-created tag values, we exclude VM Instance CIs with cmdb\_key\_value entries with _Key = CM-Resource\_Parent_ and Value contains Microsoft.DesktopVirtualization/hostpools/
    -   We exclude Hyper-V desktop CIs from the cmdb\_ci\_hyper\_v\_instance class based on Instantiates::Instantiated By relationships to cmdb\_ci\_computer CIs
    -   Note that when upgrading from a version/patch level prior to each of these changes to a version/patch level with one of these changes, there may be a noticeable decrease in subsequent daily counts

Daily counts also include entries of type Unknown, which are reflected as Unresolved Monitored Objects in the ITOM License à License Report list.

### Viewing daily counts

Note that the ITOM Licensing Dashboard does not provide a view of daily counts For ITOM Observability yet, but is expected to soon.

The ITOM License à License Daily Usage Count option presents today's daily count entries, i.e. using the filter "Aggregated=false" (as the Aggregated field indicates that the value is a computed 90-day average) and "Created on Today" by default (which if viewed before the daily count is performed that day will appear empty). To see earlier entries, modify the default date filter and add a filter of "Application=Observability".  

Alternatively, daily counts can be viewed in ITOM License à License Report by changing the default "Aggregated=true" filter to "Aggregated=false", filtering by "Application=Observability", and further filtering/sorting by CI Category or Updated as desired.

### Viewing the list of licensed CIs

The list of license-counted CIs (at the current moment, which may vary from the time of the last daily count) can be [generated on-demand](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/it-operations-management/task/itom-licensing-count.html) by navigating to ITOM License à Report ITOM Licensable CIs. Check the box for the Observability application (and optionally any others), update the Max Results limit value(s) if needed, add any desired additional filter criteria, and then click Populate licensable CIs. This initiates a job that will populate a table of CIs in the background. Refresh this page until the Status column shows Completed. Then click Show Licensable CIs to open the results table, which can be further filtered and sorted as desired.

Note that in some instances the population job has become stuck in the Running state and cannot be canceled.  See [KB1000108](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000108) for steps to correct this.

### Compliance-reported consumption

Each day, we recompute the average of daily counts from the last 90 days, in order to smooth out potential high and low swings in increasingly dynamic environments. This 90-day moving average is reported as the official consumption value each day.

## ITOM Cloud Accelerate (formerly named ITOM Governance)

As of Nov 2023, ITOM Governance has been renamed to ITOM Cloud Accelerate.  ITOM SU Licensing store app v3.3 reflects this change in the licensing UI.

### Daily Cloud Account Management count logic

Each day, all CIs of the effective licensable classes that were coming under purview are listed in the sn\_itom\_cpg\_lu\_ci table.

Entries from this table are subsequently merged and deduplicated with CIs counted by other features of ITOM Cloud Accelerate into the itom\_lu\_governance\_ci table (see below).

### Daily Cloud Services Catalog count logic

Each day, all CIs of the effective licensable classes are identified that were provisioned or had their configurations updated (which can apply to cloud resources discovered & assigned to a user, rather than just provisioned via Cloud Services Catalog) are listed in the sn\_itom\_cpg\_lu\_ci table.

Entries from this table are subsequently merged and deduplicated with CIs counted by other features of ITOM Cloud Accelerate into the itom\_lu\_governance\_ci table (see below).

### Daily Cloud Configuration Governance count logic

Each day, all CIs of the effective licensable classes are identified that had their configurations scanned in any policy validation are listed in the sn\_itom\_ccg\_lu\_governance\_ci table.

Entries from this table are subsequently merged and deduplicated with CIs counted by other features of ITOM Cloud Accelerate into the itom\_lu\_governance\_ci table (see below).

### Daily Cloud Migration Assessment count logic

Each day, CIs of the effective licensable classes are identified that are assigned to an Assessment that has a status != Migration Completed.  These can be reviewed via the view sn\_cloud\_migration\_resource\_by\_task.

Entries from this table are subsequently merged and deduplicated with CIs counted by other features of ITOM Cloud Accelerate into the itom\_lu\_governance\_ci table (see below).

Note that Cloud Migration Assessment is being sunset from Zurich.

### Daily filtering logic for deduplicated CIs

Each day, CIs are merged and deduplicated from the tables of the various features of ITOM Cloud Accelerate into the itom\_lu\_governance\_ci table. This table is further filtered based on the following criteria:

-   Duplicate of (duplicate\_of) is empty
-   Status (install\_status) is not retired (7), stolen (8) or absent (100)
    -   As of v3.1 of the [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb), if CSDM Lifecycle attributes are in use, CIs with the following combination of Life Cycle Status and Life Cycle Stage Status values will be excluded instead of filtering by Status (install\_status):
        -   Life Cycle Status = End of Life and Life Cycle Stage Status = Pending Disposal, Retired, In Transit, Disposed, Donated, RMA, Sold, Pending Certificate, Vendor Credit, Buyout, Lease Return, Expired, Cancelled or Obsolete
        -   Life Cycle Status = Missing and Life Cycle Stage Status = Lost or Stolen
        -   Life Cycle Status = Defective and Life Cycle Stage Status = In Stock or In Transit
-   Desktop exclusions from the Server category  
    -   CIs of type cmdb\_ci\_vmware\_instance (which is a child of cmdb\_ci\_vm\_instance) are excluded based on Guest ID (guest\_id) values that indicate Windows desktops: win2000ProGuest, win31Guest, win95Guest, win98Guest, windows7\_64Guest, windows7Guest, windows8\_64Guest, windows8Guest, windows9\_64Guest, windows9Guest, winVista64Guest, winVistaGuest, winXPHomeGuest, winXPPro64Guest, winXPProGuest, and (as of v3.6) windows11\_64Guest and windows12\_64Guest
    -   Azure VDI CIs from the cmdb\_ci\_vm\_instance class are excluded based on Provisioned From::Provisioned relationships to Image (cmdb\_ci\_os\_template) CIs with Object ID (object\_id) values that start with /microsoftwindowsdesktop
    -   When Azure creates VDIs, it creates Host pools tags, which we store in the cmdb\_key\_value table for the associated VM Instance CI.  Based on these Azure-created tag values, we exclude VM Instance CIs with cmdb\_key\_value entries with _Key = CM-Resource\_Parent_ and Value contains Microsoft.DesktopVirtualization/hostpools/
    -   Hyper-V desktop CIs from the cmdb\_ci\_hyper\_v\_instance class are excluded based on Instantiates::Instantiated By relationships to cmdb\_ci\_computer CIs
    -   Note that when upgrading from a version/patch level prior to each of these changes to a version/patch level with one of these changes, there may be a noticeable decrease in subsequent daily counts

### Viewing daily counts

See the ITOM Licensing Dashboard section above for the preferred view of daily counts.

The ITOM License à License Daily Usage Count option presents today's daily count entries, i.e. using the filter "Aggregated=false" (as the Aggregated field indicates that the value is a computed 90-day average) and "Created on Today" by default (which if viewed before the daily count is performed that day will appear empty). To see earlier entries, modify the default date filter and add a filter of "Application=Cloud Accelerate".  

Alternatively, daily counts can be viewed in ITOM License à License Report by changing the default "Aggregated=true" filter to "Aggregated=false", filtering by "Application=Cloud Accelerate", and further filtering/sorting by CI Category or Updated as desired.

### Viewing the list of licensed CIs

The list of license-counted CIs (at the current moment, which may vary from the time of the last daily count) can be [generated on-demand](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/it-operations-management/task/itom-licensing-count.html) by navigating to ITOM License à Report ITOM Licensable CIs. Check the box for the Cloud Accelerate application (and optionally any others), update the Max Results limit value(s) if needed, add any desired additional filter criteria, and then click Populate licensable CIs. This initiates a job that will populate a table of CIs in the background. Refresh this page until the Status column shows Completed. Then click Show Licensable CIs to open the results table, which can be further filtered and sorted as desired.

Note that in some instances the population job has become stuck in the Running state and cannot be canceled.  See [KB1000108](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000108) for steps to correct this.

### Compliance-reported consumption

Each day, we recompute the average of daily counts (deduplicated between the various features of ITOM Cloud Accelerate) from the last 90 days, in order to smooth out potential high and low swings in increasingly dynamic environments. This 90-day moving average is reported as the official consumption value each day.

## ITOM Optimization

### Daily Cloud Provisioning and Governance count logic

Each day, Cloud Provisioning and Governance counts CIs of the effective licensable classes meeting the following criteria at that moment:

-   Duplicate of (duplicate\_of) is empty
-   Status (install\_status) is not retired (7), stolen (8) or absent (100)
    -   As of v3.1 of the [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb), if CSDM Lifecycle attributes are in use, CIs with Life Cycle Stage values of End of Life, Missing and Defective will be excluded instead of filtering by Status (install\_status):
        -   Life Cycle Status = End of Life and Life Cycle Stage Status = Pending Disposal, Retired, In Transit, Disposed, Donated, RMA, Sold, Pending Certificate, Vendor Credit, Buyout, Lease Return, Expired, Cancelled or Obsolete
        -   Life Cycle Status = Missing and Life Cycle Stage Status = Lost or Stolen
        -   Life Cycle Status = Defective and Life Cycle Stage Status = In Stock or In Transit
-   Has a relationship to a Stack Item (sn\_cmp\_stack\_item) entry, which itself has the following criteria:  
    -   Status (status) is not Error (3)
    -   Related to a Stack (sn\_cmp\_stack) entry with a stack\_status that is not Unmanaged (7)

CIs meeting these criteria are added to the sn\_itom\_opt\_lic\_ci table, in order to deduplicate CIs also counted that day by the Cloud Insights feature of the previous ITOM Optimization subscription (see below).

### Daily Cloud Insights count logic

\[**Note**: The original ITOM Optimization package included Cloud Insights, however in Q1 2021 this package was revised to remove Cloud Insights, in favor of packaging this capability via Software Asset Management Enterprise. Therefore, depending on which package revision has been purchased, this may or may not apply.\]

Cloud Insights regularly processes billing information from cloud providers such as AWS or Azure. For each unique cloud resource instance for which the cloud provider is charging, we use the CMDB Identification and Reconciliation Engine to identify or create a corresponding CI. We create billing metrics in MetricBase linked to each CI for each hour that the resource was running and billed by the cloud provider.

Each day, Cloud Insights counts the CIs of the effective licensable classes that have billing metrics in MetricBase from the last 24 hours (which indicates that the cloud resource instance was running in that time period).

CIs meeting these criteria are added to the sn\_itom\_opt\_lic\_ci table, in order to deduplicate CIs also counted that day by the Cloud Provisioning and Governance feature of ITOM Optimization.

### Viewing daily counts

See the ITOM Licensing Dashboard section above for the preferred view of daily counts.

The ITOM License à License Daily Usage Count option presents today's daily count entries, i.e. using the filter "Aggregated=false" (as the Aggregated field indicates that the value is a computed 90-day average) and "Created on Today" by default (which if viewed before the daily count is performed that day will appear empty). To see earlier entries, modify the default date filter and add a filter of "Application=Optimization".

Alternatively, daily counts can be viewed in ITOM License à License Report by changing the default "Aggregated=true" filter to "Aggregated=false", filtering by "Application=Optimization", and further filtering/sorting by CI Category or Updated as desired.

### Viewing the list of licensed CIs

The list of license-counted CIs (at the current moment, which may vary from the time of the last daily count) can be [generated on-demand](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/it-operations-management/task/itom-licensing-count.html) by navigating to ITOM License à Report ITOM Licensable CIs. Check the box for the Optimization application (and optionally any others), update the Max Results limit value(s) if needed, add any desired additional filter criteria, and then click Populate licensable CIs. This initiates a job that will populate a table of CIs in the background. Refresh this page until the Status column shows Completed. Then click Show Licensable CIs to open the results table, which can be further filtered and sorted as desired.

Note that in some instances the population job has become stuck in the Running state and cannot be canceled.  See [KB1000108](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000108) for steps to correct this.

### Compliance-reported consumption

Each day, we recompute the average of daily counts (deduplicated between the Cloud Provisioning and Governance and Cloud Insights features, if applicable) from the last 90 days, in order to smooth out potential high and low swings in increasingly dynamic environments. This 90-day moving average is reported as the official consumption value each day.

## Digital End-User Experience (DEX)

### Daily Desktop Assistant count logic

Each day, all CIs where the DEX Desktop Assistant has been deployed are listed in the sn\_dex\_desktop\_exp table.

Entries from this table are subsequently merged and deduplicated with CIs counted by other features of DEX into the sn\_itom\_licensing\_itom\_lu\_dex\_ci table (see below).

### Daily SaaS monitoring count logic

Each day, all CIs from which SaaS application monitoring data from the DEX Browser Plugin has been received in the past 90 days are listed in the dex\_ci\_browser\_extension table.

Entries from this table are subsequently merged and deduplicated with CIs counted by other features of DEX into the sn\_itom\_licensing\_itom\_lu\_dex\_ci table (see below).

### Daily Content Playbook count logic

Each day, End User Devices on which Playbooks have been deployed are identified via Computer (cmdb\_ci\_computer) CIs with discovery source of DEX (as identified in the sys\_object\_source table).

These CIs are subsequently merged and deduplicated with CIs counted by other features of DEX into the sn\_itom\_licensing\_itom\_lu\_dex\_ci table (see below).

### Daily filtering logic for deduplicated CIs

Each day, CIs are merged and deduplicated from the tables of the various features of DEX into the sn\_itom\_licensing\_itom\_lu\_dex\_ci table. This table is further filtered based on the following criteria:

-   Duplicate of (duplicate\_of) is empty
-   Status (install\_status) is not retired (7), stolen (8) or absent (100)
    -   As of v3.1 of the [ITOM SU Licensing store app](https://store.servicenow.com/sn_appstore_store.do#!/store/application/4cce117e53b9301046dfddeeff7b12eb), if CSDM Lifecycle attributes are in use, CIs with the following combination of Life Cycle Status and Life Cycle Stage Status values will be excluded instead of filtering by Status (install\_status):
        -   Life Cycle Status = End of Life and Life Cycle Stage Status = Pending Disposal, Retired, In Transit, Disposed, Donated, RMA, Sold, Pending Certificate, Vendor Credit, Buyout, Lease Return, Expired, Cancelled or Obsolete
        -   Life Cycle Status = Missing and Life Cycle Stage Status = Lost or Stolen
        -   Life Cycle Status = Defective and Life Cycle Stage Status = In Stock or In Transit

### Viewing daily counts

See the ITOM Licensing Dashboard section above for the preferred view of daily counts.

The ITOM License à License Daily Usage Count option presents today's daily count entries, i.e. using the filter "Aggregated=false" (as the Aggregated field indicates that the value is a computed 90-day average) and "Created on Today" by default (which if viewed before the daily count is performed that day will appear empty). To see earlier entries, modify the default date filter and add a filter of "Application=DEX".

Alternatively, daily counts can be viewed in ITOM License à License Report by changing the default "Aggregated=true" filter to "Aggregated=false", filtering by "Application=DEX", and further filtering/sorting by CI Category or Updated as desired.

### Viewing the list of licensed CIs

The list of license-counted CIs (at the current moment, which may vary from the time of the last daily count) can be [generated on-demand](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/it-operations-management/task/itom-licensing-count.html) by navigating to ITOM License à Report ITOM Licensable CIs. Check the box for the DEX application (and optionally any others), update the Max Results limit value(s) if needed, add any desired additional filter criteria, and then click Populate licensable CIs. This initiates a job that will populate a table of CIs in the background. Refresh this page until the Status column shows Completed. Then click Show Licensable CIs to open the results table, which can be further filtered and sorted as desired.

Note that in some instances the population job has become stuck in the Running state and cannot be canceled.  See [KB1000108](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000108) for steps to correct this.

### Compliance-reported consumption

Each day, we recompute the average of daily counts from the last 90 days, in order to smooth out potential high and low swings in increasingly dynamic environments. This 90-day moving average is reported as the official consumption value each day.

## Bundle vs a la Carte Subscriptions

To purchase entitlement to a given ITOM application listed above, a customer may purchase a subscription for that application specifically (referred to as an "a la carte" subscription), or via a subscription that bundles entitlement to multiple ITOM applications at once, or both.

If a customer purchases a bundle subscription for a certain number of Subscription Units (SUs), they effectively have entitlement to that many SUs for each of the bundled ITOM applications. If they purchase an a la carte subscription for a particular ITOM application, that SU entitlement is added to whatever may have been purchased via a bundle subscription.

When Subscription Unit consumption for a given ITOM application is calculated (using the ratios and 90-day moving average), it is applied first against any bundle subscription that contains that ITOM application thatmay have been purchased, and then only if there insufficient entitlement in a bundle to cover that ITOM application's consumption will the remainder be applied to an a la carte subscription if one has been purchased.

Please note that the bundle subscription includes multiple ITOM applications.  
However, the consumption for the bundle subscription is determined by the ITOM application with the highest usage, rather than the total consumption of all ITOM applications.  
  
For example, the customer is subscribed to the "ITOM AIOps Enterprise v2 - Subscription Unit" bundle, which includes the following consumptions:  
ITOM Visibility - 3000  
ITOM Health - 1500  
  
The consumption of "ITOM AIOps Enterprise v2 - Subscription Unit" will be based on ITOM Visibility, which is 3000, rather than 4500.

The usage definitions for the individual ITOM application SU consumptions prior to being attributed to the purchased subscriptions are as follows:

-   ITOM Discovery: DEFN1006848
-   ITOM Visibility: DEFN1006829
-   ITOM Health: DEFN1006832
-   ITOM HLA: DEFN1006833
-   ITOM Cloud Accelerate (formerly Governance): DEFN1006830
-   ITOM Optimization: DEFN1006828

The usage definitions for the daily SU consumption for the a la carte and bundle subscriptions are as follows:

-   Collect the licensing usage data for ITOM Prime SKU: DEFN2021966
-   Collect the licensing usage data for ITOM Prime Tanium SKU: DEFN2021972
-   Collect the licensing usage data for ITOM Advanced SKU: DEFN2021995
-   Collect the licensing usage data for ITOM Advanced Tanium SKU: DEFN2021963
-   Collect the licensing usage data for ITOM AIOps Enterprise V2 SKU: DEFN2021964
-   Collect the licensing usage data for ITOM AIOps Enterprise V3 SKU: DEFN2021965
-   Collect the licensing usage data for ITOM Visibility SKU: DEFN2021994
-   Collect the licensing usage data for ITOM Health SKU: DEFN2021959
-   Collect the licensing usage data for ITOM Health V4 SKU: DEFN2021960
-   Collect the licensing usage data for ITOM HLA SKU: DEFN2021961
-   Collect the licensing usage data for ITOM HLA V4 SKU: DEFN2021962
-   Collect the licensing usage data for ITOM Discovery SKU: DEFN2021954
-   Collect the licensing usage data for ITOM Discovery V4 SKU: DEFN2021955
-   Collect the licensing usage data for ITOM Observability SKU: DEFN2021978
-   Collect the licensing usage data for ITOM Observability V4 SKU: DEFN2021979
-   Collect the licensing usage data for ITOM Api Insights SKU: DEFN2021949
-   Collect the licensing usage data for ITOM Api Insights V4 SKU: DEFN2021950
-   Collect the licensing usage data for ITOM Dex SKU: DEFN2021951
-   Collect the licensing usage data for ITOM Dex V2 SKU: DEFN2021952
-   Collect the licensing usage data for ITOM Dex V4 SKU: DEFN2021953
-   Collect the licensing usage data for ITOM Governance SKU: DEFN2021956
-   Collect the licensing usage data for ITOM Governance V4 SKU: DEFN2021957
-   Collect the licensing usage data for ITOM Governance SKU: DEFN2021971
-   Collect the licensing usage data for ITOM Optimization SKU: DEFN2021980
-   Collect the licensing usage data for ITOM Optimization V2 SKU: DEFN2021984
-   Collect the licensing usage data for ITOM Optimization V4 SKU: DEFN2021985
-   Collect the licensing usage data for ITOM Enterprise SKU: DEFN2021967
-   Collect the licensing usage data for ITOM Enterprise V2 SKU: DEFN2021968
-   Collect the licensing usage data for ITOM Enterprise V3 SKU: DEFN2021969
-   Collect the licensing usage data for ITOM Enterprise V4 SKU: DEFN2021970
-   Collect the licensing usage data for ITOM Pro SKU: DEFN2021974
-   Collect the licensing usage data for ITOM Pro V4 SKU: DEFN2021975
-   Collect the licensing usage data for ITOM Standard SKU: DEFN2021976
-   Collect the licensing usage data for ITOM Standard V4 SKU: DEFN2021977
-   Collect the licensing usage data for OTM Discovery SKU: DEFN2021986
-   Collect the licensing usage data for OTM Foundation SKU: DEFN2021987
-   Collect the licensing usage data for OTM Health SKU: DEFN2021988
-   Collect the licensing usage data for OTM HLA SKU: DEFN2021989
-   Collect the licensing usage data for OTM Observability SKU: DEFN2021990
-   Collect the licensing usage data for OTM Standard SKU: DEFN2021991
-   Collect the licensing usage data for OTM Pro SKU: DEFN2021992
-   Collect the licensing usage data for OTM Visibility SKU: DEFN2021993

The usage definitions for the a la carte and bundle subscriptions are as follows:

-   ITOM Prime: DEFN2019793
-   ITOM Advanced: DEFN2019797
-   ITOM Prime with Tanium Endpoint Management Bundle: DEFN2021723
-   ITOM Discovery: DEFN1003616
-   ITOM Visibility: DEFN1001294
-   DEX v2: DEFN2005859
-   ITOM Health, ITOM Predictive AIOps: DEFN1001297
-   ITOM Health Log Analytics: DEFN1006525
-   ITOM Cloud Accelerate (formerly Governance): DEFN2009014
-   ITOM Optimization: DEFN1003917
-   ITOM Operator Standard: DEFN1001299
-   ITOM Operator/AIOps Professional: DEFN1001296
-   ITOM Operator Enterprise: DEFN1005622
-   ITOM AIOps Enterprise: DEFN2011356
-   Pre-2025 ITOM AIOps Enterprise: DEFN1005619
-   Pre-2022 versions of ITOM Operator Enterprise, ITOM AIOps Enterprise: DEFN1003918
-   OT Foundation: DEFN2005873
-   OT Visibility: DEFN1004964

## Resolution

n/a
