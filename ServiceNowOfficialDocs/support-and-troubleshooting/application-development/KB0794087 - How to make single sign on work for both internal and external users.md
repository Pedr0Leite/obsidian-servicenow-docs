---
title: "How to make single sign on work for both internal and external users"
aliases:
  - KB0794087
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794087
kb_number: KB0794087
last_modified: 2025-11-12
---

## How to make single sign on work for both internal and external users

  

### Issue

There is a requirement to make Single Sign On work for internal users within your company network and users accessing the instance externally from outside of your company network.

### Release

ALL

### Resolution

Navigate to sso\_properties.LIST table from filter navigator. 

Find the corresponding identity provider record configured on your instance. 

Please ensure below configurations are in place on the identity provider record on the instance:

1) 'Create AuthnContextClass' check box field on identity provider record should be unchecked. You can find this filed under 'Advanced' tab on identity provider record. 

2) 'AuthnContextClassRef Method' field should have a value of urn:federation:authentication:windows. You can find this field under 'Advanced' tab on identity provider record as well.
