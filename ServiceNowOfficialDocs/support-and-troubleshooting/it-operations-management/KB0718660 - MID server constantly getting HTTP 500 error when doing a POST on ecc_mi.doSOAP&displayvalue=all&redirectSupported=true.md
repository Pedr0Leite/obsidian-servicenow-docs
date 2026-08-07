---
title: "MID server constantly getting HTTP 500 error when doing a POST on /ecc_mi.do?SOAP&displayvalue=all&redirectSupported=true"
aliases:
  - KB0718660
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718660
kb_number: KB0718660
last_modified: 2025-01-02
---

## Issue

MID server constantly getting HTTP 500 error when doing a POST on /ecc\_mi.do?SOAP&displayvalue=all&redirectSupported=true

## Resolution

Add MID Server Property  or MID Server Configuration parameter "disable\_monitors" with value "true". Please refer to the links below:

[Create MID Server Property](https://docs.servicenow.com/csh?topicname=r_MIDServerProperties.html&version=latest "Create MID Server Property")

[Add MID Server Configuration Parameter](https://docs.servicenow.com/csh?topicname=mid-server-parameters.html&version=latest "Add MID Server Configuration Parameter")
