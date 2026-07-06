---
title: "Reusable RESTMessageV2 retry pattern"
aliases:
  - Reusable RESTMessageV2 retry pattern
tags:
  - servicenow-dev-program
  - code-snippet
  - reusable-restmessagev2-retry-pattern
  - restmessagev2
---

# Function: `retry(func, retries, delayTime)`

Retries a given function multiple times with a delay between each attempt.

## Parameters

- **`func`** (`Function`): The function to be executed and potentially retried on failure.
- **`retries`** (`number`): The number of times to retry the function if it fails or returns a null/undefined result.
- **`delayTime`** (`number`): The delay time between retries, in milliseconds.

## Returns

- **`any`**: Returns the result of the function if successful within the allowed retries; otherwise, returns the last result (which may be `null` or `undefined`).

## Description

The function attempts to execute the provided `func()` and checks for a non-null result. If the result is null or an exception occurs, it retries the function up to the specified `retries`, with a delay of `delayTime` milliseconds between each attempt.

## Example Usage

```javascript
function getToken() {
    // Simulated operation that might fail
    var request = new sn_ws.RESTMessageV2("token", "GET");
    var response = request.execute();
    var statusCode = response.getStatusCode();
    var result = null;
    switch(statusCode) {
        case 200:
            result = JSON.parse(response.getBody());
            break;
        default:
            throw new Error("request failed, http status code: " + statusCode);
    }
    return result;
}

var result = retry(getToken, 3, 2000);  // Try 3 times, with a 2-second delay between each attempt
gs.info("Operation result: " + result);
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/API for Automatic Group creation/README|API for Automatic Group creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Aadhaar Verification/Readme|Aadhaar Verification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Auth2 client credentials token cache with auto-refresh/README|Auth2 client credentials token cache with auto-refresh]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/AzureDevOps/README|AzureDevOps]]
