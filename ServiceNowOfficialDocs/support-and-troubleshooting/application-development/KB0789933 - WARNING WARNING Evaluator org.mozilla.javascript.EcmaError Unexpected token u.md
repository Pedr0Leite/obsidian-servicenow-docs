---
title: "WARNING *** WARNING *** Evaluator: org.mozilla.javascript.EcmaError: Unexpected token: u"
aliases:
  - KB0789933
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789933
kb_number: KB0789933
last_modified: 2026-06-29
---

## WARNING \*\*\* WARNING \*\*\* Evaluator: org.mozilla.javascript.EcmaError: Unexpected token: u

  

### Issue

Making a REST API call to ServiceNow instance fails with below evaluation error:

**WARNING \*\*\* WARNING \*\*\* Evaluator: org.mozilla.javascript.EcmaError: Unexpected token: u**

### Release

All releases

### Cause

This is a Javascript error, appears when you use JSON.parse(String) over an JSON object i.e. you are in an impression that the input you're passing is a string but it's already a JSON object.

### Resolution

Check your REST API script and avoid using JSON.parse(String) over an JSON object.

Reference:

1.  [RESTAPIRequestBody - Scoped, Global](https://docs.servicenow.com/csh?topicname=c_ScriptableServiceRequestBody.html&version=latestestBody.html "RESTAPIRequestBody - Scoped, Global")
