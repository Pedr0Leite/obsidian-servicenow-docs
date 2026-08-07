---
title: "Get All the CI classes"
aliases:
  - Get All the CI classes
tags:
  - servicenow-dev-program
  - code-snippet
  - get-all-the-ci-classes
  - background-scripts
---

# Get All CI Classes

A background script that lists all Configuration Item (CI) classes in your ServiceNow instance by using the TableUtils API to find all tables that extend `cmdb_ci`.

## Usage

1. Navigate to **System Definition → Scripts - Background**
2. Copy and paste the script content
3. Click "Run fix script"

## What It Does

The script:
1. Creates a TableUtils object for the base CI table (`cmdb_ci`)
2. Gets all tables that extend this base class using `getAllExtensions()`
3. Converts the Java object to JavaScript array using `j2js()`
4. Prints each CI class table name

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
