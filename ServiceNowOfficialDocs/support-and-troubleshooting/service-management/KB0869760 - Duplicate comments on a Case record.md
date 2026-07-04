---
title: "Duplicate comments on a Case record"
aliases:
  - KB0869760
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869760
kb_number: KB0869760
last_modified: 2023-12-06
---

## Duplicate comments on a Case record

  

### Issue

The user saw 10+ duplicate comments on a Case record in their instance (_sn\_customerservice\_case_ table). They wanted to know what caused the issue.

### Cause

While it is unknown what precisely caused the issue, it was found that an excessively long transaction was running and was canceled. It was theorized that the user pressed the "Post" button several times during this excessively long transaction, and that is what caused the behavior.

### Resolution

As shared above, the user's transaction where they posted the comment (which duplicated 10+ times) ran excessively long. The transaction ran for 298670 ms to be exact (about 3.9 mins of wait time), and was canceled, as per the logs:  
  
`2020-12-28 13:53:52 (257) glide.quota.manager WARNING *** WARNING *** Transaction: Cancelling transaction #3494049 /angular.do (maximum execution time exceeded): Thread Default-thread-6 (tony.stark@stark-industries.com, 8F3D776E1B91A0D001933333DD4BCBEE), after 298670ms`  
  
The strongest theory, based on past cases and the lack of information in the logs otherwise is that there were multiple attempts to post the comments during the excessively long transaction, and this caused the issue.

Additionally, it was recommended that the user speak with Tony Stark and ask what actions they took during the transaction to see if any further information could be uncovered (the behavior was not readily reproducible).
