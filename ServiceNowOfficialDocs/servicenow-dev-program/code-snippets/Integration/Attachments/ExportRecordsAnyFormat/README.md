---
title: "ExportRecordsAnyFormat"
aliases:
  - ExportRecordsAnyFormat
tags:
  - servicenow-dev-program
  - code-snippet
  - exportrecordsanyformat
  - attachments
---

The snippet can be used to export records from any table and then attach on another record. Records can be exported records from any table view based on an encoded query in any of the these formats: CSV, XLS, XLSX, PDF, JSON, XML, XSD, SCHEMA, RSS. If required, the attachment can be send out to users through a notification (with check include attachments).

#### Access & Authentication
A user with web service access and read access to the data needs to be present in the instance. The user must also have write access to the record where the file will be attached.

In the script there are two options for authentication:

1. [Credentials](https://docs.servicenow.com/en-US/bundle/vancouver-platform-security/page/product/credentials/reference/credentials-getting-started.html) - preferred
2. Using system properties to store username and password - less secure

#### Input Format

- tableName: Name of table whose records need to be exported
- recordId: sys_id of the record where the exported attachment should be uploaded, this record must exist on the same table
- recordQuery: encoded query to access the required records. For PDF files, you should only pass sys_id eg: sys_id=b3f076504750210042bd757f2ede273f
- recordView: Specify the required view, Pass empty string for default view eg: ess, portal,
- dataType: The required export format - Supported formats eg CSV, XLS, EXCEL, XLSX, PDF, JSONv2, XML, XSD, SCHEMA, RSS 
- fileName: Name of exported file along with its extension eg fileName.csv, fileName.json

EXAMPLE: ```gs.print(exportRecords(tableName, recordId, recordQuery, recordView, dataType, fileName));```

### Sample Usage

#### Export all active incidents from the ESS view into XLSX format 

```javascript
gs.print(exportRecords('incident', 'b3f076504750210042bd757f2ede273f', 'active=true', 'ess', 'XLSX', 'Active Incidents.xlsx'));
```

#### Export all active incident from the default view in JSON format

```javascript
gs.print(exportRecords('incident', 'b3f076504750210042bd757f2ede273f', 'active=true', '', 'JSONv2', 'Active Incidents.json'));
```

#### Export a record into PDF

```javascript
gs.print(exportRecords('incident', 'b3f076504750210042bd757f2ede273f', 'sys_id=b3f076504750210042bd757f2ede273f', '', 'PDF', 'record.pdf'));
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/CSVParser/README|CSVParser]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Calculate attachment hash code/README|Calculate attachment hash code]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Convert KnowledgePage to PDF/README|Convert KnowledgePage to PDF]]
