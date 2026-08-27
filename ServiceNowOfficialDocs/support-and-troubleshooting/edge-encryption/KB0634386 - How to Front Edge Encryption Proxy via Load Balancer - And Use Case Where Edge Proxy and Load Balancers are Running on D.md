---
title: "How to Front Edge Encryption Proxy via Load Balancer - And Use Case Where Edge Proxy and Load Balancers are Running on Different Ports"
aliases:
  - KB0634386
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634386
kb_number: KB0634386
last_modified: 2024-04-07
---

## How to Front Edge Encryption Proxy via Load Balancer - And Use Case Where Edge Proxy and Load Balancers are Running on Different Ports

  

### Issue

How to front Edge proxies with a load balancer | Additional Configuration Steps

  
  

# Description

* * *

Several settings need to be in place in order to successfully put a load balancer in front of one or multiple Edge proxies for Edge Encryption. This article describes settings that are in addition to what the product documentation describes.

1.  The load balancer needs to terminate SSL, that is, it also has to have its own trusted certificate that the user's browsers will accept.
    
2.  The load balancer should be listening on 443 (the port that the instance is contacted through), and communicate to the proxies on port 80 (the https or http port of the Edge Encryption proxy, preferably port 80).
    
3.  The edgeencryption.proxy.host setting in the edgeencryption.properties has to be set to the load balancer FQDN and not the proxy server FQDN.
    

**Note**: How to set up each of these items differs between load balancers, but the configuration mentioned in this article has been set up by the network teams of multiple customers successfully.

# Additional Use Case

* * *

When the Edge proxy and load balancers are running on different ports, connecting to the Edge proxy through the load balancer results in a blank page when performing any operation.

## Steps to Reproduce

1.  Start the proxy on a port (say 8082).
    
2.  Have a load balancer on a different machine listening on a different port (say 443).
    
3.  Point the load balancer to the Edge proxy.
    
4.  Connect using a browser through the <load-balancer>:443 URL.
    
    Note that a blank page is rendered as soon as any operation is performed.
    

# Solutions

* * *

There are two possible solutions for this issue:

-   Have the load balancer and Edge proxy listen on the same port number on respective hosts.
    
-   Have an iRule on F5 that intercepts server-set redirect responses and removes the server's port from the Location header.
    
    A similar issue can be found on the [F5 site](https://devcentral.f5.com/questions/vip-address-gets-member-port-appended-in-url). It includes the following iRule:
    
    \------------------------------ iRule -----------------------------------------
    when HTTP\_RESPONSE {
    # Check whether server response is a redirect
    if { \[HTTP::header is\_redirect\]} {
    # Log original and updated values
    log local0. "Original Location header value: \[HTTP::header value Location\],\\
    updated: \[string map ":\[TCP::remote\_port\]/ /" \[HTTP::header value Location\]\]"
    # Do the update, replacing :8080/ with / (where 8080 is the pool member's port)
    HTTP::header replace Location \[string map ":\[TCP::remote\_port\]/ /" \[HTTP::header value Location\]\]
    }
    }
    # Note: You could replace the current mapping, ":\[TCP::remote\_port\]/ /", with the VIP port if the virtual server is on a non-standard port:
    # Replace selected pool member's port with the VIP port
    HTTP::header replace Location \[string map ":\[LB::server port\]/ :\[clientside {TCP::local\_port}\]/" \[HTTP::header value Location\]\]
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
