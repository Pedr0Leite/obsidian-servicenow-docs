---
title: "Event Management licensing issue"
aliases:
  - KB0744932
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744932
kb_number: KB0744932
last_modified: 2024-02-23
---

## Issue

### Symptoms

The central issue is that certain CI classes are being flagged as unknown and this has an undesirable licensing implication for the customer

**Example 1 :**

Highest contributor with 74% prevalence – CIs that exist in the CMDB under non-server classes are not recognized at all and enter the em\_unique\_nodes tables as type=Unknown, is\_licensable=TRUE. We have verified the CI records existed in the CMDB at the time of the em\_unique\_nodes record creation in one of the following classes:

o Application \[cmdb\_ci\_appl\]  
o IP Router \[cmdb\_ci\_ip\_router\]  
o IP Switch \[cmdb\_ci\_ip\_switch\]  
o Telecommunications Hardware \[cmdb\_ci\_telecom\_hardware\] o Voice System Hardware \[cmdb\_ci\_voice\_hardware\]  
o Voicemail\[cmdb\_ci\_voicemail\_voice\]

**Example 2 :**

Only 2% prevalence but still needs explanation – we have CIs that have been recognized as non-server classes, some of them have is\_licensable=TRUE, and others have is\_licensable=FALSE. This leads us to believe that the determination of whether a node is licensable is not solely based on class. They fall in the following classes:

o Application – 9 is\_licensable=FALSE, 7 is\_licensable=TRUE  
o Voice System Hardware = 53 is\_licensable=FALSE, 13 is\_licensable=TRUE

### Cause

-   All CI(s) in the table cmdb\_ci which has a global domain appear as a link (see a screenshot below), counted as "Unknown" in license node calculation.  
    ![](/sys_attachment.do?sys_id=8b9b19e997608ad0f69577121153afd8)  
      
    
-   All CI(s) in the table cmdb\_ci which has a global domain appear as a string, counted correctly in license node calculation.

          ![](/sys_attachment.do?sys_id=88ec9dad97608ad0f69577121153af14)

### Resolution

-   update the domain column in the cmdb\_ci table with the string "global" instead of global's domain sys id as shown below.

               ![](/sys_attachment.do?sys_id=3bfc15ed97608ad0f69577121153af62)
