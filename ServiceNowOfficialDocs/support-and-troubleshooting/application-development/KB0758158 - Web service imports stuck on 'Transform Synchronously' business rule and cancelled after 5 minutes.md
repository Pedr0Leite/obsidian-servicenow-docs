---
title: "Web service imports stuck on 'Transform Synchronously' business rule and cancelled after 5 minutes"
aliases:
  - KB0758158
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758158
kb_number: KB0758158
last_modified: 2024-01-28
---

## Web service imports stuck on 'Transform Synchronously' business rule and cancelled after 5 minutes

  

### Issue

When many web service import requests are made to the same import set table at once, some of the import set rows remain the Pending state and are never transformed. This is only applicable for import set tables for which the transform maps do not have any coalesce field maps set. 

### Cause

Web service import rows are transformed synchronously in the same transaction as the request. This synchronous transform is triggered by the out of the box business rule 'Transform Synchronously'. However, the logs suggest that this business rule is stuck for 5 minutes before the transaction is cancelled. 

Logs:

2019-08-05 10:35:11 (681) http-3 Session created: D87E370ADB07BB84784CD498F4961942, timeout after 60 minutes of inactivity
2019-08-05 10:35:11 (682) http-3 SYSTEM New transaction D87E370ADB07BB84784CD498F4961942 #45442219 /api/now/table/<import\_set\_table>
2019-08-05 10:35:11 (873) http-26 New transaction D87E370ADB07BB84784CD498F4961942 #45442222 /api/now/table/<import\_set\_table>
2019-08-05 10:35:11 (914) API\_INT-thread-3 D87E370ADB07BB84784CD498F4961942 txid=547e7fc6db07 #45442222 /api/now/table/<import\_set\_table> Parameters -------------------------
api=api
sysparm\_display\_value=true
2019-08-05 10:35:12 (930) API\_INT-thread-3 D87E370ADB07BB84784CD498F4961942 txid=547e7fc6db07 \*\*\* Script: 50
2019-08-05 10:40:12 (201) glide.quota.manager WARNING \*\*\* WARNING \*\*\* Transaction: Cancelling transaction #45442222 /api/now/table/<import\_set\_table> (maximum execution time exceeded): Thread API\_INT-thread-3 (null, D87E370ADB07BB84784CD498F4961942), after 300328ms
2019-08-05 10:40:12 (211) API\_INT-thread-3 D87E370ADB07BB84784CD498F4961942 txid=547e7fc6db07 WARNING \*\*\* WARNING \*\*\* Long Transaction started at 08/05/19 10:35:11.873, Memory at start was 1,228, Memory is 1,625, SQL count is 423, BR count is now 1.
2019-08-05 10:40:12 (211) API\_INT-thread-3 D87E370ADB07BB84784CD498F4961942 txid=547e7fc6db07 WARNING \*\*\* WARNING \*\*\* Transaction cancelled: maximum execution time exceeded
2019-08-05 10:40:12 (213) API\_INT-thread-3 D87E370ADB07BB84784CD498F4961942 txid=547e7fc6db07 Slow business rule 'Transform synchronously' on <import\_set\_table>:51, time was: 0:04:59.260
2019-08-05 10:40:12 (217) API\_INT-thread-3 D87E370ADB07BB84784CD498F4961942 txid=547e7fc6db07 SEVERE \*\*\* ERROR \*\*\* com.glide.sys.TransactionCancelledException: Transaction cancelled: maximum execution time exceeded
java.lang.RuntimeException: com.glide.sys.TransactionCancelledException: Transaction cancelled: maximum execution time exceeded

  
Since there are no coalesce field maps in the transform map, the system checks if the transform should be done serially or concurrently.   
This is determined by the system property 'glide.import\_set\_insert\_serialized\_when\_no\_coalesce' controls the processing of web service import sets which have no coalesce field(s) defined. When this property is set to false (default), the instance will perform transformations concurrently from the source to the target table. When this property is set to true, the instance will perform transformations one at a time for a given staging table.

### Resolution

You may apply one of the below two solutions:

1\. Set the system property 'glide.import\_set\_insert\_serialized\_when\_no\_coalesce' to false. (Recommended)  
This will apply to all import set tables where there are no coalesce field(s).   
  
OR  
  
If you'd like transformations only for the current import table to be done concurrently, the above property can be overridden by creating a new property for this specific import staging table.   
2\. Create a new property 'glide.import\_set\_insert\_serialized.<import\_set\_table\_name>' and set it to false.

When you go with this approach, it'll solve the issue with the current import set table but if you have other web service imports with no coalesce field maps, you may run into the same issue with that table as well.

### Related Links

[Web Service Import Mode](https://docs.servicenow.com/csh?topicname=r_ImportSetMode.html&version=latest)
