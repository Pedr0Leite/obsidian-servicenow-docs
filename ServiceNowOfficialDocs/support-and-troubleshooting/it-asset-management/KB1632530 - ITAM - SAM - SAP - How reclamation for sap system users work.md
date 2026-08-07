---
title: "ITAM - SAM - SAP - How reclamation for sap system users work"
aliases:
  - KB1632530
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1632530
kb_number: KB1632530
last_modified: 2024-02-14
---

## ITAM - SAM - SAP - How reclamation for sap system users work

  

### Summary

SAP Reclamation candidate generation flow - 

1) Create all reclamation rules for all the required named user type in the table (samp\_sw\_reclamation\_rule). "Applies to" should be selected as "SAP Named User", and provide "minimum t-code required" for the selected named user type. 

2) Assign all transaction codes to each reclamation rule - open the reclamation rule form view and click on the "edit" in the tab "SAP Transaction Codes". 

3) Run "SAM - SAP Transaction Optimization" job to generate latest reclamation candidates for all SAP system users.

\-----

Note:

i) before executing step #2 delete all existing SAP reclamation candidates in the table 'samp\_sw\_reclamation\_candidate' where Publisher = SAP

ii) Above job considered only those SAP system user (samp\_sap\_system\_user) whose named user type's reclamation rule is defined. 

For example:   
1) A User has created 3 reclamation rules for named user types - SAP Application Professional, SAP Application Limited professional, SAP Application ESS User with "Minimum transaction codes required" value as 2, and "aggregate usage by" = Last Month.

2) All SAP system users of these 3 named user types would get processed one by one in the transaction optimization flow (i.e. reclamation candidate generation flow).

Let's assume a user "Abel Tuter" who is "SAP Application Professional" named user type (from table "samp\_sap\_system\_user" whose is a 'dialog' type)

    i) If samp\_sap\_user\_active\_transactions have all active t-codes for "Abel tuter" in last month are more or equal 2. (Also, those 2 or more t-codes must be present in the nut vs t-codes mapping table "samp\_named\_user\_type\_has\_transactions"). No optimization required for this user. 

   ii) Otherwise, if minimum required t-codes are less than 2 then as we see there are 2 more reclamation rule defined whose nut type is cheaper than application professional, so will first check for most cheapest nut first which is ESS in this case.

   iii) let's say "Able tuter" has t-codes present in the mapping table equal or more than 2 for ESS. Then reclamation candidate (samp\_sw\_reclamation\_candidate) would be created with main "Optimized named user type" as ESS.

   iv) Further flow checks all other possible optimized nut also. If Limited professional also get qualified like ESS did in step (iii) then on the generated reclamation candidate it would show up in the "Other matching named user types".

   v) further end user can claim or reject any reclamation candidate after reviewing it. 

How Ranking or pricing between nut works?

\- Ranking of named user type between Professional, Limited Professional, and ESS done through "Rank" as mentioned in the "samp\_named\_user\_type". Higher the rank of a nut, cheaper is the cost of it. 

Here in above example Professional is most costly(rank=412,000), Limited Professional is cheaper than it(rank=413,000), and most cheaper is ESS (rank=415,000). 

If entitlement (alm\_license) are defined then pricing (avg price= total cost/purchased rights) between these 3 nut type would be considered from it i.e as per the license cost bought by customer. Otherwise, by default through named user type table as explained above.   
  
\----  
This entire flow is defined in the script include "SAPTransactionOptimization"

### Release

Release or environment - 

Supported for Tokyo, Utah, Vancouver, Washington and later releases.  

### Related Links

1) [https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/task/t\_AddAReclamationRule.html](https://docs.servicenow.com/bundle/vancouver-it-asset-management/page/product/software-asset-management2/task/t_AddAReclamationRule.html)  
  
2) Master KB - ITAM - SAM - SAP [KB0813999](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813999)
