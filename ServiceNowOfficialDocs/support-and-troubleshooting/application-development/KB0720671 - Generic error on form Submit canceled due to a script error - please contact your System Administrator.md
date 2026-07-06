---
title: "Generic error on form: \"Submit canceled due to a script error - please contact your System Administrator\""
aliases:
  - KB0720671
tags:
  - servicenow
  - support-kb
  - client-scripts
  - roles
  - scripting
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720671
kb_number: KB0720671
last_modified: 2025-11-10
---

## Generic error on form: "Submit canceled due to a script error - please contact your System Administrator"

  

### Issue

Receiving error on form: "Submit canceled due to a script error - please contact your System Administrator"

### Symptoms

The following generic error message is displayed when a user submits a form:

![Error message in red "Submit cancelled due to a script error"](sys_attachment.do?sys_id=d77311be939292d4e7eef35d6cba105a "Submit error message") 

### Release

All Release

### Cause

As the error states, this means a Client Script has thrown an error during submission of the form.

This generic error is displayed to users if they do not have the **client\_script\_admin** role.

In some cases the issue will not be reproducible by your admin user and there will be no debug output in the browser's javascript console. If this is the case you will need to assign this role to the user and then impersonate them to reproduce and see the actual error being thrown.

### Resolution

Troubleshooting the actual error being triggered will involve further investigation.

To see the error being generated you will need to reproduce the issue with a user that has the **client\_script\_admin** role.

### Related Links

Best Practices: [Client Scripting Technical Best Practices](https://developer.servicenow.com/dev.do#!/guides/xanadu/now-platform/tpb-guide/client_scripting_technical_best_practices)

## Related

- [[KB0697413 - In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()]]
- [[KB0696583 - Setting 'setSectionDisplay' function to 'false' does not hide the form section.]]
- [[KB0713125 - 'itil' roled users are not able to see the 'Closed' state on the choice list for incidents]]
