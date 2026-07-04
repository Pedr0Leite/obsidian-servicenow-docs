---
title: "Troubleshooting the Table Cleaner Scheduled Job"
aliases:
  - KB0551417
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551417
kb_number: KB0551417
last_modified: 2026-04-30
---

## Issue

-   Table Cleaner is running excessively long
-   Table Cleaner is intermittently cleaning a certain table
-   Table Cleaner is causing replication lag
-   System degradation during Table Cleaner operation

# How Table Cleaner Works

Table Cleaner is an internal feature to manage the cleanup of very large tables. The feature is mainly configured through a module of the same name that is not visible to customers or partners. Do not configure the related table without the assistance of ServiceNow.

Table Cleaner is essentially a scheduled job that runs every hour and deletes all records older than a specified date. For example, there is an out-of-box table cleaner configuration record that deletes all cmdb\_tcp tables that have not been updated in the last 24 hours that have been marked absent = true.

Due to the high-risk nature of creating a new Table Cleaner, it should only be done with the assistance of ServiceNow development or if there is a documented, reviewed, and approved workaround.

## Table Cleaning Modes

### **Iterative**

If a table has the "iterativeDelete" attribute on its dictionary record then it must be deleted in an _iterative_ fashion. If a table is determined to require iterative deletes, the Table Cleaner job will run in iterative mode. Iterative table cleaner mode uses a GlideRecord.query() loop to go through each matching record in a table and delete them one by one.

N.B. Iterative delete mode is normally used for a larger variety of tables but for the purposes of Table Cleaning, the only thing that goes through iterative delete are tables that have the attribute explicitly set.

### **Bulk**

The normal mode for Table Cleaner is _bulk operation_ mode. In this mode, Table Cleaner deletes multiple records with a single database operation. The two types of bulk operation modes are:

-   Chunk - As of Helsinki, this optimized method of deleting records first queries for all the sys\_ids of records that match the Table Cleaner condition and then uses that list as the query criteria for a bulk delete statement. This method avoids costly gap-lock that can cause database contention during Table Cleaning. (See PRB650197.) To enable chunk processing you must activate the property _**glide.db.tablecleaner.chunk\_delete\_sysid**_. In Helsinki this table cleaning method will only be used for testing but should become the default method of table cleaning in the Istanbul release. This is also better for reducing replication impact since fewer statements are issued.
    
-   Nibble - As of Geneva, this was the method used for all out-of-box Table Cleaners and is described in more detail below.
    

## How the Table Cleaner "Nibbles"

Table Cleaner has a functionality called "nibble" that breaks the records to be deleted into small groups so it can "nibble" instead of trying to delete them all at once. This functionality enables the process to delete in a series of nibbles to prevent long-running deletes that could potentially lead to performance issues.

This functionality works as follows (the capitalized words refer to actual variables in the TableCleaner code):

1.  Calculate a DELTA in Milliseconds between the value of the sys\_updated\_on field for the YOUNGEST record and the ELDEST record to be deleted.
    
2.  Get the COUNT of records older than the youngest record to be deleted. For example:
    
    SELECT COUNT(\*) FROM cmdb\_tcp WHERE absent = 1 AND sys\_updated\_on < \[24 hours ago\]
    
3.  Divide the COUNT by desired size of nibbles (controlled by the property, glide.db.nibble.size, 250 by default) to find the NUMBER OF NIBBLES required
    
4.  Divide the DELTA by the NUMBER OF NIBBLES to find out how many Milliseconds should hypothetically contain the desired number of records. This value becomes the NIBBLESIZE.
    
5.  Start a loop that increments the ELDEST variable by the NIBBLESIZE each time.
    
6.  Delete everything older than the value of ELDEST.
    
7.  Sleep for the amount of time it took to do step 6 multiplied by a _sleep factor_ (determined either by the attribute "nibbleSleep" on the dictionary record of the table or the default sleep value set by "glide.db.nibble.sleep" or 1, if the property does not exist)  
      
    
8.  Do another loop unless ELDEST is younger than YOUNGEST.  
    The desired result of this design is DELETE statements that look like the following example, assuming a NIBBLESIZE of 5:31 minutes:  
    DELETE \* FROM X WHERE sys\_created\_on < "2015-02-34 02:15:27"  
    DELETE \* FROM X WHERE sys\_created\_on < "2015-02-34 02:20:38"  
    DELETE \* FROM X WHERE sys\_created\_on < "2015-02-34 02:25:59"  
    ... 

The localhost logs will contain output like the following examples:

-   Every time a chunk delete begins for a new table:  
      
    TableCleaner deleting by key: <column name>  
    
-   Every time an iterative delete completes cleaning a table:  
      
    TableCleaner DELETED approximately <number of records deleted in that nibble> old records from <table> via **iterative deletes**  
    
