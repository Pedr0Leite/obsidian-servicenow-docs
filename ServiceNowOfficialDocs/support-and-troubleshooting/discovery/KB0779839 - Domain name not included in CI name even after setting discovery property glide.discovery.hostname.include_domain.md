---
title: "Domain name not included in CI name even after setting discovery property \"glide.discovery.hostname.include_domain\""
aliases:
  - KB0779839
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779839
kb_number: KB0779839
last_modified: 2024-04-07
---

## Domain name not included in CI name even after setting discovery property "glide.discovery.hostname.include\_domain"

  

### Issue

**The domain name is not included with CI name for AIX Server even after setting the discovery property  “glide.discovery.hostname.include\_domain”.**

### Release

**Madrid Release**

### Cause

The issue is with the discovery property “glide.discovery.hostname.ssh\_trusted” enabled. For that, we pull the result of command “uname -a” output, which has NO idea of the domain the hosts DNS is a part of. By including include domain in the hostname, they cancel each other out, with SSH trusted name source as the priority.  Hence there is no use of setting the property "**glide.discovery.hostname.include\_domain"** to true along with the property **"glide.discovery.hostname.ssh\_trusted".**

### Resolution

Disable the discovery property “**glide.discovery.hostname.ssh\_trusted**” and enable only the property **“glide.discovery.hostname.include\_domain”.**

\- Login to the instance

\- Type “Discovery Definition” in Application Navigator

\- Open Discovery Definition -> properties

\- Uncheck “SSH is trusted host name source” and Save it
