---
title: Set up Google Cloud Platform service accounts
description: Create and configure cloud service accounts at ServiceNow AI Platform for the corresponding Google Cloud Platform \(GCP\) service accounts.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/set-up-gcp-service-accounts.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Set up a cloud service account, Access to cloud environments for ITOM products, IT Operations Management]
---

# Set up Google Cloud Platform service accounts

Create and configure cloud service accounts at ServiceNow AI Platform for the corresponding Google Cloud Platform \(GCP\) service accounts.

GCP service account is a unique account typically used by an application or compute workload, such as a Compute Engine instance, rather than a user. A service account is identified by its email address, which is unique to the account. It’s used to authenticate and authorize interactions between your application and various GCP services.

## Verify the REST API Permissions

Download the [Cloud Discovery patterns spreadsheet](https://downloads.docs.servicenow.com/resource/enus/api/servicenow-discovery-patterns-api-details.xlsx) so you can grant user permissions required for running the [[r-discovery|Discovery]] patterns. In addition to permissions, the spreadsheet also includes useful information such as pattern names, types, CI Classes, and links to vendor documentation. New patterns are available quarterly, so check periodically to be sure you have the latest version of the spreadsheet.

-   **[[itom-create-google-api-credentials|Configure the Google API credentials for Cloud Discovery]]**  
Create Google API credentials to allow Cloud Discovery to access the data on your Google account securely.
-   **[[google-api-credentials-form|Google API Credentials Form]]**  
Fill in the Google API Credentials form to configure the credentials.
-   **[[create-gcp-service-accounts|Create GCP service accounts]]**  
Create Google Cloud Platform \(GCP\) service accounts on the ServiceNow AI Platform to access your GCP account during GCP discovery.
-   **[[gcp-access-and-permission-using-policies|GCP access and permission using policies]]**  
Google Cloud Platform \(GCP\) access and permission using policies provide privileges for secure cloud resource utilization and management in GCP.

**Parent Topic:**[[setup-cloud-service-account|Set up a cloud service account]]

## Related

- [[itom-create-google-api-credentials|Configure the Google API credentials for Cloud Discovery]]
- [[google-api-credentials-form|Google API Credentials Form]]
- [[create-gcp-service-accounts|Create GCP service accounts]]
- [[gcp-access-and-permission-using-policies|GCP access and permission using policies]]
- [[setup-cloud-service-account|Set up a cloud service account]]
- [[r-discovery|Discovery]]
