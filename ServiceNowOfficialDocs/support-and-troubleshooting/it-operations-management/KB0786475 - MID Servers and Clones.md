---
title: "MID Servers and Clones"
aliases:
  - KB0786475
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786475
kb_number: KB0786475
last_modified: 2025-08-26
---

## MID Servers and Clones

  

### Summary

This KB article has some general info on how MID Servers are affected by Instance Clones, and some of the things you need to keep in mind.

## Table of Contents

-   [Are MID Servers Cloned?](#mcetoc_1ftkuc52i14)
-   [The MID Server's login credential](#mcetoc_1ftkuc52i15)
    -   [Issue record: User x with mid\_server role not associated with a MID Server. No login attempts within reporting period.](#mcetoc_1hcv738mjk)
-   [The MID Server's Mutual Authentication Certificate](#mcetoc_1ftkuc52i16)
-   [The Instance Credentials table](#mcetoc_1ftkuc52i17)
    -   [Cloud Service Account records](#mcetoc_1hjmqfe882)
-   [The MID Server's own records](#mcetoc_1ftkuc52i18)
    -   [MID Server Clusters](#mcetoc_1iosk5k69b)
-   [Extension Contexts](#mcetoc_1gnmrupi09) 
-   [Encryption Keys](#mcetoc_1httmo3cr2b)
-   [Records and settings that reference MID Servers](#mcetoc_1ftkuc52i19)
    -   [Default Orchestration MID Server](#mcetoc_1h11tdaju3)
-   [Attachments](#mcetoc_1ftkuc52i1a)
-   [Clones that change the Version of the instance](#mcetoc_1ftkuc52i1b)
    -   [MID Servers trying to Downgrade](#mcetoc_1gnmrupi0a)
    -   [Code mismatches due to preserving files](#mcetoc_1gnmrupi0b)
-   [Agent Client Connector](#mcetoc_1ftkuc52i1c)
-   [Discover and Service Mapping Patterns](#mcetoc_1ftkuc52i1d)
    -   [Uploaded File attachments missing](#mcetoc_1gq9473fv6)
    -   [Patterns are completely missing](#mcetoc_1gq9473fv7)
-   [Health Log Analytics](#mcetoc_1ftkuc52i1e)
-   [Full Clones](#mcetoc_1ftkuc52i1f)

## Are MID Servers Cloned?

No. When a production instance is cloned over a sub-production instance, the production instance's MID Servers are not duplicated or copied, and the sub-production instance will not end up with the same MID Servers as production.

MID Server installations will always point to the same single instance url set in the config.xml file of that installation, regardless of whether that instance is now actually a copy of another instance.

You will need at least one MID Server installation for each instance. You can install multiple MID Servers on the same host server to accomplish this, so long as they have different MID Server names.

In order to be able to effectively test MID Server features in sub-production instances, it is recommended to mirror the production MID Server configurations and install the MID Servers within the same network environments.

## The MID Server's login credential

After a clone has overwritten a target instance with a new configuration, data and even a different version, existing MID Servers for that target instance will still be trying to connect to it using the same username and password that was originally configured for the MID Server.

The user table in the instance will now be a copy of the source instance's user table, and so the MID Server may be trying to log in with a user that now doesn't exist in the instance or may have a different password. That behavior is controlled by the "Preserve users and related tables" checkbox in the options when requesting a clone.

To avoid this possibility, the recommendation is to use the same username and password for MID Servers on all instances. Different MID Servers for different functions can have different passwords, but the MID Servers for a particular function (e.g. Discovery of a particular region/datacenter) would use the same username/password.

For more information, see: [Active MID Server post-](https://docs.servicenow.com/csh?topicname=mid-post-clone-issue-resolution.html&version=latest "Active MID Server post-cloning credential issues")[cloning credential issues](https://docs.servicenow.com/csh?topicname=mid-post-clone-issue-resolution.html&version=latest "Active MID Server post-cloning credential issues")

**Known issue:**

The Clone History log in the source instance, and the comments in the Change Request record in the ServiceNow Support portal, may show this text which indicates a problem that means we will probably not have preserved the MID Server login user:

Preserve sys\_user related table feature is turned off due to PRB1391196. If you need to preserve the users and related tables,  
you can follow the following KB article: [https://hi.service-now.com/kb\_view.do?sysparm\_article=KB0817569](https://hi.service-now.com/kb_view.do?sysparm_article=KB0817569)

This will probably cause the MID Server to be Down after the clone, and this error along the top of the MID Server form. The User mentioned may not actually exist:

Error MessageLogged in user 'XXX' is missing the following roles: mid\_server. Add the missing roles to this user. More Info 

To resolve this, create a new user, with the missing user's user\_id, and set the password the same as had been used when the MDI Servers were installed. Don' t forget to also add the mid\_server role.

### Issue record: User x with mid\_server role not associated with a MID Server. No login attempts within reporting period.

If mid server role users from the source instance get copied in the clone, you may end up with issues records for "User x with mid\_server role not associated with a MID Server". Those may also end up as events and alerts in the Event Management Self-Health Monitoring feature.

Deleting any users with mid\_server role, that are not used in the target instance, can be deleted to avoid those alerts.

## The MID Server's Mutual Authentication Certificate

For Quebec and later instances, the MID Server can optionally authenticate with the instance using [Mutual Authentication (mTLS)](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/product/mid-server/concept/mid-unified-keystore.html#install-mid-mutual-auth "Mutual Authentication (mTLS)") instead of a username+password. The certificate imported into the MID Server install needs to match the certificate imported to the instance table "User Client Certificates" \[sys\_user\_certificate\] for the MID Server to authenticate with the instance.

Those records and their attachments need to be preserved and excluded in clones if different users and certificates are being used between the clone source and target.

## The Instance Credentials table

Prior to the New York release, clones would replace the Credentials table \[discovery\_credentials\] with the records from the source of the clone. Since New York, this table is both Excluded and Preserved in the clone, so that the sub-production instance keeps the Credential records it used to have before the clone.

This table is used by Discovery/Service Mapping probes from the MID Server, but also some other recent integrations features that may not even use the MID Server.

It is possible to configure this behavior yourself, if you do not want to use the default settings. For more information, see:  
[Exclude a table from cloning](https://docs.servicenow.com/csh?topicname=t_ExcludeATableFromCloning.html&version=latest "Exclude a table from cloning")  
[Data preservation on cloning target instances](https://docs.servicenow.com/csh?topicname=data-preservation.html&version=latest "Data preservation on cloning target instances")

Note: These excludes/preservers, including the out-of-the-box ones, only take effect if the "Exclude tables specified in Exclusion List" and "Exclude audit and log data" options are checked when requesting the clone.

There is a problem with Data Preserver and Exclude code in the clone engine, where it doesn't automatically preserve all child tables of extended tables. This breaks the OOTB Exclude setting in New York for discovery\_credentials, and also custom settings, leaving corrupt credential records on the target. For more information and a workaround, see:  
[KB0717208/PRB1305469 Excluding table-per-class (TPC) extended tables from a clone can cause orphaned Discovery Credentials with the 'Record not found' error when trying to open them](https://hi.service-now.com/kb_view.do?sysparm_article=KB0717208 "KB0717208/PRB1305469 Excluding table-per-class (TPC) extended tables from a clone can cause orphaned Discovery Credentials with the 'Record not found' error when trying to open them")  
That was fixed, then broken again by PRB1403259. A more recent problem PRB1391898 causes the same corruption, related to the preservers rather than excludes.  
This should be fixed now.

If the source and target instance have different plugins installed, then you can also get corrupt credential records. For example:

-   You install Cloud Management on the sub-prod instance, which adds extended tables to the Discovery Credentials tables specific to Cloud functionality. e.g. sn\_cmp\_ssh\_credentials. 
-   You create a sn\_cmp\_ssh\_credentials credential. Being an extended table, that means you have the same sys\_id in both discovery\_credentials and sn\_cmp\_ssh\_credentials tables.
-   You clone from production, which does not have Cloud Management installed, and so the sub-prod instance instance will now not have the Cloud Management plugin any more, or it's tables.
-   The default excludes/preservers mean the discovery\_credentials table on the dev instance is preserved. The record with sys\_class\_name=sn\_cmp\_ssh\_credentials still exists in the dev instance, but the sn\_cmp\_ssh\_credentials table does not any more, meaning the corrupt record can't be opened, edited, deleted, and may also break MID Servers trying to load credentials. 

To avoid breaking those records, you will need to install the same plugin(s) on production before the clone, or delete those credential records before the clone. If you have broken records because of this cause, installing the plugin after won't help, because you will still be missing the sys\_id from the child table, and the record will remain corrupt. It will probably need deleting using a Table Cleanup \[sys\_auto\_flush\] job, as that deletes at a lower level that lists and forms. That method is describes in:  
[KB0723549 How to repair Discovery Credentials not accessible after clone](https://hi.service-now.com/kb_view.do?sysparm_article=KB0723549 "KB0723549 How to repair Discovery Credentials not accessible after clone")

As of the end of 2021, most TPC extended table related clone engine problems are solve, except this one:  
[PRB1542851 A clone can corrupt the discovery\_credentials table on the target instance, leaving orphan/ghost records with a class that no longer exists, preventing MID Server using all credentials](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000116 "PRB1542851 A clone can corrupt the discovery_credentials table on the target instance, leaving orphan/ghost records with a class that no longer exists, preventing MID Server using all credentials")

### Cloud Service Account records

These are similar to Credential records, in that they save the credential for Discovery, but are CI records in the CMDB.

There is unfortunately always at least one known problem open at any given time, related to TPP and clones, that basically makes it unlikely that preserving and/or excluding an individual child class such as cmdb\_ci\_cloud\_service\_account will work. You are likely to end up with corrupt records remaining that cannot be seen, or opened, or updated, or deleted.

Broken records are left behind, usually where the sys\_id is in cmdb, but the parts of the record in cmd$par1 or cmdb$par2 are missing.

The sys\_class\_path value may not match after a clone, because the records are kept, but the records defining the class path symbols will be copied from the sour instance in the sys\_db\_object records.

The account\_id is also a unique field, which means it has a unique constraint at the SQL level. If corrupt records exist, they won't be seen in most cases. While they still exist in the table, they will prevent a good record being inserted again for the same account id.

**Solution**:  
Don't even try to exclude and preserve Cloud Service Account records in Clones. A re-clone, without excluding and preserving any CI classes, will repair the CMDB table.

## The MID Server's own records

A MID Server installation can only be used by one instance. Production MID Servers will remain pointing to production, and so any records for those MID Servers don't need to be copied, and so are excluded from the clone. MID Servers for the sub-production instance will still be pointing to that, so records for those MID Servers need preserving.

This includes related records such as Properties, Parameters, Clusters, Capabilities, IP Ranges, Applications, Issues and records for the MID Server Dashboard.

Warning: Prior to Madrid, there was a known problem which means this isn't done properly. Upgraded instances may also not get the fixed exclude/preserve lists, and may need fixing manually. The fix for this problem is available as part of the Madrid Release.

MID Server Properties is a difficult table, because some are for all MID Servers, but others are for specific MID Servers. A clone will delete and overwrite those records. Any specific MID Server with non-default MID Server Properties may need manually re-configuring after a clone (which is PRB1388744).

**There are some ecc\_agent... tables which should never be excluded in clones**, because they contain Code, which is also version specific. Excluding these can cause missing or mismatched code after a clone, and the MID Server won't work as expected.

-   ecc\_agent\_jar
-   ecc\_agent\_mib
-   ecc\_agent\_script
-   **ecc\_agent\_script\_file**
-   **ecc\_agent\_script\_include**
-   ecc\_agent\_script\_param
-   sa\_pattern
-   and others..

These are mostly tables that extend ecc\_agent\_sync\_file, and is code that is synched to the MID Server to then be available to probes running in the mid server. Those being missing after a clone would cause various probes from practically any MID Server related feature or integration to fail due to missing dependencies.

Note: These excludes/preservers, including the out-of-the-box ones, only take effect if the "Exclude tables specified in Exclusion List" and "Exclude audit and log data" options are checked when requesting the clone.

### MID Server Clusters

MID Server Clusters are specific to the MID Servers in them, which are specific to the instance, so these are preserved and excluded. But feature settings that may specify a MID Server Cluster, such as Discovery Schedules or IntegrationHub connections, are copied over in the clone, so would end up with broken references to the cluster.

However there is a useful trick you can do to avoid broken references from jobs such as Discovery Schedules after clones. This will allow jobs copied from the clone source to still be able to run without needing any reconfigurarion:

-   Create the MID Server Cluster record in production/clone source.
-   Export it as XML, then import it to the sub-production/clone target instances.
-   Then in each sub-production/clone target instance, link that instances relevant MID Servers to that Cluster.

## Extension Contexts 

ecc\_agent\_ext\_context is a TPC extended table, just like discovery\_credentials, and has the same problems with orphan/ghost records.

Known problems - Check the Known Error articles for fix targets and repair/workaround info:

-   [PRB1628241 / KB1212634 Clone Excludes/Preservers are missing for SNMP Trap and vCenter Event based Discovery MID Server extension contexts (ecc\_agent\_ext\_context\_trap / ecc\_agent\_ext\_context\_vcenter)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1212634)
-   [PRB1628236 / KB1212633 Clone Excludes/Preservers are missing for Metric Intelligence MID Server extension contexts (ecc\_agent\_ext\_context\_metric)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1212633)
-   [PRB1628223 / KB1212632 Clone Excludes/Preservers are missing for Event Management MID Server extension contexts (ecc\_agent\_ext\_context\_event / eif\_listener\_context)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1212632)

For more detailed information specific to ACC, see [KB1002549 Agent Client Collector and Clones](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002549)

## Encryption Keys

Key Management Framework tables, with names starting sys\_kmf\_... should all be preserved and excluded, as these are instance specific. Those are for things such as password2 fields in records in the instance. There have been problems in the past, but by now those records ought to be handled properly in clones.

But there is another table specific to the encryption of data while being sent between instance and MID Server, which uses the records in ecc\_encryption\_key. That table was added in Paris, and should be in the out-of-box Clone preservers and excludes since Quebec. If those are missing, MID Server data encryption will be broken.

Since Vancouver, that key is encrypted using AES instead of 3DES, and since Washington DC the out-of-box DES3 record is deleted in the upgrade (PRB1678069). More info on that change can be read in:   
[KB0862631 MID Server and Credentials Encryption/Decryption - Symmetrical Keys AES256 and 3DES questions](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862631)

A missing record, or record with empty key, could cause instance side errors when running code that creates ecc\_queue records with encrypted values, such as the passwords in JDBCProbe payloads. e.g.

AbstractProgressWorker SEVERE \*\*\* ERROR \*\*\* com.glide.db.impex.JDBCProbeLoader  
java.lang.RuntimeException: com.snc.automation\_common.integration.exceptions.EncryptionException: Encryption key must be specified 

Deleting (after backing up), then inserting a new record, can usually resolve this.

## Records and settings that reference MID Servers

In settings of all features that use MID Servers, there are likely to be references to specific MID server Sys IDs. e.g.

-   Discovery Schedules set to use specific MID Servers or MID Server Clusters
-   Import Data Sources set to use specific MID Servers
-   Credential records restricted to specific MID Servers
-   etc.

A lot of those settings will have been copied over with the clone, but the MID Servers won't exist on the target instance, and so many of those features will now not work or do something unexpected and need re-configuring to use the target instance's MID Servers.

**Post-Clone Cleanup Scripts** can be used to fix or prevent a lot of these settings after a clone. e.g.  
[KB0789119 A Post-Clone script to Deactivate and Cancel Discovery Schedules](https://hi.service-now.com/kb_view.do?sysparm_article=KB0789119 "KB0789119 A Post-Clone script to Deactivate and Cancel Discovery Schedules")

It is possible to configure MID Servers to have the same sys\_id as the production MID Servers. If the installations are on the same host server, the names need to be different, but the sys\_ids can be the same. This process and the pros and cons are explained in more detail in:  
[KB0719301 How to manually Clone a MID Server so that you don't have to reconfigure all integrations features to use a different MID Server on the sub-prod instance after an Instance Clone](https://hi.service-now.com/kb_view.do?sysparm_article=KB0719301 "KB0719301 How to manually Clone a MID Server so that you don't have to reconfigure all integrations features to use a different MID Server on the sub-prod instance after an Instance Clone")

Warning: Prior to New York, Discovery Schedules set to specific production MID Servers may unexpectedly run after clones:  
[PRB1311068 / KB0788922 After a Clone, a Discovery Schedule for a Specific MID Server, which does not exist in the target instance and so is now a broken reference, will still run in a random MID Server](https://hi.service-now.com/kb_view.do?sysparm_article=KB0788922 "PRB1311068 / KB0788922 After a Clone, a Discovery Schedule for a Specific MID Server, which does not exist in the target instance and so is now a broken reference, will still run in a random MID Server")

### Default Orchestration MID Server

There are 2 places that set the default MID Server to use for Orchestration, and there are a pair of business rules on those tables that keep the values in sync. "Update orc default MID frm sys\_property" business rule on sys\_properties, and "Update orc default MID frm ecc\_agent\_app" on ecc\_agent\_application.

-   System property record "**mid.server.rba\_default**" \[sys\_properties\]  
    /sys\_properties.do?sys\_id=b7c4086d0a0005957b2ebc930bc717bd
-   MID Server "Orchestration" Application record. \[ecc\_agent\_application\]  
    /ecc\_agent\_application.do?sys\_id=b5f91a57d7002200bdbaee5b5e6103ec

There is no preserver for the specific System property. There is no preserver for the 'Orchestration' ecc\_agent\_application record, but the ecc\_agent\_application\_m2m records assigning the Orchestration application to specific MID Servers are preserved and excluded.

This means the value of the property, and the MID Server referenced from the application record, will be copied across in the clone, and will be invalid mid server names now, because they are clone source, not clone target, MID Servers.

To deal with that, there is also a Post Clone Cleanup script "Clean Non-Existent MIDs From Application", which given that both these records are cloned from the source, are bound to have non-existent mid server names in them, because the mid server in the copied record is of the clone source, not the target.  It only looks at the ecc\_agent\_application record, clears that out, and then the business rule clears out the associated property.

The author of this KB thinks that was the wrong solution, as this keeps causing support cases, and the 2 records should probably be preserved out-of-box in future, and is trying to get that changed. As a workaround, Clone Preservers can be manually added in the source instance to preserve the 2 records. The Post Clone Cleanup script can also be deactivated.

Related problem:

-   2018: PRB1254284 Fix default MID selection - added the post clone cleanup script in London version.
-   2019: PRB1378067 After the clone, the property mid.server.rba\_default is set to blank on the target instance, even though it is preserved on the source instance due to the 'Update orc default MID from ecc\_agent\_app' business rule.  
    Closed in 2019 as 'Working as Expected'. 
-   2023: PRB1673771 A clone preserver is missing for the mid.server.rba\_default system property, and the Orchestration ecc\_agent\_application record (also applies to IntegrationHub)   
    Closed in 2023 as 'This is the intended. behavior so will not fix as a defect' 

## Attachments

Often all record attachments, or just large attachments, are excluded in clones. These are not all data, and can be part of out-of-box code too. These should be copied across in clones, but often are not and the symptoms of this may not be obvious.

-   **Uploaded File** \[sa\_uploaded\_file\]  
    Some discovery patterns run scripts that come from attachments, including EC2 and Oracle Patterns.  
    See: [PRB1507034 Clone excludes attachments related to sa\_uploaded\_file table when "Exclude Attachments" is true, breaking Oracle/EC2 Discovery](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0965739 "PRB1507034 Clone excludes attachments related to sa_uploaded_file table when \"Exclude Attachments\" is true, breaking Oracle/EC2 Discovery")  
    Fixed for new clones since 2021-07-13.  
      
    
-   **Agent Client Collector Plugin** \[sn\_agent\_asset\]  
    Agent Client Collector (ACC) Plugins (Sensu Assets) sync from the instance to MID Server, then from MID Server to all ACC's that need them, extracted to a cache folder, and then executed. If the attachment is missing, any checks using those assets will fail. The ecc\_queue input will have an error something like:  
    'endpoint\_discovery.rb' is not recognized as an internal or external command  
    See: [PRB1550798 Clones that exclude large attachments break Agent Client Collector, by deleting the tar/gz files attached to ACC Plugin records in sn\_agent\_asset](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002379 "PRB1550798 Clones that exclude large attachments break Agent Client Collector, by deleting the tar/gz files attached to ACC Plugin records in sn_agent_asset")

## Clones that change the Version of the instance

### MID Servers trying to Downgrade

After a clone, existing sub-prod MID Servers will suddenly find themselves communicating with a 'different' instance compared to the previous incarnation of that instance. It will still try to connect, and will then try to upgrade/downgrade to match the version the instance is now.

Upgrades should work, and plenty of regression testing is done every release to make sure it does.

However it is possible to have a situation when the instance ends up on an earlier version (e.g. a sub-prod instance is used for an upgrade test, and then cloned over again), and then the MID Server may have problems. A MID Server running a future version compared to the instance isn't going to be able to communicate with the instance properly using API and encryption/validation features that are only present in the future instance version.

A downgrade from a version that uses Signed ZIP files to one that doesn't will require a MID Server restart before the downgrade will work:  
[MID Server fails to upgrade from a Signed ZIP file version to a Non-Signed version, because instanceinfo is cached. e.g. MP10 HF1b to NP8, or NP9 to OP2](https://hi.service-now.com/kb_view.do?sysparm_article=KB0827961 "MID Server fails to upgrade from a Signed ZIP file version to a Non-Signed version, because instanceinfo is cached. e.g. MP10 HF1b to NP8, or NP9 to OP2")

Quebec uses a new [MID Server Unified Keystore](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/product/mid-server/concept/mid-unified-keystore.html "MID Server Unified Keystore"), which is replaced as part of an upgrade to Quebec, but is not put back to the old method when downgrading.

In a Downgrade situation, especially between major versions, you are going to need to be prepared to manually re-install the MID Server. For more details of that repair process see:  
[KB0713557 How to manually Upgrade and/or Restore a MID server after a failed Upgrade](https://hi.service-now.com/kb_view.do?sysparm_article=KB0713557 "KB0713557 How to manually Upgrade and/or Restore a MID server after a failed Upgrade")

A [rekey](https://docs.servicenow.com/bundle/rome-servicenow-platform/page/product/mid-server/task/t_RekeyAMIDServer.html "rekey") may be all that is required, if you see "unable to decrypt" messages in the agent log or issues records. This seems to work after Rome to Quebec downgrades.

### Code mismatches due to preserving files

If an instance on an earlier version, or without all the same plugins installed, is overwritten in a clone from a source instance on a later version, all 'code' files need to be copied over in that clone.

If tables such as Scripted SOAP Service \[sys\_web\_service\] are preserved/excluded in the clone, then only the records from the previous target instance version will remain, if they were there in the first place, and those code version mismatches with the version the instance, or missing records because the plugin was never installed, will likely break things.

-   Don't preserve/exclude code tables that contain out-of-box scripts as well as your custom ones. It is better to export your Update Sets, and Import them again after the clone.
-   If you feel you have to do this, you can usually avoid problems if you upgrade the target instance to the same version as the source instance before the clone, and check you have all the same plugins and apps installed first as well.

For example, Scripted SOAP Service "GetMIDInfo" is used by the MID Server on startup for various data and settings from the instance, and is often changed in upgrades. If the instance app node localhost logs have errors such as this, then you will be using an old version of the record:

2023-01-26 01:44:18 (078) API\_INT-thread-6 63952EBA972CE15044E7FC000153AFE4 txid=30c52636972c \*\*\* Start #104311 /GetMIDInfo.do, user: xxx  
2023-01-26 01:44:18 (086) SOAPProcessorThreadf4c562fa972ce15044e7fc000153afb8 63952EBA972CE15044E7FC000153AFE4 txid=fcc5eefa972c \*\*\* Script: Unsupported request type: xxx

## Agent Client Connector

Each Agent Client Collector installation communicates to a MID Web Server Extension running on a specific MID Server., and therefore specific instance name  The ACC Websocket Endpoint and MID Web Server Contexts need to still be there, with the same ports and credentials setting after a clone, or the Agent Client Collectors will not be able to communicate with the MID Server and instance any more.

By version 2.1.41 (cGTM/202009) these exclude/preserve settings were included (PRB1408738).

Also see Attachments section above for **Agent Client Collector Plugin** \[sn\_agent\_asset\] attachments issues.

## Discover and Service Mapping Patterns

### Uploaded File attachments missing

Discovery Patterns, including Oracle and Amazon EC2, depend on some synched files in the Uploaded File \[sa\_uploaded\_file\] table.

If some attachments (sys\_attachment/sys\_attachment\_doc) are excluded and not preserved, some Discovery Patterns will not longer work. That can be resolved by exporting the sa\_uploaded\_file records from the clone source as XML, which will automatically include the attachments in the export, and import into the clone target to repair the missing attachments. 

For searchability, the attachment filenames and sa\_uploaded\_file sys\_ids are:

getEC2Detailsv3.ps1 fef7f75e1bfcd0107e02fc078b4bcb16  
Oracle\_PDBS.sql ee37ed860f02001003bea6f6bc767e66  
Oracle\_CDB.sql 95c66d860f02001003bea6f6bc767e4a  
options\_packs\_usage\_statistics.sql 06f603f2db0500104d2f9eb5db9619e7  
Oracle\_instance\_size.sql bc515611dbdff34003a05561ca961992

More info on file sync:  
[KB0852276 : How MID Server File Synchronisation works, to help when Troubleshooting](https://support.servicenow.com/kb?id=kb_article_view&sys_kb_id=3d6b0b7cdb5c7854d82ffb2439961954 "How MID Server File Synchronisation works, to help when Troubleshooting")

### Patterns are completely missing

If you get the following Warning in a Discovery log, a clone could be the cause:

Script error in sensor: ReferenceError: "pattern" is not defined.

In the "The MID Server's own records" section above, it was explained that the tables ecc\_agent\_jar/ecc\_agent\_mib/ecc\_agent\_script\_file should never be excluded/preserved because they are code, not data. Another key thing about those tables is that they all extend ecc\_agent\_sync\_file, and so does the Patterns table sa\_pattern.

ecc\_agent\_sync\_file and those child tables are part of the sys\_metadata Table-Per-Class extended table, that is a massive tree structure of tables, that encompasses most code tables in the instance. There is a class field on all of these records, which defines which application level table the record is in, and at the SQL level that record's sys\_id will be in sys\_metadata, plus all intermediate and child tables, adding fields at each level, when joined together make up the application level record you see on a form.

Due to how the Clone Engine handles Table-Per-Class extended tables, if you do not exclude/preserve all the child tables as well, then you can end up with partial/corrupt/ghost/orphan records that are missing sys\_ids in some of SQL tables.

If for example a customer excludes and preserves ecc\_agent\_script\_file and ecc\_agent\_sync\_file, then ecc\_agent\_script\_file records will be correctly excluded and preserved. However other classes of files in child tables will only be partially preserved/excluded.

Green is what you intended to exclude/preserve, and what you added to the clone settings.  
Yellow is what accidently also got excluded/preserved as well due to including ecc\_agent\_sync\_file in the exclude/preserve clone settings.  
Red is what will now be missing.

sys\_metadata -> ecc\_agent\_sync\_file -> ecc\_agent\_script\_file   
sys\_metadata -> ecc\_agent\_sync\_file -> ecc\_agent\_jar   
sys\_metadata -> ecc\_agent\_sync\_file -> sa\_pattern

If you look at a list of Patterns -  /sa\_pattern\_list.do - you won't see the records. If you look from the top level - /sys\_metadata\_list.do - and add a filter for Class is Discovery Patterns, then you will see the records listed, but when you try to open them, you will get a /sa\_pattern.do form that says "Record Not Found"

Repairing a plugin/app to try and get the records back won't work, because the plugin repair code, which works at an application level, cannot update the records that are corrupt at a SQL level.

Solution:

In this situation you would need to correct the clone settings, by removing ecc\_agent\_sync\_file and any tables that extend it from your clone excludes and preservers on the source instance, and then clone again.

It may be possible to to delete the ghost records and then repair the various Plugins/Apps that have pattern records in them, but this is tricky and time consuming, and would require a support case to be able to do things have changes made at a SQL level.

## Health Log Analytics

MID Server Extensions for the streaming of logs via the MID Server to the Occultus instance will be affected by Clones, and the following KB is the main source of information on this:  
[KB0867530 System Clone - Health Log Analytics | HLA Quebec](https://hi.service-now.com/kb_view.do?sysparm_article=KB0867530 "KB0867530 System Clone - Health Log Analytics | HLA Quebec")

## Full Clones

All the settings related to **Clone Exclude and Preserve settings are ignored** if the "Exclude tables specified in Exclusion List" and "Exclude audit and log data" options are un-checked when requesting the clone. We call doing that a Full Clone, and you can expect to have to set up all MID Server related things again after the clone.

A problem ticket does exist for this behaviour, even though from the point of view of the full clone this is 'working as expected', because MID Servers will still be broken. Support Cases caused by this should still be linked to it even though no change in behaviour is currently planned:  
[PRB1251951 / KB0677995 Clone fails to exclude tables like ecc\_agent when unchecking the boxes "Exclude audit and log data" and "Exclude large attachment data"](https://hi.service-now.com/kb_view.do?sysparm_article=KB0677995 "PRB1251951 / KB0677995 Clone fails to exclude tables like ecc_agent when unchecking the boxes \"Exclude audit and log data\" and \"Exclude large attachment data\"")
