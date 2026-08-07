---
title: User roles and personas in ITSM Mobile Agent
description: Learn about the various user roles and persona used to log in to ITSM Mobile Agent.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-service-management/itsm-mobile-agent/user-roles-and-persona.html
release: australia
product: ITSM Mobile Agent
classification: itsm-mobile-agent
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Exploring ITSM Mobile Agent, ITSM Mobile Agent, IT Service Management]
tags:
  - it-service-management
  - mobile
  - agents
  - itsm
  - ios-android
  - type-concept
---

# User roles and personas in ITSM Mobile Agent

Learn about the various user roles and persona used to [[install-itsm-mobile-app|log in to ITSM Mobile Agent]].

[[itsm-mobile-agent|ITSM Mobile Agent]] supports the following user persona.

## itil role

The IT agent is the primary user of the ITSM Mobile Agent application. IT agents or technicians responsible for handling and resolving IT incidents and service requests have the itil role assigned. They have access to features such as [[c_IncidentManagement|incident management]], [[c_AssetManagement|asset management]], knowledge base, ticket management, and On-call schedules. They can create, update, and resolve tickets, view their schedules and shift details, and create time off requests.

An itil user might also have more than one role assigned to them. For example:

-   sn\_incident\_write
-   sn\_change\_write
-   sn\_request\_write

Apart from the itil role, users might have the following additional roles, based on the various features available in ITSM Mobile Agent.

|Feature|User role|
|-------|---------|
|Major incidents|major\_incident\_manager|
|Hardware asset management|approver\_user:|
|On-call Scheduling|rota\_manager|
|Shift Planning|sn\_shift\_planning.admin|

## Related

- [[install-itsm-mobile-app|Log in to ITSM Mobile Agent]]
- [[itsm-mobile-agent|ITSM Mobile Agent]]
- [[c_IncidentManagement|Incident Management]]
- [[c_AssetManagement|Asset Management]]
