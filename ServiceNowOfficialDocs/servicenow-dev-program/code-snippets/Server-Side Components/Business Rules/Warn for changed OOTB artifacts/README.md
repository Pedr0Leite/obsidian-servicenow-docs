---
title: "Warn for changed OOTB artifacts"
aliases:
  - Warn for changed OOTB artifacts
tags:
  - servicenow-dev-program
  - code-snippet
  - warn-for-changed-ootb-artifacts
  - business-rules
---

# Description

Changing OOTB artifacts like Script Includes or Business Rules is never a good idea, as you will get so called skipped records in the next upgrade/patch you have to care about. Otherwise, you can get into big trouble and risk broken functionalities as well as unpredictable behavior. But many developers are not aware about the consequences when playing around with OOTB artifacts or have no idea about how to revert the changes (see https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993700 if you don't know how).

Therefore I implemented the Busines Rule "Warn for changed OOTB artifacts" which displays a warning when opening a modified OOTB artifact. The warning message also provides a link to the most recent OOTB version, where you will find a UI Action for reverting to that version.

# Business Rule

The JavaScript code of the Business Rule is written in way that be also used with a scoped application.

**Table:** `sys_metadata`

**When:** display

# Result

![Result](./screenshot.png)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
