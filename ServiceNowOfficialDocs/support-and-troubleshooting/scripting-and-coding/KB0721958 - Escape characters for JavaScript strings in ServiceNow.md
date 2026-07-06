---
title: "Escape characters for JavaScript strings in ServiceNow"
aliases:
  - KB0721958
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721958
kb_number: KB0721958
last_modified: 2026-02-18
---

## Escape characters for JavaScript strings in ServiceNow

  

### Issue

Learn how to handle special characters in JavaScript strings on the ServiceNow platform. Certain characters can generate unexpected and sometimes hard-to-identify errors in scripts. These JavaScript strings can be used within various scripting objects such as business rules, workflow scripts, ACL records, and other areas of the application. Special characters cause issues because they have a specific meaning to the JavaScript language when included in a command.

To use these characters in a string within ServiceNow scripting objects, the character must be escaped. Escaping means preceding the character with a backslash (\\) to tell the JavaScript compiler to treat the next character literally rather than interpret it in the usual manner.

### Release

All supported releases

### Resolution

#### **Method**

The three main characters that require escaping are:

-   Single quote (')
-   Double quote (")
-   Backslash (\\)

The single and double quote characters are used to begin and terminate a string in JavaScript, and the backslash character is the escape character itself.

To escape these characters, place a backslash (\\) before the character within the string that should be treated literally:

-   \\' — allows use of a single quote character
-   \\" — allows use of a double quote character
-   \\\\ — allows literal use of a backslash character

#### **Example**

The following two JavaScript statements each generate an error due to special characters within a string.

#### **Example 1: Double quotes within a double-quoted string**

var userName = "Jerome "The Race" Anderson";

This statement produces the following error:

Javascript compiler exception: missing ; before statement (null.null.script; line 1) in: var userName = "Jerome "The Race" Anderson";

#### **Example 2: Single quote within a single-quoted string**

gs.log('Please retry the operation, the expected button wasn't found on the form.');

This statement generates the following error:

Javascript compiler exception: missing ) after argument list (null.null.script; line 1) in: gs.log('Please retry the operation, the expected button wasn't found on the form.');

#### **Example 3: Backslashes in a file path**

The following statement does not necessarily generate an error, but it does not produce the expected results.

var filepath = "\\bzavr\\extra\\open\\files\\config.ini";

The filepath variable as stored in memory contains the following string:

\\bzavrextraopenilesconfig.ini

#### **Corrected examples**

To fix these issues, precede each special character in the string with the JavaScript backslash escape character:

var userName = "Jerome "The Race" Anderson";

gs.log('Please retry the operation, the expected button wasn't found on the form.');

var filepath = "\\\\bzavr\\extra\\open\\files\\config.ini"; 

#### **Additional information**

The backslash character can also represent special non-printable characters within a JavaScript string:

| Escaped character | Representation |
| --- | --- |
| \\b | Backspace |
| \\f | Form Feed |
| \\n | New Line |
| \\r | Carriage Return |
| \\t | Horizontal Tab |
| \\v | Vertical Tab |

To include a non-printable character in a JavaScript string, add the escaped character (that is, \\n to include a new line).

For example, the following statement:

var textData = "This is a test string.\\n\\rNext Line.\\tShifted line.";

When printed, produces output similar to the following:

This is a test string.  
Next Line. Shifted line.
