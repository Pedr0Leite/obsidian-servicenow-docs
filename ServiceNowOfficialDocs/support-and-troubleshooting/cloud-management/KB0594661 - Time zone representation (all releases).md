---
title: "Time zone representation (all releases)"
aliases:
  - KB0594661
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0594661
kb_number: KB0594661
last_modified: 2026-02-04
---

## Time zone representation (all releases)

  

### Issue

#### **Time zones**

Time zones that have the _Country/City_ format are **primary time zone ID**s. Other time zone IDs are links to the primary time zone. For example, _US/Pacific_ is a link to the _America/Los\_Angeles_ time zone.

Both _America/Los\_Angeles_ and _US/Pacific_ represent _Pacific Standard Time_ with the same zone offset and Daylight Savings Time (DST) schedule.

Other than the representation, there is no impact on date and time functionality.

### Facts

All times are stored in Coordinated Universal Time (UTC) and appear globally based on the system time zone. However, times appear to users in their local time zone, according to their user preference settings. Learn more about [Time Zones Representations](https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/time/reference/r_TimeZones.html#d67769e66 "Service Now Documentation Time Zones")

### Release

  All Releases

### Resolution

In the absence of a default time zone for the user or the system, the JVM (Java Virtual Machine) reads default time zone information from the machine and depending on how the machine is configured, it might return _US/Pacific_ or _America/Los\_Angeles_.

ServiceNow recommends that admins configure their system with a default timezone using the **glide.sys.default.tz** property to avoid system dependencies.

### Related Links

Documentation: 

-   [Set a system time zone](https://www.servicenow.com/docs/csh?topicname=t_SetASystemTimeZone.html&version=latest "Set a system time zone")
-   KB0785168 - [The time zone for all users on the instance is displaying US/Pacific](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785168 "The Instance default Time Zone is US/Pacific")

Other Resources:

-   [List of tz database time zones \[Wikipedia\]](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "List of tz database time zones [Wikipedia]")
-   [Native Time Zone Information and the JRE \[Java SE 8 docs - Oracle\]](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/time-zone001.html#CBBIEBDG "Native Time Zone Information and the JRE [Java SE 8 docs - Oracle]")
-   [TimeZone.getDefault() \[Java 8 API docs\]](https://docs.oracle.com/javase/8/docs/api/java/util/TimeZone.html#getDefault-- "TimeZone.getDefault() [Java 8 API docs]")
