---
title: "Data not getting imported from one instance to another through XML data source"
aliases:
  - KB0788897
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788897
kb_number: KB0788897
last_modified: 2024-04-08
---

## Data not getting imported from one instance to another through XML data source

  

### Issue

 XML files imported from another instance via data source with XML format does not import records when the XPath root node field has been set with the path like:

/unload/<table\_name> or <table\_name>

### Cause

The XPath root node value is not right when you get XML from another instance.

### Resolution

Set the XPath root node field value  to "/xml/<table\_name>"
