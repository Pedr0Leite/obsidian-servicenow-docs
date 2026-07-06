---
title: "Discovery Linux/Unix discovery fails with error \"The message store has reached EOF\""
aliases:
  - KB0743075
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743075
kb_number: KB0743075
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Classification fails when discovering a Linux/Unix server with error "**The message store has reached EOF**".

# Release

* * *

All currently supported releases.

# Cause

* * *

Discovery SSHCommand probes can use either legacy J2SSH client or the ServiceNow SSH client (SNCSSH) on individual MID Servers. SNCSSH is a ServiceNow implementation of an SSH client and is active by default for all MID Servers on new instances. Upgraded instance will need to configure it via a MID Server property.

# Resolution

* * *

Confirm if the property is already set in your instance:

1.  Navigate to "MID Server > Servers".
2.  Select the MID server which is being used for the discovery.
3.  Select the "Configuration Parameters" related list.
4.  Search for the mid.ssh.use\_snc parameter.
5.  If the parameter is not present, create the parameter with value set to true.

Note: The parameter can also be set per probe via probe parameter use\_snc\_ssh. However, it will usually be better to set this parameter on the MID server so that it does not have to be set on multiple probes.

# Additional Information

* * *

Links to additional information:

-   [MID Server parameters](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "MID Server parameters")
-   [SSHCommand parameters](https://docs.servicenow.com/csh?topicname=r_Parameters.html&version=latest "SSHCommand parameters")
-   [Add a MID Server parameter](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest#t_SetMIDServerParameters "Add a MID Server parameter")
