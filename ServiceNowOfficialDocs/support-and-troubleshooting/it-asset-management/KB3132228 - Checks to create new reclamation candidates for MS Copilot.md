---
title: "Checks to create new reclamation candidates for MS Copilot"
aliases:
  - KB3132228
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3132228
kb_number: KB3132228
last_modified: 2026-07-01
---

## Issue

1\. After attaching  MS usage data exported from MS admin to the integration profile  
2.  executed two jobs successully  
\- SAM - Collect Microsoft 365 Usage  
\- SAM - Create New Reclamation Candidates for Office 365 Integration  
  
  
3\. New software usage data have been updated:  
/samp\_sw\_usage\_list.do?sysparm\_query=norm\_product.prod\_nameLIKEplanner%5EORnorm\_product.prod\_nameLIKEvisio%5EORnorm\_product.prod\_nameLIKEcopilot&sysparm\_first\_row=1&sysparm\_view=  
  
4\. The xml from integration profile  shows the sync dates below:  
  
{"ConnectionAliasId":"SYSID","validate\_connection":"success","error\_message":"","warning\_message":"","Office365ActiveUserDetailReportRefreshDate":"2026-06-06","Office365ActiveUserDetailSyncDate":"2026-06-08 08:43:33","M365AppUserDetailReportRefreshDate":"2026-06-05","M365AppUserDetailSyncDate":"2026-06-08 09:17:21","OneDriveStorageUsageReportRefreshDate":"2026-06-06","OneDriveStorageUsageSyncDate":"2026-06-08 09:29:12","MailBoxStorageUsageReportRefreshDate":"2026-06-06","MailBoxStorageUsageSyncDate":"2026-06-08 09:32:48","activationReportRefreshDate":"2026-06-06","activationSyncDate":"2026-06-08 09:36:59","powerBIAPIStatus":"success","VisioReportRefreshDate":"6/1/2026","VisioSyncDate":"2026-06-04 14:43:34","CopilotReportRefreshDate":"6/1/2026","CopilotSyncDate":"2026-06-04 14:47:25","ProjectReportRefreshDate":"6/2/2026","ProjectSyncDate":"2026-06-04 14:45:39"}  
  
  
5 . But there's no new reclamation candidate were created for Copilot product  
  

## Resolution

Copilot follows a different code path than standard products like Exchange Online or Teams. This product must pass a 7-day sync freshness check before the code will evaluate them for reclamation.  
  
Once the Copilot sync runs successfully and CopilotSyncDate is within 7 days of the reclamation job execution, the code will proceed to evaluate Copilot subscriptions for reclamation.  
  
  
Additionally once the latest copilot usage data is synced successfully, below are the additional checks we run before creating reclamation candidates  
  
Check 1 :  
  
The code checks whether external\_created field (or sys\_created\_on if null) on the samp\_sw\_subscription record is older than last\_activity\_threshold ( example - 90 days for reclamation rule). If the subscription is newer than 90 days, stale stays false and no candidate is created.  
  
Check 2 :  
  
If the Check 1 passes , then the code evaluates staleness. If last\_activity is populated on the subscription record, it must be older than the threshold (90 days). If last\_activity is null, the outcome depends on include\_no\_activity defined on the reclamation rule — currently it is set to false, meaning null activity = not stale = no candidate.  
  
So if the subscription record has last\_activity greater than 90 days, then we will create the reclamation candidate for this assuming it has passed Check 1 listed above  
  
If the subscription record has last\_activity set to empty, then we have set the include\_no\_activity to true on the reclamation rule to consider the subscription as a reclamation candidate  
  
Check 3 :  
  
Before creating a candidate, the code checks to verify no active reclamation candidate with a low\_usage justification already exists for this subscription (either as a user\_subscription / subscription\_to\_retain on the Reclamation. Candidate header, or as an entry in the samp\_sw\_rc\_m2m\_subscription table). If a duplicate exists, creation is skipped.  
  
  
So if all the above 3 checks pass, only then the reclamation candidate is created.
