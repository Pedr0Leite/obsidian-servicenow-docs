---
title: "Skill reports show skill level name and sys_ID when the name is not unique"
aliases:
  - KB0993561
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993561
kb_number: KB0993561
last_modified: 2025-01-02
---

## Skill reports show skill level name and sys\_ID when the name is not unique

  

### Summary

Reports and Dashboards will show the skill level sys\_ID as well as the skill level name when the skill name is not unique.

For example, OOB there are two skill types with the same skill levels defined. Both Behavioural and General have skill levels:

-   Novice
-   Intermediate
-   Adavanced
-   Expert

If you open the Skill Matrix Report it will show the levels and the sys\_ID

### Instructions

If you want only the name to be displayed, you can update the report:

-   Open the report
-   Click on Configure and click on select columns
-   Select skill\_level.name instead of skill\_level
-   Update the report. This will only show the skill\_level name instead of sys\_id
