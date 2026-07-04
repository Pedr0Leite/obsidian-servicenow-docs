---
title: "Archiving - FAQ"
aliases:
  - KB0547695
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547695
kb_number: KB0547695
last_modified: 2026-04-30
---

## Issue

Since the **Archiving** functionality has been released, we have seen several customers asking questions on the subject. The aim of this article is to give the customers the possibility of checking if their question has already been answered. Please comment on the article if you have any new questions.

### 1) What is the main benefit for using the archiver tool?

\- The main benefit to archiving is to delete data from a particular table to reduce the size of the table but still retain the deleted data on an archive table in case it needs to be revisited.

\- When archiver reduces the main table size, it will improve the performance when running SQL queries against it.

### 2) Which tables should be better handled by archiver or table cleaner?

It all depends on your business requirements. It is always preferred using table cleaner because not only will the data be deleted to reduce the table size, but it also decreases the risk of causing overall db disk space issues. Archiver deletes the data from the main table, but it will not reduce the db disk space since the data is moved to an archive table.

### 3) When we archive records on a particular table, where is the archived data stored?

\- When archiving a record on a table, it is stored on an archived table that has the same table name as the main table, but with a 'ar\_' prefix.

##### NOTE: TPH (table per hierarchy) tables (like task or cmdb) are un-inherited when archive table is created, where the extended tables turn into actual archive physical tables.

**For example:**

<table style="border-collapse: collapse; width: 42.8168%; height: 59px;" border="1"><tbody><tr style="background-color: #bfedd2;"><td style="width: 50.1739%; text-align: center; border-color: #000000;"><strong>Main Table</strong></td><td style="width: 49.9538%; text-align: center; border-color: #000000;"><strong>Archived Table</strong></td></tr><tr><td style="width: 50.1739%; text-align: center; border-color: #000000;">sn_vul_vulnerable_item</td><td style="width: 49.9538%; text-align: center; border-color: #000000;">ar_sn_vul_vulnerable_item</td></tr><tr><td style="width: 50.1739%; text-align: center; border-color: #000000;">incident</td><td style="width: 49.9538%; text-align: center; border-color: #000000;">ar_incident</td></tr><tr><td style="width: 50.1739%; text-align: center; border-color: #000000;">cmdb_ci_computer</td><td style="width: 49.9538%; text-align: center; border-color: #000000;">ar_cmdb_ci_computer</td></tr></tbody></table>

### 4) How does archiver work in general and whats the behavior?

#### STEP 1: You setup an archive rule by going to https://\[instance\].service-now.com/sys\_archive\_list.do

#### STEP 2: Click new and input the information below (Not all of them are required):

-   **Name:** To give you archive rule a name
-   **Table:** To select the table you want to archive
-   **Active:** If you want to activate the archive rule
-   **Retain References:** If you want to pass the sys\_id of the reference columns instead of the display value
-   **Description:** To add a description of the archive rule
-   **Conditions:** To add the conditions of the data you want to archive
-   **Auto Re-archive:** Its a way to give a time expiration of restored archived records that will be automatically re-archived again when the set 'Auto Re-archive Duration Time' is met.
-   **Archive Related Records Tab:** Is a way to set related records of the table your archiving to also archive the related records along with it

#### STEP 3: When archive rule is setup, a OOTB job called 'Archive' runs every 1 hour and checks all the active archive rules

#### STEP 4: When the Archive Job identifies an archive rule that meets the conditions to start archiving, it will do the following:

-   **It initiates a job called 'Archive Producer - All rules' to identify the sys\_ids of the records to archive and stores it in chunks on a table called 'sys\_archive\_run\_chunk'**
-   **Then a job called 'Archiver - Job Consumer ## Node - \[Appserver name\]' is initiated to process the chunk records from 'sys\_archive\_run\_chunk' table to archive the records and store them on the archive table.**

#### STEP 5: It inserts logs of the archived records on the 'sys\_archive\_log' table

### 5) Whats the Archive Run tab?

It's a tab thats accessing the 'sys\_archive\_run' table that shows a summary in a list view for only the corresponding archive rule of the times the archiver ran, how long it took, how many records it archived and if it completed.

### 6) Whats the sys\_archive\_log table?

\- The sys\_archive\_log table is a table that contains metadata information of every archived records except the archive records that have been deleted.

\- Per archived record it contains columns like:

