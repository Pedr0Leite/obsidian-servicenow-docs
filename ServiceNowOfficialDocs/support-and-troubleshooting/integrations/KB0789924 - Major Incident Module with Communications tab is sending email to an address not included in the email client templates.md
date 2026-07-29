---
title: "Major Incident Module with Communications tab is sending email to an address not included in the email client templates"
aliases:
  - KB0789924
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789924
kb_number: KB0789924
last_modified: 2024-04-08
---

## Major Incident Module with Communications tab is sending email to an address not included in the email client templates

  

### Issue

After creating a major incident and visiting the Major Incident Workbench communication tab page there is an email address visible in the send button pop up with a  person’s name that does not seem to be part of the expected recipients list 

### Cause

The reason of seeing any additional email address in the email client is the Creation of the any custom contact definition

### Resolution

Review the list of records that have additional email addresses, you can delete or disable the record that includes the email address that you don't want to see in the email client.

The next URL will provide the list of contact definitions:

  
[https://INSTANCE\_NAME.service-now.com/nav\_to.do?uri=%2Fcontact\_definition\_list.do](https://INSTANCE_NAME.service-now.com/nav_to.do?uri=%2Fcontact_definition_list.do)

The solution will work for new major incidents. Already created incidents email list could be edited in each incident recipient list settings as the official documentation states. More info:

[https://docs.servicenow.com/csh?topicname=mi-workbench-communications-tab.html&version=latest](https://docs.servicenow.com/csh?topicname=mi-workbench-communications-tab.html&version=latest)
