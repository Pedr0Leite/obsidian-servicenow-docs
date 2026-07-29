---
title: "How to resolve SuccessFactors integration error: InvalidPathException could not find path in stream"
aliases:
  - KB0995497
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995497
kb_number: KB0995497
last_modified: 2026-05-03
---

## How to resolve SuccessFactors integration error: InvalidPathException could not find path in stream

  

### Issue

Resolve an InvalidPathException error that occurs when the SAM - Refresh SuccessFactors Integration Subscriptions scheduled job fails to download user subscriptions.

The following error appears in the system logs:

Operation(Look up Users.page$1.f880df9453d62010f263ddeeff7b12eb) failed with error: java.lang.RuntimeException: com.glide.transform.transformer.exceptions.InvalidPathException: Could not find path in stream: $.d.results  
at com.glide.transform.transformer.TransformerResultIterator.getNextRow(TransformerResultIterator.java:50)  
at com.glide.transform.transformer.TransformerResultIterator.hasNext(TransformerResultIterator.java:65)  
at com.snc.process\_flow.stream.SplittingDatastream.getNextRecord(SplittingDatastream.java:105)  
at com.snc.process\_flow.stream.SplittingDatastream.hasNext(SplittingDatastream.java:90)  
at com.snc.process\_flow.stream.ScriptParserStream.getCo(ScriptParserStream.java:127)

The REST call returns a 400 error with the following response:    
{  
"error" : {  
"code" : "COE\_PROPERTY\_NOT\_FOUND", "message" : {  
"lang" : "en-US", "value" : "\[COE0021\]Invalid property names: User/city. Please check the property name in Admin Center > OData API Data Dictionary or entity metadata. Ensure there were no data model changes that removed this field, and please execute a refresh metadata to ensure the cache is not corrupted."  
}  
}  
}  
  

Example of the 400 error returned by the REST call:

![Example of the 400 error returned by the REST call:](sys_attachment.do?sys_id=3480fb9a472e7298b8a4aa25126d43cb)

### Release

Quebec

### Cause

This error occurs when a property referenced in the integration query is not configured in SuccessFactors. In this case, the "city" property is missing or not available in the SuccessFactors OData API configuration. 

### Resolution

**Option 1: Configure the missing property in SuccessFactors** 

Contact your SuccessFactors administrator to verify that the "city" property is configured and available in the OData API Data Dictionary. 

**Option 2: Remove the missing property from the query**

If the **city** field is not required for your integration, remove it from the API call:

1.  Go to **Flow Designer** and open the **SuccessFactors Download Subscriptions** subflow.
2.  Open the **Look up Users** datastream action.
3.  In the **Query Parameters** field, locate the query string:  
      
    userId,username,defaultFullName,firstName,lastName,gender,email,state,city,nationality,country,businessPhone,status,timeZone,title,hireDate,dateOfBirth,zipCode  
      
    
4.  Remove **city** from the query. The updated query should be:  
      
    userId,username,defaultFullName,firstName,lastName,gender,email,state,nationality,country,businessPhone,status,timeZone,title,hireDate,dateOfBirth,zipCode  
      
    
5.  Select **Save**, then select **Publish**. 
6.  Run the scheduled job **SAM - Refresh SuccessFactors Integration Subscriptions**.  
     

![Image of Look up users screen in Flow Action](sys_attachment.do?sys_id=7880fb9a472e7298b8a4aa25126d4394)

**To revert changes**

If you need to revert this modification:

1.  Go to the Update Versions \[sys\_update\_version\] table.
2.  Find the record for the modified Look up Users action.
3.  Revert to the **Store Application: SuccessFactors Spoke** update set.
