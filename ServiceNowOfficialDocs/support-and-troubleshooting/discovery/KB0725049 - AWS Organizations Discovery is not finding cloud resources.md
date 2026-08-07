---
title: "AWS Organizations Discovery is not finding cloud resources"
aliases:
  - KB0725049
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725049
kb_number: KB0725049
last_modified: 2024-08-28
---

## AWS Organizations Discovery is not finding cloud resources

  

### Issue

AWS member account Discovery is completing, but no cloud resources are discovered.

### Release

Affecting London and Madrid.

New York and upwards now leverage fully configurable AssumeRole request parameters as dictated by the AWS Security Token Service AssumeRole API Action.

[https://docs.servicenow.com/bundle/newyork-it-operations-management/page/product/discovery/concept/temp-credentials-generated-by-aws.html#temp-credentials-generated-by-aws](https://docs.servicenow.com/bundle/newyork-it-operations-management/page/product/discovery/concept/temp-credentials-generated-by-aws.html#temp-credentials-generated-by-aws)

[https://docs.servicenow.com/bundle/newyork-it-operations-management/page/product/cloud-management-v2/concept/assume-aws-roles.html#assume-aws-roles](https://docs.servicenow.com/bundle/newyork-it-operations-management/page/product/cloud-management-v2/concept/assume-aws-roles.html#assume-aws-roles)

### Cause

AWS Organizations Discovery was introduced in London. There are some limitations on this product in London and Madrid releases, since it was the inaugural support for this feature.

### Resolution

In order for Cloud Discovery to work with AWS Organizations so that Member Account cloud resources can be discovered without needing to supply Member Account credentials, a few conditions must be met in your configuration of the accounts within AWS:

**ServiceNow Instance :**

-   Discovery credentials  (Cloud Service Account form) :: If this is a member account of an AWS Organization and you have configured the associated management account with a credential, leave this blank.

**AWS :**

-   In the AWS Member Account there needs to be a role present exactly named “OrganizationAccountAccessRole”
-   In the AWS Member Account there needs to be a trusted relationship between the aforementioned role and the AWS Management Account.
-   In the AWS Member Account the role must have attached an “AdministratorAccess” policy which grants “\*” Access to “\*” Resource.

**NOTE**: this is the default setup when creating Member Accounts in AWS Organizations.  If you accept the default configuration when setting up your AWS Member Accounts, no special action is required.
