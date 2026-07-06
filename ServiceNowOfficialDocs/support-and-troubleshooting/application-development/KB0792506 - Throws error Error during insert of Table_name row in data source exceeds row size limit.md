---
title: "Throws error \"Error during insert of \"Table_name\" : row in data source exceeds row size limit"
aliases:
  - KB0792506
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792506
kb_number: KB0792506
last_modified: 2024-04-08
---

## Throws error "Error during insert of "Table\_name" : row in data source exceeds row size limit

  

### Issue

When we try to load the records from data source to import set table and if the row size limit got exceeded we receive error as "Error during insert of "Table\_name" : row in data source exceeds row size limit please consider excluding fields and it shows which fields are taking larger space and specifies to exclude those fields from import to avoid this errors

### Release

All

### Cause

Max row size we can allow is 8126 bytes, but if the row ( all fields size in single row of import) exceeded this limit we through this error

### Resolution

Normally Max row size we can allow is 8126 bytes

The size of each row is determined by the amount of content in all fields, as well as the character set for text fields. For example, a row with 10 text fields each containing 1000 characters using a French character set takes 15360 bytes.

Which means it got exceeded the max row size that we allow.

In this type of situation we have two options

1) If you want to import all fields and you can't exclude any field that is reaching out max row limit then consider exporting as two different import sets like half of the fields in one import set and another half in another import set so that by dividing the fields we can avoid max row size limit.

Note: in both the import sets, include coalesce field so that we are not manipulating the Data in target table, both import set's should contain the coalesce fields to transform the data to target table correctly without mismatching or creating duplicate records in target table

2) Exclude the fields which have more bytes in size which generally ServiceNow recommend's, but again if you can't exclude those larger fields then would like to recommend option 1

Normally in LDAP import we have LDAP Attribute list to specify what fields we want to import to avoid this kind of error situations.

Example screen shot which looks like when you encounter the error

![](sys_attachment.do?sys_id=3212e401db0c38d0fec4fb2439961949)
