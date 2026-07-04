---
title: "Task and CI relationship do not display correctly"
aliases:
  - KB0547639
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547639
kb_number: KB0547639
last_modified: 2025-04-07
---

## Task and CI relationship do not display correctly

  

### Issue

Task relations do not display the relationship type, and all the associated task on the Project Task, Problem, Change Request form.

There are system properties to control the  max depth, and the number of relationships which can be associated for task relations and **cmdb\_ci**. The properties are: 

-   glide.ui.max\_relations
-   glide.ui.cmdb\_max\_depth

When **max\_relations** is reached, there will be a (**+**) added to the relation, and the relationship types would be rendered correctly. The optimum values for these properties depends on the instance to instance, but the recommended value is to set the following:

-   **Name**: glide.ui.max\_relations
-   **Type**: Integer
-   **Value**: 300

  

-   **Name**: glide.ui.cmdb\_max\_depth
-   **Type**: Integer
-   **Value**: 3

### Related Links

Please be aware of known issue **PRB614207** where the CIs on the form were running the nodes OOM, and the workaround for the issue was to create the above system properties which override the default value of 1000

While setting these properties can be used to fine tune the performance, it potentially creates an issue with the rendering of the Task and CI Relations.

Both Task and CI relations share the same UI formatters, which is the reason you can see this issue on many tables.
