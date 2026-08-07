---
title: "Using Active Query Index Hints To Improve Slow Query Execution"
aliases:
  - KB0647687
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647687
kb_number: KB0647687
last_modified: 2026-04-23
---

## Using Active Query Index Hints To Improve Slow Query Execution

  

### Issue

This article is meant to help clarify when and how to add an active query index hint in ServiceNow.

### Release

All releases

### Resolution

# Audience 

* * *

ServiceNow self-hosted customers using the MySQL database, and ServiceNow technical support engineers needing to improve a query when the database optimizer picks a suboptimal execution plan.

WARNING: Customers who are hosted by ServiceNow can refer to this information for general knowledge but will NOT be able to perform many of the steps listed below.  It is highly recommended that you create a case with ServiceNow support if experiencing slow query performance within a hosted environment.

# Topics

* * *

-   Identify Slow Query
-   Confirm slowness on the DB
-   Determine possible index(es)
-   Get the Explain Plan 
-   Compare existing indexes
-   Test for improvement with index hint
-   Configure the Active Query Index Hint form
-   Define the Query Hint
-   Confirm the improvement

#### Identify the slow Query:

##### Background:

Some users complain of slow home pages and have identified a slow query coming from a home page using the Slow Queries Module, as below: 

![Slow Queries Module](sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba103e "Slow Queries Module")

##### TIP:

To make sure you are targetting a query that is impactful and in need of optimization, consider filter options that show Average execution time > 2000ms and Execution count > 500 and an Example Java stack trace starts with Default-thread, meaning it is an interactive user transaction. Ordering the list by Total execution time assures you see the most significant query first.

Open the target query and look at the Last sighting field to ensure the query is still impacting performance and is in need of improvement. Copy the SQL in the Example field and save it in your favorite simple editor of text editor of choice. Make sure not to use MS Word or any other Rich editor.

![SQL in the Example field](sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba104e "SQL in the Example field")

#### Confirm slowness on the DB

Access the MySQL database used for the instance in question and execute the same SQL query (copied from above) to confirm the query is slow:

 ![Execute the same SQL query](/sys_attachment.do?sys_id=a43aedfd93fc2e10e7eef35d6cba1076 "Execute the same SQL query")

#### Determine possible index(es):

Looking at the where clause in the above SQL, a composite index on the following columns in the task table might be good:

assignment\_group  
state  
assigned\_to

This is just a guess right now, but see what indexes, if any, are being used currently. 

#### Get the Explain Plan:

Using the MySQL Explain Plan mechanism, notice how many rows the SQL query must access and what index is being used.

![MySQL Explain Plan](/sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba1046 "MySQL Explain Plan")

Note that while an index is being used (task\_ref2), we are still accessing 2 million rows to bring back 0 rows in our result.  Doing this takes the database 5.5 seconds.

#### Compare existing indexes:

See what columns on the task table the task\_ref2 index is created from.

![task\_ref2 index](/sys_attachment.do?sys_id=a43aedfd93fc2e10e7eef35d6cba1074 "task_ref2 index")

NOTE: Tables in MySQL Version 5.6 are limited to 64 total indexes. In this example, there are already 62 indexes on the task table.  Some indexes are composite (multi-column), and some are single-column, but there is a 64 total index limit we can't exceed.

Already near the maximum number of allowable indexes on the target table, look for a better already existing index. 

Reviewing the existing indexed columns in the task table, there is an existing index that covers all three columns from the where clause we suspected might be better. The currently used index, task\_ref2 on, has ONLY the assigned\_to column and active, as shown above.

We noted earlier that a possible index based on the where clause might be a composite index on the following columns:

assignment\_group  
state  
assigned\_to

There is an existing composite index that provides all three of the columns we think might benefit from indexing.  

![Composite index](/sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba1048 "Composite index")

#### Test for improvement with index hint:

Now that we know a possibly better index already exists, see if it speeds up our query, using a force index query hint.

![Index query hint](/sys_attachment.do?sys_id=ec3a213193306e10e7eef35d6cba1032 "Index query hint")

This same query took 5.5 seconds earlier, using the index the database optimizer thought best. Using this newly found composite index reduces the query time by about 4 seconds for this frequently used query, which is a significant improvement.  This is a case where a query hint would clearly help performance.

NOTE: This query is not ideal given the multiple OR conditions and the IS NULL.  Often it is necessary to review and try several different existing indexes carefully and to review and rewrite the query itself if improvements cannot be found. It might just as well happen that an ignore index query hint would help as much or more than a force hint. Testing is key to finding the right solution.

