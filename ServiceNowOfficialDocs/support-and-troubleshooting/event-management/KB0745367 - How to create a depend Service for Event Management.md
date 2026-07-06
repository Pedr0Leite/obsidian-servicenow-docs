---
title: "How to create a depend Service for Event Management"
aliases:
  - KB0745367
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745367
kb_number: KB0745367
last_modified: 2024-04-07
---

## How to create a depend Service for Event Management

  

### Issue

# Description

We have two Business Service that are independent of each other.  We need to have A (parent)service  B (child)service be associate with each other.  If there is a critical alert on Business Service B we will see Business Service A affected as well. 

# Procedure

1.  Go to the parent business service  
    2\. Go to a Ci within the map that does not have a outgoing connection. It can not be a cluster, but a component within the cluster is ok.  
    3\. Right click and add manual CI.  
    4\. Selection application service, and the business service child that will affect this parent service.  
    5\. Go into the event management dashboard and select the parent business service.  
    6\. You will not see the child service where it was added to the map  
    7\. click on the child and select the impact that child will have on the parent.

  

\---Adjust impact rules for a CI

[https://docs.servicenow.com/csh?topicname=t\_EMConfigureImpactRule.html&version=latest](https://docs.servicenow.com/csh?topicname=t_EMConfigureImpactRule.html&version=latest)

\--Alert impact calculation

[https://docs.servicenow.com/csh?topicname=c\_EMImpactCalculation.html&version=latest](https://docs.servicenow.com/csh?topicname=c_EMImpactCalculation.html&version=latest)

#
