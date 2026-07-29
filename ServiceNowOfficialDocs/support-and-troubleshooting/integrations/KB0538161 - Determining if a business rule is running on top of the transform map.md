---
title: "Determining if a business rule is running on top of the transform map "
aliases:
  - KB0538161
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538161
kb_number: KB0538161
last_modified: 2024-10-20
---

## Determining if a business rule is running on top of the transform map

  

### Issue

Determining if a business rule is running on top of the transform map 

Problem

* * *

Records are not being created or updated in a timely manner on the instance.

Symptoms

* * *

-   Associated transform takes longer than expected
-   Overall performance on the instance is lower when the import occurs

Cause

* * *

Various business rules are being run when the import is performed.  

  
Resolution

* * *

For large imports (10,000 to 100,000), it is advised to disable business rules. To do this:   

-   Locate the particular data source that appears to be causing the issue.
-   In the **Transforms** section, click the desired link to view the associated Transform Map.
-   Within the Transform Map record, locate the **Run Business rules** property and clear the associated checkbox.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>:&nbsp;Consider using an <span style="font-family: 'courier new', courier;">onComplete</span> transform script to run business logic, such as calculations, at the end of an import rather than on each record the way business rules do.</td></tr></tbody></table>
