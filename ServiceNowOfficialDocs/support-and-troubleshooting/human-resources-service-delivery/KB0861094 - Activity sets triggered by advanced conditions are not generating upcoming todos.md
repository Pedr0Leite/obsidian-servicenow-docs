---
title: "Activity sets triggered by advanced conditions are not generating upcoming todos"
aliases:
  - KB0861094
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861094
kb_number: KB0861094
last_modified: 2024-09-21
---

## Issue

On the HR ticket page on the employee portal its is noticed that the upcoming todos do not show up for activity sets triggered by advanced conditions.  
The release notes do not mention any limitations in regards to the new 'upcoming to-dos' feature in Orlando. So we are expecting this feature to work for advanced conditions too. Is this a bug?

## Resolution

The workflow where we creating future todos for each activity set. In 'Wait to reevaluate Trigger Script' activity of 'HR Activity Launcher' workflow, we specifically check for activity set with trigger type = advance and avoid from creating future todos for those activity sets.

Our product team has confirmed that if an activity set has trigger type as Advanced, then it is considered as an activity set which is triggered already. We create future to-dos for activity sets which are not yet to be triggered so it is expected that no future todos will be created for activity set with trigger type Advanced.

For an activity set with advanced trigger type, if the script evaluates to false now, the WF will still check periodically whether it will evaluate to true in the future. However, there's no easy way to find out from the script logic whether it will for sure evaluate to true in the future as the script outcome might change depending on future conditions/actions. Basically this is a non deterministic situation and because of this we don't show future to-dos for advanced trigger type activity set.
