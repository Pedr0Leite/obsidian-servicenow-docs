---
title: "SCOM connector would not pull events and Last error message has Unparseable date errors."
aliases:
  - KB0754367
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754367
kb_number: KB0754367
last_modified: 2024-04-07
---

## SCOM connector would not pull events and Last error message has Unparseable date errors.

  

### Issue

# Symptoms

SCOM connector instance throws the below error when the events are pulled.  
  
The error is seen on the 'Last error message' field on the 'em\_connector\_instance' table.  
  

```
failed to run 3PC groovy.lang.MissingMethodException: No signature of method: static com.service_now.mid.probe.tpcon.test.SCOMConnector.writeError() is applicable for argument types: (java.lang.String) values: [Failed to send event. java.text.ParseException: Unparseable date: "9.7.2019 5.27.05". Event{EMS='SCOM OneCloud MS Private Fabric', source='null', node='MSPSEALVSE01.mspmgmt.umnfi.net', resolution_state='Closing', severity='null', messageKey='6a2477d0-fff7-4ba2-b06e-ca875569dd5c', resource='null', businessServiceName='null', ciTypeName='null', description='Windows Defender Service Status Alert, Description: This alert will trigger if Windows Defender service is stopped', timeOfEvent=null', metricName=null'}] Possible solutions: writeError(java.lang.String)
```

# Environment

Event management plugin installed.

# Cause

OOTB SCOM connector definition has 'scom\_date\_format' connection parameter defined like this: M/d/yyyy h:mm:ss a

![](sys_attachment.do?sys_id=68ca60e6db42b450e515c22305961985)  
  
But the events coming in have the format: M/d/yyyy h.mm.ss a  
  
This caused the 'Unparseable date' error.

# Resolution

Modify the 'Connector Parameter' scom\_date\_format to the appropriate format and the connector should be able to pull event succesfully.

# Additional Information

[https://docs.servicenow.com/csh?topicname=t\_EMConfigureSCOMConnector.html&version=latest](https://docs.servicenow.com/csh?topicname=t_EMConfigureSCOMConnector.html&version=latest)
