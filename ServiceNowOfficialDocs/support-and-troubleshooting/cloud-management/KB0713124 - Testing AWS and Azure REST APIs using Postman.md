---
title: "Testing AWS and Azure REST APIs using Postman"
aliases:
  - KB0713124
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713124
kb_number: KB0713124
last_modified: 2026-05-20
---

## Testing AWS and Azure REST APIs using Postman

  

### Issue

There are several reasons to use Postman to test REST APIs: 

-   Confirming whether the MID server can reach third-party services such as Azure or AWS
-   Verifying the data structure that ServiceNow receives from third-party services
-   Confirming that the expected values are being sent and received over REST

### Release

All Supported Releases

### Resolution

### Azure

1.  [Download and install Postman](https://www.getpostman.com/apps "Download and install Postman") (postman.com)
2.  [Click Here to download the Azure Postman collection](https://app.getpostman.com/run-collection/8088015fa8e6df7d59ed#?env%5BAzure%20REST%5D=W3siZW5hYmxlZCI6dHJ1ZSwia2V5IjoidGVuYW50SWQiLCJ2YWx1ZSI6IiJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50SWQiLCJ2YWx1ZSI6IiJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50U2VjcmV0IiwidmFsdWUiOiIifSx7ImVuYWJsZWQiOnRydWUsImtleSI6InJlc291cmNlIiwidmFsdWUiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5Ijoic3Vic2NyaXB0aW9uSWQiLCJ2YWx1ZSI6IiJ9LHsia2V5IjoiYWN0aW9uIiwidmFsdWUiOiIiLCJkZXNjcmlwdGlvbiI6IiIsInR5cGUiOiJ0ZXh0IiwiZW5hYmxlZCI6dHJ1ZX1d "Click Here to download the Azure Postman collection") (getpostman.com)
3.  Make sure the Azure REST environment is active, then select Manage Environment using the settings cog.  
      
    ![Azure 'My Workspace'](sys_attachment.do?sys_id=76a14fd847c94b5cac90112a636d43ef)
4.  Set your environment variables in the "Current Value" column:  
      
    ![Azure 'Manage Environments'](sys_attachment.do?sys_id=32a14fd847c94b5cac90112a636d43f4)
5.  Variables:  
    1.  tenantId: Azure Dashboard > Azure Active Directory > Manage/Properties > Copy "Directory ID"
    2.  clientId: Azure Dashboard > Azure Active Directory > App Registrations > Select/Create > Copy "Application ID"
    3.  clientSecret: Select App Registration > Settings > Keys > Create new "Passwords" > Copy Secret Key "Value"
    4.  subscriptionId: Azure Dashboard > Subscriptions > Select > Overview > Copy "Subscription ID"
    5.  action: API call that you wish to make (e.g: resourceGroups?api-version=2014-04-01)
6.  After setting the variables, run the Get AAD Token step to obtain the Bearer token for API authentication.
7.  Run the Azure REST API Request action to receive a response from Azure.  
      
    ![Azure REST API Request](sys_attachment.do?sys_id=baa14fd847c94b5cac90112a636d43f8)  
      
    
8.  Some modifications may be required — such as the HTTP action or the URL — to make specific API requests.  Refer to the "[Azure Resource Explorer](resources.azure.com)" for further details on how the API call should be formatted.

### AWS

1.  [Download and install Postman](https://www.getpostman.com/apps "Download and install Postman")
2.  [Click Here to download the AWS Postman collection](https://app.getpostman.com/run-collection/62b7df2540c21664612b#?env%5BAWS%20REST%5D=W3sia2V5IjoiYWNjZXNzS2V5IiwidmFsdWUiOiIiLCJkZXNjcmlwdGlvbiI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5Ijoic2VjcmV0S2V5IiwidmFsdWUiOiIiLCJkZXNjcmlwdGlvbiI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiY29udGVudFR5cGUiLCJ2YWx1ZSI6ImFwcGxpY2F0aW9uL2pzb24iLCJkZXNjcmlwdGlvbiI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5Ijoic2VydmljZSIsInZhbHVlIjoiIiwiZGVzY3JpcHRpb24iOiIiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6InJlZ2lvbiIsInZhbHVlIjoiIiwiZGVzY3JpcHRpb24iOiIiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6InZlcnNpb24iLCJ2YWx1ZSI6IiZWZXJzaW9uPTIwMTYtMTEtMTUiLCJkZXNjcmlwdGlvbiI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiYWN0aW9uIiwidmFsdWUiOiIiLCJkZXNjcmlwdGlvbiI6IiIsImVuYWJsZWQiOnRydWV9XQ== "Click Here to download the AWS Postman collection")
3.  Make sure the AWS REST environment is active, then select Manage Environment using the settings cog.  
      
    ![AWS REST API Request tab in Postman](sys_attachment.do?sys_id=aea10fd847c94b5cac90112a636d43c2)  
      
    
4.  Set your environment variables in the "Current Value" column  
      
    ![AWS Manage Environments](sys_attachment.do?sys_id=6aa14fd847c94b5cac90112a636d4382)
5.  Variables  
    1.  accessKey: Programmatic API access key from configured IAM user
    2.  secretKey: Programmatic API secret key from configured IAM user
    3.  contentType: Generic JSON format since Postman's default value will cause errors
    4.  service: Name of the AWS API service you're attempting to query
    5.  region: Optional. Specific region for the query, if desired
    6.  version: Enforce versioning for V4 signing protocol, which is what Postman will be using for authentication
    7.  action: API call you're wanting to make
6.  If done correctly, after filling out these variables you should be able to get a response by clicking "Send"  
      
    ![AWS REST API Request](sys_attachment.do?sys_id=f2a14fd847c94b5cac90112a636d4387)  
      
    
7.  Note that you may need to change the HTTP request type (GET, POST, PUT) depending on the desired API call. You may also need to modify the URL to accommodate additional requirements depending on the API call (e.g: Buckets for S3 requests). You can reference the API guides in Additional Information for more details on how the API call should be formatted.

### Related Links

-   [Identify AWS resources with Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html#genref-aws-service-namespaces "Identify AWS resources with Amazon Resource Names (ARNs)")
-   [API references](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-ref.html "API references")
-   [Azure REST API Browser](https://docs.microsoft.com/en-us/rest/api/?view=Azure "Azure REST API Browser")
-   [Azure Resource Explorer](https://resources.azure.com/ "Azure Resource Explorer")
