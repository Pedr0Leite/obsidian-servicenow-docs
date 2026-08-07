---
title: "Parse csv file and read each row"
aliases:
  - Parse csv file and read each row
tags:
  - servicenow-dev-program
  - code-snippet
  - parse-csv-file-and-read-each-row
  - server-side
---

We have a ServiceNow api to parse Excel file(GlideExcelParser) however it wouldn't work for parse CSV as a file (not a CSV string using "sn_impex.CSVParser()")
there is a alternate way to read csv logic.js logic parse the CSV as file and can read all the rows/columns
this can be used in any server side scripting , just need to pass the attachment sys_id
This comes very handy when your receving a CSV as email to serviceNow and need to update records based on incoming CSV file vales
Ex:input CSV:![image](https://github.com/gowdah/code-snippets/assets/42912180/857f8fa1-6671-44ae-b105-779f2d7d4fc5)



ex:output:XYZ,abc,Hemanth

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
