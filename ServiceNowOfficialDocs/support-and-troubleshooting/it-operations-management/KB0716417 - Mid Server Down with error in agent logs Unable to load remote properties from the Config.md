---
title: "Mid Server Down with error in agent logs \"Unable to load remote properties from the Config\""
aliases:
  - KB0716417
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716417
kb_number: KB0716417
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

After an instance Upgrade the MID Server status is down, version is not updated as well.  If you check in the MID Server host, MID Server application is running and you can see from the agent logs the MID Server has been upgraded because Installed version is the same as Assigned version and you get the message "Installed packages are up-to-date":

![](sys_attachment.do?sys_id=6d3b606adb42b450e515c2230596199a)

Also on the same agent logs you will see these warnings, and severe errors:

![](sys_attachment.do?sys_id=e53b606adb42b450e515c223059619a0)

# Release

* * *

All supported Family Versions.

# Cause

* * *

This is caused by a Field Read ACL on sys\_metadata_._  You can validate this further by enabling "Debug Security" and then impersonating MID Server Instance user.  The debug will show we are triggering two Read ACLs ecc\_agent\_property and sys\_metadata.\* and the one blocking us in this case is sys\_metatdata.\*/read

![](sys_attachment.do?sys_id=213b606adb42b450e515c223059619a6)

# Resolution

* * *

Add a Field Level Read ACL for ecc\_agent\_property.\* as below:

![](sys_attachment.do?sys_id=693b606adb42b450e515c223059619ab) 

# Additional Information

* * *

Please note that the MID Server will query other records in the instance and may trigger the same severe error, in which case please add the appropriate ACL.  As always please validate in your sub-production first.  When in doubt please raise an incident in HI.

References:

[ACL Rule Types](https://docs.servicenow.com/csh?topicname=acl-rule-types.html&version=latest#d898410e282 "ACL Rule Types")

[How to create an ACL](https://docs.servicenow.com/csh?topicname=t_CreateNewACL.html&version=latest "How to create an ACL")

[ACL Debugging](https://docs.servicenow.com/csh?topicname=c_AccessControlRulesDebug.html&version=latest "ACL Debugging")
