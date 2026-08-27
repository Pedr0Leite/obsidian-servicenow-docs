---
title: "The 'Run as' field in Scheduled email of reports"
aliases:
  - KB0656449
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656449
kb_number: KB0656449
last_modified: 2024-12-12
---

## Issue

It is possible to configure the Scheduled Email of Report page to include a Run as option. What this means is that a user can specify a different user to run the automated report distribution.This can be an actual user on your instance or a configured dummy user that has sufficient permissions to generate a useful report.

Scheduled email of reports is described here: [https://docs.servicenow.com/csh?topicname=t\_ScheduleAReport.html&version=latest](https://docs.servicenow.com/csh?topicname=t_ScheduleAReport.html&version=latest "https://docs.servicenow.com/csh?topicname=t_ScheduleAReport.html&version=latest").

Configuring form layout is described here: [https://docs.servicenow.com/](https://docs.servicenow.com/ "https://docs.servicenow.com/")

(These two links point to Jakarta documentation, but the same help files exist for all supported releases through Kingston.)

If the administrator (or other user) configures the Scheduled Email of Report form to include the **Run as** field, the following message displays when that user chooses another user to run the report: 

**Data that the user selected in the Run as field does not have access to will be excluded from the generated report. If that user does not have access to any data in the report, an empty report is generated.  
**

This message is meant to convey two things:

1.  The selected user running the report may not see the same content in the report that you would, and therefore the recipients of the scheduled report will see different content as well.  
2.  The selected user running the report may see no content at all due to business rules applied to the source tables and report ACLs.

For more information, see [Business rules](https://docs.servicenow.com/csh?topicname=c_BusinessRules.html&version=latest "Business rules") and [Access control list rules](https://docs.servicenow.com/csh?topicname=access-control-rules.html&version=latest "Access control list rules"). (These two links also point to Jakarta documentation, but the same help files exist for all supported releases through Kingston.)
