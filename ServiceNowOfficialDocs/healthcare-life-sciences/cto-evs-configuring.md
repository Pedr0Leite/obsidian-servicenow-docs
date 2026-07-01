---
title: Configuring Care Team Operations for Environmental Services
description: Set up the Care Team Operations for Environmental Services application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/healthcare-life-sciences/cto-evs-configuring.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Care Team Operations for Environmental Services, Healthcare Operations, Healthcare and Life Sciences]
tags:
  - healthcare-life-sciences
  - type-concept
---

# Configuring Care Team Operations for Environmental Services

Set up the [[cto-evs-landing|Care Team Operations for Environmental Services]] application.

## Configuration overview

1.  [[cto-evs-activate|Install Care Team Operations for Environmental Services]]

    Install the Care Team Operations for Environmental Services application \(sn\_cto\_evs\) if you have the admin role.

2.  [[cto-evs-setup-plugins|Set up work order synchronization in Care Team Operations for Environmental Services]]The Field Service Management \[com.snc.work\_management\] plugin is required for work order synchronization to function with Care Team Operations for Environmental Services.
3.  [[cto-evs-assign-roles|Set up roles for Care Team Operations for Environmental Services]]

    Ensure that the correct roles are assigned to users of Care Team Operations for Environmental Services.

4.  [[cto-evs-create-support-teams|Create healthcare organizations for your healthcare EVS support teams]]

    [[hcls-sm-configure-healthcare-organizations|Create a healthcare organization]] to represent the fulfilling healthcare organization for environmental services cases.

5.  [[cto-evs-add-members-support-team|Add members to your healthcare environmental services support organization]]

    Add members to your Environmental Services support organization to provide visibility and access to EVS cases.

6.  [[cto-evs-create-location-support-group|Create a group for all location support agents in Care Team Operations for Environmental Services]]

    Create a group for location support agents with the sn\_cto\_evs.loc\_support\_agent role assigned so that users added to this group will inherit the collection of roles for Care Team Operations for Environmental Services.

7.  [[cto-evs-create-group-location-managers|Create a group for all location managers in Care Team Operations for Environmental Services]]

    Create a group for location managers with the sn\_customerservice.svc\_location\_manager assigned so that users added to this group will inherit the collection of roles for Care Team Operations for Environmental Services.

8.  [[cto-evs-assignment-groups|Set up assignment groups for Care Team Operations for Environmental Services]]

    Associate assignment groups with your healthcare organizations to determine which user groups are associated with specific healthcare organizations.

9.  [[cto-evs-state-decision-tables|Modify state decision tables in Care Team Operations for Environmental Services]]

    Use Decision Builder to change the state mappings for cases and incidents work orders in Care Team Operations for Environmental Services.

10. [[cto-evs-add-custom-record-producers|Add custom record producers to the service catalog in Care Team Operations for Environmental Services]]

    Add customer record producers to the service catalog for use with Care Team Operations for Environmental Services.

## Related

- [[cto-evs-activate|Install Care Team Operations for Environmental Services]]
- [[cto-evs-setup-plugins|Set up work order synchronization in Care Team Operations for Environmental Services]]
- [[cto-evs-assign-roles|Set up roles for Care Team Operations for Environmental Services]]
- [[cto-evs-create-support-teams|Create healthcare organizations for your healthcare EVS support teams]]
- [[cto-evs-add-members-support-team|Add members to your healthcare environmental services support organization]]
- [[cto-evs-create-location-support-group|Create a group for all location support agents in Care Team Operations for Environmental Services]]
- [[cto-evs-create-group-location-managers|Create a group for all location managers in Care Team Operations for Environmental Services]]
- [[cto-evs-assignment-groups|Set up assignment groups for Care Team Operations for Environmental Services]]
- [[cto-evs-state-decision-tables|Modify state decision tables in Care Team Operations for Environmental Services]]
- [[cto-evs-add-custom-record-producers|Add custom record producers to the service catalog in Care Team Operations for Environmental Services]]
- [[cto-evs-landing|Care Team Operations for Environmental Services]]
- [[hcls-sm-configure-healthcare-organizations|Create a healthcare organization]]
