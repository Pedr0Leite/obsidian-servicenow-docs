---
title: "User domain does not match the workflow domain"
aliases:
  - KB0538170
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538170
kb_number: KB0538170
last_modified: 2024-09-20
---

## User domain does not match the workflow domain

  

### Issue

User domain does not match the workflow domain | Identifying domains of interoperating entities

# Symptoms

* * *

Symptoms may include the following:

-   Workflow did not run when expected
-   Workflow did not run on a specific record
-   Cannot publish workflow
-   Publishing workflow takes too long
-   Cannot modify checked out workflow
-   Cannot start workflow
-   Workflow does not trigger
-   Stalled workflow 

# Domains and Workflows (Pre-Eureka)

* * *

The inserted record takes on the domain of the logged-in user. This insertion may invoke a workflow that resides in the global domain. The workflow creates a context that is initially associated with the logged-in user's domain. The workflow may also create other artifact records in the following ways:

-   **Initiating User's Domain:** Approvals or tasks may be created along the workflow path until a waiting activity is encountered. These initial records give the domain of the logged-in user who inserted the record.
-   **Restarting User's Domain:** When a waiting workflow is restarted by an approval or rejection, or by a closed or canceled task, it will resume as the user that performed the approval or task-related action on the record. All artifacts that are created by the workflow after the restart, and before the next waiting state, are created with the domain of the restarting user.

# Domains, users, and groups (pre-Eureka)

* * *

Users can be associated with domains in several ways:

-   **Company Domain:** The most common way to bind a user to a domain is to create a Company record in the desired domain, and then associate the user with that company.
-   **Group:** A user may be a member of a group. This group can be associated with a company. When the user is considered for an approval or task process through their group, the interaction will interpret the user in the domain to be associated with the company of the group.  
-   **Managed Domain:** The user or group can have its **Managed Domain** flag set to **true**. If this field is selected, then the user or group must also have a domain associated directly to them. The domain overrides any other company domain for the user or group.

# Avoiding issues with workflows (pre-Eureka)

* * *

If domain separation is used strictly to separate companies within a Managed Service Provider (MSP) instance, then it is possible to avoid issues that result from different domains of various users interacting within a workflow during its lifetime. The following steps ensure that all entites share the same company:

1.  Create a domain for each tenant. A tenant is a company that is a client of the MSP.
2.  Create a Company record for the domain of the tenant, and assign it the company domain.
3.  Create all users for the tenant company _inside_ the Company record and do _not_ select the **Managed Domain** option.
4.  Create all groups for the tenant company _inside_ the Company record and do _not_ select the **Managed Domain** option.

Because workflows reside in the global domain for these scenarios, they need to include groups and users in approval activites for multiple companies. Managing workflows is the responsiblity of a domain-trained adminstrator.

# Workflows in domains – the right way (Eureka and beyond)

* * *

As of the Eureka release, support for workflows in domain-separated environments is available. Common workflows can be authored at top-level domains and then placed into child domains. The workflows can then be customized for different companies or divisions.

The following diagram depicts the flow of data (workflow contexts) and processes (workflow versions) within a domain tree:

 ![](/oceanic-tree.pngx)
