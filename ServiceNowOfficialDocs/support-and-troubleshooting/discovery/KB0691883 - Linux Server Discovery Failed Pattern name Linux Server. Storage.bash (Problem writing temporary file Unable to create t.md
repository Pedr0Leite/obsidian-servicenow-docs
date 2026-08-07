---
title: "Linux Server Discovery Failed: Pattern name: Linux Server. Storage.bash (Problem writing temporary file: Unable to create temporary file)"
aliases:
  - KB0691883
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691883
kb_number: KB0691883
last_modified: 2024-04-07
---

## Linux Server Discovery Failed: Pattern name: Linux Server. Storage.bash (Problem writing temporary file: Unable to create temporary file)

  

### Issue

# Symptoms

* * *

Linux Server Discovery Failed: Pattern name: Linux Server. Storage.bash (Problem writing temporary file: Unable to create temporary file)

During Linux server Discovery, the Linux Server pattern with the following error in the Agent log:

HorizontalDiscoveryProbe SEVERE \*\*\* ERROR \*\*\* Unable to create temporary file

# Release

* * *

Any

# Cause

* * *

User in credential does not have access to /tmp in the target Linux host

# Resolution

* * *

1.  Ensure that Credential specified on the Instance is able to write to /tmp on Target Linux host.
2.  Ensure that MID server is run by the Local Administrator account.

If above troubleshooting steps has been completed then try setting the mid server parameter to "mid.ssh.use\_snc"

set the mid server to true for "mid.ssh.use\_snc"

Set the MID Parameter   
\=====================   
1\. Navigate to -> MID Server -> Servers -> Select MID Server    
2\. Then click on "Configuration Parameters" tab -> New -> Parameter name -> "mid.ssh.use\_snc" and value "true".   
Then restart the MID server and ran a quick discovery again to the same IP address to test it out. 

  ![](/sys_attachment.do?sys_id=e89aa0a6db42b450e515c22305961926)
