---
title: "Slow processing of scheduled job 'Perspectium MultiOutput'"
aliases:
  - KB0789826
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789826
kb_number: KB0789826
last_modified: 2024-04-08
---

## Slow processing of scheduled job 'Perspectium MultiOutput'

  

### Issue

Scheduled jobs 'Perspectium MultiOutput Processing' are slow to process lasting several minutes or hours even though they are scheduled to run every thirty seconds.

### Release

All releases.

### Cause

Perspectium MultiOutput Processing jobs are scheduled to run repetitively every thirty seconds. The jobs execute the Script Include named 'Perspectium' which makes an HTTP POST JSON request to a Perspectium integration URL in the form of https://acme.perspectium.net/multiinput. This POST request then waits for the reply back with data before processing it and repeating the process according to the schedule.  
  

Depending on the size of the HTTP POST response, the scheduled 'MultiOutput Processing' job will remain in memory for several minutes or hours in one or several worker threads in the instance nodes.  
  

jobs                                   duration  node              thread  
\-------------------------------------- --------- ----------------- --------  
Perspectium MultiOutput Processing 1   0:12:48   instancename003   worker.0  
Perspectium MultiOutput Processing 2   0:18:05   instancename004   worker.2  
  

The delay can be found in the node localhost log in the parameter 'response\_time' as detailed in the sample line below:  
  

2019-12-16 12:34:56 (000) worker.0 worker.0 txid=2b9cddfedbe1 OUTBOUND\_HTTP: protocol=HTTP/1.1 response\_status=200 response\_time=97203 request\_length=5004172 response\_length=0 app\_scope=global session\_id=glide.scheduler.worker.0 transaction\_name="Perspectium MultiOutput Processing" user\_name=system mid\_server= source\_table=sysauto\_script source\_record=12345678901234567890123456789012 system\_id=app123456.abc0.service-now.com:instancename001 method=POST log\_level=Basic scheme=https hostname=acme.perspectium.net path=/multiinput url=[https://acme.perspectium.net/multiinput](https://ernst-young.perspectium.net/multiinput)

### Resolution

Since the delay is due to the volume of data transferred from the Perspectium endpoint to the ServiceNow instance and not a lack of resources, it is advised to evaluate the and moderate the amount of data being requested and received.

### Related Links

Perspectium ServiceNow Online Documentation [http://wiki.perspectium.com/doku.php](http://wiki.perspectium.com/doku.php)
