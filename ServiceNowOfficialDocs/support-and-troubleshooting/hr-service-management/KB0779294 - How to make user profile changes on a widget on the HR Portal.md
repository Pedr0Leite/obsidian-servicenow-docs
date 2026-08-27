---
title: "How to make user profile changes on a widget on the HR Portal"
aliases:
  - KB0779294
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779294
kb_number: KB0779294
last_modified: 2024-04-08
---

## How to make user profile changes on a widget on the HR Portal

  

### Issue

Need to make a change on a the "About" widget on the HR Portal so the number that displays there is the "Business Phone" not the mobile phone.

### Release

Madrid, New York

### Resolution

\[code\]**Steps to Reproduce:** \[/code\]  
1\. Log onto <instance name>  
2\. Impersonate HR User  
3\. Open My HR Portal  
4\. Click on my name on the top right hand corner of the page  
5\. Select profile and navigate to the "About" section

  
\[code\]**Solution:** \[/code\]  
  
To remove the Mobile phone from the HR Profile form, you do not need to edit the Widget. The data being displayed on the HR Portal comes from the Service Portal view of the User Profiles.  
  
To get only the Business Phone to display, here are the steps to follow:  
  
Go to User Administration --> Users --> Open any record.  
  
Change the view of the record from Default view to Service Portal view.  
  
Once the view is Service Portal view from the User record --> Do Configure --> Form Layout --> Remove Mobile phone from the selected list --> Save the form.  
  
Now go to HR Portal and refresh the page. You will only see Business Phone displayed.
