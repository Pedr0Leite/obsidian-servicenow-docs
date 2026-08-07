---
title: "How to avoid live form feature triggering th onchange client script on another user screen"
aliases:
  - KB0748577
  - How to avoid live form feature triggering the onchange client script on another user screen
tags:
  - servicenow
  - support-kb
  - client-scripts
  - live-form
  - onchange
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748577
kb_number: KB0748577
last_modified: 2024-04-07
---

## How to avoid live form feature triggering th onchange client script on another user screen

  

### Issue

# Symptoms

Consider a scenario where User 1 views an incident record in his browser window and at the same time User 2 is also viewing the same incident record in his separate browser window.

Let's consider that "live form" feature is enabled and there is a onchange client script on priority field which has a alert().

With this scenario, when User 1 changes the priority of the incident record, User 2 gets the onchange client script (on the priority field) gets executed on his screen and the alert() window shows up.

# Release

Any supported release. 

# Cause

Due to the live form feature when the original user was modifying the record which was viewed by another user, he/she gets the priority changed in his form as well, this triggers the onchange event for priority field eventually onchange client script is invoked.

# Resolution

You can workaround the situation via using the `g_form.isLiveUpdating()` API and decide the execution of client-side script accordingly.

# Additional Information

[isLiveUpdating](https://developer.servicenow.com/app.do#!/api_doc?v=madrid&id=r_GF-isLiveUpdating "isLiveUpdating")

[Client scripts](https://docs.servicenow.com/csh?topicname=client-scripts.html&version=latest "Client scripts")

## Related

- [[KB0749175 - Global variables declared on onLoad client script are not accessible from another onChange client script]]
- [[KB0711972 - oldValue returns empty value instead of the previous value for onChange client scripts]]

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort action when description is empty/ReadMe|Abort action when description is empty]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Abort direct incident closure without Resolve State/readme|Abort direct incident closure without Resolve State]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Field Decoration/README|Add Field Decoration]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Add Image to Field Based on Company/README|Add Image to Field Based on Company]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Adding Placeholder on Resolution Notes/README|Adding Placeholder on Resolution Notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Client Scripts/Auto Update Priority based on Impact and Urgency/readme|Auto Update Priority based on Impact and Urgency]]
