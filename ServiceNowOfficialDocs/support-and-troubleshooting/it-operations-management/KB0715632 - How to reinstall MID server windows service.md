---
title: "How to reinstall MID server windows service"
aliases:
  - KB0715632
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715632
kb_number: KB0715632
last_modified: 2025-01-03
---

## How to reinstall MID server windows service

  

### Issue

# Description

* * *

Customer renamed the mid server wrapper name in wrapper-override.conf

ie:

from

wrapper.name=snc\_mid\_kingston

to

wrapper.name=snc\_mid\_kingston1

and causing mid server unable to upgrade due to pre-check failure

Snippet from mid server agent log

10/22/18 17:56:13 (898) AutoUpgrade.3600 SEVERE \*\*\* ERROR \*\*\* Aborting MID Server upgrade due to pre-upgrade check failure: Service snc\_mid\_kingston1 does not exist

# Procedure

* * *

Reinstall the mid server windows service

1.  Stop the mid server
2.  Ensure wrapper-override.conf has the right information on wrapper name.
3.  Open command prompt with administrator privilege. Navigate to "<MID\_server\_install\_path>/agent" and issue "start.bat"

ie:

C:\\kingston\\agent>start.bat

C:\\kingston\\agent>bin\\mid.bat start  
wrapper | ServiceNow MID Server Kingston1 service installed.  
wrapper | Starting the ServiceNow MID Server Kingston1 service...  
wrapper | ServiceNow MID Server Kingston1 started.

# Applicable Versions

* * *

Jakarta, Kingston, London

# Additional Information

* * *

You can delete the non-applicable windows service via sc delete from command prompt

ie:

sc delete <service\_name>

![](/sys_attachment.do?sys_id=867cec6edb42b450e515c223059619ea)
