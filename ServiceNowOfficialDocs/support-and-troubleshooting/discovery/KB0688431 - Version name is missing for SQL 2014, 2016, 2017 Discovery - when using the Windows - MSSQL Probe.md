---
title: "Version name is missing for SQL 2014, 2016, 2017  Discovery - when using the \"Windows - MSSQL\" Probe"
aliases:
  - KB0688431
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688431
kb_number: KB0688431
last_modified: 2024-04-07
---

## Version name is missing for SQL 2014, 2016, 2017 Discovery - when using the "Windows - MSSQL" Probe

  

### Issue

# Symptoms

* * *

Version name is missing for SQL 2014, 2016, 2017  Discovery - when using the "Windows - MSSQL" Probe.

# Release

* * *

Any 

# Cause

* * *

Instance is configured to use "Windows - MSSQL" Probe for SQL server discovery. With this probe, it will only populate the version up to 2012. 

To check:  
Navigate to -> Discovery Definition -> Processes -> Microsoft SQL Server -> Triggers Probe -> 

"Powershell-Windows-MSSQL" should be "active" one if there is 2. 

Sensor:

Navigate to -> Discovery Definition -> Sensors -> "Windows - MSSQL"

line 58 to 75 - shows that Version available is up to 2012.

# Resolution

* * *

1\. Use Pattern instead of Probe.

If Probe is preferred instead of Pattern then below is the possible workaround/customization.

1\. Add follow to the script.  (ref: [http://sqlserverbuilds.blogspot.com/](http://sqlserverbuilds.blogspot.com/) )

 Navigate to -> Discovery Definition -> Sensors -> "Windows - MSSQL"

\--

case '14':

return '2017';

case '13':

return '2016';

case '12':

return '2014';

\------

2\. Add a choice list.

  
         1. Navigate to -> Discovery definition -> Tables -> MSFT SQL Instance -> Table Column                   (Version name) -> Under the Related Link -> Choice

         2. Add the choice 2014,2016,2017 and follow the sequence.
