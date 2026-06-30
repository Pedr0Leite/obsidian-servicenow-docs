---
title: Create a configuration to publish TRM data
description: Define configuration for a Technology Reference Model \(TRM\) catalog that can be published to the knowledge base article.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/config-trm-data-to-publish.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Working with the publishing center, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Create a configuration to publish TRM data

Define configuration for a Technology Reference Model \(TRM\) catalog that can be published to the knowledge base article.

## Before you begin

Role required: sn\_apm.apm\_admin and knowledge\_admin

## About this task

Publishing a TRM catalog involves creating a publishing configuration in the Publishing Center and executing it to generate knowledge base content.

**Note:** If you can’t republish the catalog due to permissions, contact a knowledge administrator to republish and apply the changes.

## Procedure

1.  Navigate to **Workspace** &gt; **[[ea-workspace|Enterprise Architecture Workspace]]**.

2.  Open the Setup page by selecting the Setup icon \[Omitted image "setup-icon.png"\] Alt text: Setup icon.

3.  Select the expand row icon \(\[Omitted image "ExpandIcon.png"\] Alt text: Expand Row icon\) next to **Publishing Center**.

4.  Select **All**.

5.  Select **New**.

6.  On the form, fill in the fields.

    For field information, see [[create-pub-config-form|Create publishing configuration form]].

7.  Select **Save**.

    The details are saved and the configuration is available in the Publishing Center list.

    After a publishing configuration is created, the **Catalog type** and **Access type** fields become read‑only.


## Result

When you create a new TRM publishing configuration, the system automatically creates default publishing components. The following related records are created automatically:

-   **Article configurations**- For TRM, this tab displays the Software and Hardware product links along with display fields to appear on the knowledge base. By default, system displays the article configuration and content configuration for the product to be published. You can open the links to modify the article configuration and life cycle configuration. For more details, see [[modify-trm-cat-pub-config|Edit a published TRM catalog configuration]].
-   **Portals**- displays associated portals, where the knowledge base is published. You can associate a new knowledge base to the service portal. For more details, see Associate a portal to the knowledge base.

    **Note:** You can see this tab only when you have the Service Portal admin \(sp\_admin\) role assigned to you.

-   **Run logs**- displays the publishing status. You can also open the run log link and article configuration links to see all details for the published catalog. For more details, see [[view-run-log|View publishing status and run log]].

**Parent Topic:**[[working-with-publishing-center|Working with the publishing center]]

**Related topics**  


[Edit a published TRM catalog configuration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/modify-trm-cat-pub-config.md)

[[associate-portal-to-trm-cat|Associate a portal with a knowledge base]]

[[publish-trm-cat-to-kb|Publish a TRM catalog to the knowledge base]]

[View publishing status and run log](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/view-run-log.md)

[[access-the-published-kb|Access the published TRM catalog knowledge base]]

[[understand-publishing-output|Understanding the publishing results and knowledge base output]]

## Related

- [[create-pub-config-form|Create publishing configuration form]]
- [[modify-trm-cat-pub-config|Edit a published TRM catalog configuration]]
- [[view-run-log|View publishing status and run log]]
- [[working-with-publishing-center|Working with the publishing center]]
- [[associate-portal-to-trm-cat|Associate a portal with a knowledge base]]
- [[publish-trm-cat-to-kb|Publish a TRM catalog to the knowledge base]]
- [[access-the-published-kb|Access the published TRM catalog knowledge base]]
- [[understand-publishing-output|Understanding the publishing results and knowledge base output]]
- [[ea-workspace|Enterprise Architecture Workspace]]
