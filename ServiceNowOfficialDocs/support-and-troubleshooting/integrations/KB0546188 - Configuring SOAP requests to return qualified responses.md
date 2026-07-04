---
title: "Configuring SOAP requests to return qualified responses"
aliases:
  - KB0546188
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546188
kb_number: KB0546188
last_modified: 2026-07-02
---

## Configuring SOAP requests to return qualified responses

  

### Issue

Some web service clients may consider SOAP responses from a ServiceNow instance to be invalid.

### Symptoms

The web service client encounters one of these errors:

-   The SOAP response from the ServiceNow Web service is invalid
-   The SOAP response cannot be parsed
-   The namespace is missing in the SOAP response

### Release

### Cause

By default, response elements in ServiceNow SOAP responses are not qualified. Some web service clients may only accept qualified responses.  
  
All elements within a qualified schema must be associated with a namespace. This association is made by prepending an element with a prefix defined by an xmlns attribute. It is also possible to specify a qualified namespace without a prefix in a qualified schema. This is known as the _default namespace_. All global elements within an unqualified schema must be associated with a namespace, and all child elements must not be associated with a namespace. The _default namespace_ is invalid when used in an unqualified schema.  
  
The following examples show how an element may specify a namespace, or use the default namespace.

-   **Qualified, namespace specified**  
    -   <snow:parent xmlns:snow="https://servicenow.com/snow">  
         <snow:child>I am qualified</snow:child>  
        </snow:parent>
        
-   **Qualified, default namespace**  
    -   <parent xmlns="https://servicenow.com/snow">  
         <child>I am qualified too</child>  
        </parent>
        
-   **Unqualified, namespace specified**  
    -   <snow:parent xmlns:snow="https://servicenow.com/snow">  
         <child>I am unqualified</child>  
        </snow:parent>
        
-   **Unqualified, default namespace (invalid XML)**  
    -   <parent xmlns="https://servicenow.com/snow">  
        <child>I am not a valid XML document</:child>  
        </parent>
        

### Resolution

Perform one of these actions to resolve the issue:

-   Set the system property **glide.wsdl.schema.UnqualifiedElementFormDefault** to **false**. Setting this property to false causes all inbound SOAP traffic to return qualified responses.
-   Include the request parameter elementFormDefault=qualified in the request URI. For example, use **<instance>.service-now.com/<table\_name>.do?WSDL&elementFormDefault=qualified** to obtain a qualified WSDL, or use **<instance>.service-now.com/<table\_name>.do?SOAP&elementFormDefault=qualified** to obtain a qualified response when querying a table

For more information, see the "**Setting Namespace Requirements**" section in [Direct Web Services](https://docs.servicenow.com/csh?topicname=c_DirectWebServices.html&version=latest "Direct Web Services").

### Related Links

[Direct Web Services documentation on ServiceNow docs](https://docs.servicenow.com/csh?topicname=c_DirectWebServices.html&version=latest) 

For more information on qualified and unqualified responses, refer to these document: [Oracle namespaces](http://www.oracle.com/technetwork/articles/srivastava-namespaces-092580.html "Oracle namespaces")
