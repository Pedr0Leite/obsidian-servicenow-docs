---
title: "Orchestration activity in workflow will not accept Record Producer variables"
aliases:
  - KB0713585
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713585
kb_number: KB0713585
last_modified: 2024-04-07
---

## Orchestration activity in workflow will not accept Record Producer variables

  

### Issue

# Symptoms

* * *

A Record Producer has been created and a workflow has been attached, however the variable values defined in the Record Producer are not being passed to the workflow activity.

# Release

* * *

Jakarta 

# Cause

* * *

Variable needs to be mapped to the field of the target table.

# Resolution

* * *

As an example, consider the record producer below targeted to the table **sc\_task**:

![](sys_attachment.do?sys_id=b9aa68a6db42b450e515c223059619a6)

In the Related Links -> Variables, the variable defined needs to be mapped out to a field in the target table, in this example, the variable "**Order name**" is being mapped to the Description field of the **sc\_task** table: 

![](sys_attachment.do?sys_id=7daa68a6db42b450e515c223059619ab)

In the workflow activity in this example, you can access the variable value with current.description:

![](sys_attachment.do?sys_id=fdaa68a6db42b450e515c223059619b0)

# Additional Information

* * *

[Record Producer](https://docs.servicenow.com/csh?topicname=c_RecordProducer.html&version=latest "Record Producer")
