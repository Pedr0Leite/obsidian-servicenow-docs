---
title: "PolicyKit issues with Linux MID Servers using non-admin accounts"
aliases:
  - KB0815542
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815542
kb_number: KB0815542
last_modified: 2026-04-17
---

## PolicyKit issues with Linux MID Servers using non-admin accounts

  

On system using systemd, you may need to create PolKit rules and SELinux policies for the MID Server. The policies are only needed when you see the related errors. SELinux errors can occur when installing the MID Server in a home directory, but do not appear if installing in a common place such as /opt. 

The following sample PolKit policies are only for demonstration purposes. Please consult the system administrators when using them.

Check the version first, some environment may have older version. To check the version, use command

```
pkaction --version
```

Make sure the user is in the "midserver" group or specify the group in the script. Also need to put the service name to be whatever the user set if not "mid.service".

**/usr/share/polkit-1/rules.d/00-midserver.rules** (**for version 0.106 or later**)

polkit.addRule(function(action, subject) {  
    if (action.id == "org.freedesktop.systemd1.manage-units" &&  
                            subject.isInGroup("midserver") &&  
                            action.lookup("unit") == "mid.service") {  
        return polkit.Result.YES;  
    }  
});

**/etc/polkit-1/localauthority/50-local.d/99-midserver.pkla (for version before 0.106)**

\[midserver Permissions\]  
Identity=unix-group:midserver  
Action=org.freedesktop.systemd1.manage-units  
ResultAny=yes  
ResultInactive=yes  
ResultActive=yes
