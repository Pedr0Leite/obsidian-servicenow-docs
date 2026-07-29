---
title: "URL with parameter XML exports raw data only"
aliases:
  - KB0635940
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635940
kb_number: KB0635940
last_modified: 2024-04-07
---

## URL with parameter XML exports raw data only

  

### Issue

URL with parameter XML exports raw data only

  
  

# Problem

* * *

When exporting from the list view and using the **Export > XML** menu option, the raw data of selected records is exported with the associated journal fields (Additional Comments and Work Notes) and attachments. However, using **XML parameter on the URL** exports only the raw data of the records.

<table class="internalTable" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Data exported</strong></td><td style="vertical-align: middle; text-align: left;"><strong>URL with XML parameter</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Menu "Export &gt; XML"</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Raw data</td><td style="vertical-align: middle; text-align: left;"><strong>Yes</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Yes</strong></td></tr><tr class="sp" style="background-color: #dedede;"><td style="vertical-align: middle; text-align: left;">Attachments</td><td style="vertical-align: middle; text-align: left;">No</td><td style="vertical-align: middle; text-align: left;"><strong>Yes</strong></td></tr><tr class="sp" style="background-color: #dedede;"><td style="vertical-align: middle; text-align: left;">Journal fields</td><td style="vertical-align: middle; text-align: left;">No</td><td style="vertical-align: middle; text-align: left;"><strong>Yes</strong></td></tr><tr class="sp" style="background-color: #dedede;"><td style="vertical-align: middle; text-align: left;">Currency information</td><td style="vertical-align: middle; text-align: left;">No</td><td style="vertical-align: middle; text-align: left;">No</td></tr><tr class="sp" style="background-color: #dedede;"><td style="vertical-align: middle; text-align: left;">Audit</td><td style="vertical-align: middle; text-align: left;">No</td><td style="vertical-align: middle; text-align: left;">No</td></tr><tr class="sp" style="background-color: #dedede;"><td style="vertical-align: middle; text-align: left;">Data store on other tables</td><td style="vertical-align: middle; text-align: left;">No</td><td style="vertical-align: middle; text-align: left;">No</td></tr></tbody></table>

# Symptoms

* * *

This problem occurs when exporting the records using the URL containing the XML parameter. After importing the XML, there are no attachments or journal fields like **Work Notes** or **Additional Comments** on those records. However, some XML exports do contain the raw data plus the attachments and journal fields.

# Cause

* * *

The context menu **Export >** **XML** contains the logic to export the records, the attachments, and the journal fields. However, although the XML parameter informs the application server to export the raw data of the records in the URL query, it contains no logic to export attachments, journal fields, audit records, currency fields, or any other data store on a different table.

# Resolution

* * *

If you need to export the attachments and journal fields (for example, **Work Notes** and **Additional Comments**), use the **Export > XML** menu option.  
  
![Export > XML](sys_attachment.do?sys_id=c5ebe4eadb42b450e515c223059619ed "Export > XML")  
Here is the result of the export: The incidents get exported with the journals and attachments.  
  
![Export > XML result](sys_attachment.do?sys_id=c9ebe4eadb42b450e515c223059619f2 "Export > XML result")  
  

If you do need to use the URL parameter, then you will need to create the logic to export the associated attachment and journal fields directly on their tables.  
  
![Using XML parameter](sys_attachment.do?sys_id=8debe4eadb42b450e515c223059619f7 "Using XML parameter")  
  
![Using XML parameter results](sys_attachment.do?sys_id=51ebe4eadb42b450e515c223059619fd "Using XML parameter results")  
  
The following guide provides information to help you understand how to export attachments and journals.  
  

<table class="internalTable" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Data exported</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Table containing the data</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Relationship</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Raw data</td><td style="vertical-align: middle; text-align: left;">table on the URL</td><td style="vertical-align: middle; text-align: left;">raw record</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Attachments</td><td style="vertical-align: middle; text-align: left;">sys_attachment</td><td style="vertical-align: middle; text-align: left;">table_sys_id = sys_id of the raw record</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Attachments_docs</td><td style="vertical-align: middle; text-align: left;">sys_attachment_doc</td><td style="vertical-align: middle; text-align: left;">sys_attachment = sys_id of the attachment</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Journal fields</td><td style="vertical-align: middle; text-align: left;">sys_journal_field</td><td style="vertical-align: middle; text-align: left;">element_id = sys_id of the raw record</td></tr></tbody></table>

Note that journal fields are stored in the \[sys\_journal\_field\] table. They are linked to the records by the sys\_journal\_field.element\_id = sys\_id of the raw record.

Attachments are stored in the \[sys\_attachment and \]sys\_attachment\_doc tables. They are linked to the records by sys\_attachment.table\_sys\_id = sys\_id of the raw record, and sys\_attachment\_doc.sys\_attachment = sys\_id of the attachment.
