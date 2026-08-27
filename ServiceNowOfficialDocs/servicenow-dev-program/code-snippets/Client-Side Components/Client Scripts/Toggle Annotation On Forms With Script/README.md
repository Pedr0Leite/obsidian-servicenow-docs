---
title: "Toggle Annotation On Forms With Script"
aliases:
  - Toggle Annotation On Forms With Script
tags:
  - servicenow-dev-program
  - code-snippet
  - toggle-annotation-on-forms-with-script
  - client-scripts
---

# Use Case
This method can be used to show/hide/toggle form annotations through client-side script.

# Limitation
This script works only with form annotations of the following types:
- Info Box Blue
- Info Box Red
- Section Details
- Text

# Usage

### Show form annotations
```javascript
SN.formAnnotations.show();
```

### Hide form annotations
```javascript
SN.formAnnotations.hide();
```

### Toggle form annotations
```javascript
SN.formAnnotations.toggle();
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
