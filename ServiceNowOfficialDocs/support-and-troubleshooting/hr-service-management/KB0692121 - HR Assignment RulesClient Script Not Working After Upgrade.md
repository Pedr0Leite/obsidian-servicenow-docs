---
title: "HR Assignment Rules/Client Script Not Working After Upgrade"
aliases:
  - KB0692121
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692121
kb_number: KB0692121
last_modified: 2024-04-07
---

## HR Assignment Rules/Client Script Not Working After Upgrade

  

### Issue

# Symptoms

* * *

-   Assignment rule does not update HR case
-   Custom business rule/client script does not update case record

# Release

* * *

Kingston

# Environment

* * *

Upgraded from Istanbul to Kingston 

# Resolution

* * *

\- Custom business rule/client script does not update case record

This business rule is not working due to the actions set to run. For example, when the code below was added to this business rule as a test:   
  
current.short\_description = 'Beneficiary Change';   
  
This updated as expected. However, in this case you made need to write a statement checking what the hr\_service field is set to, then update the short description based on that value. This was also able to set to an after insert business rule and set a script:   
  
var test = current.hr\_service.getDisplayValue();   
current.short\_description = test;   
current.update();   
  
This also set the short description field as expected. Again, these are just a couple examples of how this can work. You will need to determine the best method of implementing for your needs. These are simply examples to show that this implementation should be possible. 

\- Assignment rule does not update HR case

  
This behavior was related to how the testing was conducted. Notice on the assignment rule the Table field is set to HR Case. However, users are not updating the COE field on the Case Creation UI. When User A changes the HR service field to 'Beneficiary Change' the COE field is defaulting to HR Total Rewards case. This is the table associated with the record being created. Since this table does not match the table in the assignment rule, the assignment group is not being filled in. A quick way to test this is to update the assignment rule Table field to HR Total Rewards case.
