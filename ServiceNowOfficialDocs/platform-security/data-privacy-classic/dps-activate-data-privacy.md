---
title: Activate data privacy
description: Data Privacy includes data classification and anonymization and is installed from the ServiceNow Store.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/data-privacy-classic/dps-activate-data-privacy.html
release: australia
product: Data Privacy \(Classic\)
classification: data-privacy-classic
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Data privacy, Data Privacy, Platform Privacy]
tags:
  - platform-security
  - data-privacy
  - consent
  - gdpr
  - classic
  - type-task
---

# Activate data privacy

[[data-privacy-landing|Data Privacy]] includes [[data-classification|data classification]] and anonymization and is installed from the ServiceNow Store.

## Before you begin

To use [[dps-data-anonymization|data anonymization]], [[data-privacy-classic|Data Privacy \(Classic\)]] must first be activated with the [[servicenow-vault-landing|ServiceNow Vault]] entitlement. See [Activate data privacy \(Classic\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/data-privacy-classic/install-data-privacy.md) for additional information.

**Note:** Installing the Data Privacy Store App will auto install the [[dds-data-discovery|Data Discovery Store]] App, Data Privacy \(Classic\) plug-in, and the Data Classification plugin.

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All** &gt; **Data Privacy**.

2.  Find the application using the [[adaptive-auth-filter-criteria|filter criteria]] and search bar.

    You can search for the application by its name or ID. If you cannot find an application, you may have to [[c_requestAPI|request]] it from the ServiceNow Store.

    Visit the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/home) to view all the available apps, and for information about submitting requests to the store. For cumulative release notes information for all released apps, see the [ServiceNow Store version history release notes](https://www.servicenow.com/docs/bundle/store-release-notes/page/release-notes/store/sn-store-release-notes.html).

3.  Select a version from the list and select **Install**.

    In the Install dialog that is displayed, any dependencies that are installed along with your application are listed.

4.  If you are prompted, follow the links to the ServiceNow Store to get any additional entitlements for dependencies.

5.  If demo data is available and you want to install it, select the **Load demo data** check box.

    Demo data comprises sample records that describe application features for common use cases. Load demo data when you first install the application on a development or test instance.

    **Important:** If you don't load the demo data during installation, it's unavailable to load later.

6.  Select **Install**.

## Related

- [[data-privacy-landing|Data Privacy]]
- [[data-classification|Data Classification]]
- [[dps-data-anonymization|Data anonymization]]
- [[data-privacy-classic|Data privacy \(Classic\)]]
- [[servicenow-vault-landing|ServiceNow Vault]]
- [[dds-data-discovery|Data Discovery Store]]
- [[adaptive-auth-filter-criteria|Filter criteria]]
- [[c_requestAPI|request]]
