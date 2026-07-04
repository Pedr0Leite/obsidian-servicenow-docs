---
title: "Adding \"Changes to\" and \"Changes from\" operators to SLA Definition Start/Pause/Stop condition sections"
aliases:
  - KB0790046
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790046
kb_number: KB0790046
last_modified: 2024-04-08
---

## Adding "Changes to" and "Changes from" operators to SLA Definition Start/Pause/Stop condition sections

  

### Issue

The user wanted to know why, on SLA Definitions, they could not select "changes to" or "changes from" operators like they could elsewhere on the Platform (e.g. with notifications).

### Resolution

After a conversation with the Product Owners for Service Level Agreements (SLAs), it was found that the operators "changes to" and "changes from" are purely a configuration driven capability (for condition builders). Looking at the below sys\_dictionary entry for the Reset condition section of a SLA Definition, note the attributes:

-   `extended_operators=VALCHANGES;CHANGESFROM;CHANGESTO`  
      
    reference: /nav\_to.do?uri=sys\_dictionary.do?sys\_id=066c1ceedbc33300cab952c8dc9619db%26sysparm\_view=advanced

Enabling these operators in the other three SLA Definition sections is as simple as adding those attributes per section (Start, Stop, Pause).  
  
The reason these operators were only added to Reset conditions was to keep complexity down. Using the "change from" and "changes to" operators is going to make "crafting" the conditions a little more complicated, unless the Cancel and Resume conditions are also used.  
  
Using the operators on Stop conditions introduces the same complexity issue. If they are utilized, the user would need to ensure that the Start condition no longer matches after the Stop condition has been matched, otherwise they will get new SLAs that they likely are not expecting/do not want.
