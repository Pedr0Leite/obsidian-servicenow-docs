---
title: "How to resolve OfficeXmlFileException for Data Source file imports"
aliases:
  - KB0780856
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780856
kb_number: KB0780856
last_modified: 2026-01-20
---

## How to resolve OfficeXmlFileException for Data Source file imports

  

### Issue

Resolve an OfficeXmlFileException error that occurs when importing files using a Data Source configured with the attachment retrieval method.

When you run the Data Source, you see the following error:

"com.glide.db.impex.datasource.DataSourceException: org.apache.poi.poifs.filesystem.OfficeXmlFileException: The supplied data appears to be in the Office 2007+ XML. You are calling the part of POI that deals with OLE2 Office Documents. You need to call a different part of POI to process this data (eg XSSF instead of HSSF)"

The Data Source is configured with:

-   Type: File
-   Format: CSV
-   File Retrieval Method: Attachment

### Release

All supported releases

### Cause

This error occurs when a Data Source was previously configured with File Retrieval Method set to SCP, and the File Path field value was not cleared before changing the retrieval method to Attachment.

Because File Path is not a valid parameter for the attachment retrieval method, the import fails. To confirm this is the cause, select Show XML on the Data Source record and verify that File Path contains a value.

### Resolution

To resolve this error, clear the File Path field value:

1.  Go to the **Data Source** record. https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_data\_source.do?sys\_id=<sys\_id>
2.  Change **File Retrieval Method** to **SCP**.
3.  Clear the **File Path** field.
4.  Change **File Retrieval Method** back to **Attachment**.
5.  Select **Save**.
6.  Select **Test Load 20 Records** to verify the import completes without error.

### Related Links

[Data Sources (product documentation)](https://docs.servicenow.com/csh?topicname=c_DataSources.html&version=latest)
