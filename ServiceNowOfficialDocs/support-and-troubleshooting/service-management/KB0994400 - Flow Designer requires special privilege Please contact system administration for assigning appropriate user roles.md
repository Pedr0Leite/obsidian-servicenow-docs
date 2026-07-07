---
title: "Flow Designer requires special privilege\" Please contact system administration for assigning appropriate user roles\"
aliases:
  - KB0994400
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994400
kb_number: KB0994400
last_modified: 2026-02-22
---

## Issue

User cannot access flow or flow execution. Error is "Flow Designer requires special privilege. Please contact system administration for assigning appropriate user roles"

## Resolution

Check if the user has a flow\_operator and flow\_designer role.

Make sure if the user has an access to the scope on where the Flow is built. Admin role user can sometimes be restricted access to certain scopes.

Check if the user encountering the issue has a user ID containing "\\" character. If user has this in the user ID, check the property "glide.ui.escape\_all\_script" and set it to true
