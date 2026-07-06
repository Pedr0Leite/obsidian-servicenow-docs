---
title: "Existing archive rule on task/cmdb child table prevents creation of new archive rule in parent task/cmdb table"
aliases:
  - KB0790981
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790981
kb_number: KB0790981
last_modified: 2024-08-05
---

## Existing archive rule on task/cmdb child table prevents creation of new archive rule in parent task/cmdb table

  

### Issue

### **For Cmdb table issue example:**

#### **1) We want to implement archiving for the cmdb tables and its children tables.**

#### **2) We originally had a rule that worked at the cmdb\_ci table at a high level.**

#### **3) We archived Computers and Personal Computers, but then if I tried to setup an archive for CMDB\_CI the table was not shown, in order to archive it.**

#### **4) Therefore, we modified the existing archive rule with one at the lowest level of that chain of extended tables to be CMDB\_CI\_PC\_Hardware then tried to create a new rule for its parent table CMDB\_CI\_Computer, it was still not shown.** 

### **For Task table issue example:**

#### **1) We want to implement archiving for the task tables and its children tables.**

#### **2) We originally had a rule that worked at the task table at a high level.**

#### **3) We archived children tables from the task table, but then if I tried to setup an archive for the task table, the table was greyed out that did not allow us to select it in order to archive it.**

#### **4) We also have archived children tables from the task table where it does not allow us to create archive rules for 2nd layer children tables of 1st layer children tables from the task table.** 

### Release

#### **This applies to all environments**

### Cause

#### **1) We found out that the reason why you can't select the parent task or parent cmdb table or 2nd layer children tables from 1st layer children tables of task or children tables from cmdb is because unfortunately our system is not designed to create multiple archive rules per hierarchy (vertically) in any table that has extended tables (children tables).**

#### **2) This is a known issue documented on PRB713693**  
  
**3) If you modify the only existing 1st layer children archive rules, then the parent task or parent cmdb table or 2nd layer extended tables will not be grayed out to allow you to select it.**

**IMPORTANT: The archiver allows to create multiple archive rules for Table per Hierarchy table that are Horizontally in the same level, but it will not allow you to create archive rules for the Table Per Hierarchy table's parent or children (Vertically).**

####   
  

### Resolution

#### **WARNING****:** **This approach will work in respects to archiving, but will not make Archive Destroy fully work for children cmdb or task archive tables due to PRB1764668.**

#### **The best solution I have for you to be able to archive per hierarchy in one archive rule is the following:**

####   
**Modify the existing archive rule on the top hierarchy task Or 1st children layer hierarchy from task or cmdb, then start adding the conditions on the extended tables you want to archive. For example:**

####   
Example for cmdb table:

  
Table: cmdb  
  
Condition: Class is a Hardware  
           OR Class is a Computer  AND name....   
           OR Class is a Printer...AND name CONTAINS........etc

####   
  
Example for task table:

  
Table: task  
  
Condition: Task Type is Planned Task  
           OR Task Type is Issue  AND number....   
           OR Task Type is Incident...AND number STARTSWITH........etc