#### Configure the Active Query Index Hint form (if required):

NOTE: PRB1439443 - Active Query Index Hints do not work on tables with truncated aliases. For example, a physical table named x\_nuvo\_f8s\_work\_order with a logical name x\_nuvo\_facilities\_work\_order would not be able to receive an index hint. As a workaround,d you can just use an Active Query Rewrite.  

Now that we have confirmed an existing index helps the query execute faster, we can create an active query index hint within the ServiceNow instance. Up until now, everything has been to find a way to speed up query execution.  Here we implement the corrective action on the platform. 

In the filter navigator, type Active Query Index Hints and click the New button. If the page looks nearly black, like below, it will have to be configured. If the form has more fields, scroll down to the next section.

NOTE: Self-hosted customers will need to request maint user credentials from ServiceNow to access this active query index hint module.

![Active query index hint module](sys_attachment.do?sys_id=ec3a213193306e10e7eef35d6cba1038 "Active query index hint module")

Do the following to add the required form fields:

1.  Navigate to Configure > Form Layout  
    ![Navigate to Configure > Form Layout](sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba1042 "Navigate to Configure > Form Layout")
2.  Add the following selected fields:  
    
    ![Add selected fields](sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba104c "Add selected fields")
    
3.  Save the changes to the form layout above, and the empty form should look like the following:  
    ![Save the changes](sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba103c "Save the changes")

#### Define the Active Query Index Hint:

From the Slow Queries module, we identified the slowest and most frequent query (a /home.do call) and targeted this for improvement.  We then found that forcing an index hint improved the query execution time significantly, and now we will define an Active Query Index Hint.

1.  Enter the Example (target) query, the Table name, Hint type, Index name, and Correlation name like the example below.  
    ![Example (target) query](sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba1044 "Example (target) query")  
      
    Be aware of the following:
    -   The yellow highlighted area above shows the resulting force hint by columns and not the name. This is a quirk of the form and should still work as expected. Once saved, the index hint example will show the index name - see below.
    -   The index name selection pop-up gives the option to search by index name but will display the columns once selected.
    -   The Correlation name is the table alias from the query itself.
2.  Once the Table name, Hint type, Active flag, and other details have been entered, save or submit the hint.  Note there is a validation process that occurs, and upon successful save, you will see a blue success message like the one below:  
    ![Success message](sys_attachment.do?sys_id=ec3a213193306e10e7eef35d6cba1034 "Success message")
3.  Compare the example rewrite SQL (shown in red above) to that which was earlier tested at the database:  
    ![Example rewrite SQL](/sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba103a "Example rewrite SQL")

NOTE: Spacing, copy and paste of special characters and embedded carriage returns are all significant and can cause the platform query hint to not be implemented properly.  Spaces must be maintained if the example query had extra spaces, the query hint must have the same.  This is why a simple text editor works best, as special characters will not be inadvertently inserted into the hint.

#### Confirm the improvement:

Confirming the improvement to the SQL execution time for the target can be done in a couple of ways.

1.  If the source of the query is known, for example, a specific filter, report, or widget on a page, we can enable Debug SQL (Detailed) and confirm that the platform is properly substituting the original version of the query with that which we defined with the force index hint above:  
    -   From our original query at the beginning of this article, we know the source was a /home.do call.  In this case, the user homepage and widget were known, and we can quickly confirm that the platform is properly substituting the query via the debug output:  
        ![Debug output](sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba104a "Debug output")  
          
        The original timing is immediately available by setting the earlier defined index hint to be inactive (or having verified it firsthand before the index hint)  
          
        ![Original query, slow execution](sys_attachment.do?sys_id=ec3a213193306e10e7eef35d6cba1036 "Original query, slow execution")
2.  If the source of the query is not clearly understood, we can simply watch the Slow Query module using the same parameters we originally used to identify the target query and check that the last sighting displays a time prior to our index query hint.  The new forced index query should also be visible with a very recent Last sighting time stamp, using appropriate filter conditions within the Slow Queries module.  
      
    This example shows the original and the new version of the query with the force index hint displayed:  
    ![Original and the new version of query](sys_attachment.do?sys_id=fc3a213193306e10e7eef35d6cba1040 "Original and the new version of query")

NOTE: This same process of verification and hint creation can be used for ignore, force, and use hint types.  This note could apply equally to each.
