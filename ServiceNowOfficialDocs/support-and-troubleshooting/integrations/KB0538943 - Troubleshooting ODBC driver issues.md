---
title: "Troubleshooting ODBC driver issues"
aliases:
  - KB0538943
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538943
kb_number: KB0538943
last_modified: 2025-04-07
---

## Troubleshooting ODBC driver issues

  

### Issue

This article guides you through the process of troubleshooting ODBC driver issues. It provides steps to help you eliminate common causes for your problem by verifying that the configuration  is correct.

Symptoms may include the following:

-   Cannot connect to the instance
-   Error message received during processing
-   Instance runs out of memory during processing
-   Queried information lost
-   Precision errors received
-   Connection dropped

  

### Release

Any currently supported ODBC Driver release.

### Resolution

Determine whether any of the troubleshooting steps below are true for your environment. Each step provides a link to an article that will help you eliminate possible causes and take corrective action as necessary. 

1.  Before you begin the next steps in the troubleshooting path, review the ODBC troubleshooting checklist to eliminate those common causes. For more information, see [ODBC Troubleshooting Checklist](/kb_view.do?sysparm_article=KB0538995&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=e46e03dd6f1525402f250bae9f3ee48340d40f698536b303ef913980af1f4ac1b006f6f3&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0538995&sysparm_topic= "ODBC Troubleshooting Checklist").
2.  Verify that your instance is running the latest ODBC version. For more information, see [KB0538945: Determining if you have the latest ODBC driver version](/kb_view.do?sysparm_article=KB0538945&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=967a520c6f55a9002f250bae9f3ee40e7600e4f2d68c5e5f42ee287d7658520a1454a2da&sysparm_nameofstack=&sysparm_product=&sysparm_search=determining+if+you+have+the+latest+odbc+driver&sysparm_topic= "Determining if you have the latest ODBC driver version").
3.  Verify that the ODBC driver is working correctly by testing smaller queries and excluding 3rd party applications. For more information, see [KB0538948: Determining if your ODBC driver is working correctly](/kb_view.do?sysparm_article=KB0538948&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=967a520c6f55a9002f250bae9f3ee40e7600e4f2d68c5e5f42ee287d7658520a1454a2da&sysparm_nameofstack=&sysparm_product=&sysparm_search=determining+if+your+odbc+driver&sysparm_topic= "Determining if your ODBC driver is working correctly").
4.  Determine if the instance has run out of memory due to large result sets. For more information, see [KB0538950: Determining if ODBC processing has failed due to low memory](/kb_view.do?sysparm_article=KB0538950&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=967a520c6f55a9002f250bae9f3ee40e7600e4f2d68c5e5f42ee287d7658520a1454a2da&sysparm_nameofstack=&sysparm_product=&sysparm_search=odbc+processing+has+failed&sysparm_topic= "Determining if ODBC processing has failed due to low memory").
5.  Determine if the correct time zone is used during ODBC processing. For more information, see [KB0538951: Determining the time zone for ODBC processing](/kb_view.do?sysparm_article=KB0538951&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=410357086f9da9002f250bae9f3ee486176f7033967f2fa6a750697bbab2e5baac9a70b0&sysparm_nameofstack=&sysparm_product=&sysparm_search=time+zone+for+odbc+processing&sysparm_topic= "Determining the time zone for ODBC processing").
6.  Determine if precision errors are causing issues with queries. For more information, see [KB0538953: Determining if precision errors are causing issues with ODBC queries](/kb_view.do?sysparm_article=KB0538953&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=410357086f9da9002f250bae9f3ee486176f7033967f2fa6a750697bbab2e5baac9a70b0&sysparm_nameofstack=&sysparm_product=&sysparm_search=precision+errors&sysparm_topic= "Determining if precision errors are causing issues with ODBC queries") and see [KB0542327: Resolving Precision Errors in Web Service SUM Functions](/kb_view.do?sysparm_article=KB0542327 "KB0542327: Resolving Precision Errors in Web Service SUM Functions").
7.  Determine if field type is causing issues with queries. For more information, see [KB0542651: Determining if field type is causing issues with ODBC queries](/kb_view_customer.do?sysparm_article=KB0542651 "KB0542651: Determining if field type is causing issues with ODBC queries").
8.  Determine if missing values in queries are causing issues with queries. For more information, see [KB0542664: Determining if table fields are missing values in ODBC queries](/kb_view_customer.do?sysparm_article=KB0542664 "KB0542664: Determining if table fields are missing values in ODBC queries").
9.  Determine if data in ODBC cannot be viewed due to user role. For more information, see [KB0542667: Determining if user is missing query role to view ODBC data](/kb_view_customer.do?sysparm_article=KB0542667 "KB0542667: Determining if user is missing query role to view ODBC data").
10.  Determine if a third party tool is causing issues with ODBC queries. For more information, see [KB0542682: Determining if a third party tool is causing issues with ODBC queries](/kb_view_customer.do?sysparm_article=KB0542682 "KB0542682: Determining if a third party tool is causing issues with ODBC queries").
11.  Determine if a secondary view is causing issues with ODBC database tables. For more information, see [KB0542671: Determining if a secondary view is causing issues with ODBC database tables](/kb_view_customer.do?sysparm_article=KB0542671 "KB0542671: Determining if a secondary view is causing issues with ODBC database tables").
12.  Determine if custom integration is causing issues with ODBC query. For more information, see [KB0542676: Determining if custom integration is causing issues with ODBC queries](/kb_view_customer.do?sysparm_article=KB0542676 "KB0542676: Determining if custom integration is causing issues with ODBC queries").
13.  Determine if an upgrade is required to fix ODBC query issues. For more information, see [KB0542680: Determining if an upgrade is needed for ODBC](/kb_view_customer.do?sysparm_article=KB0542680 "KB0542680: Determining if an upgrade is needed for ODBC").
14.  Determine if the client is unable to load the driver due to a large JVM heap size. For more information, see [KB0538982: Determining if your client application was unable to load the driver](/kb_view.do?sysparm_article=KB0538982 "KB0538982: Determining if your client application was unable to load the driver").
15.  Determine if a parallel query is failing. For more information, see [KB0551938: ODBC driver fails to get data or connect when invoking multiple or parallel connections](/kb_view.do?sysparm_article=KB0551938 "KB0551938: ODBC driver fails to get data or connect when invoking multiple or parallel connections.").

If the problem still exists after following these steps, gather as much detail as you can about the problem before contacting Customer Support. Questions to ask yourself before submitting incident include: 

-   Did you try to connect in different environments (that is, did you try it at work and at home)?
-   Did you have any co-workers try it on their machines?
-   Did you try different Operating Systems?
-   Have you been able to successfully connect in the past?
-   If so, when did it stop working and can you think of anything that may have changed? 
-   Is it possible for you to try on a brand new install machine for testing?

### Related Links

  

<table class="noteTable" style="font-size: 10pt; height: 27px;" align="left"><tbody><tr style="height: 27px;"><td style="vertical-align: middle; text-align: center; height: 27px; width: 26.4px;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left; height: 27px; width: 1020px;"><span style="font-size: 10pt;"><strong>Note</strong>:&nbsp;If your problem still exists after trying the steps in this article: Submit an incident to Customer Support and note this Knowledge Base article ID (KB0538943) in the problem description. For more information, see&nbsp;<a title="Submitting an Incident" href="http://www.servicenow.com/support/contact-support.html" target="_blank" rel="noopener noreferrer nofollow">Submitting an Case</a>&nbsp;in product documentation.</span></td></tr></tbody></table>
