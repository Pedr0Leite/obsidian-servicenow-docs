---
title: "MID Server install file fails to unzip due to \"Windows Security Warning\" blocked access for installer.bat as potentially harmful"
aliases:
  - KB0779823
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779823
kb_number: KB0779823
last_modified: 2024-04-07
---

## MID Server install file fails to unzip due to "Windows Security Warning" blocked access for installer.bat as potentially harmful

  

### Issue

Windows may prevent all files being extracted from a MID Server installer ZIP file in some circumstances. This will prevent you installing the MID Server.

The popup seen will be like this:

Windows Security Warning  
Windows found that this file is potentially harmful.  
To help protect your computer, Windows has blocked access to this file.  
Name: installer.bat

![](sys_attachment.do?sys_id=ad7c43fcdb8434d0471f9c41ba9619de)

### Release

All

### Cause

Windows is wrong about the file. This is a false positive.

### Resolution

1.  Right-click the ZIP file in Windows Explorer, and select "Properties".
2.  In the General tab, click "Unlock", then "OK"
3.  Try extracting it now, and it'll work.

![](sys_attachment.do?sys_id=7d7c83fcdb8434d0471f9c41ba96192b)
