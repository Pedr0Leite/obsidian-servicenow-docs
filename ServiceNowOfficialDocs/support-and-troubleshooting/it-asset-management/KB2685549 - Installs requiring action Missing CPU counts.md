---
title: "Installs requiring action: Missing CPU counts "
aliases:
  - KB2685549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2685549
kb_number: KB2685549
last_modified: 2025-12-19
---

## Installs requiring action: Missing CPU counts

  

### Issue

Software Installation marked as unlicensed with reason as "Missing CPU core count"

### Symptoms

1\. Here under "Installs requiring action", notice 2 records for "SEAPP25" server.![](/sys_attachment.do?sys_id=fd1dc93687753a1857288519dabb3523 "Screenshot 1.png")

2\. Both those records referring to the same install.![](/sys_attachment.do?sys_id=7a8051fe87f53a1857288519dabb357f "Screenshot 6.png")

3\. Windows Server "SEAPP25".   
<cpu\_core\_count>2</cpu\_core\_count>  
<cpu\_count>2</cpu\_count>

And this Windows Server "SEAPP25" is Virtualized by ESX Server "sesaux161"![](/sys_attachment.do?sys_id=d1dd45fa87753a1857288519dabb357b "Screenshot 2.png")

4\. ESX Server "sesaux161" is Member of VMware vCenter Clusters "SESACLU4 - Intel" & "SESACLU4 - Intel"![](/sys_attachment.do?sys_id=5b7ec57287b53a1857288519dabb358a "Screenshot 3.png")

5\. We do have other ESX Servers as {sesaux135, sesaux136, sesaux154}... which are part of Clusters "SESACLU4 - Intel" & "SESACLU4 - Intel"  
![](/sys_attachment.do?sys_id=4c6fc97a87b53a1857288519dabb3580 "Screenshot 4.png")

6\. And from the above :-

ESX Server "sesaux136"   
Windows Server "SESANT426"   
<cpu\_core\_count/>  
<cpu\_count>1</cpu\_count>  
  
ESX Server "sesaux154"   
Windows Server "ACP16M"  
<cpu\_core\_count/>  
<cpu\_count>1</cpu\_count>

### Release

Zurich

### Cause

We do see two Windows Server "SESANT426" & "ACP16M" do have EMPTY "cpu\_core\_count" and "cpu\_count" which belongs to same cluster.  
And hence we do see "Missing CPU Core Count" on those servers.![](/sys_attachment.do?sys_id=0521193a87393a1857288519dabb3574 "Screenshot 7.png")

### Resolution

Make sure "cpu\_core\_count" & "cpu\_count" are populated for the above servers and run fresh recon and check the results.
