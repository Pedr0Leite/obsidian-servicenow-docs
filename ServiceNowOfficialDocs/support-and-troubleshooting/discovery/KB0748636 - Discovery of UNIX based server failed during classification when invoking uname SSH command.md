---
title: "Discovery of UNIX based server failed during classification when invoking uname SSH command"
aliases:
  - KB0748636
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748636
kb_number: KB0748636
last_modified: 2024-04-07
---

## Discovery of UNIX based server failed during classification when invoking uname SSH command

  

### Issue

# Symptoms

Discovery of UNIX based server fails during classification when invoking uname SSH command. Symptoms include seeing one of the following string in the ECC queue during classification phase:

\===Service-Now EOO Marker===

\===Service-Now Exit Status Prefix===

\===Service-Now Exit Status Suffix===

\===Service-Now\_Password\_Prompt===

# Release

Instances upgraded from prior to Geneva

# Cause

J2SSH is used on the mid server. In order for mid server to connect to target servers, it needs a ssh client. In Helsinki and older releases, there are two ssh clients in mid sever, J2SSH and SNC\_SSH. J2SSH is not supported since Geneva. New instances should use SNC\_SSH.

# Resolution

Enable the ServiceNowSSH Client by adding the following mid server property:

<table style="width: 100%; border-collapse: collapse; border-style: none;" border="1"><tbody><tr><td style="width: 50%;">mid.ssh.use_snc</td><td style="width: 50%;">true</td></tr></tbody></table>

# Additional Information

[MID Server parameters](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "MID Server parameters")
