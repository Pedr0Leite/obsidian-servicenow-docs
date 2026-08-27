---
title: "No data shown for a particular indicator in Performance Analytics"
aliases:
  - KB0547461
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547461
kb_number: KB0547461
last_modified: 2024-04-30
---

## No data shown for a particular indicator in Performance Analytics

  

### Issue

No data shown for a particular indicator in Performance Analytics 

Problem

* * *

There is no data shown on the scorecard / dashboard for a particular indicator in Performance Analytics even though there is data in the system.

Cause

* * *

The most likely causes are:

-   the indicator is not included in any job
-   one of the restraints in the [Collecting Data for Performance Analytics](https://docs.servicenow.com/csh?topicname=c_ClctData.html&version=latest "Collecting Data for Performance Analytics") may have prevented the data for the indicator to be collected

  
Resolution

* * *

To check if the indicator is included in a job (you must have the pa\_admin or pa\_data\_collector role to perform these steps):

1.  Navigate to **Performance Analytics > Data Collector > Jobs**.
2.  Scroll down to the bottom of the form and check if the indicator is included in the Indicators related list.
3.  If not, click **Edit** and add the indicator.
4.  Click **Save**.
5.  You can also view the Job Logs and see if there are any errors or warnings for this indicator.

To check if a restraint in the properties prevented the data from being collected:

1.  Navigate to **Performance Analytics > System > Properties**
2.  Check the settings in the **Performance Analytics Data Collector** section.
