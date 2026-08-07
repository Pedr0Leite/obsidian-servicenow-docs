---
title: "Sentiment Analysis not working"
aliases:
  - KB0870531
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870531
kb_number: KB0870531
last_modified: 2026-04-23
---

## Sentiment Analysis not working

  

### Issue

To setup sentiment analysis below steps need to be followed-

Step 1: Configuring Sentiment Analysis  
  
Open "Sentiment Connector Configuration".  
Open any Configuration already present like Google.  
Open "credential Alias" of the configuration.  
Setup the connections under the "Connections" related list.  
Make sure to pass correct Connection Alias, Connection URL in HTTP(s) Connection record and API Key Credential.  
Make sure to check the default and active checkbox for the "Sentiment Connector Configuration" you are configuring. In this case it is Google.  
  
Step 2: Opt-In for a Survey for Sentiment Analysis  
  
Navigate to Survey > View Surveys.  
Open any active survey for which you wanted to configure Sentiment Analysis.  
Under "Other Options" tab on the form, there is a checkbox "Allow Sentiment Analysis" which must be checked for the Sentiment Analysis to be performed for any survey.  
  
Please note: You can Opt-In for Sentiment Analysis at the Survey Definition level or for any text-type question at the Question/Metric Level.  
  
Step 3: Sentiment Analysis results  
  
Once all the above configuration is done, let some survey results been submitted for the survey for which Sentiment Analysis is turned on.  
There is an ASYNC event script which will be executed to perform Sentiment Analysis.  
Wait for the job to complete and you will see results in "Question Sentiment Results".

### Release

NA

### Resolution

To diagnose the connectivity between the ServiceNow and third party vendor, the below script in background scripts need to be run-  
  
var sa = new sn\_nlp\_sentiment.SentimentAnalyser();  
var result = sa.analyze("test");  
//gs.info(result);  
  
gs.info(JSON.stringify(result));  
  
Please Note : Third Party Connector credential details or API keys needs to be obtained by customers then only Sentiment Analysis results will be obtained.
