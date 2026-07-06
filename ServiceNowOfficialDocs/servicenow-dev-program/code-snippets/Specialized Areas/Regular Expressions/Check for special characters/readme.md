---
title: "Check for special characters"
aliases:
  - Check for special characters
tags:
  - servicenow-dev-program
  - code-snippet
  - check-for-special-characters
  - regular-expressions
---

# Special Characters Validation (onChange Client Script)

This script validates user input in a specific field and prevents the use of disallowed special characters.  
It is designed to run as an **onChange client script** .

## Functionality

- When the user changes the value of a field, the script checks if the new value contains any special characters.
- If disallowed characters are found, the field is cleared and an error message is displayed to the user.
- The validation uses a regular expression that includes common special characters such as `~`, `@`, `|`, `$`, `^`, `<`, `>`, `*`, `+`, `=`, `;`, `?`, `` ` ``, `'`, `(`, `)`, `[`, and `]`.

## How to Use

1. Add the script as an **onChange client script** on the field you want to validate.
2. Replace the placeholder `'<your_field_name>'` in the script with the actual field name.
3. Customize the regular expression if you want to allow or block different characters.

## Example Behavior

- Input: `Hello@World` → ❌ Invalid → Field is cleared, error message shown.
- Input: `HelloWorld` → ✅ Valid → No action taken.

## Notes

- The script uses `g_form.clearValue()` to reset the field and `g_form.showErrorBox()` to display feedback.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Adhaar validation/README|Adhaar validation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Allow Characters + - ) ( for Phone numbers/README|Allow Characters + - ) ( for Phone numbers]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/AllowAnyLanguage/README|AllowAnyLanguage]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Check if number has 10 digits/README|Check if number has 10 digits]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Consecutive duplicate words/README|Consecutive duplicate words]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Regular Expressions/Credit Card Number Validator/README|Credit Card Number Validator]]
