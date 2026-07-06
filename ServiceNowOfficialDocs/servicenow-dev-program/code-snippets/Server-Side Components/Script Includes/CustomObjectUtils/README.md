---
title: "CustomObjectUtils"
aliases:
  - CustomObjectUtils
tags:
  - servicenow-dev-program
  - code-snippet
  - customobjectutils
  - script-includes
---

# CustomObjectUtils

A utility class to provide methods for safely accessing nested object properties. The class can be initialized to use either ES5 or ES12 (ECMAScript 2021) methods.

## Initialization

To use the utility, you need to create an instance of the `CustomObjectUtils` class. By default, it uses the ES5 methods. If you want to use the ES12 methods, pass `true` to the constructor.

```javascript
var utils = new CustomObjectUtils(); // For ES5
var utils = new CustomObjectUtils(true); // For ES12
```

## Methods

### safeAccess (ES5)

Safely accesses nested object properties.

- **Parameters**:
  - `obj` (Object): The object to access.
  - `path` (string): The dot-separated path to the property.
- **Returns**: The accessed value or `false` if not found.
- **Example**:

```javascript
var myObj = { a: { b: { c: 42 } } };
var value = utils.safeAccess(myObj, 'a.b.c');
console.log(value);  // Outputs: 42
```

### safeAccessModern (ES12)

Safely accesses nested object properties using modern JavaScript features.

#### Modern Features Used:

- **Optional Chaining** (`?.`): Allows reading the value of `key` within a chain of connected objects without having to explicitly check if each reference in the chain is valid.
- **Nullish Coalescing** (`??`): Returns the right-hand operand when the left operand is `null` or `undefined`.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
