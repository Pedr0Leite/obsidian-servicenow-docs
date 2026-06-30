---
title: Configuring Care Team Operations for Biomed
description: The following setup steps need to occur prior to using Care Team Operations for Biomed.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/healthcare-life-sciences/configuring-cto-biomed.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Care Team Operations for Biomed, Healthcare Operations, Healthcare and Life Sciences]
---

# Configuring Care Team Operations for Biomed

The following setup steps need to occur prior to using [[care-team-operations-for-biomed|Care Team Operations for Biomed]].

## Configuration overview

1.  [[cto-biomed-activate|Install Care Team Operations for Biomed]]

    Install the Care Team Operations for Biomed application \(sn\_cto\_biomed\) if you have the admin role.

2.  [[cto-biomed-plugin-info|Set up work order synchronization in Care Team Operations for Biomed]]

    The Field Service Management \[com.snc.work\_management\] plugin is required for work order synchronization to function with Care Team Operations for Biomed.

    For Care Team Operations for Biomed to create work orders from Healthcare Biomed cases, the Field Service Management \[com.snc.work\_management\] plugin must be installed.

3.  [[cto-biomed-set-up-roles|Assign roles for Care Team Operations for Biomed]]

    Ensure that the correct roles are assigned to users of Care Team Operations for Biomed.

4.  [[cto-biomed-create-org|Create healthcare organizations for your biomed support teams]]

    [[hcls-sm-configure-healthcare-organizations|Create a healthcare organization]] to represent the fulfilling healthcare organization for healthcare biomed cases.

5.  [[cto-biomed-assign-members|Add members to your biomed support organization]]

    Add members to your Biomed healthcare organization to provide visibility and access to Healthcare Biomed cases.

6.  [[cto-biomed-create-agent-groups|Create a group for all location support agents in Care Team Operations for Biomed]]

    Create a group for location support agents with the sn\_cto\_biomed.loc\_support\_agent assigned so that users added to this group will inherit the collection of roles for Care Team Operations for Biomed.

7.  [[cto-biomed-creare-manager-group|Create a group for all location managers in Care Team Operations for Biomed]]

    Create a group for location managers with the sn\_customerservice.svc\_location\_manager assigned so that users added to this group will inherit the collection of roles for Care Team Operations for Biomed.

8.  [[cto-biomed-set-up-assignment-groups|Set up assignment groups for Care Team Operations for Biomed]]

    Associate assignment groups with your healthcare organizations to determine which user groups are associated with specific healthcare organizations.

9.  [[cto-biomed-modify-states|Modify state decision tables in Care Team Operations for Biomed]]

    Use Decision Builder to change the state mappings for cases and incidents work orders in Care Team Operations for Biomed .

## Related

- [[cto-biomed-activate|Install Care Team Operations for Biomed]]
- [[cto-biomed-plugin-info|Set up work order synchronization in Care Team Operations for Biomed]]
- [[cto-biomed-set-up-roles|Assign roles for Care Team Operations for Biomed]]
- [[cto-biomed-create-org|Create healthcare organizations for your biomed support teams]]
- [[cto-biomed-assign-members|Add members to your biomed support organization]]
- [[cto-biomed-create-agent-groups|Create a group for all location support agents in Care Team Operations for Biomed]]
- [[cto-biomed-creare-manager-group|Create a group for all location managers in Care Team Operations for Biomed]]
- [[cto-biomed-set-up-assignment-groups|Set up assignment groups for Care Team Operations for Biomed]]
- [[cto-biomed-modify-states|Modify state decision tables in Care Team Operations for Biomed]]
- [[care-team-operations-for-biomed|Care Team Operations for Biomed]]
- [[hcls-sm-configure-healthcare-organizations|Create a healthcare organization]]
