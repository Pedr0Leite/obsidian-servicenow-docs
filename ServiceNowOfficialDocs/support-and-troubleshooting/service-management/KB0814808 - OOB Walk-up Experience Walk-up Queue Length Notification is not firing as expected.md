---
title: "OOB Walk-up Experience \"Walk-up Queue Length\" Notification is not firing as expected"
aliases:
  - KB0814808
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814808
kb_number: KB0814808
last_modified: 2024-04-08
---

## OOB Walk-up Experience "Walk-up Queue Length" Notification is not firing as expected

  

### Issue

The user is concerned that their Out of Box (OOB) "Walk-up Queue Length" notification message is not firing as expected. They believe that an OOB event ('sn\_walkup.interaction.queue.threshold') should be fired when a Walk-up location's 'Queue length notification' value is me, but this is not happening.

### Resolution

This issue is a result of PRB1326586.

The "resolution" to PRB1326586 was that the dead code (which was never meant to be released - this was done by accident) was removed from the product. The manager notification was created at the beginning of the Madrid release, but removed late in the Madrid release when Walk-up adopted the Advanced Work Assignment routing and data model changes.  
  
Because of how late in the release this change was made, the Product Owners opted to remove the triggers for the notification code instead of removing all of the code. This feature was never released and no mention of it was made in the documentation, but because remnants of the logic existed, some confusion was caused, resulting in some users being lead to believe that a certain functionality should be present.  
  
Again, the PRB fix was to remove the rest of the dead code so that future users would not run into the same confusion.
