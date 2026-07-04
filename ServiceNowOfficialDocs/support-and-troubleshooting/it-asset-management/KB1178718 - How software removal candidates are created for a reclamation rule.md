---
title: "How software removal candidates are created for a reclamation rule"
aliases:
  - KB1178718
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1178718
kb_number: KB1178718
last_modified: 2026-05-26
---

## How software removal candidates are created for a reclamation rule

  

### Summary

This article describes how the Software Asset Management (SAM) reclamation process creates removal candidates by scanning installed software products associated with a reclamation rule. 

### Release

All supported releases

### Instructions

### **Script include and scheduled job**

The SAMPReclamationUtil script include creates removal candidates:

/sys\_script\_include.do?sys\_id=9c18c292cb632200f2de77a4634c9c73

This script include is called during execution of the scheduled job "SAM - Identifying New Reclamation Candidates":

/sysauto\_script.do?sys\_id=b84cb463676222007d59cbb35685efda

### **Conditions for removal candidate creation**

For each software product in the reclamation rule, the process checks the following conditions: 

1.  A Normalized Product (not the Product) exists in the Software Installations \[cmdb\_sam\_sw\_install\] table.
2.  The record has an Installed On field pointing to a computer or host with the software product  in the \[cmdb\_sam\_sw\_install\] table .
3.  The record has a valid Assigned to field populated in the \[cmdb\_sam\_sw\_install\] table .
4.  Conditions 1-3 match with the Configuration Item in the Software Usage \[samp\_sw\_usage\] table.
5.  The Last used before filter condition on the reclamation rule is satisfied.

### **User field matching logic**

The Assigned to field on the configuration item must match the User field on the usage record according to the following logic:

| 
CI Assigned to field

 | 

Usage record User field

 | 

Result

 |
| --- | --- | --- |
| 

Empty

 | 

Empty

 | 

Removal candidate created

 |
| 

Empty

 | 

Has value

 | 

Removal candidate NOT created

 |
| 

Has value

 | 

Empty

 | 

Removal candidate NOT created

 |

### **Output**

Removal candidates are created in the Software Reclamation Candidates \[samp\_sw\_reclamation\_candidate\] table for records in the Software Usage \[samp\_sw\_usage\] table that satisfy all conditions.

### Related Links

[Add a software reclamation rule](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/t_AddAReclamationRule.html "Add a software reclamation rule")

[Add a software removal candidate](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/t_AddAReclCandidate.html "Add a software removal candidate")
