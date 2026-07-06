---
title: "Software Asset Management content library is incomplete or has fewer records than expected in SAMP tables"
aliases:
  - KB0694718
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694718
kb_number: KB0694718
last_modified: 2026-06-19
---

## Software Asset Management content library is incomplete or has fewer records than expected in SAMP tables

  

### Issue

The default scheduled job SAM - Apply latest content changes runs every week to retrieve incremental data from the central repository (CDS) and update the SAMP-related tables on the instance. If this job has not run correctly, the Software Content Library may be incomplete or show fewer records than expected.

The following tables are updated by the Download Software Content jobs:

-   **samp\_content\_version**
-   **samp\_sw\_publisher**
-   **samp\_sw\_product\_category**
-   **samp\_sw\_product**
-   **samp\_sw\_package**
-   **samp\_sw\_entitlement\_definition**
-   **samp\_product\_map**
-   **samp\_package\_map**
-   **samp\_sw\_product\_definition**
-   **samp\_sw\_product\_process**
-   **samp\_m2m\_suite\_entitlement\_def**
-   **samp\_lifecycle\_definition**
-   **samp\_price\_list**
-   **samp\_named\_user\_type**
-   **samp\_dmap\_downgrade\_model**
-   **samp\_file\_name**
-   **samp\_file\_map**
-   **samp\_file\_set**
-   **samp\_sw\_subscription\_integration**
-   **samp\_sw\_subscription\_product\_definition**
-   **samp\_sap\_license\_metric**

As an admin, the names of these scheduled jobs are visible. Hover over the information icon on a job to see which content type it covers, such as Publisher, Package, and so on.

Sample URL for Download Software Content jobs:

https://<instance\_name>.service-now.com/cds\_client\_schedule\_list.do?sysparm\_query=nameSTARTSWITHDownload%20Software%20Content%3A

  
  

### Release

All releases

### Resolution

**Note:** **Only the maint user can perform steps 1 through 3**. Run the specific job outside of peak usage hours in the production instance, as these jobs take time to download the complete data.

1.  Go to the intended **Download Software Content** job record.
2.  Open the record and locate the **Last Updated On** field. If the field is not visible, add it to the form.
3.  **Clear the Last Updated On field** so that it is empty, then save the record.
4.  **Run the job**. This downloads the complete data from the CDS to the instance.
5.  After the job completes, run the SAM - Apply latest content changes job.

![Data service: Download schedule](/sys_attachment.do?sys_id=b3e80f5d47e9cb945ab5156c736d43b5 "Data service: Download schedule")
