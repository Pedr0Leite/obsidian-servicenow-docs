---
title: "Discovery Error - You cannot call a method on a null-valued expression."
aliases:
  - KB0723716
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723716
kb_number: KB0723716
last_modified: 2024-04-07
---

## Discovery Error - You cannot call a method on a null-valued expression.

  

### Issue

* * *

-   On executing discovery for Windows devices, it fails to classify the devices and throws an error.  
    
-   The issue is about devices not getting classified. When discovery tries to discover a device, it throws a warning during classification steps and set the status of discovery to complete. This article will demonstrate on the investigations and probable use cases, hence in future, if discovery fails with the same error, then this can be one of the cause and worth trying to fix.

Steps to Reproduce  

* * *

-   Connect to ServiceNow instance.
-   Initiate quick discovery or scheduled discovery for Windows devices.
-   validate the WMI Classify probe.

Error  

* * *

-   Discovery fails to classify the device and throws the error as below  
      
     **_Active, couldn't classify: No WMI connection, now finished - you cannot call a method on a null-valued expression._**

Cause  

* * *

-   Servicenow sends below query payload to fetch data as a part of WMI Classify step.  
    `<parameter name="WMI_FetchData" value="root\virtualization\v2\Msvm_ComputerSystem.Name,HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Tcpip/Parameters/Domain,   ``HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Tcpip/Parameters/Hostname,root\MSCluster\MSCluster_Resource.PrivateProperties,root\MSCluster\MSCluster_Resource.Name,   root\MSCluster\MSCluster_Node.Name,root\MSCluster\MSCluster_Cluster.Name,root\MSCluster\MSCluster_ClusterToResource.GroupComponent,root\MSCluster\MSCluster_ClusterToResource.PartComponent,   root\MSCluster\MSCluster_ClusterToNode.Antecedent,root\MSCluster\MSCluster_ClusterToNode.Dependent,root\virtualization\Msvm_ComputerSystem.Name,   root\MSCluster\MSCluster_Resource.Type,Win32_ComputerSystem.Domain,Win32_ComputerSystem.Name,Win32_OperatingSystem.Caption,Win32_OperatingSystem.Version"/>`  
      
    
-   Below are the 2 parameters for which data the data is found to be missing under registry attributes.   
    `HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Tcpip/Parameters/Domain,    KEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Tcpip/Parameters/Hostname`  
      
    
-   Below screenshot shows the parameters.  
    ![](/sys_attachment.do?sys_id=826a2466db42b450e515c223059619cd)  
    

Resolution  

* * *

-   The missing values for the registry attribute are added for affected devices so that discovery can fetch the required data.  
    
-   After making the change, discovery classifies the device successfully.
