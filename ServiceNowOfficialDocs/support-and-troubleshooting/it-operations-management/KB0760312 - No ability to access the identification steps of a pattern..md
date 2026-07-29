---
title: "No ability to access the identification steps of a pattern."
aliases:
  - KB0760312
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760312
kb_number: KB0760312
last_modified: 2024-07-31
---

## No ability to access the identification steps of a pattern.

  

### Issue

To enter **debug** mode of a pattern, a pattern has to be opened from **pattern designer** and then if we click on the identification step, it acts as a hyperlink and redirects to the internal steps that would eventually let us get into the debug mode by using the UI action 'Debug Mode'.

There can be a situation where we could locate a pattern, open it in the pattern designer to find that there is no ability to access the identification step and it appears as if the hyperlink is broken. The below screenshot can be referred for understanding the scenario.

![](sys_attachment.do?sys_id=317eed751b5af890ccc253da234bcbe4)

### Cause

There would be 2 different types of patterns, **excluding** Shared Libraries-

1) **Infrastructure** Patterns, that typically are used to target devices.

2) **Application** patterns that target different types of applications installed on Devices. 

As patterns are being used in both horizontal and top-down discoveries, both the above types are available once discovery is activated on the instance. 

This kind of inability would usually be seen for patterns of type '**Application**' as they are significantly used during the **top-down** discovery. The identification steps can be viewed and the ability to enter Debug mode for such kind patterns only if the Service Mapping plugin is active/enabled. 

### Resolution

For the application patterns that are explicitly referenced in top-down discovery, it's mandatory to have the Service Mapping plugin enabled for accessing the internals of them. So, in this scenario.

1) Check to see is the **Service Mapping plugin** is active on the instance. 

2) If no, the customer has to be made aware so that a decision from their organization level can be taken for activation, if needed.

3) If Horizontal discovery is the only need, then most of the application type patterns are not referenced and hence they stay inactive, though they can be viewed from pattern designer.
