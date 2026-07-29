---
title: "IP Address Validation"
aliases:
  - IP Address Validation
tags:
  - servicenow-dev-program
  - code-snippet
  - ip-address-validation
  - regular-expressions
---

This snippet extracts IPv4 and IPv6 addresses from free text. For single-value validation, see `validateIPInput.js` and `Validate IPv6 Address/script.js`.

The regex in `getIP4OrIPV6address.js` finds both IPv4 and IPv6 addresses within arbitrary text content.

IPv6 coverage includes:
- Full addresses like `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Compressed forms like `fe80::1` (`::` for omitted zeros)
- IPv4-embedded forms like `::ffff:192.168.1.1`

IPv4 validation now strictly enforces each octet to be in the range 0–255.

Valid IPv4 examples:

- 192.168.1.1
- 127.0.0.1
- 0.0.0.0
- 255.255.255.255
- 1.2.3.4

Invalid IPv4 examples (correctly rejected by the regex):

- 256.256.256.256
- 999.999.999.999
- 1.2.3

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
