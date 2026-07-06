---
title: "Discovery throws errors: Cannot remove item \\<IP_address>\admin$\temp\file_name.txt: The process cannot access the file '\\<IP_Address>\admin$\temp\file_name.txt' because it is being used by another process."
aliases:
  - KB0743782
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743782
kb_number: KB0743782
last_modified: 2024-04-07
---

## Discovery throws errors: Cannot remove item \\\\\\admin$\\temp\\file\_name.txt: The process cannot access the file '\\\\\\admin$\\temp\\file\_name.txt' because it is being used by another process.

  

### Issue

# Symptoms

During discovery of windows devices, some of the probes would need access to admin share on the device and throws errors if the credentials do not have enough permissions.

# Release

All releases.

# Cause

Some of the probes like _Windows - Application Dependency Mapping_ would run Powershell scripts and stores the result in a txt file in admin drive.  
  
After reading the file it would try to remove the file. If the credentials used for discovery do not have enough permissions to access admin share we see an error similar to this:  
  

```
Discovery throws error: Cannot remove item \\<IP_address>\admin$\temp\file_name.txt: The process cannot access the file '\\<IP_Address>\admin$\temp\file_name.txt' because it is being used by another process.
```

# Resolution

Ensure that the credential used for discover is able to write/read below path:  
  

```
\\<IP_address>\admin$\temp\ Refer to Discovery probe permissions as per docshttps://docs.servicenow.com/csh?topicname=r_AdditionalPermissions.html&version=latest
```
