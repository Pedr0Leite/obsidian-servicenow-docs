---
title: "Importing data into fields that are platform encrypted results in  \"Error while creating cipher for encryption context.: no thrown error\"  during transform"
aliases:
  - KB0760047
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760047
kb_number: KB0760047
last_modified: 2024-04-07
---

## Importing data into fields that are platform encrypted results in "Error while creating cipher for encryption context.: no thrown error" during transform

  

### Issue

When importing data into an Encrypted field via transform, the following error can be seen:

"Error while creating cipher for encryption context.: no thrown error"  
  

### Cause

  
This is an expected behavior since the transform runs as system and system user does not have the necessary encryption context.

### Resolution

1.  First Import data as clear text
2.  then enable encryption context and run (as a user having the encryption context) a script to encrypt the data in batches.

\-- OR --

1.  Use other imports like easy import or web services import
    
    NOTE: To make REST calls work with encryption: 
    
    On POST to insert/update values then the URL parameter to use is sysparm\_input\_display\_value=true  
    On GET request to retrieve values decrypted, it is sysparm\_display\_value=true
