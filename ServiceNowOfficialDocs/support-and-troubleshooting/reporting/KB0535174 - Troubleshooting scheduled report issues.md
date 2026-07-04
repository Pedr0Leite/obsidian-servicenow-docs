---
title: "Troubleshooting scheduled report issues"
aliases:
  - KB0535174
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535174
kb_number: KB0535174
last_modified: 2026-05-12
---

## Troubleshooting scheduled report issues

  

### Issue

This article guides you through the process of troubleshooting errors in scheduled reports. It provides steps to help you eliminate common causes for your problem by verifying that the configuration of your networking is correct.

Symptoms may include the following: 

-   Scheduled report fails to run.
-   Not all data appears in the scheduled report.
-   Cannot schedule a report.
-   Scheduled report is empty.
-   Scheduled report fails to run at a specified time
-   Scheduled reports are not delivered to user

### Release

All

### Resolution

Review the email log to confirm that an email has been sent.

To review the email log:

1.  Navigate to **System logs > Emails**. Search for the email that was sent out.

Confirm the report is active. To confirm: 

1.  Navigate to **Scheduled reports**.
2.  Find the report mentioned. 
3.  Right-click the header and click **Show XML**.
4.  Find the active tag and make sure it is set to true.  
    -   If not true, scheduled report will not run.
5.  Confirm that the report is being sent to the correct users.  
    -   To do this, go into the scheduled report and see who this report is being sent to. For example, **Users and groups**.
6.  Verify that the proper schedule conditions are set. To verify that the proper conditions are set, go into the scheduled report, and check the **RUN** time. These are the following options: _daily_, _weekly_, _monthly_, _periodically_, _Once_, or _on demand_. 
7.  If the conditional flag has been set, check the conditions in the script to make sure the script does not have any issues. (Refer to the person who wrote the script if this is customary.)
8.  Verify that the _run as_ user has the correct permissions. Scheduled Reports are distributed via email.  
    -   Scheduled reports created by an individual whose user account is deactivated might not display any data. To ensure that the desired data is displayed, an active user must recreate the scheduled report.
    -   The user has to be able to at least view the report. If not, a blank/empty attachment will be emailed out.
9.  Try recreating the scheduled report to see if issue is resolved.
10.  Determine if there are null pointer exceptions in the log files. Check log files, search for _NullPointer_ exceptions.
11.  Refer to the following documentation for the types of reports that can be scheduled, and the roles required, [Automate report distribution](https://docs.servicenow.com/csh?topicname=t_ScheduleAReport.html&version=latest)
12.  To schedule a multi-level and send as pdf have this plugin enabled - Webkit HTML to PDF (com.snc.whtp) plugin.
13.  If domain separation is enabled, make sure the user trying to schedule the report has access/visibility to the report in that domain
14.  If scheduled report is not executing in the right time zone, check whether the _run\_as_ field is empty or populated with a user name:  
       
     -   If the _run\_as_ field is empty, the report runs in the system time zone.
     -   if the _run\_as_ field is populated with a user name, the report runs in the time zone of the user.  
           
         Note: To manually specify the time zone, configure the form to add the **Run As tz** field to the Scheduled Report form.  
           
         
15.  If scheduled reports are not delivered to user, turn on the **Allow Notifications** and **Primary email** switch.  
     Check if the users email address is present in the "Primary Email" record the cmn\_notif\_device table.  
     The "Primary Email" record could erroneously be active while empty. 

For more information, see the documentation topic [Scheduled jobs](https://docs.servicenow.com/csh?topicname=c_ScheduledJobs.html&version=latest "Scheduled jobs").

\* If not all the data appears in the scheduled report:

1.  The main cause of this is due to ACLs that have not been set up. Verify that a user can access the data that is in the table. If they can see the data that is in the table, its most likely not an ACL issue. 
2.  Check to make sure that the **_run as_** user is set to **active**. If the user is not active in in the instance, this will cause problems. 
3.  Make sure the data is not dynamic. If the data is changing, and the scheduled report runs, the data will be different or won't be available.  
      
    \* If there is no data in the attachment, check that the can at least view the report.
