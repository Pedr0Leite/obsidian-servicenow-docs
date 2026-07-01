---
title: Setting up a user as a Unified Consumer
description: Set up a user as a Unified Consumer by creating a single, unified profile that supports both the internal and external personas in the Customer Service Management \(CSM\) application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/setting-up-a-user.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configuring a user as a Unified Consumer, Configuring a Unified User, User management, Set up your environment, Configure, Customer Service Management]
---

# Setting up a user as a Unified Consumer

Set up a user as a Unified Consumer by creating a single, unified profile that supports both the internal and external personas in the [[c_CustomerServiceManagement|Customer Service Management]] \(CSM\) application.

## Overview of Unified Consumer

You can model a single user both as an employee \(snc\_internal\) and a business-to-consumer \(B2C customer\) by creating a unified profile. By unifying multiple profiles for a single user in the Customer Service Management \(CSM\) application, you don't need to create and manage multiple user accounts for that user.

**Note:** You can also configure an external Unified Consumer, who lacks an internal \(snc\_internal\) role and isn’t an employee, by using similar setup tasks.

The following table describes how to set up the tasks for activating a Unified Consumer.

|Task|Description|
|----|-----------|
|Activate a Unified Consumer|Activate a Unified Consumer by updating the ConsumerImpl script include to display other sys\_user records in the reference list for the csm\_consumer table. For more information, see [[activate-unified-consumer|Activate a Unified Consumer]].|
|Create a consumer record|Create a consumer record with the user, designating that user as a consumer. For more information, see [[create-a-consumer-record|Create a consumer record]].|
|Assign a role to a user|Assign the Unified Consumer \(sn\_customerservice.unified\_consumer\) role to the user. For more information, see [Assign a role to a user](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_AssignARoleToAUser.md).|
|Associate an existing user with a consumer record|Associate a Unified Consumer user with a consumer record by creating a consumer user and then linking the user with a consumer record. For more information, see [[associating-users-to-a-consumer-record|Associate an existing user to a consumer record]].|

**Note:** Both a consumer record and the Unified Consumer role are required for consumer functionality. Create the consumer record before assigning the role. If the role is assigned without a linked consumer record, the user cannot perform consumer activities and may experience unexpected behavior. If the consumer record exists but the role is missing, the user cannot access consumer features such as cases, [[sold-product|sold products]], or [[install-base-item|install base items]].

**Related topics**  


[[configuring-employee-as-a-consumer|Configuring a user as a Unified Consumer]]

[[roles-installed-with-employee-as-consumer|Roles installed with Employee as a Consumer]]

[[features-supp-and-unsupp-by-unified-consumer|Supported and unsupported roles and features]]

## Related

- [[activate-unified-consumer|Activate Unified Consumer]]
- [[create-a-consumer-record|Create a consumer record]]
- [[associating-users-to-a-consumer-record|Creating and associating a Unified Consumer user to a consumer record]]
- [[configuring-employee-as-a-consumer|Configuring a user as a Unified Consumer]]
- [[roles-installed-with-employee-as-consumer|Roles installed with Employee as a Consumer]]
- [[features-supp-and-unsupp-by-unified-consumer|Supported and unsupported roles and features]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[sold-product|Sold products]]
- [[install-base-item|Install base items]]
