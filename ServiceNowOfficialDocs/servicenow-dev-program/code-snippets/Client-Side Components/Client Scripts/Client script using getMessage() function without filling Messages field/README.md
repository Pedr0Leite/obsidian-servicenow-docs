---
title: "Client script using getMessage() function without filling Messages field"
aliases:
  - Client script using getMessage() function without filling Messages field
tags:
  - servicenow-dev-program
  - code-snippet
  - client-script-using-getmessage-function-without-filling-messages-field
  - client-scripts
---

# Client scripts using getMessage() function without filling Messages field

**Problem scenario :**
Developers while writing a client script uses getMessage() function but there are no messages preloaded in the 'Messages' field in client script form

**Solution :**
Write an onSubmit client script to check the above scenario and prevent client script submission with an error message on top of the form.

Check the file `script.js` file for example.

Note : As a best practice for this scenario use 'Checks' in the'Instance scan' feature of serviceNow. If Instance scan is not configured in your instance yet or if you want to avoid the problem during development itself then use this client script.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
