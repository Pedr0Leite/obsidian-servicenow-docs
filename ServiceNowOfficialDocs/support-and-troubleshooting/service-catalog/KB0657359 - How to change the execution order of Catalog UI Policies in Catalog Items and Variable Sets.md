---
title: "How to change the execution order of Catalog UI Policies in Catalog Items and Variable Sets"
aliases:
  - KB0657359
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657359
kb_number: KB0657359
last_modified: 2024-04-07
---

## How to change the execution order of Catalog UI Policies in Catalog Items and Variable Sets

  

### Issue

How to change the execution order of Catalog UI Policies in Catalog Items and Variable Sets

  
  

# Overview

* * *

This article helps to understand the order of execution of Catalog UI Policies, and the usage of the system property **glide.sc.ui\_policy.variable\_set\_run\_first**. These aspects are important when designing Catalog Items.

  

  

Catalog UI Policies can be found in a Catalog Item, or in a Variable Set. As described in the documentation below, out of the box, Catalog UI Policies on Variable Sets will run first, followed by Catalog UI Policies on Catalog Items.

  

Ref.:

[https://docs.servicenow.com/csh?topicname=r\_ServiceCatalogProperties.html&version=latest](https://docs.servicenow.com/csh?topicname=r_ServiceCatalogProperties.html&version=latest)

[https://docs.servicenow.com/csh?topicname=c\_ServiceCatalogUIPolicy.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ServiceCatalogUIPolicy.html&version=latest)

  

A Variable Set contains common variables that will be used in many Catalog Items. Within in a Variable Set, you might want to make a variable mandatory. In order to do this, you will need to create a Catalog UI Policy within the Variable Set.

  

However, for a particular Catalog Item, you might not want that variable to be mandatory or hidden. To avoid this, create a Catalog UI Policy on the Catalog Item. UI Policies for catalog items always take precedence over UI Policies for variable sets. Catalog UI Policies will run last, meaning the variable will not be mandatory.

  

The mentioned property **glide.sc.ui\_policy.variable\_set\_run\_first** will reverse the order.

  

The default value for this property is **true**.  Variable Set UI Policies run first, Catalog Item UI Policies run last.

  

If you notice that your UI Policies are running in an odd or unexpected order, check the value of this property an ensure that it is set to true.

  

Setting this property to **false** is not recommended. Always design your Catalog UI Policies across Catalog Items and Variable Sets around the documented run order: Variable Sets first, Catalog Items last.
