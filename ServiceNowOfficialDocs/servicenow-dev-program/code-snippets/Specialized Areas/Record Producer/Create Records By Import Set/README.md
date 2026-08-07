---
title: "Create Records By Import Set"
aliases:
  - Create Records By Import Set
tags:
  - servicenow-dev-program
  - code-snippet
  - create-records-by-import-set
  - record-producer
---

# Create Records importing an excel spreadsheet in the record producer.
The script import the excel spreadsheet in the Data Source table (sys_data_source) and trigger the tranform map, creating the records.

## Configuration
Step 1. Create a Transform Map

Step 2. Add the table name field to "Data Source" and the excel template file 
![table name field](config1.png)

Step 3. Insert a description with a link to the user download the template
![description and template](config2.png)

Step 4. Insert the script and change the static fields

Step 5. The users need to drop attach the file and submit the record producer
![attach and submit](config3.png)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Record Producer/Update Incident Record from Record Producer/README|Update Incident Record from Record Producer]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0693899 - On Service Portal the record producer form does not display all subcategories option for users with no role|On Service Portal the record producer form  does not display all subcategories option  for users with no role]]
