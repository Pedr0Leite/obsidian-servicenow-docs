---
title: "Understanding User Criteria and ACLs in Knowledge v3"
aliases:
  - KB0550924
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550924
kb_number: KB0550924
last_modified: 2026-06-03
---

## Understanding User Criteria and ACLs in Knowledge v3

  

### Issue

For more information on this topic, see [Control access at the knowledge base level through user criteria](http://docs.servicenow.com/?context=CSHelp:UserCriteria-KB&version=latest).

For more information on this topic, see [Managing access to knowledge bases and knowledge articles](http://docs.servicenow.com/?context=CSHelp:user-access-knowledge&version=latest).

With the Fuji release, knowledge functionality is upgraded to Knowledge v3. Prior to Knowledge v3, ACLs and roles were used to determine who can view and create knowledge content. With Knowledge v3, this functionality was replaced with User Criteria.

User criteria allow knowledge managers to implement and modify security without a system administrator's involvement, as well as define separate security configurations for different knowledge bases.

Refer to the ServiceNow product documentation for more information about these topics.

-   [Knowledge v3](https://docs.servicenow.com/csh?topicname=c_KMv3Migration.html&version=latest "Knowledge v3")
-   [User Criteria](https://docs.servicenow.com/csh?topicname=t_SelectUCArticle.html&version=latest "User Criteria")

### Release

Fuji and newer - Knowledge v3

### Resolution

### Video Tutorial

This video demonstrates how to create user criteria records and apply them to control user access to knowledge bases.

### Basic Principles

Several basic principles apply to all instances when configuring user criteria in knowledge.

-   A knowledge manager can specify which users **Can read** and **Can contribute** to a knowledge base by creating and selecting user criteria.
-   A user must have at least one role to contribute. This requirement is independent of any user criteria selected for a knowledge base.
-   If no user criteria is selected for a knowledge base, all users can read and all users with roles can contribute to that knowledge base.
-   Selecting a single user criteria record in the **Can read** and **Can contribute** related lists restricts the audience and contributors of that knowledge base to those users.
-   Users included in the **Can contribute** user criteria can also read articles. You do not need to explicitly grant these users read-access.
-   Knowledge search results include articles from all knowledge bases the current user has access to. If user criteria prevents a user from viewing an article, that article does not appear in search results for that user.
-   User criteria records are shared between Knowledge and the Service Catalog.

### ACLs in Knowledge v3

Knowledge v3 is intended to be used with user criteria alone. For best results, do not use ACLs to control access in Knowledge v3. Though ACLs control access in lists and forms, only user criteria is respected when you browse or search knowledge; ACLs are not. If you use ACLs to restrict content in Knowledge v3, these ACLs apply only when a user opens an article.

### Recommendations for Adopting Knowledge v3

Follow these recommendations when configuring Knowledge v3:

-   Remove custom ACLs from the kb\_knowledge table and replace them with user criteria. Mixing ACLs and user criteria may result in unexpected behavior.
-   Do not restrict access to knowledge bases for the purpose of targeting search results. Instead, create categories within the knowledge base to allow users to filter content when browsing or searching knowledge.

### Example Use Cases

Several use cases are available describing pre-Fuji knowledge configurations that use ACLs, and how to migrate these configurations to Knowledge v3 using user criteria.

####  Example 1 

_"ACME North America has a knowledge base with articles visible to users based on the department that they work in. If the user is part of the HR department, there are articles that only they can see. Everyone can read IT department articles but only the IT department and Knowledge department can write them. Additionally there are articles that all users can read. "_

 You can implement this configuration in Knowledge v3:

1.  Create these knowledge bases:  
    -   Company Knowledge Base
    -   HR Knowledge Base
    -   IT Knowledge Base
2.  Create a user criteria record with the following values.  
    -   **Name:** ACME North America
    -   **Company:** ACME North America.
3.  Create a second user criteria record with the following values.  
    -   **Name** ACME North America Knowledge Department
    -   **Company:** ACME North America
    -   **Department:** Knowledge Department
    -   **Match All**: Selected
4.  Create a third user criteria record with the following values.  
    -   **Name:** ACME North America IT Department
    -   **Company**: ACME North America
    -   **Department:** IT Department
    -   **Match All:** Selected
5.  Configure the user criteria for the knowledge bases using the table below.

| **Knowledge base** | **Can read** | **Can contribute** |
| --- | --- | --- |
| Company Knowledge Base | ACME North America | ACME North America Knowledge Department |
| HR Knowledge Base | ACME North America HR Department | ACME North America HR Department |
| IT Knowledge Base | ACME North America | ACME North America IT Department and ACME North America Knowledge Department |

Using this configuration the Company Knowledge Base articles are visible to all users, the HR Knowledge Base is completely private to the HR department, and the IT Knowledge Base is available to all users but maintained only by the IT and Knowledge departments.

#### Example 2

"_ACME Europe has a knowledge base where some articles are visible only to internal users. On each knowledge article record, Knowledge department members can control if the article is for internal or external users. ACME Europe users can see all articles. Only the Knowledge department can create articles._"

You can implement this configuration in Knowledge v3:

1.  Create these knowledge bases:  
    -   Internal Knowledge Articles
    -   External Knowledge Articles
2.  Create these user groups:  
    -   Internal Users
    -   External Users
3.  Specify if each user is internal or external by adding that user to the appropriate group.
4.  Create a user criteria record with these values:  
    -   **Name**: ACME Europe
    -   **Company**: ACME Europe
5.  Create a second user criteria record with these values:  
    -   **Name**: ACME Europe Knowledge Department
    -   **Company**: ACME Europe
    -   **Department**: Knowledge Department
    -   **Match All:** Selected
6.  Create a third user criteria record with these values:  
    -   **Name**: Internal users
    -   **Groups**: Internal Users
7.  Create a fourth user criteria record with these values:  
    -   **Name**: External Users
    -   **Groups**: External Users
8.  Configure the user criteria for the knowledge bases using the table below.

| **Knowledge base** | **Can read** | **Can contribute** |
| --- | --- | --- |
| Internal Knowledge Articles | ACME Europe and Internal Users | ACME Europe Knowledge Department |
| External Knowledge Articles | ACME Europe and External Users | ACME Europe Knowledge Department |

Using this configuration the Knowledge department does not need to indicate if each article is internal or external. Access is managed automatically by publishing to the correct knowledge base.
