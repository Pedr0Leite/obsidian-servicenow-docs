---
title: "Including Demo Data in a Scoped Application"
aliases:
  - KB0689588
tags:
  - servicenow
  - support-kb
  - scoped-apps
  - demo-data
  - application-files
  - sys_metadata_link
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0689588
kb_number: KB0689588
last_modified: 2025-09-16
---

## Including Demo Data in a Scoped Application

  

### Issue

This article will walk you through how to include demo-data in a Scoped Application.

### Creating non-metadata application files

Demo data, or non-metadata application files, are files that are included in a scoped application to provide some demonstration of the functionality of the application. Records on regular metadata tables (tables that extend sys\_metadata) will always be included in the application automatically, and you do not need to move them. In fact, you will not even have the option to do so because the **Create Application File** UI action is not available on metadata tables.

Once a non-metadata file has been moved into the application, it will appear on the Application Files related list on the sys\_app record as a **Metadata Snapshot** class, and will be published with your application. A record is also generated on the sys\_metadata\_link table, which is responsible for linking that record to the correct package folder.

### Application file creation options

The **Create Application File** UI action provides three options: New Install and Upgrades, New Install, and New Install with Demo Data. Each of these options corresponds to a specific folder in the application package. Ultimately, these options correspond to specific values in the **Directory** column on the associated sys\_metadata\_link record. The options and their respective directory values are as follows:

-   New Install and Upgrades: update
-   New Install: unload
-   New Install with Demo Data: unload.demo

If you want to change an option later for demo data that has already been created, open the associated sys\_metadata\_link record and modify the **Directory** field according to the standard mappings.

### For more information

See the [Create application files to include sample data](https://docs.servicenow.com/csh?topicname=t_IncludeApplicationData.html&version=latest) product documentation topic.

## Related

- [[KB0695169 - Changes to a scoped application are not being applied when the update is installed]] — related scoped application packaging/update behavior
- [[KB0813696 - When attempting to create an updateset in a scoped Application, it is getting created in the 'global' instead of the sco]] — another scoped application configuration pitfall
- [[t_IncludeApplicationData]] — official docs on including demo data in scoped applications
