---
title: "Export all or only specific columns using XML"
aliases:
  - KB0610525
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0610525
kb_number: KB0610525
last_modified: 2025-12-16
---

## Export all or only specific columns using XML

  

### Issue

Export all or only specific columns using XML 

Overview

* * *

When exporting using the default export XML of a list or record, all columns from the table are included. This article explains how to export only specific columns and the sys\_id of the record. Importing those XMLs in a target instance when there already is a record with the sys\_id in the export file will only update the column(s) included in the export file while leaving the other columns as they are. If there is no record for that sys\_id, it will be created.

When exporting large amounts of data you may need to review the following:

[Export Limits](https://docs.servicenow.com/csh?topicname=c_ExportLimits.html&version=latest "Export Limits") 

[Breaking up Large Exports](https://docs.servicenow.com/csh?topicname=t_BreakUpALargeExport.html&version=latest "Breaking up Large Exports") 

Other articles that may be helpful with debugging are:

[Enable export debug logging](https://docs.servicenow.com/csh?topicname=c_EnableExportDebugLogging.html&version=latest "Enable export debug logging")

Process

* * *

1.  Open up form view for the intended table https://<myinstance>.service-now.com/<TableName>.do
2.  Right-click on the form window and select **Configure > Form Layout**. 
3.  In **Form View and section**, click in the **View name** field and select **New**.
4.  Create a new form layout adding only the columns you want to export.
5.  Click **Save**. 
6.  To test the new view, click the menu icon ![](sys_attachment.do?sys_id=01b1c32693f97250f538fb2d6cba1094) and select **View > <yournewviewname>**.  
    Only the columns you specified and want to export are displayed.
7.  To obtain the record XML, add the following URL to your instance adjusting the three listed variables:   
    Use this for all records without view: https://<myinstance>.service-now.com/<TableName>.do?XML&useUnloadFormat=true[  
    Use this for all records without filter: https://<myinstance>.service-now.com/<TableName>.do?XML&useUnloadFormat=true&sysparm\_view=<ViewName>](https://\<myinstance\>.service-now.com/\<TableName\>.do?XML&sysparm_view=\<ViewName\>)[  
    ](https://\<myinstance\>.service-now.com/\<TableName\>.do?XML&sysparm_view=\<ViewName\>)[Use this for all records with a filter:  https://<myinstance>.service-now.com/<TableName>.do?XML&useUnloadFormat=true&sysparm\_view=<ViewName>&sysparm\_query=<yourQueryHere>](https://\<myinstance\>.service-now.com/\<TableName\>.do?XML&sysparm_view=\<ViewName\>)  
    -   myinstance = Name of your instance
    -   TableName = Name of the table you would like to export
    -   ViewName = Name of the view you just created  
          
        The XML export of these records is displayed.  
          
        
8.  In browser click S**ave page as**.
9.  Save the file as an XML file.  
    The file is now ready to import into an instance. It should only contain the sys\_id of the record and the columns from the list view.
10.  Note: The generated file should have a quick spot check done on it to confirm it only contains the intended fields. A typo in the view name, or the view being created on a different table than the one being exported may lead to all rows being exported instead of just the expected ones.

  

Example

* * *

On Instance A, create a new field named Test on the incident table and added data. Create the same field on Instance B. Need to add the populated data from Instance A into Instance B without changing all of the other fields on the incident table.

1.  Navigate to the Incident table in List view **incident\_list.do**
2.  Select a record.
3.  Clicked the menu icon ![](sys_attachment.do?sys_id=b0b1c32693f97250f538fb2d6cba108d) and selected **Configure > Form Layout**.
4.  Created a form named **Migrate** .
5.  Added only the **Test** field to the form.
6.  Saved the form.
7.  Navigate to the following link:   
      
    https://instanceA.service-now.com/incident.do?XML&useUnloadFormat=true&sysparm\_view=Migrate  
      
    
8.  Saved the file as import.XML.
9.  Logged in to Instance B.
10.  Right-clicked on List view and selected **Import XML**.
11.  Selected XML file.
12.  Imported data.
13.  Confirmed the data was now located in Instance B with no changes to other fields. 

Notes

The export limits apply when using this methodology, so if you are exporting more than the "glide.xml.export.limit" setting ensure you increase this property 

[https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/exporting-data/concept/c\_ExportLimits.html#d96966e61](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/exporting-data/concept/c_ExportLimits.html#d96966e61)

### Release

.

### Resolution

.
