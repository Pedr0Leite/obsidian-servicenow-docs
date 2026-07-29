---
title: "Hybrid Script Include for AJAX or Server Side Parameters"
aliases:
  - Hybrid Script Include for AJAX or Server Side Parameters
tags:
  - servicenow-dev-program
  - code-snippet
  - hybrid-script-include-for-ajax-or-server-side-parameters
  - script-includes
---

This example shows how one could code a script include that might be called in two different scenarios. One being a client AJAX call, and the other being a server side call, from another script include perhaps.

Example usage:
Client script AJAX call:

        var ajax = new GlideAjax('example_hybrid_parameters');
        ajax.addParam('sysparm_name', 'exampleHybrid');
        ajax.addParam('sysparm_parm1', parm1);
        ajax.addParam('sysparm_parm2', parm2);
        ajax.addParam('sysparm_parm3', parm3);
        ajax.addParam('sysparm_parm4', parm4);
        ajax.getXMLAnswer(exampleResponse);

    Call from server side script:

        var pr = new example_hybrid_parameters();
        result = pr.checkPrereq(parm1, parm2, parm3, parm4);
        return result;

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
