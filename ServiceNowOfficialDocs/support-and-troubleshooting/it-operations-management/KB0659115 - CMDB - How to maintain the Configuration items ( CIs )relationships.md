---
title: "CMDB - How to maintain the Configuration items ( CIs )relationships"
aliases:
  - KB0659115
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0659115
kb_number: KB0659115
last_modified: 2025-04-07
---

## CMDB - How to maintain the Configuration items ( CIs )relationships

  

### Issue

The CMDB, in contrast to a static asset list, helps you track not only the configuration items (CIs) within your system but also the relationships between those items.

A relationship in the CMDB consists of two CIs and a relationship type:

-   Parent CI
-   Child CI
-   Type of the relationship that links both CIs

For example, in the \[Server1\] \[Managed by\] \[Server2\] relationship:

-   Server1 is the child CI
-   Server2 is the parent CI
-   \[Managed by\] is the relationship type

For example, a web application might read data from a particular instance of Oracle, which in turn might depend on a piece of the underlying hardware. Most CIs in a CMDB have multiple relationships to other CIs, users, and groups.

We can view the list of CIs having the relationship using the link - / cmdb\_rel\_ci\_list.do

The relationships between CIs can be automatically discovered. If you use Discovery, many relationships can be automatically loaded into the system through the discovery process. If you import your data from another system, you may need to build relationships.

You can add to automatically discovered relationships, create new relationships, or edit relationships for a CI by launching the CI relationship editor from the CI form.

Working with New CI Formatter to add CI relationships \[manually\]

[https://docs.servicenow.com/search?q=CI+relations+formatter](https://docs.servicenow.com/search?q=CI+relations+formatter)

Monitor CIs relationship health

[https://docs.servicenow.com/search?q=CI+relationship+health](https://docs.servicenow.com/search?q=CI+relationship+health) 

CMDB Health measures CI relationship health using separate KPI and metrics.

**Orphan relationship**: A relationship that is missing a parent or missing a child.

**Duplicate relationship**: A relationships that have an identical parent, child and relationship type.

**Stale relationship**: A relationship in which one of the CIs is stale. For a stale CI – its associated relationships are also stale.

The CMDB Health Dashboard - Relationship Compliance Processor dashboard job must run to generate data for these reports. If this job is not active, please activate and run the job periodically.

Please do contact Technical Support for any assistance on this at International Toll-Free Phone Number (UIFN): **+1 800-400-50900**
