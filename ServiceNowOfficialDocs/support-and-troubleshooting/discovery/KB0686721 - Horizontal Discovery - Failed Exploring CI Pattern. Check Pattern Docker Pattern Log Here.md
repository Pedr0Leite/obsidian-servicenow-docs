---
title: "Horizontal Discovery - Failed Exploring CI Pattern. Check Pattern Docker Pattern Log Here"
aliases:
  - KB0686721
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686721
kb_number: KB0686721
last_modified: 2024-04-07
---

## Horizontal Discovery - Failed Exploring CI Pattern. Check Pattern Docker Pattern Log Here

  

### Issue

# Symptoms

* * *

Horizontal Discovery fails when discovering Docker Virtualization Application. Discovery logs shows "Failed Exploring CI Pattern. Check Pattern Docker Pattern Log Here":

![Discovery Log](sys_attachment.do?sys_id=66a8682edb02b450e515c22305961979 "Discovery Log")

When you click on the link "Here", Horizontal Discovery Log shows the pattern failed at step "guard against unrunnable commands"

![](sys_attachment.do?sys_id=2aa8682edb02b450e515c2230596197e)

# Release

* * *

From Jakarta

# Cause

* * *

This is due to missing credential privileges being used by Discovery.  For Docker Virtualization discovery we require the credential to be root or the credential should be a member of the docker

group.  This is detailed in our product documentation [here](https://docs.servicenow.com/csh?topicname=c-docker-virtualization.html&version=latest "here") under the section User Privileges. 

# Resolution

* * *

  
Either use a root credential or add the user credential to the docker group by logging into the Linux server targeted by Discovery and running the command "sudo usermod -a -G user\_name docker".

This will add Linux user with name "user\_name" to the group "docker".
