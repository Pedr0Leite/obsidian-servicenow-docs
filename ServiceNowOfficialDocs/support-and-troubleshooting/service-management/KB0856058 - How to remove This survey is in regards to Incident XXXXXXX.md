---
title: "How to remove \"This survey is in regards to Incident: XXXXXXX\""
aliases:
  - KB0856058
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856058
kb_number: KB0856058
last_modified: 2024-04-08
---

## How to remove "This survey is in regards to Incident: XXXXXXX"

  

### Issue

How to remove "This survey is in regards to Incident: XXXXXXX"

### Resolution

Following lines from 'assessment\_take2' UI page shows the message In the HTML line 433 to 441. You may add another condition or comment these lines to get rid of the alert.  
  
/sys\_ui\_page.do?sys\_id=012918babfb001007a6d257b3f073996&sysparm\_view=&sysparm\_record\_target=sys\_ui\_page&sysparm\_record\_row=1&sysparm\_record\_list=nameSTARTSWITHassessment\_take2%5EORDERBYname&sysparm\_record\_rows=1  
  
\[code\]

```
<j2:if test="$[GlideMobileExtensions.getDeviceType() == 'doctype']">                            <div class="notification notification-info">                                $[gs.getMessage('This {0} is in regards to {1}: ', msgArr)]                                <a onClick="openTaskOverlay(event)" class="related-task-link">${task_record}</a>                                <button data-dismiss="alert" class="btn btn-icon close icon-cross">                                    <span class="sr-only">Close</span>                                </button>                            </div>                        </j2:if>
```

\[/code\]
