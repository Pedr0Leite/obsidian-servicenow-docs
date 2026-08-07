---
title: "PII Redactor"
aliases:
  - PII Redactor
tags:
  - servicenow-dev-program
  - code-snippet
  - pii-redactor
  - script-includes
---

There are many implementations where there is a need to redact PII data from servicenow tables as par of audit requirements.
e.g Instances may have catalog item for the newly onboarded users to order hardware equirement.
This catalog item will contain variable to store shipping information of users which is PII data.
Audit will not want other users to see this PII data.

I have created a script include which redacts PII data from variables, audit log, audit history, emails based on different paramters.

Example Usage:

Below sample code redacts PII data from requested item variables which contain PII Data.

```ruby
 var sc = new GlideRecord('sc_item_option_mtom');
    sc.addQuery('request_item', '<SYSID_OF_RITM>');
    sc.query();
    while (sc.next()) {

        var r = new piiRedaction().redactPii('sc_req_item','<SYSID_OF_RITM>',sc.sc_item_option.value);

    }

```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
