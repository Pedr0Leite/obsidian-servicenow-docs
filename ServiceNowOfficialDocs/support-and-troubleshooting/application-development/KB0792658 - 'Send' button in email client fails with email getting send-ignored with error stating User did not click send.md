---
title: "'Send' button in email client fails with email getting send-ignored with error stating User did not click send"
aliases:
  - KB0792658
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792658
kb_number: KB0792658
last_modified: 2026-08-21
---

## Issue

When user clicks on 'Send' button in email client, the email is getting send-ignored. The error string says User did not click send, even if the user did.

System logs show errors:  
  
"FAILED TRYING TO EXECUTE ON CONNECTION glide.10 (connpid=347252): INSERT INTO sys\_email0051"

SEVERE \*\*\* ERROR \*\*\* FAILED TRYING TO EXECUTE ON CONNECTION glide.10 (connpid=347252): INSERT INTO sys\_email0051 (\`body\`,\`notification\_type\`,\`headers\`,\`instance\`,\`subject\`,\`sys\_mod\_count\`,\`weight\`,\`sys\_updated\_on\`,\`type\`,\`sys\_id\`,\`error\_string\`,\`sys\_updated\_by\`,\`deleted\`,\`mailbox\`,\`reply\_to\`,\`receive\_type\`,\`user\_id\`,\`sys\_created\_on\`,\`recipients\`,\`target\_table\`,\`state\`,\`user\`,\`sys\_created\_by\`) VALUES(?,'SMTP','X-ServiceNow-Source: EmailClient  
X-ServiceNow-SysEmail-Version: 2

## Resolution

Remove current.update from on-before business rule on sys\_email table (as it's firing on "before" so, it's not needed). 

The out-of-the box Business Rule "Set Inbox" should be enabled to fire on 'insert' and 'update'.

## Additional Information
