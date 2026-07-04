---
title: "Table API FAQs"
aliases:
  - KB0534905
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0534905
kb_number: KB0534905
last_modified: 2026-04-30
---

## Table API FAQs

  

### Issue

The following Frequently Asked Questions are related to the ServiceNow REST Table API.

### Release

All Releases

### Resolution

### FAQs

1.  **Why are my values different in the UI compared to the values I use for POST or PUT?  
    **The UI shows the display value of actual data in the database, which is manipulated data. The REST API inserts and updates values as given in requests and they can be different from what you see. You can force the REST API to treat input values as display values by passing the sysparm\_input\_display\_value request parameter.  
     
2.  **How does _sysparm\_input\_display\_value_ actually affect my input request?  
    **Depending on the different types of fields, we try to resolve the input to get actual valid values to be inserted into the database. For example, if you send the display name for a reference field, the system gets the sys\_id for the value in the request and stores it in the database. For date and time fields, when this parameter is true the date and time value is inserted adjusted for the current user's timezone. When false, the date and time value is inserted using the UTC timezone.
3.  **What does sysparm\_query return? How can I get an encoded query for my requirement?  
    **The sysparm\_query parameter returns an encoded query that can be interpreted by ServiceNow. To get a properly encoded query, you can use a UI filter.  
      
    
4.  **What happens if I supply multiple records in POST, PUT, and PATCH operations?  
    **Multiple records are not supported. If you give multiple records, only the first record gets worked on and the rest of them are ignored.  
      
    
5.  **Why are POST, PUT, and PATCH not working for a Database view?  
    **Database views are read-only; you can't insert or update records into the Database view.  
      
    
6.  **How is the latest version different from v1?**  
    We versioned the API for backward compatibility. The latest always points to the latest version/implementation, which is v1 for Eureka.  
     
7.  **How can I filter my response results? How can I get an encoded query for my requirement?  
    **The sysparm\_query parameter takes in an encoded query that can be interpreted by the ServiceNow platform. To get a properly encoded query for your requirement, you can use a UI filter.  
     
8.  **Why doesn't my response have fields specified in the view parameter?**  
    There are multiple reasons. For example, a request parameter name/value or sysparm\_fields parameter may be specified with a typo. Also, there is a chance you don't have access to those fields due to ACL restrictions and those fields are masked in the response.  
     
9.  **What happens if I send a PUT/PATCH request with an id of a resource/record that does not exist? 404 Not Found or Upsert?**  
    A **404 Not found** exception.  
     
10.  **Will there be support for Import Set Services using the REST API, with access to the Response object?**  
     Yes and No. For the Eureka release, import sets are the same as other tables. You can insert a record and you will get a response with data in that table, but nothing about transformation results.  
      
11.  **What is the difference between PUT and PATCH?**  
     In the REST world, PUT and PATCH have different semantics. PUT means replace the entire resource with given data (so null out fields if they are not provided in the request), while PATCH means replace only specified fields.  For the Table API, however, PUT and PATCH mean the same thing.  PUT and PATCH modify only the fields specified in the request.  
      
12.  **How are Display Values vs. Actual Values treated in the REST API?  
     **In ServiceNow, there is the concept of display values and actual values. The actual value represents the raw value in the database, whereas the display value represents the user-understandable value that is usually shown in the UI.  
     
     For some fields, there are significant differences in how these values display in the UI vs. in the database.  For example:
     
       
     -   **Encrypted text:** The database value is encrypted, while the displayed value is unencrypted based on the user's encryption context.
     -   **Reference fields:** The database value is sys\_id, but the display value is a display field of a referenced record.
     -   **Date fields:** The database value is in UTC format, while the display value is based on the user's time zone.
     -   **Choice fields:** The database value may be a number, but the display value will be more descriptive.  
           
         There are other fields where the actual value and display value vary. Display values are manipulated based on the actual value in the database and user or system settings and preferences.
13.  **Related question: why is the default setting for the _sysparm\_input\_display\_value_ parameter false, if the recommended setting is true?   Why does the user need to provide this parameter?**  
     This is for consistency.  During data retrieval, you get actual values, and again, to be consistent, input values are treated as actual values during data manipulation.
     
14.  **How is REST different from other APIs, such as SOAP and JSONv2?**  
     SOAP supports the display value on data retrieval, but not on data manipulation. For SOAP insert/update operations, input values are always treated as display values and are manipulated.
     
     JSONv2 also supports the display value on data retrieval, but not on data manipulation. For JSONv2 insert/update operations, input values are always treated as actual values and are not manipulated.  
       
     With REST, you get the best of both. Users have more control over how they get data in and out of the system.
     
15.  **Does REST support sorting and Orderby?**  
     Yes.  You can specify Orderby in an encoded query to sort the results.  See the sysparm\_query parameter in [Table API](https://docs.servicenow.com/csh?topicname=c_TableAPI.html&version=latest "Table API").
     
16.  **Can I empty out values for fields using REST?**  
     Yes, By passing empty strings for values, you can nullify or empty the field's values. For example, sending {"short description":""} will empty the **short\_description** field for the specified record.
     
17.  **How are currency fields handled by the Table API?**
     
     When performing a REST request, returned currency values are converted to the local currency based on the user’s **Locale.** When inserting data, no conversion is performed. This behavior applies to fields of the types **Currency** or **Price**.
     
     For example, if a user in the UK locale queries records with currency values in USD, the returned values are converted to GBP. However, if this user adds a new record with the currency field value in GBP, the value is stored in GBP without being converted to USD. This GBP value will be displayed in USD if queried by a user in the US locale.
