---
title: "CMP Troubleshooting using Cloud Orchestration Trail and Cloud API Trail "
aliases:
  - KB0686737
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686737
kb_number: KB0686737
last_modified: 2025-08-25
---

## CMP Troubleshooting using Cloud Orchestration Trail and Cloud API Trail

  

### Issue

# CMP Process Overview & Troubleshooting

Find below how a particular Catalog Request is fulfilled in the CMP Processes. Understanding this process flow will help to troubleshoot issues that customers face when they see unexpected results. 

![](sys_attachment.do?sys_id=c82ff026db0ab450e515c223059619f3)

While troubleshooting a particular request you should be able to follow the above process flow using the Cloud Orchestration Trail and the Cloud API trail. 

**Navigate to the Cloud Admin Portal --> Operate --> Trails**

Each of the stage in the above process flow has corresponding log messages in the Cloud Orchestration Trail and Cloud API Trail.

The Orchestration Trail kick starts soon after the order is submitted. You should see thins in Orchestration Logs. 

Requests to Provision or Discovery a resource go to the MID Server. The MID Server talks to the Cloud Providing Service/Data Center using the Cloud API. For logs related to CAPI use the CPI trail. In other words when the request has gone out of the ServiceNow instance, use the CAPI trail to follow the request. 

In other words the following stages are logged in the **Cloud Orchestration Trail:**  
Catalog Item Request  
Workflow and Policy Execution  
Cloud Orchestration  
  

The last stage is logged in the **Cloud API Trail** 

**How To Use these Trails:**

-   Use the Request Item Field and show matching records for the Request that corresponds to the one that you are trying to follow. 
-   Use the Number field to sort the records to see the messages in the correct sequence (do not use the Created field for the same)
-   To check what data has been sent to the external data center you will need to click on the record in the Cloud API trail. It will indicate the MID server that was used and the data that was routed to the MID Server. Open the route\_data.  The Log value entry is the input data that is sent. 
-   You can check route\_status for error. Once you open this entry , the log value will show you the error message returned 
-   error\_detail shows you the detail of the error.  If you create an INT Task for the development team please include these details for the Developer. Bear in mind that some CAPI are implemented in java and few are Java script REST APIs. 

**Some Screen Shots Displaying the above information:**

![](sys_attachment.do?sys_id=8c2ff026db0ab450e515c223059619f8)

![](sys_attachment.do?sys_id=002ff026db0ab450e515c223059619fe)

![](sys_attachment.do?sys_id=802f3426db0ab450e515c22305961903)

If you need to check on the Cloud API Implementation, navigate to Design--> Cloud API    
Find the API for which you want to check implementation and open the record using the information (i) button on the record  
Check the Script Type and Request Script fields 

If the Script Type is null and Request Script field is empty then it is assumed that this is a java implementation

For Azure for example the APIs are scripted and you can see the following Create Node example below:

![](sys_attachment.do?sys_id=042f3426db0ab450e515c22305961908)

If there are any issues you should be looking into the script to debug and check if the required parameters were passed correctly or not.
