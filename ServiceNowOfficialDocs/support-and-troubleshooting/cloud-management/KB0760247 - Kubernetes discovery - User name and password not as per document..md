---
title: "Kubernetes discovery - User name and password not as per document."
aliases:
  - KB0760247
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760247
kb_number: KB0760247
last_modified: 2024-04-08
---

## Kubernetes discovery - User name and password not as per document.

  

### Issue

-   ServiceNow offers support for Kubernetes discovery and the procedure is explained in [Kubernetes discovery](https://docs.servicenow.com/csh?topicname=kubernetes-discovery.html&version=latest "Kubernetes discovery") document. However, even after following the steps, the Kubernetes resources cannot be discovered. 
-   The problem observed here is with Credential configuration. The expected outcome of  command is as below.

  
![Locate the lines that contain information on password and username.](https://docs.servicenow.com/)

-   However, on executing the command, the output we see is as below.

  
![](sys_attachment.do?sys_id=6dd52738db0078d022e0fb24399619dd)

-   This article will demonstrate on the investigations and probable use cases, hence in future, if a similar error occurs then this can be one of the cause and worth trying to fix.

### Cause

-   This issue with the unsupported Kubernetes configuration.

### Resolution

-   ServiceNow Kubernetes Discovery supports credential configuration using Username and password as well as using bearer token. Thus to make it work, we need to have valid UserName details.  
-   In order to get the username and password details, we recommend using **_kubectl config view_** command to get the correct user details as per the screenshot in the document.
-   If, in an environment, **_kubectl config view_** command is not showing the expected details then need to get the "supported" command from Kubernetes admin to fetch username and password details.
