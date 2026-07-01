---
title: Configuring Care Team Operations for Facilities
description: Set up the Care Team Operations for Facilities application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/healthcare-life-sciences/cto-facilities-configuring.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Care Team Operations for Facilities, Healthcare Operations, Healthcare and Life Sciences]
tags:
  - healthcare-life-sciences
  - type-concept
---

# Configuring Care Team Operations for Facilities

Set up the [[cto-facilities-landing|Care Team Operations for Facilities]] application.

## Configuration overview

1.  [[cto-facilities-activate|Install Care Team Operations for Facilities]]

    Install the Care Team Operations for Facilities application \[sn\_cto\_facilities\] if you have the admin role.

2.  [[cto-facilities-fsm-plugin|Set up work order synchronization in Care Team Operations for Facilities]]

    The Field Service Management \[com.snc.work\_management\] plugin is required for work order synchronization to function with Care Team Operations for Facilities.

3.  [[cto-facilities-assign-roles|Set up roles for Care Team Operations for Facilities]]

    Ensure that the appropriate roles are assigned to users of Care Team Operations for Facilities.

4.  [[cto-facilities-create-support-team|Create healthcare organizations for your healthcare facilities support teams]]

    [[hcls-sm-configure-healthcare-organizations|Create a healthcare organization]] to represent the fulfilling healthcare organization for healthcare facilities cases.

5.  [[cto-facilities-add-members-support-team|Add members to your healthcare facilities support organization]]

    Add members to your facilities support organization to provide visibility and access to healthcare facilities cases.

6.  [[cto-facilities-create-group-support-agents|Create a group for all location support agents in Care Team Operations for Facilities]]

    Create a group for location support agents with the sn\_cto\_facilities.loc\_support\_agent role assigned so that users added to this group will inherit the collection of roles for Care Team Operations for Facilities

7.  [[cto-facilities-create-group-managers|Create a group for all location managers in Care Team Operations for Facilities]]

    Create a group for location managers with the sn\_customerservice.svc\_location\_manager assigned so that users added to this group will inherit the collection of roles for Care Team Operations for Facilities.

8.  [[cto-facilities-assignment-groups|Set up assignment groups for Care Team Operations for Facilities]]

    Associate assignment groups with your healthcare organizations to determine which user groups are associated with specific healthcare organizations.

9.  [[cto-facilities-modify-state-tables|Modify state decision tables in Care Team Operations for Facilities]]

    Use Decision Builder to change the state mappings for cases and incidents work orders in Care Team Operations for Facilities.

10. [[cto-facilities-add-customer-record-producer|Add custom record producers to the service catalog in Care Team Operations for Facilities]]

    Add custom record producers you've configured into service catalogs in Care Team Operations for Facilities.

## Related

- [[cto-facilities-activate|Install Care Team Operations for Facilities]]
- [[cto-facilities-fsm-plugin|Set up work order synchronization in Care Team Operations for Facilities]]
- [[cto-facilities-assign-roles|Set up roles for Care Team Operations for Facilities]]
- [[cto-facilities-create-support-team|Create healthcare organizations for your healthcare facilities support teams]]
- [[cto-facilities-add-members-support-team|Add members to your healthcare facilities support organization]]
- [[cto-facilities-create-group-support-agents|Create a group for all location support agents in Care Team Operations for Facilities]]
- [[cto-facilities-create-group-managers|Create a group for all location managers in Care Team Operations for Facilities]]
- [[cto-facilities-assignment-groups|Set up assignment groups for Care Team Operations for Facilities]]
- [[cto-facilities-modify-state-tables|Modify state decision tables in Care Team Operations for Facilities]]
- [[cto-facilities-add-customer-record-producer|Add custom record producers to the service catalog in Care Team Operations for Facilities]]
- [[cto-facilities-landing|Care Team Operations for Facilities]]
- [[hcls-sm-configure-healthcare-organizations|Create a healthcare organization]]
