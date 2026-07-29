---
title: "Indian Mobile Numbers"
aliases:
  - Indian Mobile Numbers
tags:
  - servicenow-dev-program
  - code-snippet
  - indian-mobile-numbers
  - regular-expressions
---

# Here's an example of how you can utilize regex in a Business Rule in ServiceNow:

```
(function executeRule(current, previous) {
var regex = /^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$/;
var fieldValue = '919876543210'; // Replace with your field name
if (fieldValue && !fieldValue.match(regex)) {
        current.setAbortAction(true);
        gs.info('Invalid mobile number format.');
    }
})(current, previous);
```
# Valid Scenarios 
+91-9883443344 <br />
9883443344 <br />
09883443344 <br />
919883443344 <br />
0919883443344 <br />
+919883443344 <br />
+91-9883443344 <br />

# Invalid Scenarios

WAQU9876567892 <br />
ABCD9876541212 <br />
0226-895623124 <br />
6589451235 <br />
0924645236 <br />
0222-895612 <br />
098-8956124 <br />
022-2413184 <br />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
