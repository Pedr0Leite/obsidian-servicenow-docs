---
title: "When a CI is reclassified, the reconciliation rules do not apply"
aliases:
  - KB0749743
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749743
kb_number: KB0749743
last_modified: 2025-04-08
---

## Issue

# Symptoms

Reconciliation rules are not getting honored if the class of the CI is modified.

# Release

Applicable from Helsinki and above

# Environment

Example:

Set the following Reconciliation rules on the Computer class:

**Reconciliation Rule #1**

Data Source: Manual Entry  
Applies to: Computer  
Attributes: All

**Reconciliation Rule #2**

Data Source: Service-now  
Applies to: Computer  
Attributes: CPU Name

**Steps for Testing**

1.  Find a CI belonging to the Computer class in the CMDB and update the following fields:

Class >> cmdb\_ci\_server  
CPU Name >> Test CPU  
CPU Type >> Test CPU Type

2.  Run Quick Discovery on the CI
3.  Check the CI record. It would have updated the fields as below:

Class >> cmdb\_ci\_computer  
CPU Name >> \[The exact name of the CPU as existed before making the changes as in step 1\]  
CPU Type >> \[The exact CPU type as existed before making the changes as in step 1\]

4.  Update the CI record with the following fields:

CPU Name >> Test CPU  
CPU Type >> Test CPU Type

5.  Launch the Quick Discovery
6.  Check the CI record. It would have updated the fields as below:

CPU Name >> \[The exact name of the CPU as existed before making the changes as in step 1\]  
CPU Type >> Test CPU Type

# Cause

This is an expected behaviour.

# Resolution

No remediation action is required.
