---
title: Setting up AWS service accounts
description: Create and configure cloud service accounts at ServiceNow AI Platform for the corresponding Amazon Web Services \(AWS\) service accounts.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/setup-aws-service-accounts.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Set up a cloud service account, Access to cloud environments for ITOM products, IT Operations Management]
tags:
  - it-operations-management
  - type-concept
---

# Setting up AWS service accounts

Create and configure cloud service accounts at ServiceNow AI Platform for the corresponding Amazon Web Services \(AWS\) service accounts.

## Verify the REST API Permissions

Download the [Cloud Discovery patterns spreadsheet](https://downloads.docs.servicenow.com/resource/enus/api/servicenow-discovery-patterns-api-details.xlsx) so you can grant user permissions required for running the [[r-discovery|Discovery]] patterns. In addition to permissions, the spreadsheet also includes useful information such as pattern names, types, CI Classes, and links to vendor documentation. New patterns are available quarterly, so check periodically to be sure you have the latest version of the spreadsheet.

Ensure that you are familiar with the hierarchy of AWS service accounts in your environment. For example, if there are AWS Organizations, set up the management and member accounts at ServiceNow AI Platform to reflect that hierarchy. You can set up the AWS service accounts of the following types:

-   **Discrete account**: Standalone account, with no management account.
-   **Management account**: Management account that may or may not contain member accounts \(subaccounts\).

    **Note:** Some ServiceNow UI screens may refer to management accounts as master accounts.

-   **Member account**: Subaccount that belongs with the \(management\) account.

-   **[[access-aws-accounts|Access setup for AWS service accounts]]**  
Cloud Discovery and [[cloud-management-v2-landing-page|Cloud Provisioning and Governance]] need access to resources in the Amazon Web Services \(AWS\) service accounts. Learn about different methods of configuring such access.
-   **[[aws-create-creds-cloud-mgt|Configure access to the AWS accounts using permanent AWS credentials]]**  
To securely access data on your provider account, the Discovery process must present appropriate credentials. To make the credentials available to Discovery and Cloud Provisioning and Governance, you first create a user with programmatic access in the AWS Management Console. You then securely store the credentials in a service account at ServiceNow AI Platform.
-   **[[create-aws-service-accounts|Create AWS service accounts]]**  
Create AWS service accounts on the ServiceNow AI Platform to access your AWS account during AWS discovery.
-   **[[configure-iam-role-aws-account|Configure temporary credential access for trusted AWS accounts]]**  
Configure the trusting account whose resources need to be accessed, to rely on the trusted account using the Identity and Access Management \(IAM\) role.
-   **[[aws-trusted-credential-less|Configure credential-less access using trusted AWS accounts]]**  
Set up a trusted credential-less account that other AWS accounts can rely on for access.
-   **[[configure-iam-role-aws-member|Configure access for trusting AWS member accounts in trust chain]]**  
Configure access for AWS member accounts by using a trust chain from the accessor through the management account.
-   **[[config-mid-iam-roles|Configure the MID Server for AWS IAM roles]]**  
Configure the MID Server to retrieve the temporary security credentials associated with an IAM role.
-   **[[aws-create-user-policy-cloud-mgt|Control AWS access and permissions using policies]]**  
Configure policies with the necessary level of permissions to provide access to the AWS resources for Cloud Discovery and Cloud Provisioning and Governance.

**Parent Topic:**[[setup-cloud-service-account|Set up a cloud service account]]

## Related

- [[access-aws-accounts|Access setup for AWS service accounts]]
- [[aws-create-creds-cloud-mgt|Configure access to the AWS accounts using permanent AWS credentials]]
- [[create-aws-service-accounts|Create AWS service accounts]]
- [[configure-iam-role-aws-account|Configure temporary credential access for trusted AWS accounts]]
- [[aws-trusted-credential-less|Configure credential-less access using trusted AWS accounts]]
- [[configure-iam-role-aws-member|Configure access for trusting AWS member accounts in trust chain]]
- [[config-mid-iam-roles|Configure the MID Server for AWS IAM roles]]
- [[aws-create-user-policy-cloud-mgt|Control AWS access and permissions using policies]]
- [[setup-cloud-service-account|Set up a cloud service account]]
- [[r-discovery|Discovery]]
- [[cloud-management-v2-landing-page|Cloud Provisioning and Governance]]
