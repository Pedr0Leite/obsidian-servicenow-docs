---
title: "Troubleshooting an import that is taking a long time to complete"
aliases:
  - KB0538436
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538436
kb_number: KB0538436
last_modified: 2025-08-25
---

## Troubleshooting an import that is taking a long time to complete

  

### Issue

This article guides you through the process of troubleshooting an import that is taking a long time to complete. It provides steps to help you eliminate common causes for your problem by verifying that the configuration of your networking is correct.

Symptoms may include the following:  

-   No rows are returned
-   Connectivity issues (log message)
-   Import takes a really long time
-   Import does not complete
-   Import stopped in the middle
-   Import says complete, but not all data is present
-   User cannot log in through LDAP
-   Scheduled import does not run at the defined time
-   Data discrepency after report
-   Data is truncated
-   Import fails after upgrade

### Resolution

Determine whether any of the troubleshooting steps below are true for your environment. Each step provides a link to an article that can help you eliminate possible causes and take corrective action as necessary. 

1.  Determine if there is a significant number of records being imported. For more information, see [KB0538405: Determining if there is a significant number of records being imported](/kb_view.do?sysparm_article=KB0538405&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=3dd03afd8ce46100957b906f2c8a66b083d75f74da35a18e6f25cf173c2ece1e6e1b932d&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0538405&sysparm_topic= "KB0538405: Determining if there is a significant number of records being imported").
2.  Determine if a business rule script is impacting your import. For more information, see [KB0538161: Determining if a business rule is running on top of a transform map](/kb_view.do?sysparm_article=KB0538161&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=3dd03afd8ce46100957b906f2c8a66b083d75f74da35a18e6f25cf173c2ece1e6e1b932d&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0538161&sysparm_topic= "KB0538161: Determining if a business rule is running on top of a transform map").
3.  Determine if another process is running at the same time as the import. For more information, see [KB0538402: Determining if another process is running at the same time as the import](/kb_view.do?sysparm_article=KB0538402&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=3dd03afd8ce46100957b906f2c8a66b083d75f74da35a18e6f25cf173c2ece1e6e1b932d&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0538402&sysparm_topic= "KB0538402: Determining if another process is running at the same time as the import").

<table class="noteTable" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: If your problem still exists after trying the steps in this article, submit an incident to Technical Support and note this Knowledge Base article ID (KB0538434) in the problem description. For more information, see <span style="text-decoration: underline;"><span style="color: #0000ff;"><a title="Customer Support" href="https://support.servicenow.com/kb_view.do?sysparm_article=KB0547260" target="_blank" rel="noopener noreferrer"><span style="color: #0000ff; text-decoration: underline;">Submitting an Incident</span></a></span></span>.</td></tr></tbody></table>
