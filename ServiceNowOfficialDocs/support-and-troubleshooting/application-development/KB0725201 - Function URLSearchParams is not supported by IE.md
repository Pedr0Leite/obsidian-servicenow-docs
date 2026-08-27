---
title: "Function URLSearchParams is not supported by IE"
aliases:
  - KB0725201
tags:
  - servicenow
  - support-kb
  - client-scripts
  - browser-compatibility
  - internet-explorer
  - javascript
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725201
kb_number: KB0725201
last_modified: 2024-04-07
---

## Function URLSearchParams is not supported by IE

  

### Issue

# Symptoms

* * *

The function 'URLSearchParams' in Client Script cannot parse URL parameters in IE. 

# Release

* * *

London release

# Cause

* * *

This function is not supported by IE. It is not an issue with ServiceNow.  
[https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/URLSearchParams#Browser\_compatibility](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/URLSearchParams#Browser_compatibility)

# Resolution

* * *

Using Javascript code

## Related

- [[KB0726412 - Unable to change background color of reference field using g_form.getControl in client script]] - other client-script browser-compatibility issue
- [[KB0745114 - Catalog client script is not hiding the container and the variables within the container]] - client-script troubleshooting

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
