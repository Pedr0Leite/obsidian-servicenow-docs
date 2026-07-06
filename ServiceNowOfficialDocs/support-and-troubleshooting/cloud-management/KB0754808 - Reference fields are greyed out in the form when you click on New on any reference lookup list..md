---
title: "Reference fields are greyed out in the form when you click on \"New\" on any reference lookup list."
aliases:
  - KB0754808
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754808
kb_number: KB0754808
last_modified: 2024-04-07
---

## Reference fields are greyed out in the form when you click on "New" on any reference lookup list.

  

### Issue

# Overview

Reference fields are greyed out in the form when you click on "New" on any reference lookup list.

# Versions

All

# Example

The system will not allow you to create an infinite loop of records.   
  
Please find the below example:   
  
1) Open any incident.   
2) Click on **Related records** section.   
3) Click on reference search Icon on **Problem**.   
4) Click on New   
4) On the new problem, record observe that the reference icon is read-only.   
  
**Observe that all the reference fields in the problem are greyed out.** 

# Additional Information

Clicking on Reference and New is supported only till one level as this can go on loop.
