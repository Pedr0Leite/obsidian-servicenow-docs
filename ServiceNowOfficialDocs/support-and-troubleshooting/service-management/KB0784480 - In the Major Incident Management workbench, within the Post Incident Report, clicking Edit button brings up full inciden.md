---
title: "In the Major Incident Management workbench, within the Post Incident Report, clicking \"Edit\" button brings up full incident form instead of a HTML box to put in some text. Why?"
aliases:
  - KB0784480
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784480
kb_number: KB0784480
last_modified: 2025-10-16
---

## In the Major Incident Management workbench, within the Post Incident Report, clicking "Edit" button brings up full incident form instead of a HTML box to put in some text. Why?

  

### Issue

When the user is opening up their Major Incident Management workbench, they click into the "Post Incident Report" section.

Under the "Overview", "Findings", etc., when clicking the "Edit" button, the user is not seeing the expected HTML box to enter some text. Instead, they are seeing the full incident form. they wanted to know why.

### Resolution

The reason the above behavior is happening is that the user has a custom View Rule in place for the incident table which is forcing a certain view and interrupting the Major Incident Management workbench functionality.

Here is the View Rule URL:

-   https://instance.service-now.com/nav\_to.do?uri=sysrule\_view.do?sys\_id=d25263e0db4913005f4af4821f9619fa

To stop this behavior, simply deactivate the custom View Rule.
