---
title: "When discovery/Identification engine creates new CI or updates existing one"
aliases:
  - KB0727271
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727271
kb_number: KB0727271
last_modified: 2024-04-07
---

## When discovery/Identification engine creates new CI or updates existing one

  

### Issue

# Overview

* * *

How discovery identification engine works while identifying for existing Cis and takes a decision on whether to create new CI or updates the existing one.

# Discovery identification matching process

* * *

Discovery tries to find if an existing entry in found in the CMDB by looking at identification rules. We will take an example of Hardware Rule:

https://<instance\_name>.service-now.com/nav\_to.do?uri=cmdb\_identifier.do?sys\_id=a1d19344c3b33100d8d4bea192d3aedc

![](sys_attachment.do?sys_id=3f8ef862db0ab450e515c223059619bc)

The matching process occurs from top to bottom, lowest priority first.

Rule 1 is the topmost rule with serial\_number and serial\_number\_type. 

The search will be on the cmdb\_serial\_number table.

There are two possibilities in this scenario:

Case 1: The discovery payload contains serial\_number and serial\_number\_type

            In this case, the Identification engine searches the table cmdb\_serial\_number for the match and again it will have two more possible outcomes:

           Match found: It will ignore the other rules with priorities 200, 300 and 400 in this example and updates the respective CI.

               Identifier: Hardware Rule, Rule 1 Searched on <cmdb\_serial\_number> for attributes: serial\_number,serial\_number\_type:Match.

           Match not found: It will continue with next higher order rules and continues until a match is found.

               Identifier: Hardware Rule, Rule 1 Searched on <cmdb\_serial\_number> for attributes: serial\_number,serial\_number\_type:No Match.

Case 2: Discovery payload doesn't contain either serial\_number or serial\_number\_type fields. 

           In this case, it will show up a message in discovery logs stating, "Skipped Identifier entry" and continues to next rule.

Identifier: Hardware Rule, Rule 1 Searched on <cmdb\_serial\_number> for attributes: serial\_number,serial\_number\_type:Skipped Identifier Entry.

This process continues until the match is found on the tables defined in Identifier rules. If there is no match found after running all the rules, then it will create a new CI.

# Additional Information

* * *

This youtube video provides complete information regarding the discovery identification process:

[CMDB Identification and Reconciliation Framework](https://www.youtube.com/watch?v=_e1tDlcDKrk&feature=youtu.be "CMDB Identification and Reconciliation Framework")
