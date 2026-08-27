---
title: "How to configure email client templates on tables"
aliases:
  - KB0780319
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780319
kb_number: KB0780319
last_modified: 2025-05-27
---

## How to configure email client templates on tables

  

### Issue

Unlike common tables like incidents, custom tables need additional configuration to support email client templates.

### Release

  Yokohama

### Resolution

#### Email client attributes

-   The table needs an attribute to support the email client.
-   The dictionary entry of the table collection should have the attribute **email\_client**

  
By default the Incident table has this enabled.

To enable the email client for another table: 

1.  Open a record in the table.
2.  On the form, from the menu icon, select **Configure**, and then select **Dictionary**
3.  In the Dictionary Entries list, open the first record.
4.  On the form, in the Related Links section, select **Advanced view.**
5.  Search for the record type, for example 'incident'. 
6.  In the Attributes field, enter **email\_client=true**
7.  Select **Update.**

  
For detailed instructions see the ServiceNow Documentation [Enable the email client for a table](https://docs.servicenow.com/csh?topicname=c_EnableTheEmailClient.html&version=latest "Client templates")  
  
  

#### Create an email client template (optional)

Create a custom template for each table that uses the email client. Once created, define the prepopulated values for recipients and email content. 

For details, see [Create an email client template.](https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/notification/task/t_CreateAnEmailClientTemplate.html)  
  
  

#### Use Quick Messages

This feature displays a drop-down list from which to select predefined content for consistent messaging. 

**Note**: There must be at least two (2) quick messages otherwise the drop-down list will not display in the email client pop-up form. 

For detailed setup instructions, see [Define a quick message.](https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/notification/task/t_QuickMessages.html)  
  
  

### Related Links

[Exploring the email client](https://www.servicenow.com/docs/bundle/yokohama-platform-administration/page/administer/notification/reference/exploring-email-client.html)
