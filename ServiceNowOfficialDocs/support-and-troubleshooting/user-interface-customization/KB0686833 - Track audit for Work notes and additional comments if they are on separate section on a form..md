---
title: "Track audit for Work notes and additional comments if they are on separate section on a form."
aliases:
  - KB0686833
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686833
kb_number: KB0686833
last_modified: 2025-01-03
---

## Issue

  
  

# Description

* * *

Customers might want to have Journal Input fields - Work Notes & Additional Comment in different sections of the form. Upon doing so certain features on the form might not work as expected.

# Procedure

* * *

If the Journal Input fields - Work Notes & Additional Comments are not stacked above the activities (filtered) in one section of the form, the activity stream will not show the correct audits, and certain features like Post and Save might not work as expected.

Additionally, customer might also want the audit for additional comments to be visible. Upon changing the dictionary type for additional comments to Journal, the audit will be visible in legacy format.

1.  Place additional comment in the Notes section.
2.  Create a new section - **Work Notes**, and stack the work notes on top of activities filtered.
3.  Save the form layout.
4.  Input some text in the work notes area, and click on Post button
5.  The added work notes will be seen in the activity stream.
6.  Input another text in **Additional Comment**s and click on Save button.
7.  The comments added in Step 6, is added as an additional _comment_. (This happens because additional comments in Journal Input type field)
8.  The activity stream in the Notes section will also have the inputs added in Step 6 labeled as additional comments.

![](sys_attachment.do?sys_id=3d7aa866db42b450e515c2230596195b)

![](sys_attachment.do?sys_id=f57aa866db42b450e515c22305961961)

# Applicable Versions

* * *

Kingston, London, Madrid

# Additional Information

* * *

The workaround for this is to change the comments & work notes also to Journal type.

With this, the Save button will save the work notes and additional comments in their respective sections.

However, the activity stream will no longer be visible, as the activity stream will only work as expected when both additional comments & work notes are Journal Input type, and stacked above the activities (filtered)

[https://docs.servicenow.com/csh?topicname=c\_ActivityFormatter.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ActivityFormatter.html&version=latest)
