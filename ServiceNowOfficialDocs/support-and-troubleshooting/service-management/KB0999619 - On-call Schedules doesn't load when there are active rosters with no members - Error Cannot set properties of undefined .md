---
title: "On-call Schedules doesn't load when there are active rosters with no members - Error: Cannot set properties of undefined (setting 'user')"
aliases:
  - KB0999619
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999619
kb_number: KB0999619
last_modified: 2026-06-24
---

## On-call Schedules doesn't load when there are active rosters with no members - Error: Cannot set properties of undefined (setting 'user')

  

### Issue

You have reported an issue with On-call Schedules not loading when there are active rosters with no members.  
When an on-call roster has no members, the on-call schedule page does not load.  
  
Observed Console error:  
  
angular\_includes\_1.4.jsx?v=10-28-2021\_1851:109 TypeError: Cannot set properties of undefined (setting 'user')  
at sn\_on\_call\_now.app.jsdbx?v=10-28-2021\_1851&c=34\_963:320  
at Array.forEach ()  
at buildDataModel (sn\_on\_call\_now.app.jsdbx?v=10-28-2021\_1851&c=34\_963:302)  
at url (sn\_on\_call\_now.app.jsdbx?v=10-28-2021\_1851&c=34\_963:390)  
at angular\_includes\_1.4.jsx?v=10-28-2021\_1851:121  
at r.$eval (angular\_includes\_1.4.jsx?v=10-28-2021\_1851:135)  
at r.$digest (angular\_includes\_1.4.jsx?v=10-28-2021\_1851:133)  
at r.$apply (angular\_includes\_1.4.jsx?v=10-28-2021\_1851:136)  
at g (angular\_includes\_1.4.jsx?v=10-28-2021\_1851:89)  
at T (angular\_includes\_1.4.jsx?v=10-28-2021\_1851:94

### Release

All

### Cause

  
This behavior is caused by the incorrect Roster/Shift definition.  
The error in the console occurs when system is trying to fetch member name which is not present and throws an error  
  
To explain in detail the issue with the configuration:

You have a Group that has Rota with multiple shifts that have no rostered members at all in cmn\_rota\_member\_list. But there are coverages created for that roster.

In the On-Call Calendar you are providing coverage for a roster  (but members are not present in that roster).

The error will occur under the above scenarios for the Group and ultimately cause the On-call Schedule not to load.  
  

### Resolution

  
  
SOLUTION PROPOSED:  
  
One solution could be to add members in that roster, as it is expected that you have roster members for whom you are providing coverage.  
To do this, navigate to the relevant roster 'cmn\_rota\_roster' and in the Members related list, add members.

Alternatively, to instantly get the On-call Schedule page loading, delete those coverage spans on the On-Call calendar.  
  
  
  

### Related Links

  
Please note: We have an existing PRB PRB1533691 for the specific reason that an impacted On-Call Group with incorrectly defined Shift causes the On-Call Schedules page not to load.  
This prb is fixed in SanDiego.
