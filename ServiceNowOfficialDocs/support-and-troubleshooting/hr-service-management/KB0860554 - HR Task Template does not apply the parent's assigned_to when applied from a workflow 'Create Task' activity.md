---
title: "HR Task Template does not apply the parent's assigned_to when applied from a workflow 'Create Task' activity "
aliases:
  - KB0860554
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860554
kb_number: KB0860554
last_modified: 2026-02-26
---

## HR Task Template does not apply the parent's assigned\_to when applied from a workflow 'Create Task' activity

  

### Issue

When an HR Task is created from a Workflow Activity 'Create Task', the Template selected on the WF Activity will not be applied.

**Set-Up:**

1\. Create a new HR Template "Test Template-Not assigning from parent case":  
\- Name: Test Template-Not assigning from parent case  
\- Table: HR Task  
\- Owning Group: HR Tier 1  
\- On the 'Additional Fields' tab:

-   Parent Case Table: HR Case
-   Assign To: Assigned To

![](sys_attachment.do?sys_id=c6643871871fbe542d5cbbb5cebb3505)

2\. Create a new Workflow "Add Beneficiary Task":

  
Properties:

-   Table: HR Total Reward Case
-   If condition matches: Run Workflow Always
-   Condition: 'HR Service IS Beneficiaries Inquiry' AND 'State CHANGES TO Ready'

![](sys_attachment.do?sys_id=de643871871fbe542d5cbbb5cebb3573)

Add an activity of Type: Create Task

-   Name: Create HR Task
-   Task type: HR Task \[sn\_hr\_core\_task\]
-   Priority: 3
-   Task values from: Template
-   Task Template: Test Template-Not assigning from parent case

![](sys_attachment.do?sys_id=1e643871871fbe542d5cbbb5cebb350b)

**Steps to Reproduce:** 

  
1\. Create New Case  
2\. Pick any user  
3\. Select HR Service = 'Beneficiaries Inquiry' and create the case  
4\. On the case form, assign the case to an agent and save the record  
5\. Move the case to 'Ready for Work' to trigger the workflow

**Behaviour:**

The HR Task will be generated, the Template values will be applied, but the assigned\_to from the parent case is NOT set, even though the HR Task Template specifies to assign the task to the parent case's assigned\_to.

### Release

Any release

### Cause

The "template" field on the HR Template determines what values are to be set on the "table" \[in this case table is "sn\_hr\_core\_task"\] when the task is created. However, when the template's assignment\_type is _fulfiller_ and the assigned\_to is "parent case assign to", the assigned\_to value is not populated in the "template" field of HR template, as shown below.  
  

```
<template>short_description=Test Template-Not assigning from parent case^hr_task_type=mark_when_complete^state=10^set_reminder=true^when_to_send=1^interval=1^email_template=037f9369c3733200b599b4ad81d3aebc^task_support_team=users_and_groups^parent_case_users=6ac478f5e7400300d3dd8a63c2f6a956^EQ</template>
```

  
However, if the assignment\_type is _fulfiller_ and assigned\_to is "Named User" and the assigned\_to is populated as one the users, then the template field gets the assigned\_to which will eventually set the assigned\_to field of the HR Task.  
  

```
<template>short_description=Test Template-Not assigning from parent case^hr_task_type=mark_when_complete^state=10^set_reminder=true^when_to_send=1^interval=1^email_template=037f9369c3733200b599b4ad81d3aebc^task_support_team=users_and_groups^parent_case_users=6ac478f5e7400300d3dd8a63c2f6a956^assigned_to=22826bf03710200044e0bfc8bcbe5dec^EQ</template>
```

  
This is because the Workflow uses the GlideTemplate class in order to set the values in a table, and GlideTemplate references the "Templates" \[sys\_template\] table. Hence until and unless assigned\_to is populated in the template field as shown in the second case, the assigned\_to of an HR Task is not getting populated.  
  
Basically, the "**Create Task**" workflow activity does not take the assignment\_type of fulfiller/employee fields into consideration, being them specific to the "HR Templates" \[s\_hr\_core\_template\] table (rather than "Templates" \[sys\_template\] table).

In order to populate the assigned\_to field based on the assignment type, OOB there is a \[before insert\] Business Rule "Apply Template (before)" on the "HR Task" \[sn\_hr\_core\_task\] table which requires the "template" and "parent" columns of the task to be set in order to populate the" assigned\_to" of the HR Task before inserting the record.

The activity "Create Task" is a platform feature which is used to create a task based on "sys\_template", whereas sn\_hr\_core\_template is an HR table that extends sys\_template.

This Workflow Activity uses the method "\_createTask()" defined in Script Include "WFCreateTaskActivityUtils" in order to create a task and it does not populate neither the "template" field of the task nor the the "parent" field, hence the BR "Apply Template (before)" on HR Task does not trigger and the "assigned\_to" field is not populated.  
  

The above explains why in this scenario the platform workflow activity "Create Task" cannot be used in this case.

### Resolution

If an HR Template has to be used, the two possible options are:

  
1) A custom workflow activity needs to be created in order to fill the values. Script Include "hr\_TemplateUtils" can be used in order to apply the template

2) For an HR Service, set the "fulfillment" type as Service Activity, which will create tasks and approvals based on configuration, as described in the product documentation:

[Configure a service activity for an HR service](https://docs.servicenow.com/csh?topicname=configure-service-activity-for-hr-service.html&version=latest "Configure a service activity for an HR service")
