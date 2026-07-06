---
title: "OOB HR-integration with Success factor is throwing error for \"Worker Profiles\"
aliases:
  - KB0758299
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758299
kb_number: KB0758299
last_modified: 2025-01-22
---

## Issue

\-- OOB HR-integration with Success factor is throwing error for "Worker Profiles" scheduled run.

\-- Scheduled run for the success-factor is throwing error when Integration services which all are using "prev\_sync\_date" from value stored in job tracker 

## Resolution

You can check whether the system date time format is yyyy-mm-dd or not.

If not, the script defined in the Outbound Schema Mapping named as : "HR Integrations Outbound Schema Mapping" will not be able to render the last\_modified\_date. You may need to update the script.

Eg:- Customer is having a date time format as dd-MMM-yy, we have updated the script as shown below

\========

answer = (function getValueForTarget(externalSourceId , source) {  
var previousSyncDate = source.getValue('prev\_sync\_date');  
var glideDateTimeValue = new GlideDateTime();  
glideDateTimeValue.setDisplayValue(previousSyncDate);  
var result=glideDateTimeValue.getValue().toString().split(" ");  
var actualResult = result\[0\]+"T"+ result\[1\]+"Z";  
return actualResult;  
  
})(externalSourceId , source);  
  
\=======
