---
title: "Mid server alerts are being sent to the users who has \"sn_vul_r7.admin\" role, since it contains 'mid_server' role."
aliases:
  - KB0725789
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725789
kb_number: KB0725789
last_modified: 2026-05-22
---

## Mid server alerts are being sent to the users who has "sn\_vul\_r7.admin" role, since it contains 'mid\_server' role.

  

### Issue

# Symptoms

* * *

"User <user name> with mid\_server role not associated with a MID Server. No login attempts within reporting period" It has been in the alert console after installing store application "Rapid7 Integration".

# Cause

* * *

This happens if any user has mid\_server role and its not associated with any MID server, as we should not use mid\_server role for normal users.

With the activation of Rapid 7 integration, the vulnerability users group contains the role sn\_vul\_r7.admin which contains mid\_server role. This is OOTB behavior. As a result, all the users in that vulnerability group are receiving below alerts.

"User <user name> with mid\_server role not associated with a MID Server. No login attempts within reporting period"

### Release

Any

### Resolution

# Resolution

* * *

As a workaround,

01) We need to add read acl with sn\_vul\_r7.admin on both \`ecc\_agent\` & \`ecc\_agent.\*\`

02) And then remove the "mid\_server" role from sn\_vul\_r7.admin contains

Steps:

a) Navigate to System security > Access Control (ACL)

b) Search for the tables 'ecc\_agent' & 'ecc\_agent.\*' with operation as 'read'

c) Add 'sn\_vul\_r7.admin' role for both the tables.

https://<instance-name>.service-now.com/sys\_security\_acl.do?sys\_id=18966e1183130000dada83ec37d929c8  
https://<instance-name>.service-now.com/sys\_security\_acl.do?sys\_id=1c70ad13531202001f175f43911c0876

d) Navigate to Vulnerability group users consists of sn\_vul\_r7.admin role.

e) Remove the ""mid\_server" role from sn\_vul\_r7.admin contains.

https://<instance-name>.service-now.com/sys\_user\_role.do?sys\_id=b5688a62e7370300809a268b03f6a9f4

### Related Links

# Additional Information

* * *

Importance of the role "mid\_server" associated with sn\_vul\_r7.admin

It's just to enable Vulnerability Admin to select from available Mid Servers on Rapid7 Configuration page.
