---
title: "KBArticleExpPDF"
aliases:
  - KBArticleExpPDF
tags:
  - servicenow-dev-program
  - code-snippet
  - kbarticleexppdf
  - script-includes
---

This utility contains a script include which generates PDF export of knowledge article  and this script include handles all HTML formatting of Knowledge article as well.
Also, this utility will handle any images attached in KB article body.

Sample Script to call this Script Include:

new PolicyPDFHelper().getPDFBase64('b10db60e2fc738101d84d2172799b69c','landscape');

// First paramter is sys_id of KB article from kb_knowledge record
// Second Parameter is PDF Export Mode. Accepted inputs are landscape or portrait.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
