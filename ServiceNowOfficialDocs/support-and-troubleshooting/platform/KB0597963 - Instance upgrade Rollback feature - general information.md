---
title: "Instance upgrade Rollback feature - general information "
aliases:
  - KB0597963
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597963
kb_number: KB0597963
last_modified: 2024-04-07
---

## Issue

## Why a new rollback feature?

Key drivers for introducing this feature are:

-   ServiceNow upgrades are live
-   Our patching and forced upgrade programs require customers to stay on latest patch versions
-   If something goes wrong during upgrade, we need a fast and safe alternative to remediate and proceed forward

  

#### What is rollback?

-   Rollback bundled in **com.glide.rollback** plugin that is activated by default on Helsinki upgrade
-   Visible only to maint users
-   Runs on any in-family upgrade:  
    -   Customers will reach out to ServiceNow to report issues following an upgrade
    -   ServiceNow executes the rollback directly in the customer instance
-   Supports plugin activation/upgrade – plugins must opt-in via supports\_rollback attribute in plugin.xml
-   Availableto maint users in **Scripts > Background** 

  

#### How does it work?

-   Runs during database upgrade, including Fix Scripts!
-   Listens for changes on upgrade thread  
    -   DML: Inserts / Updates / Deletes
-   RollbackDBListener  
    -   DDL: Schema Changes
-   RollbackDDLChangeListener
-   Records nearly everything the upgrade thread does, ignoring explicitly excluded tables (for example, syslog, sys\_email, rollback metadata tables)
-   Deny listed operations  
    -   schema Drops (tables or columns), although Index drops are ok
    -   Re-parenting / Column promotion
    -   Table Truncate
    -   Table/Column Rename
    -   Column Type changes
    -   Column width decrease

  

## Troubleshooting considerations

#### Why did the upgrade not record for rollback?

-   Upgrade recording level property (**glide.rollback.upgrade\_recording\_level**):  
    -   family: \[DEFAULT\] Only record in-family upgrades
    -   all: Record every upgrade no matter what
    -   none: Do not record any upgrade
-   In-family upgrade compares glide.war to glide.war.assigned at start of upgrade
-   Check log file at start of upgrade\_complete for details around “in-family” decision:  
    -   Upgrading within family (glide), recording changes for rollback
    -   Unable to parse one or both file names, not recording upgrade for rollback
    -   NOT upgrading within family ('%s' vs. '%s'), not recording changes for rollback
    -   Will be followed by from=\[<glide.war>\], to=\[<glide.war.assigned>\]

#### Why is my recorded rollback incomplete?

-   Check for exception during rollback
-   Property **glide.rollback.recording.on\_exception** determines how system responds:  
    -   DEFAULT: continue\_without\_rollback – Rollback will stop recording, mark rollback invalid, but continue upgrade
    -   abort: Upgrade is aborted - this setting is really only used in testing/validating patch builds as a way to fail fast
    -   continue: Rollback continues, basically ignoring the error, and upgrade continues

#### Why wasn't <change> recorded?

-   Check table exclusion list in RollbackRecorderUtils.java
-   Check localhost logs around time of change
