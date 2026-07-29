---
title: "Troubleshooting issues with completed update sets"
aliases:
  - KB0535178
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535178
kb_number: KB0535178
last_modified: 2024-04-30
---

## Troubleshooting issues with completed update sets

  

### Issue

Troubleshooting issues with completed update sets

  
Purpose  

* * *

This article guides you through the process of troubleshooting issues with completed update sets. It provides steps to help you eliminate common causes for your problem by verifying that the configuration of your networking is correct.

Symptoms

* * *

Symptoms may include the following:   

-   There are instance issues post-commit
-   Update set shows as committed but has inconsistencies
-   Not everything is updated after the update set completes

Resolution

* * *

Validate that each troubleshooting step below is true for your environment. Each step provides instructions or a link to an article to eliminate possible causes and take corrective action as necessary. The steps are ordered in the most appropriate sequence to isolate the issue and identify the proper resolution. 

1.  Verify that the expected records are contained in the update set. See the following article: [KB0535248: Verifying that expected records are contained in the Update Set](/kb_view.do?sysparm_article=KB0535248&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=6d712d9bc5d31100c14d4c84a9fa2377213d6e240dfb68b77da85b49a2568572d6071d57&sysparm_nameofstack=&sysparm_product=&sysparm_search=verifying+that+expected+records+are+contained&sysparm_topic= "KB0535248: Verifying that expected records are contained in the Update Set").
2.  Verify if you are affected by one of the Known Errors impacting update sets. See the following articles: [KB0523691: Update set preview displays backed out update set data](/kb_view.do?sysparm_article=KB0523691&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=e51bd61e870b1100957bb3aeef434d0ffd1620f84826fcf244efcd9b0de48955442e4b76&sysparm_nameofstack=&sysparm_product=&sysparm_search=%22update+set%22+commit&sysparm_topic=Known+Error+Database "KB0523691: Update set preview displays backed out update set data"); [KB0522588: Unique records are not displaying an error when previewing or committing an update set](/kb_view.do?sysparm_article=KB0522588&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=e51bd61e870b1100957bb3aeef434d0ffd1620f84826fcf244efcd9b0de48955442e4b76&sysparm_nameofstack=&sysparm_product=&sysparm_search=%22update+set%22+commit&sysparm_topic=Known+Error+Database "KB0522588: Unique records are not displaying an error when previewing or committing an update set"); [KB0523177: Cannot commit update sets after datacenter migration](/kb_view.do?sysparm_article=KB0523177&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=e51bd61e870b1100957bb3aeef434d0ffd1620f84826fcf244efcd9b0de48955442e4b76&sysparm_nameofstack=&sysparm_product=&sysparm_search=%22update+set%22+commit&sysparm_topic=Known+Error+Database "KB0523177: Cannot commit update sets after datacenter migration"); or [KB0522903: Update Set Commits are unnecessarily slow due to CollisionDetector](/kb_view.do?sysparm_article=KB0522903&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=e51bd61e870b1100957bb3aeef434d0ffd1620f84826fcf244efcd9b0de48955442e4b76&sysparm_nameofstack=&sysparm_product=&sysparm_search=%22update+set%22+commit&sysparm_topic=Known+Error+Database "KB0522903: Update Set Commits are unnecessarily slow due to CollisionDetector").
3.  Verify which records will be captured with an update set. See the following article: [KB0535262: Checking which records will be captured in an Update Set](/kb_view.do?sysparm_article=KB0535262&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=f4a4379d87031100957bb3aeef434dd26161472981ff9eb33416fb342ecdb9a1f33d1f6f&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0535262&sysparm_topic= "KB0535262: Checking which records will be captured in an Update Set"). 
4.  Troubleshoot the update set preview. See the following article: [KB0535263: Troubleshooting Update Set Preview](/kb_view.do?sysparm_article=KB0535263&ni.dependent.topic=kb_knowledge.category&sysparm_category=&sysparm_ck=f4a4379d87031100957bb3aeef434dd26161472981ff9eb33416fb342ecdb9a1f33d1f6f&sysparm_nameofstack=&sysparm_product=&sysparm_search=KB0535263&sysparm_topic= "KB0535263: Troubleshooting Update Set Preview").

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: If your problem still exists after trying the steps in this article:<ul><li>Submit an incident to ServiceNow <a title="Customer Support" href="http://www.servicenow.com/support/contact-support.html" target="_blank" rel="noopener noreferrer nofollow">Customer Support</a> and note this Knowledge Base article ID (KB0535178) in the problem description.</li></ul></td></tr></tbody></table>
