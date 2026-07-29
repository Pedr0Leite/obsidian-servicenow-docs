---
title: "How to test AWS REST API using POSTMAN"
aliases:
  - KB0782183
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782183
kb_number: KB0782183
last_modified: 2025-06-23
---

## How to test AWS REST API using POSTMAN

  

### Summary

In Cloud Service Account discovery, sometimes few of the attributes of cloud resources not updated in CMDB.  This article explains how to test AWS REST API using POSTMAN.  In this example, I have taken image resource (Amazon Machine Image) for testing.

### Release

All

### Instructions

1.  Download and Install POSTMAN from the link "[Download POSTMAN"](https://www.getpostman.com/downloads/ "Download POSTMAN")
2.  Launch Postman  
      
              ![](sys_attachment.do?sys_id=7e5550491b25c058d01143f6fe4bcb47)  
      
      
    
3.  Click New on Top Left and choose “Request”  
      
      
             ![](sys_attachment.do?sys_id=7a5550491b25c058d01143f6fe4bcb04)  
      
    
4.  Enter “Request Name” and type any name in “Select a collection or folder to save to”  
      
      
    1.  Create Collection
    2.  Save  
          
        ![](sys_attachment.do?sys_id=be5550491b25c058d01143f6fe4bcb06)  
          
          
        
5.  Choose the operation “GET” and enter below URL  
      
    [https://ec2.amazonaws.com](https://ec2.amazonaws.com)  
      
    
6.  Go to “Params” tab and enter below query params  
      
    -   **Key-Value  
          
        **
        -   Action                         DescribeImages
        -   Version                      2016-11-15
        -   ImageId                      <give the AMI object id >  
              
            ![](sys_attachment.do?sys_id=f25550491b25c058d01143f6fe4bcb49)  
              
              
            
7.  Go to the “Authorization” tab and choose Type “AWS Signature” and enter below information  
      
    1.  \- AccessKey
    2.  \- SecretKey
    3.  \- AWS Region (Ex: us-east-1 i.e image location)
    4.  \- Service Name (Ex: ec2)  
          
          
        
8.  Click Send request  
      
                        ![](sys_attachment.do?sys_id=7a5550491b25c058d01143f6fe4bcb4a)  
      
      
    
9.  On successful execution, you will find the status code as “200” and the output of the REST API is available in the body.  
      
      
    1.  ![](sys_attachment.do?sys_id=365550491b25c058d01143f6fe4bcb08)
