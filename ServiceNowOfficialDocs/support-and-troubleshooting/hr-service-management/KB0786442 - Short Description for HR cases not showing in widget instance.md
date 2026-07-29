---
title: "Short Description for HR cases not showing in widget instance"
aliases:
  - KB0786442
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786442
kb_number: KB0786442
last_modified: 2026-03-31
---

## Short Description for HR cases not showing in widget instance

  

### Issue

Short Description data for HR cases not showing in widget (https://<instance\_name>.service-now.com/hr?id=requests#hr).

When you configure Widget instance to show HR cases (Ex: Title = My HR Cases, ID=hr\_case) but short description data will not be displayed.

Widget Instance: Data Table from Instance Definition Widget (or) Data Table from URL Definition Widget

### Release

Madrid, New York

### Cause

HR is a scoped application and the widget need to access data from a script include of different scope then it need to be allowed in RCA table (Restricted Caller Access or **sys\_restricted\_caller\_access**).

Short Description here is a field in the Task table and is in Global application scope, hence data table widget in HR scope was not able to access the field.

### Resolution

The short description was not displayed because of the Restricted Caller Access Privilege on Read operation for Data Table widget.

  
Steps to find :

1.  Go to **sys\_restricted\_caller\_access.list**
2.  Search for "short\_description" as an example.
3.  Check for Operation "Read" and Source "Widget: Data Table"
4.  Open the record and the Status should be updated from "Requested" to "Allowed".  
      
    

After modifying it, you will be able to see the short description displayed on HR portal > HR cases.  
  
Please read more about RCA here:  
[https://docs.servicenow.com/csh?topicname=set-RCA-level.html&version=latest](https://docs.servicenow.com/csh?topicname=set-RCA-level.html&version=latest)

[https://docs.servicenow.com/csh?topicname=case-knowledge-management-landing-page.html&version=latest](https://docs.servicenow.com/csh?topicname=case-knowledge-management-landing-page.html&version=latest)
