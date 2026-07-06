---
title: "How to troubleshoot attachments which are encrypted with \"Encryption Support\" plugin gets corrupted intermittenly?"
aliases:
  - KB0688847
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0688847
kb_number: KB0688847
last_modified: 2026-06-17
---

## How to troubleshoot attachments which are encrypted with "Encryption Support" plugin gets corrupted intermittenly?

  

### Issue

# Description

* * *

As per the "[Encryption scripting samples](https://docs.servicenow.com/csh?topicname=c_EncryptionSupport.html&version=latest "Encryption scripting samples")", you can setup a insert/update business rule on sys\_attachment table so that when an attachment is attached to the task record, it gets auto encrypted as per the "[Encryption context](https://docs.servicenow.com/csh?topicname=t_EncryptionContextSetup.html&version=latest "Encryption context")" available for the logged in user.

However, there can be situation, where the encrypted attachment gets corrupted, intermittently. This article will detail on how can we investigate this issue scenario. 

# Procedure

* * *

 **Checking the transaction and logs:**

1.  Note down the time of attachment from the record as below,![](sys_attachment.do?sys_id=bf1d6862db82b450e515c2230596192d)
2.  Look into the transaction log with the user who attached the attachment as shown in the attached screenshot,![](sys_attachment.do?sys_id=3b1d6862db82b450e515c22305961933)
3.  Based on the session and node information collected from transaction log, get the node log from specific node. ( There are various way by which you can collect the node log, for example via [catalog](<How to use the Gather Instance Node Logs tool> "catalog"))
4.  Review the node log around the time of attachment attached, this should give us a clue

**Make sure that original attachment is valid and not corrupted:**

It is possible that if the original attachment is corrupted, the encrypted result will be corrupted as well and hence make sure you have valid original attachment.

**Make sure the encryption business rule is run only for the user who had valid encryption context:**

In the encryption business rule on sys\_attachment table, make sure that you check the condition like below,

gs.getUser().hasRole("<Encryption context name>)

So that business rule will be executed only for the users who has valid encryption context, else customer might run into known problem,

"PRB1252502 - SysAttachment.changeEncryptionContext API is corrupting attachments when user doesn't have access to encryption context being changed to"

If you do not prefer having the condition, then include in the encryption code to check the logged in users role whether it is associated with the valid encryption context before trying encryption.

**Make sure there is no multiple/recursive update business rule running on sys\_attachment table and causing encryption to run multiple time for the same attachment.**

You can verify this via logging as the user who has encryption context (and has admin access) and then turn on the session debug, then try attaching a attachment, the session debug will reveal if there is a recursive/multiple call for encryption business rule.

Note: Encryption support will not work, when you impersonate, you must log on as the person, who has encryption context associated with his role.

# Applicable Versions

* * *

Any supported release.

# Additional Information

* * *

[Encryption scripting example](https://docs.servicenow.com/csh?topicname=c_EncryptionSupport.html&version=latest "Encryption scripting example")

[Encryption Support](https://docs.servicenow.com/csh?topicname=c_EncryptionSupport.html&version=latest "Encryption Support")

[Encryption context](https://docs.servicenow.com/csh?topicname=t_EncryptionContextSetup.html&version=latest "Encryption context")

[Business Rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Business Rules")
