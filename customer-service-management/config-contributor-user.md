---
title: Configure Contributor Users
description: The CSM Contributor User plugin enables you to engage middle office teams in resolving customer issues and requests.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/config-contributor-user.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [User management, Set up your environment, Configure, Customer Service Management]
---

# Configure Contributor Users

The CSM Contributor User plugin enables you to engage middle office teams in resolving customer issues and requests.

## Before you begin

Role required: admin

## About this task

With the provided roles, relationships, and user profile attributes, contributors can report and collaborate on cases created for customers, service organizations, or themselves.

The CSM Query Rules plugin is automatically activated by the CSM Contributor User plugin \(com.snc.csm\_contributor\_user\). The CSM Contributor User plugin is moved to App Store beginning with the Australia release. For more information, see [[csm-query-rules|CSM Query Rules]].

## Procedure

1.  Activate the CSM Contributor User plugin \(com.snc.csm\_contributor\_user\).

2.  Assign the [[csm-contributor-user-roles|contributor user roles]] to middle office users.

3.  [[configure-data-model-relationships|Create relationships]].

4.  Confirm the **sn\_cs\_queryrules.use\_query\_rules** property is set to true.

## Related

- [[csm-query-rules|CSM Query Rules]]
- [[csm-contributor-user-roles|Contributor user roles]]
- [[configure-data-model-relationships|Create relationships]]
