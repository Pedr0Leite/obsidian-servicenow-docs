---
title: " Removal Candidates were created without a CI and software install details when Bulk reclamation is true."
aliases:
  - KB2294789
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2294789
kb_number: KB2294789
last_modified: 2025-07-13
---

## Removal Candidates were created without a CI and software install details when Bulk reclamation is true.

  

### Summary

When Bulk reclamation is marked as TRUE, removal candidates/reclamation candidates were created without a CI and software install details  
Bulk Reclamation means the ability to have multiple installations associated with a single reclamation candidate.

1.  Why were Removal Candidates created without a CI?

-   Bulk Reclamation involves more than one Removal of Software Installation. It can be on the same CI or a different CI.
-   As it is not possible to choose a single CI from the list of Software installs, Bulk reclamation does not add any Configuration items on removal candidates/reclamation candidates  
      
    2\. Why were Removal Candidates created without a Software Installation?
-   The Software Installation field is left blank in these removal candidates/reclamation candidates because these removal candidates/reclamation candidates were created as Bulk reclamation as TRUE.
-   Because of having multiple installations associated with a single reclamation candidate, it is not possible to install multiple details in the same field, so installations were populated separately under the related list of the removal candidates/reclamation candidates.
