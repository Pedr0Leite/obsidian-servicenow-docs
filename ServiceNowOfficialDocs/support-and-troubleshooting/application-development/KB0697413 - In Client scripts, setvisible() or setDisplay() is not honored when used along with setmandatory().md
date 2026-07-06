---
title: "In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()"
aliases:
  - KB0697413
tags:
  - servicenow
  - support-kb
  - client-scripts
  - ui-policy
  - GlideForm
  - g_form
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0697413
kb_number: KB0697413
last_modified: 2024-01-28
---

## In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()

  

### Issue

# Symptoms

* * *

setVisible() and setDisplay() are working as expected but when these APIs used with setMandatory(), setVisible/setDisplay is not honored. 

# Release

Istanbul, Jakarta, Kingston, London 

# Cause

* * *

From Istanbul onwards, we specifically and intentionally block setVisible or setDisplay calls on Mandatory fields to prevent scenarios where a field is mandatory, but not visible to be populated. This is designed functionality that is behaving as expected.

# Resolution

* * *

In order to display and make fields mandatory at the same time:

\-- Use UI Policies instead of client script. Its also recommended using UI Policies over client script due some of the benefits check this doc: [Use UI policy instead of a client script](https://docs.servicenow.com/csh?topicname=client-script-best-practices.html&version=latest#ariaid-title5 "Use UI policy instead of a client script")

\-- If UI Policy is not helping you to achieve your functionality use setMandatory and setVisible in two separate client scripts.

## Related

- [[KB0696583 - Setting 'setSectionDisplay' function to 'false' does not hide the form section.]]
- [[KB0711972 - oldValue returns empty value instead of the previous value for onChange client scripts]]
- [[KB0720671 - Generic error on form Submit canceled due to a script error - please contact your System Administrator]]
