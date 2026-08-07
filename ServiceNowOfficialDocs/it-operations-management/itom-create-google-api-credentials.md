---
title: Configure the Google API credentials for Cloud Discovery
description: Create Google API credentials to allow Cloud Discovery to access the data on your Google account securely.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/itom-create-google-api-credentials.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Set up Google Cloud Platform service accounts, Set up a cloud service account, Access to cloud environments for ITOM products, IT Operations Management]
tags:
  - it-operations-management
  - type-task
---

# Configure the Google API credentials for Cloud Discovery

Create Google API credentials to allow Cloud [[r-discovery|Discovery]] to access the data on your Google account securely.

## Before you begin

Ensure that the latest versions of the following applications are installed:

-   Discovery and [[c_ServiceMappingOverview|Service Mapping]] Patterns
-   Visibility Content
-   CMDB CI Class Models

Role required: discovery\_admin

## Procedure

1.  Configure the GCP credentials either by importing a JSON file or by filing in the record manually.

<table id="choicetable_fch_mpt_c1c"><thead><tr><th align="left" id="d365925e93">

Option

</th><th align="left" id="d365925e96">

Actions

</th></tr></thead><tbody><tr><td id="d365925e102">

**Import the JSON file**

</td><td>

1.  When receiving the email from GCP, download the JSON file.
2.  Navigate to **Discovery** &gt; **Credentials**.
3.  Select **New** and then select **Google API Credentials**.
4.  Select **Import JSON File**
5.  Select **Choose File** and choose the JSON file you downloaded.
6.  Select **Upload Credential Data**.


</td></tr><tr><td id="d365925e165">

**Configure the credentials manually**

</td><td>

1.  Navigate to **Discovery** &gt; **Credentials**.
2.  Select **New** and then select **Google API Credentials**.
3.  Select **New**.
4.  In the form, fill in the fields according to the form description.

For description of the form fields, see [[google-api-credentials-form|Google API Credentials Form]].

5.  Select **Submit**.


</td></tr></tbody>
</table>
**Parent Topic:**[[set-up-gcp-service-accounts|Set up Google Cloud Platform service accounts]]

## Related

- [[google-api-credentials-form|Google API Credentials Form]]
- [[set-up-gcp-service-accounts|Set up Google Cloud Platform service accounts]]
- [[r-discovery|Discovery]]
- [[c_ServiceMappingOverview|Service Mapping]]
