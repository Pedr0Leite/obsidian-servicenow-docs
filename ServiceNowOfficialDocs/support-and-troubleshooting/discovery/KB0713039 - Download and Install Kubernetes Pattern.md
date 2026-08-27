---
title: "Download and Install Kubernetes Pattern"
aliases:
  - KB0713039
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713039
kb_number: KB0713039
last_modified: 2025-01-03
---

## Download and Install Kubernetes Pattern

  

### Issue

# Description

* * *

Download and Install **Kubernetes** Pattern

# Applicable Versions

* * *

Jakarta and newer

# Procedure

* * *

## **Downloading the Kubernetes Pattern**

1.  Login to the [ServiceNow App Store](https://store.servicenow.com/ "ServiceNow App Store") using your HI credentials.
2.  Find "**Discovery and Service Mapping Patterns**" using the search capabilities  
      
    ![](sys_attachment.do?sys_id=90996822db42b450e515c223059619ab)  
      
      
    
3.  Click on"Request Install"  
      
    ![](sys_attachment.do?sys_id=58996822db42b450e515c223059619d5)  
      
      
    
4.  Provide the Instance name where you want to install the pattern and click on "Validate Instance"
5.  Once validated, fill the "Reason for Request"
6.  Click on "**Request**"
7.  Wait for the  screen to pop "Your Request is auto Approved"  
      
    ![](sys_attachment.do?sys_id=98996822db42b450e515c223059619da)  
      
      
    
8.  Verify Request history, it will populate the instances where the pattern is installed, the new instance name also should be available.

## **Installing the Kubernetes Pattern** 

1.  In your instance, navigate to **System Applications > Applications**
2.  Select **Downloads** from the top menu
3.  "Discovery and Service Mapping Patterns" should be available for **"Install"**
4.  Click "**Install**"   
      
    ![](sys_attachment.do?sys_id=2099a822db42b450e515c22305961905)  
      
    

**Verifying Kubernetes Pattern**

1.  Navigate to **Pattern Designer > Discovery Patterns**
    -   **OR** sn\_discovery\_patterns\_list.do
    -   Search in **"Name"** field for **"Kubernetes"**
2.  Now we see the pattern installed successfully with all available parameters.   
      
    

# Additional Information

* * *

-   [Kubernetes discovery](https://docs.servicenow.com/csh?topicname=kubernetes-discovery.html&version=latest "Kubernetes discovery")
-   [Kubernetes event discovery](https://docs.servicenow.com/csh?topicname=kubernetes-event-discovery.html&version=latest "Kubernetes event discovery")
