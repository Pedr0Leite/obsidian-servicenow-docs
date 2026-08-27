---
title: "Error message \"Record doesn't exist or ACL restricts the record retrieval\" appearing when ITIL users try to disallow notifications"
aliases:
  - KB0717149
tags:
  - servicenow
  - support-kb
  - acl
  - sys_user
  - notifications
  - security-constraints
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717149
kb_number: KB0717149
last_modified: 2024-04-07
---

## Error message "Record doesn't exist or ACL restricts the record retrieval" appearing when ITIL users try to disallow notifications

  

### Issue

# Symptoms

* * *

When an ITIL user tries to disallow notifications as shown in the below screenshot, getting error,

Record doesn't exist or ACL restricts the record retrieval  
  
![](sys_attachment.do?sys_id=e95aac26db42b450e515c223059619d9)

Observed below error in the session debug log while reproducing the issue,

```
11:30:06.582: TIME = 0:00:00.000 PATH = record/sys_user/write CONTEXT = Soufiane MIR RC = false RULE =not evaluated access denied not evaluated not evaluated record/sys_user/write Globallog11:30:06.586: No Record found: com.glide.rest.domain.ServiceException: No Record found: com.glide.notification.cmn.RestUtilities.getNoRecordFound(RestUtilities.java:17) com.glide.notification.cmn.RestUtilities.throwNoRecordFound(RestUtilities.java:13) com.glide.notification.preference.service.PostUpdateAllOperation.updateAll(PostUpdateAllOperation.java:50) com.glide.notification.preference.service.NotificationPreferenceRestService.updateAll(NotificationPreferenceRestService.java:211) sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) java.lang.reflect.Method.invoke(Method.java:498) com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:43) com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:271) com.glide.processors.AProcessor.runProcessor(AProcessor.java:483) com.glide.processors.AProcessor.processTransaction(AProcessor.java:205) com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:178) com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:167) com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31) com.glide.sys.Transaction.run(Transaction.java:2038) java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) java.lang.Thread.run(Thread.java:748)log11:30:06.587: #944808 [REST API] RESTAPIProcessor : Handling exception No Record found
```

# Release

* * *

Any supported release.

# Cause

* * *

For the affected user, "record/sys\_user/write" custom ACL was denying write access to sys\_user record.

# Resolution

* * *

Review the record/sys\_user/write custom ACL and modify the role condition as per your business requirement.

# Additional Information

* * *

[Configure system settings](https://docs.servicenow.com/csh?topicname=configure-messaging-user-settings.html&version=latest "Configure system settings")

## Related

- [[KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif]] - same error message, different underlying ACL
- [[KB0750584 - Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables]]
- [[access-control-rules]] - official docs on ACL rule evaluation

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0688916 - When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form|When Vendor Core plugin is installed, unable to view assigned_to and caller_id fields on the incident form]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0695387 - For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get |For users with the itil, catalog, or approval_admin role, when they attempt to access the My Approvals module, they get message Security constraints prevent access to requested page]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0713543 - Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)|Admins have limited access to modules, tables, etc. (even though the ACLs are set in place, they fail)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0720507 - Caller and Assigned to fields are missing on forms for tables extended from Task|Caller and Assigned to fields are missing on forms for tables extended from Task]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725874 - Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_grou|Reference Fields like 'Requestor', 'Assignment group', and 'Assigned to' that are referencing to sys_user, sys_user_group are not available on the form.]]
