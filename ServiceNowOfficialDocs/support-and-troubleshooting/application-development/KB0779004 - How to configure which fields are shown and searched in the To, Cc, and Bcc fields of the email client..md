---
title: "How to configure which fields are shown and searched in the To, Cc, and Bcc fields of the email client."
aliases:
  - KB0779004
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779004
kb_number: KB0779004
last_modified: 2024-05-08
---

## How to configure which fields are shown and searched in the To, Cc, and Bcc fields of the email client.

  

### Summary

If you need to change which fields are shown or searched on the email reference fields within the email client such as the To field. You can edit a system property "glide.ui.email\_client.email\_address.disambiguator".

### Instructions

1.  Navigate to sys\_properties.list
2.  Search for "glide.ui.email\_client.email\_address.disambiguator"
3.  Set the fields from sys\_user as needed separated by a semi colan. 
4.  Save the record.

### Related Links

There is also a property "[glide.ui.email\_client.email\_address.disambiguator\_search](https://empjjackson9.service-now.com/sys_properties.do?sys_id=d49033047f2003007f005212bdfa9187&sysparm_record_target=sys_properties&sysparm_record_row=1&sysparm_record_rows=2&sysparm_record_list=nameCONTAINSglide.ui.email_client.email_address.disambiguator%5EORDERBYDESCsys_updated_on)" Which can be set to false if you only want to show the additional fields but not search them. 

Since Tokyo this configuration has moved to the default Email Client Configuration record.

Please follow [Define email client recipient qualifiers](https://docs.servicenow.com/bundle/washingtondc-platform-administration/page/administer/notification/task/define-email-recipient-qualifiers.html) to configure this
