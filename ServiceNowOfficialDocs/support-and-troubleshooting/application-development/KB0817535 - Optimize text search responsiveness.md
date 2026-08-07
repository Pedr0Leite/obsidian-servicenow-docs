---
title: "Optimize text search responsiveness "
aliases:
  - KB0817535
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817535
kb_number: KB0817535
last_modified: 2025-07-07
---

## Issue

To improve text search performance, focus on tables that have the largest number of text search terms. The following steps decrease table sizes by excluding stop words and adjusting other key parameters. 

## Resolution

To perform the following steps, sign into your instance with an admin or maintenance role. 

**Step 1. Set the threshold for automatic stop words**

1.  Go to **System Definition** > **Text Indexes** https://<instance\_name>/ts\_index\_name\_list.do?sysparm\_query=
2.  Open a table record, for example, Task.
3.  Ensure that the **AutoStop** checkbox is selected.
4.  Set **Auto threshold** to 50,000.
5.  Select **Save**.

**Note**: Consider how often a term should be found before it becomes trivial and thus not worth being text searchable. 

**Step 2. Reset text search caches**

1.  Go to **System Definition** > **Text Indexes** https://<instance\_name>/ts\_index\_name\_list.do?sysparm\_query=
2.  In Related links, select **Reset Text Search Caches**.

**Step 3. Rerun TS Index Stats**

1.  Go to **System Scheduler** > **Scheduled Jobs**.
2.  Open the **TS Index Stats** record. 
3.  Select **Execute Now**.
4.  Monitor the job until it completes either by watching the worker on the node that picks it up or on the sys\_trigger list.

**Step 4. Set Stop Mode on the task tables**

1.  Once TS Index Stats finishes, go back to the **ts\_index\_name** table. (https://<instance\_name>/ts\_index\_name\_list.do?sysparm\_query=)
2.  Select the **Task table** record.
3.  Scroll down to the stop words that were generated and in the **Stop Mode** column, select all the records and change them to **Neither Index Nor Query** as follows:
    -   Copy the URL only for the stop words of a table and open the URL in a new window.
    -   Right click on column header **Stop Mode**.
    -   Select **Update All**.  
        **Note**: This appears only if you open the stop words in a new window. 
    -   In the new form that opens, from the drop-down list, select **Neither Index Nor Query** 
    -   Select **Update**.

**Step 5: Regenerate indexes**

1.  Return to the **ts\_index\_name** table > **task**.
2.  For each table, select the related link **Regenerate Text Index**, and then select **Submit**.
3.  Let the process complete, and then select the next table.
4.  Select **Regenerate Text Index**.
5.  Verify that the text index event is processing and finishes.

**Additional considerations**

-   While regenerating text indexes, not all text search terms are retrieved for end users.
-   This process can take at least one day, therefore, for best results, do this during times with decreased workloads, such as on a Friday afternoon. 
-   Test in a subproduction environment first.

## Additional Information

For more information, see the following product documentation:

[Enable automatic stop words for a table](https://docs.servicenow.com/csh?topicname=t_ConfigureAnAutomaticStopWord.html&version=latest)

[Configure a table-specific stop word](https://docs.servicenow.com/csh?topicname=t_ConfigureATableSpecificStopWord.html&version=latest)

## Related

- [[KB0750759 - Text search does not return results if Date or DateTime fields is used as search query]]
- [[KB0542700 - Debugging legacy text search issues]]
