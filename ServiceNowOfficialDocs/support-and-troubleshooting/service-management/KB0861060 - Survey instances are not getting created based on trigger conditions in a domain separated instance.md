---
title: "Survey instances are not getting created based on trigger conditions in a domain separated instance"
aliases:
  - KB0861060
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861060
kb_number: KB0861060
last_modified: 2026-06-24
---

## Survey instances are not getting created based on trigger conditions in a domain separated instance

  

### Issue

Assessment survey instances are not getting created for every request and incident based on trigger conditions.

STEPS TO REPRODUCE/OBSERVE BEHAVIOR:  
Open an Incident  
Resolve an Incident by setting state to resolved and filling other mandatory fields.  
Save

### Release

All

### Cause

  
MOST PROBABLE CAUSE:  
We identified that the User who was the caller and who we were trying to trigger the survey for is in a different domain to that of the Survey Record  
  
When impersonating and changing to the affected users domain we had no access to the Survey, we get record not found.  
  
  

### Resolution

  
To resolve this issue you will need to change the domain of your Survey to global so that the Survey can be triggered for ALL Users regardless of their domains.  
  
Otherwise you need to explicitly configure domain based Surveys that represent your Users domains.  
  
  
  

### Related Links

Please reference the below documentation for Survey domain configuration  
  
https://docs.servicenow.com/csh?topicname=domain-separation-surveys.html&version=latest
