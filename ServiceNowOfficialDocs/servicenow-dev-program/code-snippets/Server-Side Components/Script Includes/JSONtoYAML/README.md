---
title: "JSONtoYAML"
aliases:
  - JSONtoYAML
tags:
  - servicenow-dev-program
  - code-snippet
  - jsontoyaml
  - script-includes
---

Hi Everyone,

This code is to convert JSON object into Yaml format.

To use this please pass the JSON object as below to this function as shown below

var conYaml = global.SCRIPTINCLUDENAME ('JSON OBJECT');

conYaml will hold the converted Yaml.

**Inputs**:
{ hello: 'world', hello2: [ 'hello', 'world' ] }

**Outputs**:
---
hello: world
hello2:
- hello
- world

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
