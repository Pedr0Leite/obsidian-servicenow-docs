---
title: "User profile name does not match name used in connect and live feed."
aliases:
  - KB0781504
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781504
kb_number: KB0781504
last_modified: 2024-04-07
---

## Issue

Some users are seeing an issue where their user profile names do not match with the names used in connect or live feed.

For example, user profile name is Abel Tuter. However, the name being used in connect or live feed is David Loo.

## Resolution

1) Navigate to the live\_profile table list

2) Filter the list where Document is the affected sys\_user record (note it has to be searched by the sys\_id of the sys\_user record)

3) The search result should return a record where the name on "Document" does not match with the "Name" being used

4) Update the "Name" field to the proper value and save the record

## Additional Information

Note that there was a known problem (PRB711715) where when a sys\_user record is updated the corresponding live\_profile record is not updated, which is likely the source of this issue. PRB711715 has been fixed in Istanbul and beyond.

If the issue is still observed beyond Istanbul this is likely due to the live\_profile record being created before Istanbul was released and hence why it did not get the proper fix then (the issue is not automatically fixed for old data; it only prevents the issue from happening).
