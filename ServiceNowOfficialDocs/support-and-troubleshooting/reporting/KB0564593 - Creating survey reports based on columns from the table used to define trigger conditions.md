---
title: "Creating survey reports based on columns from the table used to define trigger conditions"
aliases:
  - KB0564593
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564593
kb_number: KB0564593
last_modified: 2024-04-07
---

## Creating survey reports based on columns from the table used to define trigger conditions

  

### Issue

Creating survey reports based on columns from the table used to define trigger conditions

  
  

# Problem

* * *

Customers cannot create survey reports based on columns from the source data table that is used when defining trigger conditions.

Because the source data table information is stored as a document reference in the Survey instance and dot-walking is not available for this type of reference, you cannot write conditions that reference source data fields.  

# Workarounds

* * *

There are two possible workarounds for this situation:

-   For surveys triggered from the task records, Geneva now has a view called task\_assessment\_detail to provide a view like the legacy task\_survey\_detail view. This view provides columns from Metric Type, Assessment/Survey Instance, Task, and Metric Results.  
      
    For example, if the requirement is to report on Incident-triggered Survey Responses by Assignment group, the following report can be set up on Task Assessment Details.
    
    ![](/sys_attachment.do?sys_id=d41ae4e2db42b450e515c22305961953)
-   Using Related Fields, which can be set up to capture particular columns from the source table while configuring the trigger. These values are captured during the instance creation as Related Record columns (Related Record 1 to 5). The related record can then be used in filters, grouped by clause, and so on.
    
    For example, say the intent is to report on survey results for the current month based on the Assignment group. The Related Field can be mapped to the Assignment group in the trigger setup. When the incident survey is sent out, the Assignment group on the incident would be captured as Related Record 1 on the survey instance. The report can use Related Record 1 to set up report filters, group by clauses, and so on.
    

The following example uses an Assignment Group mapped to Related Field 1 which is captured as Related Record 1 on the Survey instance and then used in the report on Metric results.

**Trigger Setup:**

![](/sys_attachment.do?sys_id=281ae4e2db42b450e515c2230596196c)

**Metric Results Including Related Record values from Survey/Assessment Instance.**

![](/sys_attachment.do?sys_id=a81ae4e2db42b450e515c22305961974)

**Report Creation:**

![](/sys_attachment.do?sys_id=a81ae4e2db42b450e515c2230596198d)
