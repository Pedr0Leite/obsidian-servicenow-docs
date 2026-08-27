---
title: "\"Updated on\" filed on the Software installation record."
aliases:
  - KB2606978
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2606978
kb_number: KB2606978
last_modified: 2025-11-05
---

## "Updated on" filed on the Software installation record.

  

Software installation records will never get updated by discovery or any other sources, rather when re-discovering the same record will update the "Last scanned" field on the installation record. So, "Last Scanned" is the filed will need to checking is need information when the installation record is discovered instead of updated\_on.  
  
Process:  
  
\=> When the information of software installations for a server are brought we just compare is the matching software installation record exists, if exist we update the Last scanned field. If record doesn't exist we create a new record and the rest all old data of the software installation are deleted.   
  

\[-\] Cause of the update on the "Updated on" filed:   
  
\=> The "Updated on" filed can be updated by different job like Reconciliation, Normalization or Software install Deduplication job.
