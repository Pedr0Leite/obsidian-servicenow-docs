---
title: "Duration and Timer field values use the UTC timezone in the ODBC Driver version 1.0.10"
aliases:
  - KB0583982
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0583982
kb_number: KB0583982
last_modified: 2024-04-07
---

## Duration and Timer field values use the UTC timezone in the ODBC Driver version 1.0.10

  

### Issue

Duration and Time field values use the UTC timezone in the ODBC Driver version 1.0.10

  
  

# Automatic changes in ODBC 1.0.10

* * *

Starting with the 1.0.10 version of the ODBC Driver, duration and timer field values are displayed using the UTC timezone. Prior to 1.0.10, duration and timer field values were displayed using the local time of the computer the ODBC Driver is installed on.

This change affects only queries on the raw field values and does not affect queries on display values.

# Legacy support

* * *

The ODBC Driver property LegacyDurationTimeZone was added to provide support for legacy configurations. This property is false by default.

To display duration and time fields using the display value instead of the UTC value, [set this property to true](https://docs.servicenow.com/csh?topicname=r_SettingODBCProperties.html&version=latest "set this property to true"). This property should be used only to preserve compatibility with legacy configurations.

# Querying display values

* * *

You can query the display value of a duration or timer field. To query the display value, add **dv\_** to the start of the field name, such as **dv\_delivery\_time** to query the display value of the **Delivery time \[delivery\_time\]** field.
