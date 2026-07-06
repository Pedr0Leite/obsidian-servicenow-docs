---
title: "CMP - MID Server selection customization for Cloud Operations"
aliases:
  - KB0749536
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749536
kb_number: KB0749536
last_modified: 2025-08-06
---

## CMP - MID Server selection customization for Cloud Operations

  

### Issue

-   Working with CMPv1 plugin was designed to execute the Cloud Resource Discovery without a MID server and uses APIProxy probes.
-   Starting from the CMPv2 plugin, the Cloud Resource Discovery and Cloud Orchestration are designed to use MID Server.  
      
    -   Refer: [Set up MID Servers to connect Cloud Management](https://docs.servicenow.com/csh?topicname=mid-server-configuration-cloud.html&version=latest "Set up MID Servers to connect Cloud Management")  
          
        
-   The IP based Discovery have availability to select specific MID server while Discovery of the Resources, but, the Cloud Discovery do not have the same 
-   The MID server configured for Cloud Discovery either should have "ALL" in the capabilities or specific Cloud Provider. Example: AWS, AZURE, VMWARE, etc.. 
-   If we have "ALL" in the MID server capabilities, all the Cloud provider discovery can go through, but if we have AWS as capability it means only AWS Cloud Discovery is allowed 
-   ServiceNow recommends having MID capabilities according to the Cloud Vendor rather configuring with "ALL" considering the Load. 

#### **Requirement** 

-   It is observed or necessary to have the Cloud Discovery and Cloud Orchestration operations to go through MID server depending on the environment 
-   As the current Cloud MID selection is random and depending on only the MID Capabilities, the Cloud Discovery and CAPI Operations pass through random MID server
-   User requirement is to have Specific MID server to use for Specific Cloud Vendors for both Discovery and CAPI operations.

### Release

London P\* & Madrid P \*

Instance with  Cloud Management Plugin activated

### Resolution

#### **Methods to select Specific MID for CAPI Operation and Cloud Discovery**

1.  Choose to have individual MID servers for each Cloud Provider and have respective capabilities.  
    Example: Consider the environment requirement have AWS and VMware Cloud Providers, then configure 2 MID servers and in one MID server enable  the capabilities to AWS  only and other have VMWare, so the Cloud Operations will continue to pass the operations  according to the capabilities and use specific MID as per capabilities  
      
    
2.  [CMP - Use MIDOverride Selection Filter](https://support.servicenow.com/kb_view.do?sysparm_article=KB0749539 "CMP - Use MIDOverride Selection Filter")
3.  CAPIMidSelector script include: Please revert this script include to out-of-the-box, starting from "London" release this script include is depreciated and should not be used.
4.  [CMP - Configure CloudMidSelectionApi](https://support.servicenow.com/kb_view.do?sysparm_article=KB0749543 "CMP - Configure CloudMidSelectionApi")

### Related Links

[How to configure a web proxy to allow MID server to connect to Azure / AWS in Cloud Management (CMPv2)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0679023 "How to configure a web proxy to allow MID server to connect to Azure / AWS in Cloud Management (CMPv2)  306 views") 

[Selecting Particular MID for Cloud discovery and Provisioning.](https://community.servicenow.com/community?id=community_question&sys_id=fed56e58db7faf00fece0b55ca961988 "Selecting Particular MID for Cloud discovery and Provisioning.")

[CMP request not routed to appropriate MID Server](https://support.servicenow.com/kb_view.do?sysparm_article=KB0634678 "CMP request not routed to appropriate MID Server")
