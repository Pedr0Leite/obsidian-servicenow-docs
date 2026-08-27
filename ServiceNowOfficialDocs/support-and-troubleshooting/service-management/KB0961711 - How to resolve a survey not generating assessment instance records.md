---
title: "How to resolve a survey not generating assessment instance records"
aliases:
  - KB0961711
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961711
kb_number: KB0961711
last_modified: 2026-02-16
---

## How to resolve a survey not generating assessment instance records

  

### Issue

Troubleshoot issues where a survey stops triggering or stops generating assessment instance records. When running instance creation scripts in /sys.scripts.do, the message "instance is not created" may appear.

The following scripts may be used to test assessment instance creation:

**HR case trigger condition test**

var gr = new GlideRecord("sn\_hr\_core\_case"); gr.get("<sys\_id\_of\_record>"); (new sn\_assessment\_core.AssessmentCreation()).conditionTrigger(gr, '<sys\_id\_of\_trigger\_condition>'); 

**Direct assessment creation test** 

var instanceId = new SNC.AssessmentCreation().createAssessments("<sys\_id\_of\_survey\_def>", "", "<sys\_id\_user>"); 

If assessment instances are not created, the following warning message may appear in the log:

\[AssessmentCreation - createInstances\_Parameters\]: For assessment 158a17920f226bc0484991dbe1050e9b, for user 3b8a6e79134cab004744bd122244b072, instance is not created. Possible reasons are:   
1\. Please make sure that at least one metric category has at least one assessable record associated.   
2\. Please make sure that at least one metric category has at least one metric.   
3\. Please make sure that if domain plugin is installed, at least one assessable record is visible to this user.   
4\. Please make sure that at least one metric category is accessable to this user - check the roles on category.   
5\. Please make sure that this user has required roles to access the assessable record.: no thrown error \[AssessmentCreation - createInstances\_Parameters\]: For assessment 158a17920f226bc0484991dbe1050e9b, for following users \[3b8a6e79134cab004744bd122244b072\], no instance is created. Please find previous error messages for details.: no thrown error 

### Release

All supported releases

### Resolution

Review each condition listed in the warning message. To check for a related assessable record, complete the following steps:

1.  Go to **Assessments** \> **Assessable Records**.
2.  Change the **Evaluation method** from **Assessment** to **Survey**.
3.  Search for the survey name in the **Name** field.
4.  In the **Category** related list, select **Edit**.
5.  In the available and selected lists, move the correct category to the selected side.
6.  Select **Save**.
