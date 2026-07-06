---
title: "High Semaphore wait times when there is no Semaphore exhaustion"
aliases:
  - KB0755688
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755688
kb_number: KB0755688
last_modified: 2026-04-23
---

## Issue

This article explains why semaphore wait times are high for users' transactions in situations where there are no semaphore exhaustions.

## Resolution

In the instances under the transaction logs, it can be observed that semaphore wait times are high, as shown in the example snapshot below. The big data, or in the stats page, the semaphore usage is normal, and there won't be any exhaustion.       

#### Example

-   In the example below, it can be seen that the semaphore wait time for transaction number 4718989 is 258 ms. The subsequent transaction, with transaction number 4718990, has a semaphore wait time of 7,649 ms, followed by the transaction with TXN number 4718991, which has a wait time of 14,535 ms.
-   The **"created"** column in the transaction below indicates the time at which the transaction was completed.  
      
    

![Semaphore wait time example](/sys_attachment.do?sys_id=7dca65524705e614b7832920326d43dd "Semaphore wait time example")  
  

-   According to the logs, the above three transactions started at the same timestamp, 23:59:11, by the user with the same session.  

              2019-07-15 23:59:11 (438) http-23 New transaction 84C2CAA3DBE2B7848444F698F4961947 #4718989 [/hr\_task.do](https://support.servicenow.com/hr_task.do)  
              2019-07-15 23:59:11 (458) http-26 New transaction 84C2CAA3DBE2B7848444F698F4961947 #4718990 [/hr\_task.do](https://support.servicenow.com/hr_task.do)  
              2019-07-15 23:59:11 (495) http-22 New transaction 84C2CAA3DBE2B7848444F698F4961947 #4718991 [/hr\_task.do](https://support.servicenow.com/hr_task.do)

-   According to the session synchronization, the execution of the above transactions will be completed serially, one after another, based on their transaction numbers, as shown in the snapshot above.
-   The three transactions started simultaneously, due to session synchronization a session wait time has been occurred along with semaphore wait time.
-   If observed closely, the semaphore wait time for the current transaction is nearly equal to the sum of the semaphore wait time and the session wait time of the previous transaction.

          For example, the semaphore wait time for transaction number 4718990 is 7649 ms, which is nearly equal to the sum of the semaphore and session wait times for transaction number 4718989.

                                                            258+7411~=7649ms(4718990's)

                      Likewise, the 4718991's semaphore wait time is nearly equal to the aggregation of 4718990's semaphore and session wait times, respectively

                                                          7649+6923~=14535 ms(4718991's) 

-   The semaphore wait times are high when users try to open records, such as hr\_task, simultaneously on multiple tabs in the same browser, as in the above example.
-   Another example is when users attempt to attach attachments, such as to an Incident, in a drag-and-drop fashion. 

2019-07-16 02:13:14 (424)  txid=debb4327db6e EXCESSIVE \*\*\* End #4717262 [/sys\_attachment.do](https://support.servicenow.com/sys_attachment.do), user: r.yao, total time: 0:00:07.943, processing time: 0:00:01.912, total wait: 0:00:06.031, session wait: 0:00:02.173, semaphore wait: 0:00:03.858   
2019-07-16 02:13:16 (298)  txid=92bb0fe7db6e EXCESSIVE \*\*\* End #4717269 [/sys\_attachment.do](https://support.servicenow.com/sys_attachment.do), user: r.yao, total time: 0:00:09.729, processing time: 0:00:01.874, total wait: 0:00:07.855, session wait: 0:00:01.913, semaphore wait: 0:00:05.942  
2019-07-16 02:13:18 (150)   txid=22bb4327db6e EXCESSIVE \*\*\* End #4717275 [/sys\_attachment.do](https://support.servicenow.com/sys_attachment.do), user: r.yao, total time: 0:00:11.478, processing time: 0:00:01.851, total wait: 0:00:09.627, session wait: 0:00:01.874, semaphore wait: 0:00:07.753

All the above transactions started at the same time, but a couple of transactions got completed with a semaphore wait time.

The transaction with number 4717269's semaphore wait time is 5 seconds, which is equal to the sum of the earlier transaction 4717262's session and semaphore wait times (2 + 3).

  
**The above-discussed semaphore wait time can be avoided if the end users don't generate transactions simultaneously.**
