---
title: "Validate IPv6 Address"
aliases:
  - Validate IPv6 Address
tags:
  - servicenow-dev-program
  - code-snippet
  - validate-ipv6-address
  - regular-expressions
---

# IPv6 Address Validator

This snippet validates **IPv6 addresses** in both full and compressed formats using JavaScript regex.

### Features
- Supports full and shortened IPv6 formats (`::` compression)
- Validates loopback (`::1`) and link-local (`fe80::`) addresses
- Rejects invalid hex groups and multiple `::`

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
