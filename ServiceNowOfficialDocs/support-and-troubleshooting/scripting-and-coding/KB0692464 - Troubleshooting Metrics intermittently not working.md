---
title: "Troubleshooting Metrics intermittently not working"
aliases:
  - KB0692464
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692464
kb_number: KB0692464
last_modified: 2024-01-28
---

## Troubleshooting Metrics intermittently not working

  

### Issue

# Symptoms

* * *

A metric definition setup on a task record was not triggered intermittently, for example lets consider a metric definition for field "Assignment Group" on incident table. 

When there is any change on the incident record with the "Assignment Group" field, the defined metric definition, should create a metric record as shown in the below screenshot. 

![](sys_attachment.do?sys_id=302cec2edb42b450e515c223059619a4)

However, this was not happening intermittently during specific scenario, i.e when a work-flow sets the "Assignment Group" field after record creation, this article will detail on this specific scenario.

# Release

* * *

Any supported release. 

# Cause

* * *

The metric events are triggered by the out of the box provided business rule "metrics events" ("[uri=sys\_script.do?sys\_id=35f9861dc0a808ae00ecf631cc51888c](uri=sys_script.do?sys_id=35f9861dc0a808ae00ecf631cc51888c "uri=sys_script.do?sys_id=35f9861dc0a808ae00ecf631cc51888c")").   
  
Ideally, the metrics event business rule suppose to run after executing the "start workflow" out of the box business rule. So that, if there is any work flow activity which does update the record for which metric definition exists, system will trigger its metric definition.

However, both the business rules has the same execution order of "10000". Thus task record gets updated by the work flow in couple of seconds from the creation time.

Due to these reasons, there is a possibility that "metrics event" business rule execution might get missed and hence it will not create the metrics record. for that specific record update coming from work-flow. 

# Resolution

* * *

Set the order field value of "metrics event" business rule greater than "start workflow" business rule. 

# Additional Information

* * *

[metrics](https://docs.servicenow.com/csh?topicname=c_MetricDefinitionSupport.html&version=latest "metrics")

[Business Rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Business Rules")

[Workflow](https://docs.servicenow.com/csh?topicname=c_WorkflowOverview.html&version=latest "Workflow")
