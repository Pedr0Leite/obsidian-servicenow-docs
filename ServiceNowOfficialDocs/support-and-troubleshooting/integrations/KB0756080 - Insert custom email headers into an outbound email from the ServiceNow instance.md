---
title: "Insert custom email headers into an outbound email from the ServiceNow instance"
aliases:
  - KB0756080
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756080
kb_number: KB0756080
last_modified: 2026-03-04
---

## Insert custom email headers into an outbound email from the ServiceNow instance

  

Use a business rule to insert custom email headers into an outbound email generated from the default ServiceNow mail infrastructure instance. A business rule is a server-side script that runs when a record is displayed, inserted, updated, or deleted, or when a table is queried.

For details on business rules and complete field definitions, see the product documentation, [Classic business rules.](https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/script/business-rules/concept/c_BusinessRules.html)

**Note:** If your instance uses your organization's own mail server or a hosted service such as Office 365, set up a rule using your mail server software or service to add the custom header. 

### Create the business rule

Select or complete the following options: 

-   **Name**: Add Custom Email Headers (or a name of your choosing)
-   **Table:** Email \[sys\_email\]
-   **When to run**: Before  
    -   Select **Insert**
    -   Select **Update**
-   **Order**: 100
-   **Advanced**   
    -   Use the following script as an example (replace **X-MyCustomHeader** with the name of the header and current.instance with the variable or literal value that you want in the header:
        
        (function executeRule(current, previous /\*null when async\*/) {  
          
            if(current.headers.indexOf("X-MyCustomHeader") < 0){  
                current.headers = "X-MyCustomHeader:" + current.instance + "\\n" + current.headers;  
            }  
          
        })(current, previous);
        

### Applicable versions

This was tested on the Madrid release, but will most likely work on other versions.

**Additional information**

This solution is considered a customization and out of scope for support, and cannot be guaranteed to always work in a future version of ServiceNow. 

Credit for the business rule code above goes to several ServiceNow Community posts on this subject, and was also tested as working by a customer who raised a case on the issue.
