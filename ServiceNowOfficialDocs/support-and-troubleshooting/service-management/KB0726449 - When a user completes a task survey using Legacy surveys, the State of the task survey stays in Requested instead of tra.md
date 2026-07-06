---
title: "When a user completes a task survey using Legacy surveys, the State of the task survey stays in \"Requested\" instead of transitioning to a State of \"Completed\"
aliases:
  - KB0726449
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726449
kb_number: KB0726449
last_modified: 2024-04-07
---

## When a user completes a task survey using Legacy surveys, the State of the task survey stays in "Requested" instead of transitioning to a State of "Completed"

  

### Issue

# Symptoms

* * *

-   All task\_survey records which were completed by their respective assigned users are staying in a State of "Requested" instead of transitioning to a State of "Completed".

# Release

* * *

-   Kingston Patch 7

# Cause

* * *

After a thorough investigation across multiple teams of Product Owners, it is our recommendation that the user move to the current Survey Management application, as the future of Survey Management lay in the current application, versus in legacy surveys.

# Resolution

* * *

As mentioned above, it is our recommendation that the user migrate to the current Survey Management application.  
  
If the user is not ready to move to the current Survey Management application, here is a possible suggestion which could help with this behavior:  
  
To prevent this behavior from happening in the future (a fix-forward option), perhaps the user could create a Business Rule with a query string where the Survey is the "General Survey" Survey and find a current.response on the task on the task\_survey table. It is using the Task ID from the survey\_response table and making a connection to the sys\_id on the task\_survey table to the 'task' field. Once these two match, it will set the state to "Completed".   
  
As such a Business Rule would be custom, writing and testing it would be something that the user and their development team would handle, as Support engineers are experts in OOB behaviors, and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementing of customizations like this is not in Support's area of expertise.  
  
If the user would prefer to migrate to the current Survey Management application, here are some helpful documents to assist with the migration process: 

-   [Legacy survey migration](https://docs.servicenow.com/csh?topicname=c_MigrateSurveys.html&version=latest "Legacy survey migration")
