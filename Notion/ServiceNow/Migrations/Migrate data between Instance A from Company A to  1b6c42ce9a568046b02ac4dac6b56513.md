---
aliases:
  - "Migrate data between Instance A from Company A to"
tags:
  - migrations
  - update-sets
  - data-export
  - scoped-applications
  - instance-data-replication
---

# Migrate data between Instance A from Company A to Instance B of Company B

# 

### **Instructions**

The scope of customer support for these activities will be minimal and only related to functionality. This is an implementation request, and we have limited scope from the Technical Support break-fix objective for these requests. The best option is to work with your account representatives to involve ServiceNow Professional services in these implementation requests.

### **OOB Option**

We have an existing module by which this can be initiated very quickly, as well as the documentation.

[Instance Data Replication](https://docs.servicenow.com/csh?topicname=instance-data-replication.html&version=latest)

**Restore Option**

**Restore Instance A from Company A to Instance B of Company B**

Customers can request a company's backup to be copied over an instance of another company. For this, we need two cases: one for the Source company, where the Primary customer contact provides the approval to use their backup ( Data and configurations), and another for the Target company, where their Primary customer contact will give the backup to be restored over ( Data and configurations).We will be doing this internally from the backend. Any cross-data references and security aspects, including sensitive data, are to be considered. We do not have a way to exclude this information during the restore process as this is an automated Backup restore. We will only proceed after getting approvals from both parties on their respective cases.

**Plugins and Store applications if it is restored from Company A to Company B**If the Source company purchased plugins/products, these will be restored to the target company in "ACTIVE" status. Please work with your account reps on the licensing questions. Once installed, plugins cannot be uninstalled and will remain active as plugins are configuration files that will be copied over with this Restore.

[Uninstall a ServiceNow plugin](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716414)

[Plugins Visibility / Activation / Licensing](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759221)

**Manual Migration**

**Migration of configuration**

Configurations can be transferred from one instance to another in Update-sets.

**Migration of Custom Scoped app**

Apps in installed status will be transferred over as "Installed". If you were using APPREPO to publish and install the custom app, it would only be possible if the instances were moved to a different company. The scope of these apps is uniquely identified as "x_appcreatorcode-**, and this appcreatorcode is unique to the company unless the instance is linked to the owner of appcreatorcode organisation, the publish option will not be available, and published app updates will not be available for installation, and appcreatorcode is different.

You can refer to more information in the section    "[How to move Custom Scoped Applications between instances](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961293)"

**Migration of data**Data can be downloaded as XML/Excel/CSV and transferred to the target instance using Import functionalities.These are not easy and very complex. The reference data, sys_attachment, sys_audit, and other related data should also be transferred. These will have interdependencies and should be tried and tested on SUBPROD instances before applying them to PROD. Failing to transfer this will result in orphan data, which should be fixed by finding and exporting other dependent data.Export restrictions(count of records and size) can be applied, and the data should be exported in smaller chunks.More details on  [Exporting data](https://docs.servicenow.com/csh?topicname=c_ExportData.html&version=latest)

It would be best to consider the Fields of a table in both instances. Store apps/Custom apps and Plugins are configurations, and this can add columns/fields to the table from which you are trying to migrate the data. If the target instance doesn't have these fields, the data will not be imported. So, please make sure the Plugins/Apps/Custom Applications are the same on both instances and have a plan outlined to fix the missing configuration/Fields between both instances.

## Related

- [[Migrations]]
- [[Update Set Mover]]
- [[Update sets - Full Applications]]