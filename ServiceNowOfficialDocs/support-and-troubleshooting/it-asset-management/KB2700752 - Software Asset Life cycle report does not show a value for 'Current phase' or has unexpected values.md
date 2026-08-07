---
title: "Software Asset Life cycle report does not show a value for 'Current phase' or has unexpected values"
aliases:
  - KB2700752
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2700752
kb_number: KB2700752
last_modified: 2026-04-17
---

## Software Asset Life cycle report does not show a value for 'Current phase' or has unexpected values

  

### Issue

As a customer, you notice discrepancies in the Software life cycle report that amount to either missing or incorrect values on 'Current phase'

### Symptoms

On the Software Product Life cycle report, certain products have either an

a) empty value for 'Current phase', or

b) an incorrect value for 'Current phase', or

c) correct value for 'Current phase', but associated dates are blank on EOL start date / EOS start date / EOES start dates on the report. See an example screenshot 

![](/sys_attachment.do?sys_id=43d7efa193548f94057c7de86cba10e7)

### Release

Any.

### Cause

1) Content is not available on sam\_sw\_product\_lifecyle table and therefore not on the report.

2) Job 'SAM Generate Software Lifecycle report' to populate lifecycle report was not successful.

3) Current phase on the report has a value, but the associated phase Start date is blank, because such information is not publicly available.

### Resolution

1) Re-run the content download jobs to ensure you have latest content on the instance.

Navigate to /cds\_client\_schedule, search by name contains 'Download Software', sort results by 'Last Updated' date and execute the jobs.

2) If the latest content was downloaded on step (1), proceed to troubleshoot as below:

a) Check whether expected values are present on Content table sam\_sw\_product\_lifecyle.

-   If Content is missing or incorrect, please create a Content request following the [Content creation documentation](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/concept/content-request-itam.html).
-   If Content is present, but the life cycle report is not yet updated, attempt to re-run the job 'SAM - Generate Software Lifecycle report' and verify the results on samp\_job\_log table

b) If the 'Current phase' on the report has a value such as 'End of Support' for example, but the 'End of Support Start date' is blank on the report, please note that this is not necessarily a defect. When a date is empty for a populated phase, it can imply that the date is not publicly available but ServiceNow knows that the product has reached that phase. This is indicated on 'Lifecycle code' on sam\_sw\_product\_lifecyle table. Refer [documentation on life cycle code](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1642485).

![](/sys_attachment.do?sys_id=93d7efa193548f94057c7de86cba10ed)
