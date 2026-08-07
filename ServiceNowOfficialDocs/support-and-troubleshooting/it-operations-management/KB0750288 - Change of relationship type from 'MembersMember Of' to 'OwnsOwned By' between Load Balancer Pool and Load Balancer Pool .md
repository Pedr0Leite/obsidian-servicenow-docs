---
title: "Change of relationship type from 'Members::Member Of' to 'Owns::Owned By' between Load Balancer Pool and Load Balancer Pool Member"
aliases:
  - KB0750288
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750288
kb_number: KB0750288
last_modified: 2024-04-07
---

## Change of relationship type from 'Members::Member Of' to 'Owns::Owned By' between Load Balancer Pool and Load Balancer Pool Member

  

### Issue

# Overview

While doing a horizontal discovery a Load Balancer CI, if you are using probes/sensors they create a relationship of type "Members::Member Of" between Load Balancer Pool and Load Balancer Pool Member, while the patterns create a relationship of type "Owns::Owned By"

# Subject

It is a design decision that was made while developing the pattern to change the relationship type to "Owns::Owned By". So there was a containment rule added to the cmdb\_metadata\_containment table since the pattern uses Identification Reconciliation Engine (IRE) to update these relationships. 

If you like to change the relationship type to "Members::Member Of" when using patterns, you would need to make changes in the pattern steps where we are setting this relationship between Load Balancer Pool and Load Balancer Pool Member. 

Also, when using probes, the sensor code does not use IRE to update the relationship. So there is no OOB containment rule for "Members::Member Of" relationship. So changing the pattern step, without adding the containment rule would result in IRE errors. So make sure that a containment rule record is created on cmdb\_metadata\_containment table.

  

### Release

All
