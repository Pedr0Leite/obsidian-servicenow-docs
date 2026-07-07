---
title: "How to grant or restrict access to the users for the Pop-up view in schedule page (show_schedule.do)?"
aliases:
  - KB0692741
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - scheduling
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692741
kb_number: KB0692741
last_modified: 2025-01-03
---

## How to grant or restrict access to the users for the Pop-up view in schedule page (show\_schedule.do)?

  

### Issue

  
  

# Description

* * *

Configure ACLs to grant or restrict access to the users for the Pop-up view in schedule page (show\_schedule.do)?

1.  Navigate to : https://<instance\_name>.service-now.com/show\_schedule.do
2.  Double click on any day to add a schedule
3.  Notice the pop-up view for "Add Schedule Item"

We can restrict or grant access to this pop-up view to the users using ACLs.

**Image 1:** The below screenshot shows how the scheduler window looks like when you navigate to /show\_schedule.do

**Note:** The URL used to navigate to a particular schedule page (cmn\_schedule\_page) on the scheduler window looks like

[https://<instance\_name>.service-now.com/show\_schedule.do/sysparm\_type=maint](https://\<instance_name\>.service-now.com/show_schedule.do/sysparm_type=maint)

**Document for reference:** [https://docs.servicenow.com/csh?topicname=r\_CreateCalendarsWithSchedulePages.html&version=latest](https://docs.servicenow.com/csh?topicname=r_CreateCalendarsWithSchedulePages.html&version=latest)

![](/sys_attachment.do?sys_id=eef820aedb02b450e515c22305961964)

**Image 2:** The pop-up view when you double click on the schedule window to add a schedule item: 

![](/sys_attachment.do?sys_id=e2f820aedb02b450e515c2230596196a)

# Procedure

* * *

1.  The table that configures the pop-up on the scheduler is "cmn\_schedule\_span"
2.  To grant read access to a particular set of user, create a read ACL for that role on "cmn\_schedule\_span"
3.  Similarly, configure the write and delete ACLs on cmn\_schedule\_span" to manage the access on the pop-up view.

**Note:** cmn\_schedule\_span is the table that configures the Schedule Entry Layout. 

# Applicable Versions

* * *

All

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]]
- [[access-control-rules]] - official docs on access control rules

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688981 - Certain users are unable to sc_cat_item_producer records in Service Portal|Certain users are unable to sc_cat_item_producer records in Service Portal ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691976 - The users with SOAP role not able to view the incident table data even though the ACLs return true.|The users with SOAP role not able to view the incident table data even though the ACLs return true.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691989 - Ui ActionButton does not display for a user even when the ACLs and the UI action conditions grant the access to that use|Ui Action/Button does not display for a user even when the ACLs and the UI action conditions grant the access to that user]]
