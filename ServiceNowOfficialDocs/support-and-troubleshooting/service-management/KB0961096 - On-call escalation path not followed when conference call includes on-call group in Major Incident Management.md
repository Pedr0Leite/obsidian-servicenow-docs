---
title: "On-call escalation path not followed when conference call includes on-call group in Major Incident Management "
aliases:
  - KB0961096
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0961096
kb_number: KB0961096
last_modified: 2026-06-24
---

## On-call escalation path not followed when conference call includes on-call group in Major Incident Management

  

### Issue

The Incident Communication Task did not follow on-call escalation path for on-call group as expected.  
Major Incident Management and Incident Alert Management is Integrated to use On-call Module using Notify and ZOOM Conference.  
The Roster and Escalation Plan is defined in On-Call Module but is not following the escalation path where we have configured to trigger the mails in 5 minutes when notifying users.  
  
In Major incident workbench, when we add on-call group to be part of conference call ( using Zoom integration), the escalation path is not respecting the correct interval. The next persons in the escalation path are getting invited earlier than the interval set up in the escalation.  
  
STEPS TO REPRODUCE/OBSERVE BEHAVIOR:  
Open the workbench for an existing Incident e.g. INC0777403  
  
\- Go to Conference tab  
\- Click on Add Call -> Under Technical Communications  
When you click Add call, it pops up a screen to create new Communication Plan record  
\- Fill in Task Short Description as Test, Click Next  
\- In Manage Participates screen, just click on Save and it will create Communication plan  
\- Click on Start Call button in front of the newly created Communication plan  
\- Under Add participants, select Group -> Test Conference Call -> Add to Selected -> Then you can click on Start Call - The call record should have started  
\- On the MIM workbench, the Groups -> On-call Groups -> 'Test Conference Call' group -> Roster and Escalation Details -> Check the Escalation Path and expectation is that the newly created conference call record should follow this escalation path.

### Release

All

### Cause

  
Our Development team have provided the reason for the behavior. This is expected.  
  
Conference call escalation on Incident Communication Tasks follow the property - 'com.snc.iam.conference\_call\_escalation\_workflow', which refers sys\_id of the workflow which drives it.  
  
Conference call WF OOB follows a one minute wait time. See attached logic and log screenshots which shows a rough 1 minute difference. This also raises the events which we see for participant change, which drive the e-mails. The e-mails are intended as missed call reminders and generally calls will reach before email and they remain in the inbox as a note that a conference needed the user.  
  
The reason is conference calls are more aggressive in nature and it will be weird for the host to be left waiting for several minutes, which could be ok for an assignment and acknowledgment workflow.

WORKFLOW HISTORY

![](sys_attachment.do?sys_id=33c6022747a107103542f24c736d4353)

OOB WORKFLOW

![](sys_attachment.do?sys_id=bbc6022747a107103542f24c736d434d)

### Resolution

  
The behavior you report is by design.  
  
To resolve this issue to a different time you will need to change the logic.  
You can copy the default workflow and modify the wait logic.
