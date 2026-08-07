---
title: "Software Asset Workspace : How is software spend calculated?"
aliases:
  - KB2676016
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2676016
kb_number: KB2676016
last_modified: 2026-05-22
---

## Software Asset Workspace : How is software spend calculated?

  

### Related Links

The total spend in the software spend widget within the SAM workspace is calculated by the below PA indicator:  
https://{instance\_name}.service-now.com/nav\_to.do?uri=pa\_indicators.do?sys\_id=aa83aa260b450300823505c137673a34%26sysparm\_view=automated

Software spend is calculated as the sum of the total spend value of those records in the table : samp\_license\_metric\_result where the condition Software model result Latest = true  
https://{instance\_name}.service-now.com/samp\_license\_metric\_result\_list.do?sysparm\_query=software\_model\_result.latest%3Dtrue&sysparm\_view=
