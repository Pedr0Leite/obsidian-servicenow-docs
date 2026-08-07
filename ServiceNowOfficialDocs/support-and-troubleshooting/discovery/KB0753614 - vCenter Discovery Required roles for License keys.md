---
title: "vCenter Discovery Required roles for License keys"
aliases:
  - KB0753614
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753614
kb_number: KB0753614
last_modified: 2024-04-07
---

## vCenter Discovery Required roles for License keys

  

### Issue

# Overview

This article will demonstrate the roles required to Discover the roles required to Vmware License Keys.

# Additional Information

-   As per the document  "**[Discovery for VMware vCenter](https://docs.servicenow.com/csh?topicname=c_DiscoveryForVMwareVCenter.html&version=latest "Discovery for VMware vCenter")**" it is mentioned to have the  "read-only" access for the Vcenter Discovery to gather the required information.

![](/sys_attachment.do?sys_id=271d6862db82b450e515c22305961903)

-   Please refer  "[**Data collected for VMware vCenter Serve**r](https://docs.servicenow.com/csh?topicname=r_VCenterDataCollected.html&version=latest "Data collected for VMware vCenter Server")" to understand the data collected from Vmware Vcenter Discovery with "read-only" access to the credentials
-   While using Software Asset Management or similar tools, it is also required the Vcenter Discovery to gather the information of License Keys (usage) and the "read-only" access  is not sufficient to gather the information of License Keys
-   Below are the additional roles required to the Vmware credentials to populate the License Keys.  
      
    -   **read-only** 
    -   **License Admin** 

# Additional Information

-   Please communicate with Vmware admin to have the Vmware credentials with above-required privileges.
