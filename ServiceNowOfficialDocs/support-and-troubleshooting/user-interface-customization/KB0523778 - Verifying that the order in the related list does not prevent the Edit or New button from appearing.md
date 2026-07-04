---
title: "Verifying that the order in the related list does not prevent the Edit or New button from appearing"
aliases:
  - KB0523778
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523778
kb_number: KB0523778
last_modified: 2025-01-26
---

## Verifying that the order in the related list does not prevent the Edit or New button from appearing

  

### Issue

Verifying that the order in the related list does not prevent the Edit or New button from appearing

  
  
  
Overview

* * *

Permission to see the **Edit** or **New** button on a related list is determined by Security Evaluation for the first record in the list. For example, if a user has access to the second record in a related list, the system only checks security against the first record to define if the **Edit** button appears.

Procedure

* * *

To verifying the order to the records in the relate list does not prevent the Edit or New button from appearing:

1.  Navigate to the related list that does not display the **Edit** or **New** button.  
      
    In this example, the **Tasks** related list in the **Change** form does not display the **New** button. Notice that the first record in the related list is a CLAS record.
    
    ![](/sys_attachment.do?sys_id=7dcae0e6db42b450e515c22305961968 "Related List without New button")
    
2.    
    
3.  Review the order in which the related list records appear.
4.    
    
5.  Change the sorting on the related list.
6.    
    
7.  Reload the form.
    
    In this example, when a TASK record is the first record in the related list, the **New** button is now visible even though it is the same list of records.
    
    ![](/sys_attachment.do?sys_id=b9cae0e6db42b450e515c22305961987 "Related List with New button")
    
    The ACLs against the CLAS record prevent the **New** button from appearing. When the first record in the list is a TASK record, the ACL allows the **New** button to appear on the related list.
