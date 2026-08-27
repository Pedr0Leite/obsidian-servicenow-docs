---
title: "HAPROXY Discovery: Cannot locate config file: /etc/haproxy/haproxy.cfg"
aliases:
  - KB0815788
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815788
kb_number: KB0815788
last_modified: 2024-04-08
---

## HAPROXY Discovery: Cannot locate config file: /etc/haproxy/haproxy.cfg

  

### Issue

During a discovery for a HAPROXY Load Balancer, the following warning message appears:

"Cannot locate config file: /etc/haproxy/haproxy.cfg - Exit status: 1"

### Release

Any Released

### Cause

The "haproxy.cfg" file cannot be found due to the following causes:

1.  The version of HAProxy installed is the Enterprise version.
2.  The "haproxy.cfg" isn't inside the right path.
3.  The user might not have the credential to read and access the folder.

### Resolution

Below is the fix for each of the Causes mentioned above.

1.  Ensure that the version of the HAProxy installed is Community Edition.  This is because the Enterprise version is currently not supported.
2.  You can find the location of the "haproxy.cfg" file using the following command "sudo find / -name haproxy.cfg".
    -   To test if it is installed correctly run the following command "haproxy -v". The server should respond with:
        
        HA-Proxy version 1.6.3 2015/12/25  
        Copyright 2000-2015 Willy Tarreau <willy@haproxy.org>
        
3.  We can only find this when running the command with sudo.
    -   Another option is to include the must\_sudo parameter to the probe. Then we would have the command being triggered with sudo, which should work.
