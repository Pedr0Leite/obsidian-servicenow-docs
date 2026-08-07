---
title: "Solaris server Discovery Pattern Issue  ( Missing \"Name\" field ) "
aliases:
  - KB0750474
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750474
kb_number: KB0750474
last_modified: 2024-04-07
---

## Solaris server Discovery Pattern Issue ( Missing "Name" field )

  

### Issue

# Symptoms

-   While Solaris Server Discovery throws error message in logs similar to " Insertion failed with error,In payload missing minimum set of input values for criterion (matching) attributes from identify rule for table \[cmdb\_ci\_storage\_device\]. Add these input values in payload item '{"className":"cmdb\_ci\_disk","values":{"storage\_type":"disk","drive\_type":"disk","size\_bytes":"3234234234","discovery\_source":"ServiceNow","device\_interface":"scsi","model\_id":"abcdxxxx12313342","interface":"scsi","disk\_space":"231231232","sys\_class\_name":"cmdb\_ci\_disk","manufacturer":"abcdxxx12211xxxxxxx"}}' ".
-   In this case, the payload is missing "Name" field.

# Cause

-   Debug the pattern step Solaris Storage -> Get Disks which runs the following command - "iostat -Enr | tr ',' '\\n' | sed 's/^\[cs\]\[a-zA-Z0-9\_\]\*/DiskSection: Name: &/g'; echo ''" . The output is dropping the DiskSection: Name.
-   The above command works properly on Non-Zone Solaris CI but does not work on Solaris Zone machine.

# Resolution

\- Need to update command to take "Name" field into account ( change '\\n' to '\\\\n' ) - "iostat -Enr  | tr ',' '\\\\n' | sed 's/^\[cs\]\[a-zA-Z0-9\_\]\*/DiskSection: Name: &/g'; echo ''"
