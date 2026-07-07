---
title: "Gets the display value according to the specified language"
aliases:
  - Gets the display value according to the specified language
tags:
  - servicenow-dev-program
  - code-snippet
  - gets-the-display-value-according-to-the-specified-language
  - gliderecord
---

Get the display value according to the specified language.

(Install Language Plugin)

```javascript
var gr = new GlideRecord("incident");
gr.setLimit(1);
gr.query();
gr.next();
var user = gs.getUser();
var lang = user.getPreference("user.language");

// Japanese
user.setPreference("user.language", 'ja');
var outputJA = '' + gr.state.getLabel() + ' = ' + gr.state.getDisplayValue();
// English
user.setPreference("user.language", 'en');
var outputEN = '' + gr.state.getLabel() + ' = ' + gr.state.getDisplayValue();
gs.info(outputJA + ' / ' + outputEN);

user.setPreference("user.language", lang);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