-   **from\_table:** the source table it came from
-   **to\_table:** the archive table it got stored on
-   **id:** the main sys\_id of the archived record
-   **display\_value:** the subject or short description of the archived record
-   **archive\_run:** The sys\_id of the 'sys\_archive\_run' table
-   **archive:** The sys\_id of the archive rule it came from
-   **restored:** The date the archive record got restored, if the archive record has not been restored, then it will be a blank value.
-   **payload:** The xml version of the whole archived record

### 7) On an Archive Rule, what is the difference between having the 'Retained References' checked or unchecked?

**If Retained References checkbox is checked:** the archived record reference fields will be a clickable value to allow you to take you to the reference field record from the non-archived record. 

**If Retained References checkbox is unchecked:** the archived record reference fields will only be a text display value that makes it un-clickable to allow you to take you to the reference field record from the non-archived record.

### 8) If I have been archiving records with 'Retained References' unchecked and then decide to check the 'Retained References' checkbox, will the older archived records prior to checking the 'Retained References' checkbox have the references clickable?

Yes, when you check the 'Retain References' checkbox on an archive rule and OOTB job called 'Archive Reference Copy' will run to create and run 2 jobs called 'Job Reference Migration  Node - \[Node Name\]' and make the older archived records references clickable by updating them from a text field the sys\_id of the reference field.

### 9) How can we setup to have an archive rule also archive related records?

#### When creating or configuring an archive rule:

#### _To setup 2 layers down of related records:_

#### STEP 1:  Go to the 'Archive Related Records' Tab

#### STEP 2:  Click New ----> It will take you to the '/sys\_archive\_related.do' form

#### STEP 3: Input the following information:

-   **Action:** You can select the below:
    -   Archive: To archive the related record
    -   Clear: To set the related records reference column only to NULL (blank) when parent record is archived
    -   Delete: To delete the whole related records when parent record is archived
-   **Reference:** to find and set the related record relationship (_Format:_ Child Reference Table Column Label Name in Child Reference Table Label Name).
-   **Reference Table:** auto populates the child reference table label name and logical name when selecting the Reference above.
-   **Reference Element:** auto populates the child reference table column physical name when selecting the Reference above.
-   **Reference table rule:** This column does not work so it can be left blank

#### STEP 4: Click Submit

#### _To setup 3 layers down of related records:_

#### STEP 1:  Go to the 'Archive Related Records' Tab

#### STEP 2:  Click New ----> It will take you to the '/sys\_archive\_related.do' form

#### STEP 3: Input the following information:

-   **Action:** You can select the below:
    -   Archive: To archive the related record
    -   Clear: To set the related records reference column only to NULL (blank) when parent record is archived
    -   Delete: To delete the whole related records when parent record is archived
-   **Reference:** to find and set the related record relationship (_Format:_ Child Reference Table Column Label Name in Child Reference Table Label Name).
-   **Reference Table:** auto populates the child reference table label name and logical name when selecting the Reference above.
-   **Reference Element:** auto populates the child reference table column physical name when selecting the Reference above.
-   **Reference table rule:** This column does not work so it can be left blank

#### STEP 4: Click Submit

#### STEP 5: Create new archive rule for the same reference table used for the related records setup on parent archive rule above.

#### STEP 6: Set the parent archive rule on the parent reference qualifier lookup on the new archive rule to make it a child archive rule.

#### STEP 7: Repeat STEP 3 to STEP 4 for the new Child Archive Rule to setup the 3rd layer related records.

#### Example: Check the OOTB Archive Rule Setup below that has it set to 3 layers:

Archive Rule Name: Requests - Inactive and closed over 3 months ago

-   Table: Request \[sc\_request\]
-   Archive Related Record:  
    -   Reference Table: Requested Item \[sc\_req\_item\]

Archive Rule Name: Request Items (Related to parent rule Requests)

-   Table: Requested Item \[sc\_req\_item\]
-   Archive Related Record:  
    -   Reference table: Catalog Task \[sc\_task\]

### 10) How many layers down can we archive related records?

You can go as many layers down as you want, but best practice is to not go over 3 layers down of related records because you will not be able to restore the archived related records that have been archived below 3 layers down by clicking the 'Restore Record with related records' on the parent archived record. If you archived related records below 3 layers down, you will have to restore them individually using the regular 'Restore Record'.

#### **For Example:**

##### **Layer 1: Parent Archive Rule**

                                 ![](/sys_attachment.do?sys_id=4a76da6947d4355011eaf24c736d43fd)

#####                                       **Layer 2: Parent Archive Rule Related Records/Associated Child Archive Rule** 

                                                                                                                               **![](/sys_attachment.do?sys_id=4a76da6947d4355011eaf24c736d43fd)**

