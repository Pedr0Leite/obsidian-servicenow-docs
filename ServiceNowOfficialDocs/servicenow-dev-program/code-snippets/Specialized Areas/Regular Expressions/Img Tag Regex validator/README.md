---
title: "Img Tag Regex validator"
aliases:
  - Img Tag Regex validator
tags:
  - servicenow-dev-program
  - code-snippet
  - img-tag-regex-validator
  - regular-expressions
---

**Regex Pattern**
1. <img : looks for <img in text 
2. \w : looks for any word character (equivalent to [a-zA-Z0-9_])
3. \W : looks for any non-word character (equivalent to [^a-zA-Z0-9_])
4. '>' : looks for character >

**How to use**
1. Run this query in background/Fix scripts.
2. The info message will return articles having images. This is very useful information when there are broken images in articles after movement between instances or tools.
3. This can be further enhanced to replace image src if required.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
