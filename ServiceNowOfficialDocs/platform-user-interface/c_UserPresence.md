---
title: User presence
description: User presence is a Core UI feature that lets you see who is online when you're working in an instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/c\_UserPresence.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Common UI elements, Working in Core UI, Configure UIs and portals, Configure user experiences]
tags:
  - platform-user-interface
  - type-concept
---

# User presence

User presence is a [[c_UI16|Core UI]] feature that lets you see who is online when you're working in an instance.

Your avatar appears in the form header next to your name, and in multiple other places such as in [[c_activity-streams|activity streams]], [[c_VisualTaskBoards|Visual Task Boards]], live feeds, and Connect conversations. A dot on the avatar of the user represents online status.

-   Green dot if the user is logged in.
-   No dot if the user is not logged in.
-   Orange dot if the user recently logged out.

Users can add an avatar image to their live feed profile. If no image is uploaded to the live feed profile, the avatar is the user's initials.

**Note:** Live Feed does not use images uploaded to User \(sys\_user\) records.

When you're viewing a record in a form, such as an incident, you can see if other users are viewing the same record.

\[Omitted image "UserPresenceViewingRecord.png"\] Alt text: User presence in a form.

If multiple users are viewing the record, the avatar is represented by the number of users. Point your cursor to the number to see the names and avatars of the users.

When you're in a Connect conversation or entering comments in an [[activity-stream-configurable-workspace|activity stream]], you can see information about the activity of the other participant, for example if they are viewing or typing.

An administrator can disable user presence globally.

-   **[[t_DisableUserPresence|Disable user presence]]**  
You can disable user presence globally by enabling a system property.
-   **[[configure-live-form-feat|Disable live form features]]**  
User presence includes several new live form features for Core UI. You can show or hide these features using the **glide.ui16.live\_forms.enabled** property.
-   **[[configure-time-interval-user-presence|Configure time intervals for user presence]]**  
User presence shows that users are viewing a record sometimes after they have already left. The system only checks for user presence every two minutes by default. You can allow the system to check more frequently by configuring some system properties.

**Parent Topic:**[[p_CommonUIElements|Common UI elements]]

## Related

- [[t_DisableUserPresence|Disable user presence]]
- [[configure-live-form-feat|Disable live form features]]
- [[configure-time-interval-user-presence|Configure time intervals for user presence]]
- [[p_CommonUIElements|Common UI elements]]
- [[c_UI16|Core UI]]
- [[c_activity-streams|Activity streams]]
- [[c_VisualTaskBoards|Visual Task Boards]]
- [[activity-stream-configurable-workspace|Activity stream]]
