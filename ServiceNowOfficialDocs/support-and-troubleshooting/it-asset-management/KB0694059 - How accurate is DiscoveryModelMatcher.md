---
title: "How accurate is DiscoveryModelMatcher ? "
aliases:
  - KB0694059
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694059
kb_number: KB0694059
last_modified: 2024-04-07
---

## Issue

The matching logic between discovery model to software model is based on string and word matching.

  

It finds a list of potential software models that could match the current discovery model and use the one that has most in common with current discovery model as a match.

  

For example, If there is no software model found for "Microsoft Office Proofing", So for discovery model "Microsoft Office Proofing (Spanish) 2010", the best match found is "Microsoft Office 2010"

  

Similar for discovery model "Microsoft Office Proofing Tools 2013 - Español", the best match that can be found is "Microsoft Office 2013 Pro Plus"

  
  

  

## Additional Information

As a better alternative, ServiceNow introduced a normalization functionality within the Software Asset Management Premium plugin in Jakarta which is shipped with out-of-box rules that continually are updated via a remote distribution content service mechanism. Based on this functionality, ServiceNow automatically matches the software models to software installs.   
  
Please review the following documentation about ServiceNow Software Asset Management Premium Normalization:   
[https://docs.servicenow.com/csh?topicname=c\_SAMDiscovery.html&version=latest](https://docs.servicenow.com/csh?topicname=c_SAMDiscovery.html&version=latest)
