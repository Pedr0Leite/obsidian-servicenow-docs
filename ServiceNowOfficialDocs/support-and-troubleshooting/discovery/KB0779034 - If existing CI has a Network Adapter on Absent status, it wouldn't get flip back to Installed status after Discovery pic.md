---
title: "If existing CI has a Network Adapter on \"Absent\" status, it wouldn't get flip back to \"Installed\" status after Discovery pickup Active Interface."
aliases:
  - KB0779034
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779034
kb_number: KB0779034
last_modified: 2024-04-08
---

## If existing CI has a Network Adapter on "Absent" status, it wouldn't get flip back to "Installed" status after Discovery pickup Active Interface.

  

### Issue

If existing CI has a Network Adapter on "Absent" status, it wouldn't get flip back to "Installed" status after Discovery pickup Active Interface.

Step to Reproduce  
\===============  
1\. Ran a Discovery against Linux Server  
2\. Verify that the Network Adapter is populated in the "cmdb\_ci\_network\_adapter" and that there is a related "cmdb\_ci\_ip\_address\_ record pointing to this NIC.  
3\. Now manually set the Network Adapter status to "Absent".  
4\. Re-run the Discovery against the same Linux Server.  
5\. The expected result would be to flip the Network Adapter's status back to "Installed" status along with the "CI IP" (cmdb\_ci\_ip\_address)

### Resolution

1.  This is a known issue, currently tracked by the PRB1336617.
2.  The workaround is to import the Pattern Pre/Post Script xml file attached to this KB.
3.  The PRB1336617 will eventually address a similar issue with File System as well.
