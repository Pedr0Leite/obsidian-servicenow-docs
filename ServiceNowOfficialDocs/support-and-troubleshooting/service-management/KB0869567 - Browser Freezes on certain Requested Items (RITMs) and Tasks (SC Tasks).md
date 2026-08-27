---
title: "Browser Freezes on certain Requested Items (RITMs) and Tasks (SC Tasks)"
aliases:
  - KB0869567
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869567
kb_number: KB0869567
last_modified: 2023-12-01
---

## Browser Freezes on certain Requested Items (RITMs) and Tasks (SC Tasks)

  

### Issue

The user was facing an issue where certain RITMs and SC Task records were freezing, or "breaking" the browser, and the page would never load. They wanted to know why this was.

### Resolution

It was found that the behavior was caused by a custom Client Script  
  
When the custom Client Script was switched to active = false, the behavior stopped and the previously affected RITMs/SC Tasks opened perfectly. Then, when the custom Client Script was set back to active = true, the behavior reoccurred and the browser froze, loading endlessly.  
  
As the reported behavior was a result of a custom Client Script, it was recommended that the user's development team kindly review the code internally and resolve the issue internally.

It was also shared that Support Engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementation of customizations like this is not in Support's area of expertise.
