---
title: "After importing HR PDF Template into Production from sub-Prod, the record does not show in the list-view. Trying to recreate record fails due to record \"already existing\"."
aliases:
  - KB0863147
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863147
kb_number: KB0863147
last_modified: 2024-04-08
---

## After importing HR PDF Template into Production from sub-Prod, the record does not show in the list-view. Trying to recreate record fails due to record "already existing".

  

### Issue

The user tried to export an sn\_hr\_core\_pdf\_template record from Dev to Prod and it said that the same record already existed in Prod, but there were no HR PDFs in Prod in that table. The user wanted to know what was going on, and why.

### Cause

The issue was that the correct Document Revision (dms\_document\_revision) was not also carried over upon moving the parent sn\_hr\_core\_pdf\_template record over. As a result, an ACL script failure occurred, blocking visibility of the HR PDF template record (without any notice of the typical "x amount of records were removed due to security restraints" message).

### Resolution

As discussed briefly above, the reported behavior occurred as a result of a failing read operation ACL ( ref: /nav\_to.do?uri=sys\_security\_acl.do?sys\_id=72ea04ad53113200eb7c0a1806dc3436 ).

The ACL failed due to the script section evaluating as "false".

The script is as follows:

```
answer = false;if (current.isNewRecord())answer = true;var docRevision = current.document_revision;if (!gs.nil(docRevision))answer = new hr_Utils()._isDocRevOwner(docRevision);
```

Reviewing the script of the ACL, it was noted that the "docRevision" was not "nil", so the answer the system would use would be derived from the logic stored within the "if" condition ( `answer = new hr_Utils()._isDocRevOwner(docRevision);` )

From the XML of the impacted record, it was noted that the sys\_id of the "document\_revision" did not exist when searched in the dms\_document\_revision table. Hence, when the script does not find the dms\_document\_revision which should correspond with the sn\_hr\_core\_pdf\_template record, the script returns false and visibility is restricted.  
  
To resolve the issue, the user needed to pull the dms\_document\_revision record which matched the "version" (in this case, "0.1") of the document and push it to their Production instance.   
  
Once the user did this, visibility was restored as the ACL's script evaluated to "true".
