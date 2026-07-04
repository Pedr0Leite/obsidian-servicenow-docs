---
title: "FAQ: Software Model field in the Software Discovery Model Table not populating"
aliases:
  - KB0862977
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862977
kb_number: KB0862977
last_modified: 2026-04-27
---

## FAQ: Software Model field in the Software Discovery Model Table not populating

  

### Summary

##### **1\. What is Software Discovery Model**

Software discovery models can be used to help normalize the software you own with analyzing and classifying models to reduce duplication.

##### **2\. Where do we find Software discovery models**

Software discovery models are stored in the Software Discovery Model \[cmdb\_sam\_sw\_discovery\_model\] table

##### **3\. Can we create Software Discovery Models**

Manual creation of software discovery models is not feasible. A mix of fields are used by the ServiceNow platform to compare the new software discovery model to an old software model.

##### **4\. Do you find Software Model field updated in Software Discovery Models table.**

Take a note that discovery models with modified Software Model fields were either manually changed or produced prior to the "SAM Foundation"

##### **5\. Does License calculation consider software Model field on Software Discovery Model**

The Out-of-the-Box Software Model field on Software Discovery Model records has not been updated or utilized in calculations since the SAM Foundation.

##### **6\. How to check which software discovery models are related to specific software model**

The Discovery model's "Software Model" field has been deprecated.

1.  Go to the "Software Model" User Interface (UI)
2.  Choose a software model
3.  Click the link that says "Show matching Discovery models" in the form.
4.  This will display the Discovery models that are appropriate for the chosen software model.

### Related Links

[Software discovery models](https://docs.servicenow.com/csh?topicname=c_UsingSoftwareDiscoveryModels.html&version=latest "Software discovery models")

[Manage software models](https://docs.servicenow.com/csh?topicname=t_ManagingSoftwareModels.html&version=latest "Manage software models")
