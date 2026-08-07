---
title: "What is the purpose of the Business Rule 'Flows and Subflows"
aliases:
  - KB0793074
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793074
kb_number: KB0793074
last_modified: 2024-04-07
---

## What is the purpose of the Business Rule 'Flows and Subflows'

  

### Issue

An error appears with an API call that triggers a SubFlow. In the system log this error is appearing:

JavaScript evaluation error on: (function executeRule(current, previous /\*null when async\*/ ) { var view\_name = ""; if (gs.getSession().isInteractive()) { var map = gs.action.getGlideURI().getMap(); if (map.get('sysparm\_view') != null) { view\_name = map.get('sysparm\_view').toString(); if (view\_name == 'welcome\_hub\_flow') { var condition = current.addQuery('type', '=', 'flow'); current.appendOrQuery(condition, 'type', '=', ''); } else if (view\_name == 'welcome\_hub\_subflow') current.addQuery('type', 'subflow'); } } })(current, previous);

Root cause of JavaScriptException: java.lang.NullPointerException: java.lang.NullPointerException:

### Resolution

The business rule we see is a query business rule on sys\_hub\_flow table which has records which are flows and subflows in the instance.  
Now this query business rule based on if it is interaction session, line number 3:  
"An interactive session is one that involves an end-user interacting with a user interface that then retrieves information from a server. An example of this type of session is when a user logs in using the log-in screen or uses a form to query a data store. A non-interactive session is one that only involves programmatic interaction with a server such as a SOAP request to retrieve data."  
It will then check the sysparm\_view value from the URL it gets as an input if it is a flow or a subflow and based on that add the query for flow type field.
