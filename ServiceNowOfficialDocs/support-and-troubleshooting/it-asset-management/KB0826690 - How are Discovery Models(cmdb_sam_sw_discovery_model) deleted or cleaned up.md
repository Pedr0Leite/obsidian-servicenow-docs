---
title: "How are Discovery Models(cmdb_sam_sw_discovery_model) deleted or cleaned up?"
aliases:
  - KB0826690
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0826690
kb_number: KB0826690
last_modified: 2024-04-08
---

## How are Discovery Models(cmdb\_sam\_sw\_discovery\_model) deleted or cleaned up?

  

### Issue

Sometimes discovery models are no longer have any valid Software Installations(cmdb\_sam\_sw\_install) attached to it or customers would want to delete the records. But there is no option to delete the records in this table since there is a delete ACL on the table which requires "nobody" role to this to restrict delete so even "maint" users cannot delete the records.

ACL Link:  
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=43bce2601b702000aebbfbcd2c07136a

### Release

Software Asset Management plugin.

### Resolution

This is on purpose because deleting discovery models can affect reconciliation results so it would be advisable to not run deletions/modifications on the table.  
  
There is a scheduled job OOTB called "SAM - Delete Discovery Models if there are no related Installations" that would every month to delete the discovery models that are no longer have any software installation references.

Link to the job:  
https://<instance-name>.service-now.com/nav\_to.do?uri=sysauto\_script.do?sys\_id=94cf6b3987050300562e4127f5cb0bfd  
  
It is advised to run this job to clean up the records.
