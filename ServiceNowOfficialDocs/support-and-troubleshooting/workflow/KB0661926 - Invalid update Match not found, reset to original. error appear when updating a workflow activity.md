---
title: "\"Invalid update\" \"Match not found, reset to original.\" error appear when updating a workflow activity"
aliases:
  - KB0661926
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0661926
kb_number: KB0661926
last_modified: 2024-09-20
---

## "Invalid update" "Match not found, reset to original." error appear when updating a workflow activity

  

### Issue

"Invalid update" "Match not found, reset to original." error appear when updating a workflow activity

Problem

* * *

From the workflow editor, changes made to the workflow activity are not saved.  The error **Invalid update** and **Match not found, reset to original** appear; prevents changes to be saved.   

Symptoms

* * *

   

-   The error **Invalid update** appears at the top of the page.
-   The error **Match not found, reset to original** appear within the Schedule section even when no schedule, timezone, or duration is selected.
-   Changes to the activity are not saved.  

Cause

* * *

This happens when a workflow has been imported to a target instance and an activity is configured to use a custom schedule, custom time zone, or custom duration that does not exist on the target instance.  The schedule, timezone or duration will be set to none. Any future updates to this activity are not saved and triggers this error.  

  
Resolution

* * *

To solve the issue, the missing component has to be identified and updates made accordingly. 

There are 3 fields to check to identify which component is missing:

1.  Open the affected activity from workflow editor.
2.  Check one of these fields to identify the missing component:

-   Change the **Schedule based on** field to **A user-specified schedule**.  If the Schedule field shows a sys\_id instead of a label, then you have identified the component that is missing.
-   Change the **Timezone based on** field to **A specific timezone**.  If the Timezone field shows a sys\_id instead of a label, then you have identified the component that is missing.
-   Change the **Due date based on** to **A relative duration**.  If the Relative Duration field shows a sys\_id instead of a label, then you have identified the component that is missing.

Once you have identified which component is missing, you can either import the missing component from the source instance or change the missing option to another option that exists in the target instance.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: Sometimes, more than one component might be missing from an activity. These have to be corrected before updates to the activity are allowed.&nbsp;</td></tr></tbody></table>

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Warning" src="/Warning_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Warning</strong>: Deciding between importing the missing option to the target instance or use an option that already exists in the instance boils down to the business need of the customer.</td></tr></tbody></table>
