---
title: "Why is Discovery or the MID Server creating Duplicate CMDB CIs after enabling Domain Separation?"
aliases:
  - KB0659176
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0659176
kb_number: KB0659176
last_modified: 2024-04-07
---

## Why is Discovery or the MID Server creating Duplicate CMDB CIs after enabling Domain Separation?

  

### Issue

# Symptoms

* * *

After domain separation is configured on an instance, Discovery creates hardware CIs that appear to be duplicates, with the same name, serial number, and IP Address, etc. However, these CIs are under different domains.

# Release

* * *

Any

# Environment

* * *

MID Server-related CMDB data sources (such as Discovery) and Domain Separation plugin in use.

# Cause

* * *

Discovery runs and creates or updates CIs as the MID Server user, and as the Domain of that MID Server user. If that user cannot see existing CIs then it assumes they don't exist, and will create a new CI in the MID Server user's domain, instead of updating the existing CI in some other domain.

For example, if the MID server user is in the TOP/ABC domain, then the discovered CIs would also belong to domain TOP/ABC. Discovery does not look for CIs in different domains when performing de-duplication and reconciliation, and so an existing CI in domain TOP or TOP/DEF is ignored.

# Resolution

* * *

This is working as designed. If you have domain separation, different MID servers and MID server users should be created for different domains in order to discover CIs for each domain accordingly. A MID server's user, which is the user set in the config.xml file of the MID Server and is used to log into the instance to fetch and return results from jobs, should be configured for a specific domain.

If you enable Domain Separation after having already populated the CMDB from various sources, you are likely to need to manually move those 'global' domain CIs into your new domains, and set up domain-specific MID Servers and discovery schedules, before re-discovering them.

The CIs in different domains are not considered to be 'Duplicate' CIs by the Identification and Reconciliation engine or Health Dashboard jobs, however if they do represent the same hardware then manual data cleanup will be necessary and the configuration that causes CIs to be added inthe wrong domain to be corrected
