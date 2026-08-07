---
title: "Negative RegExp for Condition Builder"
aliases:
  - Negative RegExp for Condition Builder
tags:
  - servicenow-dev-program
  - code-snippet
  - negative-regexp-for-condition-builder
  - regular-expressions
---

# Negative regular expressions for Condition Builder

## What problem does it solve?

Certain condition builders (not all, unfortunately) come with a __matches regex__ operator. This is very handy to filter records based on complex rules applied to strings.

Unfortunately, there is no __does not match regex__ operator and I would have needed this on several occasions.

## Solution

The solution is to use a negative regular expression by leveraging the **?!** operator (called _Negative Lookahead_). So one needs to find the proper regex for what it should match, and then invert it with a Negative Lookahead.

For example, the following regex matches a well formed MAC address:
```
^(([A-Fa-f0-9]{2}[:-]){5}[A-Fa-f0-9]{2}).*$
```

Whereas this one matches anything that does NOT match a well formed MAC address:
```
^(?!(([A-Fa-f0-9]{2}[:-]){5}[A-Fa-f0-9]{2})$).*$
```

The script in this example shows how to use this, but it's really in a condition builder that it will be useful. As matter of fact, a script can always reverse the logic (but the condition builder cannot). The script identifies all the entries in an array that do NOT have a well formed MAC address: note that it does not use a __false__ logic in the _if_, proving that the regex does revert the logic.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check for special characters/readme|Check for special characters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
