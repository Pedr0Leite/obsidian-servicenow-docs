---
title: "User not seeing groups in global search"
aliases:
  - KB0781518
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781518
kb_number: KB0781518
last_modified: 2024-04-07
---

## User not seeing groups in global search

  

### Issue

Users are not seeing the Configuration Items search group in the global search results because they have a user preference record to not display results for Configuration Items.

### Resolution

1\. As admin, go to User Administration > User Preferences  
  
2\. Filter the list for Name starts with ts.table and User is "user name'  
  
3\. There should be one matching record by name:  
  
     ts.table.b7318c196fdd4a00fe09e82fae3ee40b ( Sometimes there are more than one record also)  
  
4\. Double click the false value in the Value field and set it to true (lowercase) and then click the green checkmark to save it.  
  
    After this change, the user should see Configuration Items results when he performs global searches.

### Related Links

If there are more than one record for that user, You have to make  true one by one and check the results.
