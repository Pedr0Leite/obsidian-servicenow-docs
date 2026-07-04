---
title: "Relationship between Business Rules and Access Control Rules (ACLs)"
aliases:
  - KB0656366
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656366
kb_number: KB0656366
last_modified: 2026-06-27
---

## Relationship between Business Rules and Access Control Rules (ACLs)

  

### Issue

Business rules are database triggers that apply consistently to records regardless of whether they are accessed through forms, lists, or web services. This is the major difference between business rules and client scripts, which apply only at client side when the form is edited.

Business rules can perform a variety of actions, including the following common types:

-   Changing field values on a form that the user is updating. Field values can be set to specific values available for that field, values copied from other fields, and relative values determined by the user's role.
-   Displaying information messages to the user.
-   Changing values of child tasks based on changes to parent tasks.
-   Preventing users from accessing or modifying certain fields on a form.
-   Aborting the current database transaction. For example, if certain conditions are met, prevent the user from saving the record in the database.
-   Administrators can set field values, create information messages, and abort transactions without writing a script.

A business rule does not honour ACLs until and unless you want them to be honored.

The following testing scenarios illustrate situations where the business rule will honor the ACLs or, based on the functions used, the business rule will not honor ACLs.

1.  Create a table named \_table\_security\_tester.
    
2.  Set up the new table u\_table\_security\_tester.
    
    1.  In the Controls section, check Create access controls.
    2.  Add a new user role: u\_table\_security\_tester\_user.
3.  Create two sys\_dictionary records.
    
    -   u\_active, with the settings true/false, read\_only
    -   u\_change, with the settings string, max length 40
4.  Create an ACL named u\_table\_security\_tester.u\_active/write with the following values:
    
    -   Admin overrides - uncheck
    -   Advanced - check
    -   script: "answer = false;")
5.  Create a business rule with the following settings:
    
    -   Name: Flip active
    -   Table: u\_table\_security\_tester
    -   When: before, Order: 100, inset: true, update: true
    -   Filter Conditions: "Change" "changes"
6.  Script:
    
    (function executeRule(current, previous /\*null when async\*/) {
    var active = !!parseInt(current.getValue("u\_active"));
    current.setValue("u\_active", !active);
    })(current, previous);
    
7.  Create UI Action with the following details:
    
    -   Name: Set Active Flag (GRS)
    -   Table: u\_table\_security\_tester
    -   Order: 100
    -   Active: True
    -   Show insert : True
    -   Show update: True
    -   Form button: True
    -   Script:  
        
        var gr = new GlideRecordSecure("u\_table\_security\_tester");
        gr.get(current.getUniqueValue());
        gr.setValue("u\_change", gs.generateGUID());
        gr.update();
        
8.  Create UI Action with the following details:
    
    -   Name: Set Active Flag (GR)
    -   Table: u\_table\_security\_tester
    -   Order: 100
    -   Active: True
    -   Show insert : True
    -   Show update: True
    -   Form button: True
    -   Script:  
        
        var gr = new GlideRecord("u\_table\_security\_tester");
        gr.get(current.getUniqueValue());
        gr.setValue("u\_change", gs.generateGUID());
        gr.update();
        
9.  Go to/u\_table\_security\_tester\_list.do.
    
10.  Create a record by giving a value test in the Change field.
     
     With the logic that has been established, whenever the value changes in the Change field and the record is saved, the active state should be reversed: true becomes false and false becomes true.
     
     Both UI Actions will generate new GUID that is unique.
     

**Test 1**: for GlideRecord - "Set Active Flag (GR) UI Action"

1.  Open the created record.
2.  Click Set Active Flag (GR) button to indicate that on every click, the value of Active field should change from True to False and False to True.

The business rule "Flip Active" updates the record even though the ACL prevents writing into Active field.

**Test 2**: for GlideRecordSecure - "Set Active Flag (GRS) UI Action":

1.  Open the created record.
2.  Click Set Active Flag (GRS) button, on every click, the value of Active field does not change.

Reason: The business rule "Flip Active" executes in the background (as can be seen with a gs.log statement) but the value is not updated because GlideRecordSecure honors the ACLs. This does not mean that business rules do honor ACLs but that the functions used in regard to business rules is what does the trick. GlideRecordSecure is a class inherited from GlideRecord that performs the same functions as GlideRecord and also enforces ACLS. For more information about the differences between GlideRecord and GlideRecordSecure, see the product documentation topic

[Using GlideRecordSecure](https://docs.servicenow.com/)

**Test 3**: REST API

Access Rest API /$restapi.do.

-   Namespace: now
-   API Table: Table API
-   API Version: latest
-   Select "Modify a record (PUT)"
-   tableName: u\_table\_security\_tester
-   sys\_id: sys\_id of the created record.
-   Request Body --> select field "Change" from the dropdown, and give a new value every time and click "Send"
-   The status code of the response is "200 OK" always, but the field "active" is not actually updated in the record.

Reason: The Business Rule "Flip Active" is executed in the background. When you check with gs.log statements, you can see the value getting updated, but because the Access control prevents the access and the sys\_dictionary record set to readonly for the record at the database, the value will not be updated. The business rule is still executing and will not honor the ACL, but the user who is performing this action using REST API does not have the appropriate access due to ACL restrictions and field being Read Only. 

By default, the REST API uses basic authentication or OAuth to enforce access controls to web resources.

ACLs defined for tables are enforced to restrict access to data.

The user ID that is used for authentication is subject to access control in the same way as an interactive user. Each request requires the proper authentication information. Ensure each request includes an Authorization header with the credentials you want to use. There is no support for inbound mutual authentication.

To allow access to tables without any authentication and authorization, add the table name to sys\_public.list. ACLs defined on tables are still enforced, and you are responsible for deactivating ACLs on tables.

For more information, see the following product documentation topics:

[REST API Security](https://docs.servicenow.com/)

[REST API table access](https://docs.servicenow.com/)

[Table API](https://developer.servicenow.com/app.do#!/rest_api_doc?v=jakarta&id=c_TableAPI)

Business rules apply consistently to records regardless of whether they are accessed through forms, lists, or web services. The results can be seen in the system logs that the value is being updated, but again the update will not happen because user performing the actions through REST API will not have access to do that with access restrictions.

For Inbound SOAP Web Service Security, to enforce basic authentication for the user associated with the instance for each WSDL or SOAP message request, administrators can set the property glide.basicauth.required to true. When enabled, each WSDL and SOAP request must contain an Authorization header as specified in the [Basic Authentication](http://www.w3.org/Protocols/HTTP/1.0/draft-ietf-http-spec.html#BasicAA) protocol. Because web services requests are non-interactive, ServiceNow always requires the Authorization header during a request.

For more information, see the product documentation topic [SOAP Web Service](https://docs.servicenow.com/csh?topicname=c_SOAPWebService.html&version=latest).
