---
title: "dns_domain is not being populated for some CIs"
aliases:
  - KB0714693
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714693
kb_number: KB0714693
last_modified: 2024-04-07
---

## dns\_domain is not being populated for some CIs

  

### Issue

## Description

"dns\_domain" field is not being updated during discovery for some CIs.

## Probable Cause:

The dns\_domain should get updated by the DNS port probe (port 53) sent within the Shazzam probe. So, if the reverse DNS of the CI's IP is not mapping to the domain name of this CI in the result of the Shazzam probe, then this field will not be updated.

## Resolution:

Update the DNS server to add a reverse DNS record for those CIs.
