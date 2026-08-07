---
title: "Setting up Performance Analytics on a Domain Separated instance"
aliases:
  - KB0547236
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547236
kb_number: KB0547236
last_modified: 2023-09-13
---

## Setting up Performance Analytics on a Domain Separated instance

  

### Issue

The PA Scores tables \[pa\_scores\], \[pa\_scores\_l1\], \[pa\_scores\_l2\] are domain separated tables. It has a domain field, and scores collected on a domain-separated instance will have a domain associated with the score. The mechanism which determines the domain of a score is either: the domain of the "run as" user, or a domain configuration.

The Domain Support plugin \[com.snc.pa.domain\_support\], which provides access to the Domain Configuration, enables the collection of scores across multiple domains using a single Data Collection Job. The use of a domain configuration record will add additional query parameters to Indicator and Breakdown Sources so that records from multiple domains are returned. In turn, the results set is aggregated per domain and a score for each domain is recorded.

### Data vs process tables

Regardless of whether a domain configuration is used or not, the domain context of where the Data Collection Job is running will always be determined by the "run as" user. This is unlikely to be an issue when collecting scores on a data table for example: \[incident\]. Common practice is to use an administrator user from the global domain for use as the "run as" user for Data Collection Jobs. Due to domain rules on data tables, this user (and the data collector running under it) will have full visibility of all incident records. However when scores are being collected on a process table (a table with a sys\_overrides field) e.g. contract\_sla using a "run as" user from the global domain restrict visibility of records on the \[contract\_sla\] table for example to the global domain. This visibility also flows down through database views, where a join is made to the \[contract\_sla\] table e.g. \[incident\_sla\].

It is common practice for MSPs to define these types of process records: business rules, SLAs client scripts, on a process domain, not in the global domain. If this is the case, a "run as" user with appropriate visibility into these process domains is required to be set on Jobs containing sources on process tables.

### MSP best practice

Please see the attached best practice doc for more information and an overview and a best practice approach for setting up Performance Analytics on a Domain Separated instance.
