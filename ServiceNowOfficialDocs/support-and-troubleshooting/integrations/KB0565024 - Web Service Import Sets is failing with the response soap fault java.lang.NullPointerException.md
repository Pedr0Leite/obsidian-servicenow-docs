---
title: "Web Service Import Sets is failing with the response \"soap fault: java.lang.NullPointerException\""
aliases:
  - KB0565024
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0565024
kb_number: KB0565024
last_modified: 2024-01-28
---

## Web Service Import Sets is failing with the response "soap fault: java.lang.NullPointerException"

  

### Issue

Web Service Import Sets fail with the response "soap fault: java.lang.NullPointerException"

# Problem

* * *

If the display value of a table returns an empty value, Web Service Import Sets returns soap fault: java.lang.NullPointerException.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: The record import happens correctly. Only the response has a display problem.</td></tr></tbody></table>

# Symptoms

* * *

Web Service Import Sets returns soap fault: java.lang.NullPointerException on the response. Notice that reference fields to the target table show "(empty)" or nothing for those records

# Cause

* * *

Most tables have an attribute set with the **Display** property set to **true**. If a new record is created or updated and the column with the **Display** value is set to an empty value, the result is identified by the **Display** value "(empty)".

As for Web Service Import Set, the results are identified by the **Display** value; empty results could cause the NullPointerException error.  
  
NOTE: Display values could be caused by newly added attributes that set **Display** to **true** accidentally.

# Resolution

* * *

On the target table, set the **Display** attribute on a non-empty column (for example, **Number**) to **true**.  
  
For more information, see the product documentation on [Web service import sets](https://docs.servicenow.com/csh?topicname=c_SOAPWebService.html&version=latest).
