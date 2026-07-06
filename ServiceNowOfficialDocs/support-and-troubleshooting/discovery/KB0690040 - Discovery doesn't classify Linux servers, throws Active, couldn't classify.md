---
title: "Discovery doesn't classify Linux servers, throws Active, couldn't classify"
aliases:
  - KB0690040
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690040
kb_number: KB0690040
last_modified: 2024-04-07
---

## Discovery doesn't classify Linux servers, throws Active, couldn't classify

  

### Issue

# Symptoms

* * *

Discovery of Linux servers fails with the following error in the Discovery Log:

Discovery doesn't classify Linux servers, throws Active, couldn't classify

# Release

* * *

Any 

# Cause

* * *

Shell is not included in the base system, for example winbind\_bash

# Resolution

* * *

One of the solutions below will work:

1.  Set the default shell for the linux discovery user as bash, ksh, or sh - this is more recommended as it is simple and more tested.
2.  Add to each MID server a mid parameter: mid.ssh.shells\_supported with the added value of winbind\_bash (value=ksh,sh,bash,winbind\_bash).

# Additional Information

* * *

[SSHCommand probe](https://docs.servicenow.com/csh?topicname=c_SSHCommandProbe.html&version=latest "SSHCommand probe")
