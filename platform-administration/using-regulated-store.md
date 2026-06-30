---
title: Using the ServiceNow Store in a regulated environment
description: Certain regulated environments require an isolated instance of the ServiceNow Store to meet data security requirements. If your instance is in a regulated environment, you might need to get apps and products from a federal or regional version of the ServiceNow Store.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/using-regulated-store.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [ServiceNow Store, Administering applications, Get started, Administer the ServiceNow AI Platform]
---

# Using the ServiceNow Store in a regulated environment

Certain regulated environments require an isolated instance of the [[servicenow-store|ServiceNow Store]] to meet data security requirements. If your instance is in a regulated environment, you might need to get apps and products from a federal or regional version of the ServiceNow Store.

## Overview of using the ServiceNow Store in a regulated environment

Regulated instances of the ServiceNow AI Platform are hosted in datacenters that comply with the specific regional, organizational, or governmental needs of the customers that use them. With a regulated instance, an organization or government body can determine specific requirements, including data residency, privacy and security, and compliance requirements.

Some regulated environments require their own isolated instances of the ServiceNow Store to meet security requirements. Isolated instances of the ServiceNow Store are available in both federal and regional regulated instances.

Not all regulated environments require an isolated instance of the ServiceNow Store. If your environment doesn't have access to an isolated federal or regional ServiceNow Store, use the commercial  instead. For more information about which environments have access to an isolated federal or regional ServiceNow Store, see [[isolated-store-instances|Environments with federal or regional ServiceNow Store instances]].

**Important:** Applications and products available in federal and regional instances of the ServiceNow Store aren't accredited. You must perform your own security review to confirm that an application or product meets the requirements for your regulated instance.

\[Omitted image "MMASSET0020992-regulatedstoreworkflow-landing.png"\] Alt text: An infographic showing a workflow for accessing the correct ServiceNow Store version, procuring an app, and installing the app. For more details, refer to the following description.

1.  Access the correct version of the ServiceNow Store for your environment.
    -   If your regulated environment has an isolated federal or regional instance of the ServiceNow Store, see [[access-regulated-store|Access the ServiceNow Store for a regulated environment]].
    -   If your regulated environment doesn't require an isolated federal or regional instance, use the procurement process for the commercial  instead. For information about procuring apps from the commercial ServiceNow Store, refer to [[getting-apps-trials|Getting apps and trials from the ServiceNow Store]].
2.  Procure an application from an isolated federal or regional instance of the ServiceNow Store.
    -   To request a 30-day trial, log in to your federal or regional instance of the ServiceNow Store and use the same process that users of the commercial ServiceNow Store do. For more information, see [[start-trial|Start an application trial from the ServiceNow Store]].
    -   To get an application that's available at no additional cost, log in to your federal or regional instance of the ServiceNow Store and use the same process that users of the commercial ServiceNow Store do. For more information, see [[store-get-free-app|Get a free application]].
    -   To request a paid application, see [[request-paid-app-regulated|Request a paid app for a regulated environment]].
    -   To complete procurement of an application for an on-premise instance, see [[get-app-on-prem|Get an app or product as an on-premise customer]].
3.  Install an application in a regulated environment.
    -   If you have a hosted instance in a regulated environment, see [Install an application or plugin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/application-manager/installing-applications-in-application-manager.md).
    -   If you self-host your instance, see [[upload-app-on-prem-instance|Upload an app to an on-premise instance]].

## Additional info

-   [Environments with federal or regional ServiceNow Store instances](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/isolated-store-instances.md)

    Certain regulated environments contain an isolated instance of the ServiceNow Store to support data security requirements. Find out whether your environment has its own federal or regional instance of the ServiceNow Store.

-   [[unavailable-listing-reg-store|Listing types not available in regulated environments]]

    To preserve data privacy standards, certain types of app listings can't be offered in federal or regional instances of the ServiceNow Store.

-   [[sn-store-tncs|Terms and conditions in the ServiceNow Store]]

    Learn about when terms and conditions must be accepted in the ServiceNow Store. Unaccepted terms and conditions block procurement and installations.

## Related

- [[isolated-store-instances|Environments with federal or regional ServiceNow Store instances]]
- [[access-regulated-store|Access the ServiceNow Store for a regulated environment]]
- [[getting-apps-trials|Getting apps and trials from the ServiceNow Store]]
- [[start-trial|Start an application trial from the ServiceNow Store]]
- [[store-get-free-app|Get a free application]]
- [[request-paid-app-regulated|Request a paid app for a regulated environment]]
- [[get-app-on-prem|Get an app or product as an on-premise customer]]
- [[upload-app-on-prem-instance|Upload an app to an on-premise instance]]
- [[unavailable-listing-reg-store|Listing types not available in regulated environments]]
- [[sn-store-tncs|Terms and conditions in the ServiceNow Store]]
- [[servicenow-store|ServiceNow Store]]
