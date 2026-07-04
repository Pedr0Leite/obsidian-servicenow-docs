---
title: "How the \"SAM - Identify Blacklisted Software\" Scheduled Job Works"
aliases:
  - KB3019275
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3019275
kb_number: KB3019275
last_modified: 2026-05-14
---

## How the "SAM - Identify Blacklisted Software" Scheduled Job Works

  

### Summary

ServiceNow SAM includes an out-of-box daily scheduled job called "SAM - Identify Blacklisted Software." When this job runs, it scans all software models that have the Restricted Software field set to true. For each restricted software model it finds, it looks at all the software installs of that title across the organisation and decides whether to create a new Software Reclamation Candidate, update an existing one, or leave it as-is.

* * *

**How the Job Finds Installs**

For each restricted software model, the job runs multiple passes across the installed software records. It handles different scenarios separately:

-   Installs that are part of a software suite
-   Installs that are standalone titles
-   Installs measured by a user-based license metric
-   Installs measured by a device-based license metric
-   Installs that have no license metric result stamped at all

This ensures every type of install for that restricted title is covered regardless of how it is licensed.

If the software model has an Install Condition configured, that condition is applied as an additional filter on every install query. Only installs that satisfy the condition are included in scope.

* * *

**How the Job Decides Whether to Create or Update a Reclamation Candidate**

Before creating a new reclamation candidate, the job checks whether one already exists for the same group of installs. It does this by looking at the related install records linked to existing candidates. If an exact match is found — meaning all the installs in scope are already linked to the same candidate and that candidate has no additional installs — the job updates that existing candidate instead of creating a new one.

If no exact match is found, the job then checks whether any of those installs are already linked to a candidate in Awaiting Revocation state. If they are, those candidates are updated rather than replaced, because they are already in an active revocation process.

If none of the above conditions apply, any existing open candidates for those installs are cancelled first, and then a new reclamation candidate is created.

* * *

**What the Reclamation Candidate Contains**

When the job creates a new reclamation candidate on the Software Reclamation Candidates table, it sets the following:

-   Justification is set to Restricted Software
-   The User field is populated from the assigned user on the software install record
-   Notify User is set to false by the job itself

When the job updates an existing candidate that was created for a different reason, it changes the justification to Restricted Software and moves the state to Awaiting Revocation. If the candidate had an active workflow or pending approval, those are cancelled before the update is applied. The job does not update candidates that already have justification set to Restricted Software or that are in Closed Complete state.

* * *

**How the Notification Is Triggered**

The notification is not triggered directly by the job. After the job inserts or updates a reclamation candidate, an out-of-box business rule called "Email user auto reclamation" fires automatically. This business rule is configured to run after any insert or update on the Software Reclamation Candidates table. Its condition checks that the justification is either Restricted Software or Unlicensed, and that the User field is not empty.

When that condition is met, the business rule queues an event which triggers the "Notify user auto reclamation" email notification. The email is sent to the user populated on the reclamation candidate record, with the subject "Unauthorized Software Use."
