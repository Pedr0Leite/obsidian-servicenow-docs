---
title: "Cloning preparations and best practices "
aliases:
  - KB2231636
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2231636
kb_number: KB2231636
last_modified: 2026-01-09
---

## Issue

Cloning preparations and best practices for PRE/POST clone

## Resolution

Best practices, pre-clone activities, post-clone activities, and the importance of configuring data preservation and table exclusions effectively.

Best Practices for ServiceNow Cloning:

1.  Communicate Clearly

-   Notify all stakeholders about the cloning schedule, downtime, and purpose of the activity.

1.  Use Clone Exclusions Thoughtfully

-   Exclude tables and data that are environment-specific or sensitive to avoid overwriting critical configurations.

1.  Leverage Data Preservation Settings

-   Preserve target instance data where necessary to retain unique configurations and records.

1.  Document and Validate

-   Maintain a checklist of excluded tables, preserved data, and post-clone actions. Validate these settings before and after cloning.

1.  Take back up of Update Set from Target instance.

Pre-Clone Activities:

1.  Plan and Communicate

-   Confirm the cloning schedule and inform all relevant teams about the impact on the target instance.
-   Share a detailed timeline and any required actions before cloning.

1.  Exclude Tables

-   Define tables to exclude during cloning to retain environment-specific configurations. Common exclusions include:
-   Integrations: sys\_properties, oauth\_entity, and API credentials.
-   MID Server Configurations: ecc\_agent table.
-   Exclude the Multi SSO tables
-   Logs and Temporary Data: Exclude system logs, demo data, or irrelevant records.
-   Audit Logs, Event Logs, Email Logs, System Logs

1.  Set Data Preservation

-   Identify and configure preserve data rules for tables that must remain unchanged in the target instance
-   Custom configurations or local integrations.
-   Preserve SAML properties
-   Preserve SAML certificates
-   Preserve SAML users
-   Admin and Developer Accounts, user accounts with admin and development roles remain intact for post-clone activities.
-   User Preferences: Preserve user-specific settings and preferences.
-   Preserve email properties and outbound email settings.
-   Preserve instance-specific URLs and integration settings
-   Preserve any custom applications
-   Keep MID server configurations
-   Preserve settings related to external system integrations

1.  Backup Target Instance Data

-   Export critical records, system properties, and configurations/update sets from the target instance that might need restoration.

1.  Test Clone Settings

-   Validate your exclude and preserve data rules to ensure they meet the cloning objectives.

Post-Clone Activities:

1.  Verify Excluded Tables and Preserved Data

-   Check that excluded tables remain untouched and preserved data is intact in the target instance.
-   Unique workflows or local customizations should be unaffected.

1.  Reconfigure Target-Specific Settings

-   Update environment-specific configurations, such as: Integration endpoints and credentials.

1.  Validate Core Functionalities

-   Test critical processes such as login, incident creation, service catalog workflows, and integrations.

1.  Communicate Completion

-   Notify stakeholders that cloning is complete and provide a summary of actions taken.

Below are the few documentations that we went through before cloning:

-   [https://www.servicenow.com/docs/bundle/washingtondc-platform-administration/page/administer/managing...](https://ind01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.servicenow.com%2Fdocs%2Fbundle%2Fwashingtondc-platform-administration%2Fpage%2Fadminister%2Fmanaging-data%2Fconcept%2Fc_SystemClone.html%23%3A~%3Atext%3DCloning%2520is%2520typically%2520used%2520to%2Cin%2520the%2520Clone%2520Admin%2520Console&data=05%7C02%7CShubhamKumar.Dubey%40ltimindtree.com%7C9ebefc764de1462785e208dd3bb39ffb%7Cff355289721e4dd7a663afec62ab9d54%7C0%7C0%7C638732364864526396%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=xDagrs2fTd4SXNfPiV7tTyJ%2FrsoZc1e4GZRoZCCy6YE%3D&reserved=0).
-   [https://www.servicenow.com/docs/bundle/washingtondc-platform-administration/page/administer/managing...](https://ind01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.servicenow.com%2Fdocs%2Fbundle%2Fwashingtondc-platform-administration%2Fpage%2Fadminister%2Fmanaging-data%2Ftask%2Ft_StartAClone.html&data=05%7C02%7CShubhamKumar.Dubey%40ltimindtree.com%7C9ebefc764de1462785e208dd3bb39ffb%7Cff355289721e4dd7a663afec62ab9d54%7C0%7C0%7C638732364864547788%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=ielZzGWz1JAtHMyNcR%2B6ma3FuoFyMFLt45iL2%2BRmvL0%3D&reserved=0)
-   [https://www.servicenow.com/docs/bundle/washingtondc-platform-administration/page/administer/managing...](https://ind01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.servicenow.com%2Fdocs%2Fbundle%2Fwashingtondc-platform-administration%2Fpage%2Fadminister%2Fmanaging-data%2Ftask%2Ft_ExcludeATableFromCloning.html&data=05%7C02%7CShubhamKumar.Dubey%40ltimindtree.com%7C9ebefc764de1462785e208dd3bb39ffb%7Cff355289721e4dd7a663afec62ab9d54%7C0%7C0%7C638732364864561032%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=waQWef45jBokvsGEl7MMM4sIiOo%2B%2B0Fp21M2bWSH60I%3D&reserved=0)
-   [https://www.servicenow.com/docs/bundle/washingtondc-platform-administration/page/administer/managing...](https://ind01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.servicenow.com%2Fdocs%2Fbundle%2Fwashingtondc-platform-administration%2Fpage%2Fadminister%2Fmanaging-data%2Fconcept%2Fdata-preservation.html&data=05%7C02%7CShubhamKumar.Dubey%40ltimindtree.com%7C9ebefc764de1462785e208dd3bb39ffb%7Cff355289721e4dd7a663afec62ab9d54%7C0%7C0%7C638732364864573985%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=eNl7Kg5nuOr5QOB%2BK7tYOkp%2Bx5xvYOekIZ4sQOMFuPE%3D&reserved=0)

Post Cloning checklist:

-   [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0547597](https://ind01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.servicenow.com%2Fkb%3Fid%3Dkb_article_view%26sysparm_article%3DKB0547597&data=05%7C02%7CShubhamKumar.Dubey%40ltimindtree.com%7C9ebefc764de1462785e208dd3bb39ffb%7Cff355289721e4dd7a663afec62ab9d54%7C0%7C0%7C638732364864589890%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=bkE8pgbZRmc%2BL8TcFa%2FWCb9PCigf4hLtTPWPfSeVGLs%3D&reserved=0)
