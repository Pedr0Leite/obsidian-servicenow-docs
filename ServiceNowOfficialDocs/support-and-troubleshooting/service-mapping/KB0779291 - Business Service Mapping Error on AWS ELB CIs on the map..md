---
title: "Business Service Mapping Error on AWS ELB CIs on the map."
aliases:
  - KB0779291
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779291
kb_number: KB0779291
last_modified: 2024-04-08
---

## Issue

After the load balancer service mapping scan runs nightly on a business service that has AWS ELB services on it, they have the following error:

"Missing pattern-based outgoing connections from load balancer. Please check the correctness of the incoming connection."

If you debug the pattern it works fine. 

If you resume discovery for just that connection the error goes away, but after nightly scan it comes back. 

If you see the discovery log, in one of the steps that used the AWS API you will see an error like the following:

"Status: 400 Server response: Response: HttpResponseProxy{HTTP/1.1 400 Bad Request"

## Resolution

Change the following system property to 20 from 100:

"sa.rediscovery.batch\_size"  
  
We changed it from 100 to 20. This will batch the probes into 20 at a time so we do not make as many requests in bulk to AWS API which is causing the timeout.
