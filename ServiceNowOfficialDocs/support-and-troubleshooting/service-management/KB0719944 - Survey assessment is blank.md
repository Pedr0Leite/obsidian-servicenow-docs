---
title: "Survey assessment is blank"
aliases:
  - KB0719944
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719944
kb_number: KB0719944
last_modified: 2025-04-01
---

## Survey assessment is blank

  

### Issue

-   **Take Assessment** renders a blank page.
-   **Take Survey** renders a blank page.
-   **Survey email link** renders a blank page

### Cause

Possible Causes:

1.  The read ACLs for asmt\_assessment\_instance were customized
2.  An assessment metric is inactive or pointing to a different assessment category
3.  The UI page "**assessment\_take2**" was customized and threw an Exception:

         java.lang.NullPointerException: com.snc.assessment\_core.questionset.AssessmentQuestionSet3.

### Resolution

1.  Check if the UI page "assessment\_take2" was customized and try to revert it to the out-of-box (OOB) version
2.  Check if the read ACLs for asmt\_assessment\_instance were customized and the users are not passing these ACLs. (Check on [https://instance-name.service-now.com/sys\_security\_acl\_list.do?sysparm\_query=nameLIKEassessment%5Ename%3Dasmt\_assessment\_instance%5Eoperation%3Dread](https://instance-name.service-now.com/sys_security_acl_list.do?sysparm_query=nameLIKEassessment%5Ename%3Dasmt_assessment_instance%5Eoperation%3Dread))
3.  If the UI page is already OOB and the users are passing the read ACLs for the asmt\_assessment\_instance, do a "Debug All" as an administrator
4.  Impersonate the user who has the blank survey issue
5.  Check the debug logs when loading the assessment survey and check for 'java.lang.NullPointerException' that may cause rendering issue for the page  
    Sample logs:
    
    17:38:09.863: Time: 0:00:00.000 for: testinstance\_1\[glide.4\] SELECT ... FROM (sys\_ui\_message sys\_ui\_message0 INNER JOIN sys\_metadata sys\_metadata0 ON sys\_ui\_message0.\`sys\_id\` = sys\_metadata0.\`sys\_id\` ) WHERE sys\_ui\_message0.\`key\` = '**Survey question 2**?' AND sys\_ui\_message0.\`language\` = 'en' /\*...\*/  
    7:38:09.867: **java.lang.NullPointerException: java.lang.NullPointerException: com.snc.assessment\_core.questionset.AssessmentQuestionSet.load**(AssessmentQuestionSet.java:895)  
     com.snc.assessment\_core.TakeAssessment.doTag(TakeAssessment.java:38)  
    \[...\]
    
6.  Check the logs for the corresponding assessment metric before the error was encountered 
7.  Check the assessment metric if it is inactive or if it is pointing to a metric on the same Assessment category
8.  If it is active, check the **Depends On** field of the assessment metric
    -   Check if this metric is active or it is pointing to a metric on the same Assessment category
