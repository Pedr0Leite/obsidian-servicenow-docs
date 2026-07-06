---
title: "Discovery failing to set DNS Domain values on some CI records"
aliases:
  - KB0754395
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754395
kb_number: KB0754395
last_modified: 2024-04-07
---

## Discovery failing to set DNS Domain values on some CI records

  

### Issue

Discovery shows failing to set the DNS Domain value on some CI records.

### Cause

Review the Discovery scan for your target CI and look for the input record on the DNS ECC Queue input payload, to see if the name was resolved. This happens when the reverse DNS lookup for a CI fails. 

The input payload would show something like this:   
<result ip\_address="x.x.x.x" result="unresolved">   
<name/>   
</result> 

For a successful reverse DNS lookup, the DNS input ECC Queue record has a domain name available, as the name was successfully resolved from the IP address.   
  
Here is an example snippet:   
<result ip\_address="x.x.x.x" result="resolved">   
<name>ABCD</name>   
</result> 

Notice the difference in the result value for the two snippets. The unsuccessful one is 'unresolved', and the successful one is 'resolved'.

### Resolution

In the above example snippets, the reason the DNS Domain is not populated for the CI is that the reverse DNS lookup fails for this CI. For this, it is recommend to check with your internal teams managing your CIs or reviewing your CI for why the reverse DNS lookup is failing.
