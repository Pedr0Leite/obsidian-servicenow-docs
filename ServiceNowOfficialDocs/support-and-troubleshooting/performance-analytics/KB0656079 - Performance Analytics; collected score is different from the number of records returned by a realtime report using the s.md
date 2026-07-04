---
title: "Performance Analytics; collected score is different from the number of records returned by a realtime report using the same conditions"
aliases:
  - KB0656079
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656079
kb_number: KB0656079
last_modified: 2024-04-07
---

## Issue

Performance Analytics; collected score is different from the number of records returned by a realtime report using the same conditions

Symptoms

* * *

Find that for an indicator using a condition that is time based, the collected score on the current day may differ from a realtime report that is run on the same day. For example, the indicator is based on e.g. the Open Incidents indicator source. The indicator has an extra condition on top of the indicator source, checking for incidents not updated after the last 5 days.  
  
When scores are collected and comparing the scores for today to a realtime report, which uses the same set of conditions, the number of records can be different. The report selects more records than the indicator score shows. The missing records seem to be the most recently updated ones.  
  
The same issue occurs when the condition on 'last updated' is placed in the indicator source directly. The preview of the indicator source will show the same data as the realtime report, but when collecting scores based on that indicator source, it does not show the most recently updated records.

Cause

* * *

When a preview is done on an indicator source or just run a realtime report that uses the **updated on or before 5 days ago** condition, it looks back 5 days from the current time and show incidents not updated since then. 

However, when PA scores are collected for an indicator or indicator source with a condition like above, it uses midnight as the timestamp and then goes 5 days back to midnight 5 days ago. This explains the difference.   
  
When a realtime report is run today at say 3pm PST it shows data not updated after 25-OCT 15:00. When that is compared to scores collected today, even if the collection is run with relative end date = 0 - so collecting scores for today, it will show data not updated after 25-OCT 00:00, which is a 15 hour time difference there. Any incidents updated within that window will show up in the report, but not in the records for the indicator. They will be there on the next day's score though. 

  
Resolution

* * *

This is intended behavior. The Performance Analytics data intends to show historic data. The advantage of cutting of on midnight implies that it does not matter at what time the collection is run. It always has the same results.  
  
If there is a requirement to see the realtime scores/records in PA scorecards as well, that can be enabled on the detailed scorecard (on indicator level); see the [View Realtime Scores](https://docs.servicenow.com/csh?topicname=c_UsePerformanceAnalyticsScorecards.html&version=latest) topic in the documention.