-   Every time a nibble completes:
    
    TableCleaner DELETED approximately <number of records deleted in that nibble> old records from <table> via **nibble  
    **
    
-   Every time a chunk completes:  
      
    TableCleaner DELETED approximately <number of records deleted in that nibble> old records from <table> via **chunk**
-   Every time either nibble or chunk completes cleaning a table:
    
    TableCleaner DELETED approximately <number of records deleted in total for a table> old records from <table> via **bulk operations**
    

## Solutions

### **Performance Degradation during Table Cleaner**

The table cleaning operation attempts to avoid any database locking by cleaning in small chunks. However, even a small chunk of records can take a very long time to delete if the WHERE clause is inefficient.

1.  The steps for troubleshooting this are the same as the steps below for #2.

### **Replication Impact** 

Sometimes the high volume of delete operations creates enough write traffic that the secondary databases cannot keep up with replication. If this occurs, you can throttle Table cleaner using the following properties or attributes:

Nibble and Chunk sleep controls how long TableCleaner will wait between each delete statement (be they nibble or chunk). Each delete is timed. This value is then multiplied by a number determined by the following property and attribute. The resulting multiplication result is how long the TableCleaner will wait between delete statements.

-   glide.db.nibble.sleep - property to control global multiplication factor for nibble sleep. Default is 1. (e.g. for every second spent doing a delete, spend 1 second sleeping)
-   nibble\_sleep - attribute on the "collection" type sys\_dictionary record for the desired table to control table level multiplication factor for nibble sleep to override the global default.
-   glide.db.tablecleaner.chunk\_delete\_sleep - property to control global multiplication factor for chunk sleep. Chunk sleep has a hard coded x/2 denominator. Default is 0 - meaning that there are no sleeps between chunk deletes by default. (e.g. if you set this value to 1, then for every second spent doing a chunk delete, spend 1/2 seconds sleeping.)
-   chunk\_delete\_sleep - attribute on the "collection" type sys\_dictionary record for the desired table to control table level multiplication factor for chunk sleep to override the global default.

### **Table Cleaner is Running Longer than Expected**

Generally, the table cleaner should be completed in a few seconds to 1 or 2 minutes. If you suspect the table cleaner is running too long, check the following:

1.  In the localhost logs check the TableCleaner DELETED messages.  
    1.  What table is running the longest? There will usually be one very clear front runner.
    2.  Are the nibble sizes around 250 to 1,000? If not, check to see if the user is experiencing [PRB646685](/nav_to.do?uri=problem.do?sys_id=135a60970f568a001c7e938172050e53) (see below)
    3.  Is the table being cleaned with _iterative_ mode? Iterative mode is the least efficient mode. Find out if the table can be cleaned without iterative mode.
2.  Review the Transaction Logs table.  
    1.  Is the SQL Time taking over 50% of the total job execution time? If so, the cause may be related to the database.  
        1.  Review the localhost logs or MySQL process list logs to see if any long-running queries were being executed by Table Cleaner.
        2.  Is there a single DELETE query that is running long and a large number of INSERT/UPDATE queries that seem to be blocked? This problem is caused by a behavior known as "gap-lock" that is required to freeze any record in the "gap" between points on an index. This issue can be avoided by basing DELETE operations on the sys\_id column - using "chunk" deletes in Helsinki ([PRB650197](/problem.do?sysparm_query=number=PRB650197 "PRB650197")).
        3.  Table Cleaner should always have a supporting indexed column to build the WHERE clause of its query. The operations that Table Cleaner executes should only be a few milliseconds each. Make sure that the query and the database have been optimized. There is a known case of such missing indexes for the Discovery tables documented in [PRB616428](/nav_to.do?uri=problem.do?sys_id=35aecdae6f6c7180a2c1f7307f3ee457 "PRB616428").
        4.  Table Cleaner will run a table locking optimize operation if 50% or more of the rows in a table have been deleted. The only exception to this rule is if the table has the "no\_optimize" attribute on the System Dictionary record. The only syslog\_transaction has this attribute out-of-the-box. Keep this in mind if you are implementing a new Table Cleaner. One particularly tricky way this can hurt you is if you are cleaning a small table that is a part of a very large table hierarchy. For example, suppose you have only 10,000 cmdb\_ci\_cloud\_template records, but your total cmdb hierarchy has 20 million records. If you clean 5,000 or more of your cmdb\_ci\_cloud\_template records, the platform will consider that more than 50% of the table being cleaned and will initiate a costly table optimize on the entire 20 million record cmdb table hierarchy since it is technically all a single table on the database!
    2.  If the time is not being taken up in SQL, the only other likely option is some kind of defect with the platform scheduled job mechanism. This category of problem is beyond the scope of this article.
