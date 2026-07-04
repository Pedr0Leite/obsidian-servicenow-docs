---
title: "Stockroom tasks are created in'Pending' state."
aliases:
  - KB0791658
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791658
kb_number: KB0791658
last_modified: 2024-04-08
---

## Stockroom tasks are created in'Pending' state.

  

### Issue

Stockroom tasks are created in'Pending' state.

### Resolution

The Stockroom tasks are being created in "Pending" state because the state is not hardcoded in the Stock Rule Runner Scheduled Job which creates these tasks.  
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_trigger.do?sys\_id=073f0b6437112000fceabfc8bcbe5d42

In turn, the system is defaulting the tasks state to "Pending" state.

To create all Stockroom tasks in a particular state the line below can be added to Stock Rule Runner Scheduled Job below.

https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_trigger.do?sys\_id=073f0b6437112000fceabfc8bcbe5d42

task.state = '3';

FROM:

// Add Task  
//we keep adding task because:  
//if procurement plugin is not enabled, then we create TASK for existing Stock Rule records  
//if procurement plugin is enabled, then we create TASK for the user who have been used to TASK  
var task = new GlideRecord('task');  
task.initialize();  
task.assigned\_to = stockLevel.stockroom.manager;  
task.assignment\_group = stockroom.assignment\_group;  
task.short\_description = 'Quantity threshold breached: '+ stockroom.name;  
task.description = 'Stockroom: ' + stockroom.name + '\\nItem: ' + model.display\_name + '\\nQuantity: ' + quantity + '\\nThreshold: ' + threshold;  
task.insert();

TO:

// Add Task  
//we keep adding task because:  
//if procurement plugin is not enabled, then we create TASK for existing Stock Rule records  
//if procurement plugin is enabled, then we create TASK for the user who have been used to TASK  
var task = new GlideRecord('task');  
task.initialize();  
task.assigned\_to = stockLevel.stockroom.manager;  
task.assignment\_group = stockroom.assignment\_group;  
task.short\_description = 'Quantity threshold breached: '+ stockroom.name;  
task.description = 'Stockroom: ' + stockroom.name + '\\nItem: ' + model.display\_name + '\\nQuantity: ' + quantity + '\\nThreshold: ' + threshold;  
**task.state = '3';**  
task.insert();

We suggest thoroughly testing the above in a sub production instance prior to implementing in production.