#####                                                                                                                                **Layer 3: Related Records of Child Archive Rule**

### 11) Can we restore archive records and how?

Yes, you can restore archived records by going to the archive record thats on the archive table and in the Related Links section in the very bottom you can click either:

-   **Restore Record:** To restore the archived record
-   **Restore Record With Related Records:** To restore the archive record and the archived related records if it has any

### 12) Is it possible to perform bulk archive restores?

Yes, it is possible to perform bulk archive restores, but only through glide scripting. Below is the KB of sample bulk archive restore scripts you can use to accomplish bulk archive restoration:

[KB0680127: How to restore multiple archived records in batch mode](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0680127)

### 13) Is it possible to perform bulk archive restores with related records?

Yes, you can create archive rules to also archive related records by doing the following:

[KB1271880: How to restore multiple archived records with related records in batch mode](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1271880)

### 14) Whats the behavior of the archive restore process?

**STEP 1:** The restored archived record is re-added back to the main table

**STEP 2:** The record on the archive table is not deleted

**STEP 3:** For the corresponding restored archived record, the 'restored' column from the sys\_archive\_log table will be populated with the date and time the archived record got restored.

### 15) Can we re-archive a restored archived record and how?

Yes, there are two ways to do it:

**Option 1:** You can access the restored archived record on the non-archived table in form view and below where it says Related Links you can click the Archive Record link. 

**Option 2:** On the archive rule you can check the 'Auto Rearchive' checkbox and then set an 'Auto Rearchive Duration Time' date and time to have the restored records automatically re-archived again when they have been restored for the amount of time you set on the 'Auto Rearchive Duration Time' date and time

### 16) Can we do a bulk re-archive for restored archived record?

Yes, it is possible to perform bulk re-archive on restored archived records, but only through glide scripting. Below is the KB of sample bulk re-archive on restored archived records script:

[KB0684703: Unable to bulk re-archive restored records](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0684703)

### 17) What happens when you re-archive a restored record in general?

**STEP 1:** The restored record gets deleted from the main non-archived table

**STEP 2:** The re-archived record is not inserted on the archive table because the archived record on the archive table has already been there because when the archived record was first restored, it was never deleted from the archived table in the first place.

**STEP 3:** The existing archive record from the archive table 'archived' column gets updated on the date and time the restored record got re-archived.

**STEP 4:** A new sys\_archive\_log record is inserted for the re-archived record with a blank value on the restored column.

### 18) Can we delete data directly from the sys\_archive\_log table?

No, the sys\_archive\_log records must not be deleted or changed because it is a requirement to have the data on the sys\_archive\_log table if you want to restore or delete archived records.

### 19) How can we delete archived data?

The only way to delete archived data is to use the Archive Destroy Rule.

Documentation Link: [Create a destroy rule](https://docs.servicenow.com/en-US/bundle/utah-platform-administration/page/administer/database-rotation/task/t_CreateADestructionRule.html)

### 20) How does the archive destroy rule work in general and whats the behavior?

#### STEP 1: You setup an archive rule by going to https://\[instance\].service-now.com/sys\_archive\_destroy\_list.do

#### STEP 2: Click new and input the information below (Not all of them are required):

-   **Name:** To give you archive rule a name
-   **Table:** To select the table you want to archive
-   **Active:** If you want to activate the archive rule
-   **Destroy Related Record:** If you want to also delete related records
-   **Archive Duration:** to specify how old the archive record has to be so it can be deleted

#### STEP 3: When archive rule is setup, a OOTB job called 'Archive Destroy' runs every 1 hour and checks all the active archive Destroy rules

#### STEP 4: When the Archive Destroy Job identifies an archive destroy rule that meets the conditions to start deleting it, will do the following:

-   **The 'Archive Destroy' job will spawn a job called 'Destroyer scheduled on node - \[Appserver name\]' that will identify the sys\_ids of the archive records to delete and stores it in chunks on a table called 'sys\_archive\_destroy\_chunk'**
-   **Then a job called 'Destroy Job Consumer ## Node \- \[Appserver name\]' it's running on' is initiated to process the chunk records from 'sys\_archive\_destroy\_chunk' table to delete the archive records.**

#### STEP 5: The corresponding deleted archived records referenced on the 'sys\_archive\_log' table will also be deleted

### 21) How can we archive cmdb related data?

Archiving cmdb data is a different process that should be handled by following this doc site: [CMDB Data Manager](https://docs.servicenow.com/csh?topicname=cmdb-data-management.html&version=latest "CMDB Data Manager")
