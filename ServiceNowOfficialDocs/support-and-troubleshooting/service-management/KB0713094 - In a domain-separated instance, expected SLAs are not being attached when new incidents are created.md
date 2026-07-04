---
title: "In a domain-separated instance, expected SLAs are not being attached when new incidents are created"
aliases:
  - KB0713094
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713094
kb_number: KB0713094
last_modified: 2024-04-07
---

## In a domain-separated instance, expected SLAs are not being attached when new incidents are created

  

### Issue

# Symptoms

* * *

-   In a domain-separated instance, when a new incident is created, certain SLAs are expected to attach. These SLAs are not attaching per the user's expectations.

# Release

* * *

Kingston Patch 3, Kingston Patch 6

# Cause

* * *

It was found that the behavior described above resulted from two main causes:

-   FIRST: There was a user who had the "snc\_read\_only" role which was prohibiting them from accessing the tables needed to create the task\_sla record(s).
-   SECOND: Users who were trying to create incidents to trigger the SLAs in Domain "Orange" were not in Domain "Orange" under the domain picker in the header - this is why the task\_sla records were not created.

# Resolution

* * *

-   FIRST: There was a user who had the "snc\_read\_only" role which was prohibiting them from accessing the tables needed to create the task\_sla record(s). 

The reason the affected user was able to create an incident at all with the "snc\_read\_only" role on their sys\_user profile, but is blocked from other tables with "snc\_read\_only" role, is because there is a system property which controls table exemptions related to the "snc\_read\_only" role: _glide.security.snc\_read\_only.tables.exempt\_create_ ( ref: /nav\_to.do?uri=sys\_properties.do?sys\_id=5b5259850f164b84ffd5ad7d51050ef2 ).

The user had the incident table in that exemption list.

-   SECOND: Users who were trying to create incidents to trigger the SLAs in Domain "Orange" were not in Domain "Orange" under the domain picker in the header - this is why the task\_sla records were not created.

1\. With domains and SLAs, there is an extra level of configuration related to SLA Definitions which is a feature called "Delegated administration" ( ref: [https://docs.servicenow.com/csh?topicname=c\_DelegatedAdministration.html&version=latest](https://docs.servicenow.com/csh?topicname=c_DelegatedAdministration.html&version=latest) ). 

This feature allows a record in one domain to override it's equivalent in a higher domain - this is useful for SLA Definitions as, for example, the user can have a default P1 SLA in the "global" domain. Then, where needed, the same P1 SLA in lower domains to override it - allowing the ability to provide different timings/conditions based on the domain of the Task. Once a table has this behavior (the user can find all the tables that support it by looking for a column called "sys\_overrides"), then querying of records works in the opposite direction: 

\- for a table that doesn't have Delegated administration, a user will be able to see all the records in their current domain plus the ones below it (e.g., a user in TOP can see records in TOP, TOP/SubDom1, TOP/Subdom1/Subdom2 etc). 

\- for a table that does have Delegated administration, a query for find all records in the user's current domain plus the ones above it (e.g., a user in TOP can see records in TOP and global only).

2\. When creating a new Task record, the default value for the "sys\_domain" field is global - but a before insert/update business rule updates this field to match the caller/caller's company.

3\. Whenever a record is created or updated through the UI, some specific domain-based code sets the domain used for processing (e.g., business rules) and data (querying of tables) so that the appropriate logic is performed on the record and associated data can be accessed. Typically these will match the domain of the record that has just been created/updated. 

Applying the above to the behavior the user is experiencing:

\- a user in the domain "TOP/Apple" logs in and creates a new Incident for a caller in the domain "TOP/Apple/Orange" 

\- on saving the record, the domain code (which runs before any business rules) checks the domain of the record which is "global" and so then looks at the domain of the current user (in this case "TOP/Apple") and uses this for the data domain 

\- the before business rule now sets the Domain field on the Incident to "TOP/Apple/Orange" 

\- SLA processing now runs and queries for SLA Definitions (this is limited to the data domain - e.g., "TOP/Apple") and as this is a delegated administration table, the records in "TOP/Apple/Orange" are not found and so no Task SLAs are created 

The reason the SLA attaches and the behavior works when the record is updated is because the domain code then finds the "TOP/Apple/Orange" domain in the Incident and so the data domain is set to this before the business rules are processed and the Orange SLA Definitions are now found immediately, without issue. 

Setting the domain picker to the correct domain solves the issue on creation as the domain code will use the session domain which is correct for the record that is about to be created.  
  
To remedy incidents which have been affected by either of these cases, please feel free to use the Repair SLAs functionality ( ref: [https://docs.servicenow.com/csh?topicname=c\_RepairSLAs.html&version=latest](https://docs.servicenow.com/csh?topicname=c_RepairSLAs.html&version=latest) ).
