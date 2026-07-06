---
title: "Splunk Add-on Integration: Connectivity error  with ServiceNow  (SSLError: CERTIFICATE_VERIFY_FAILED)"
aliases:
  - KB0743591
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743591
kb_number: KB0743591
last_modified: 2024-05-01
---

## Splunk Add-on Integration: Connectivity error with ServiceNow (SSLError: CERTIFICATE\_VERIFY\_FAILED)

  

### Issue

When you click on **Event Action** button in Splunk, you will see connectivity error with \[SSL: Certificate\_verify\_Failed\]

command=" ", Unable to connect to ServiceNow. Error: Traceback (most recent call last): File "/opt/splunk/etc/apps/TA-ServiceNow-SecOps/bin/sn\_connect.py", line 42, in postData return requests.post(url, auth=(user, pwd), headers=headers, data=dataValues) File "/opt/splunk/lib/python2.7/site-packages/requests/api.py", line 88, in post return request('post', url, data=data, \*\*kwargs) File "/opt/splunk/lib/python2.7/site-packages/requests/api.py", line 44, in request return session.request(method=method, url=url, \*\*kwargs) File "/opt/splunk/lib/python2.7/site-packages/requests/sessions.py", line 456, in request resp = self.send(prep, \*\*send\_kwargs) File "/opt/splunk/lib/python2.7/site-packages/requests/sessions.py", line 559, in send r = adapter.send(request, \*\*kwargs) File "/opt/splunk/lib/python2.7/site-packages/requests/adapters.py", line 382, in send raise SSLError(e, request=request) SSLError: \[SSL: CERTIFICATE\_VERIFY\_FAILED\] certificate verify failed (\_ssl.c:741)

### Release

ServiceNow Splunk Add-on, SecOps Add-on (3921)

### Cause

Splunk contains its own Python environment, that is different than the host’s Python environment (for both Windows and Linux installs). ServiceNow's current Splunk Add-on, ServiceNow SecOps Add-on (3921) - leverages a Python script to handle the connect command, to talk to ServiceNow. This Python script leverages the Splunk Python instance that explicitly trusts certain SSL CA Certs (local to Splunk’s Python environment)  
  
Customers with ServiceNow leveraging internally issued SSL certificates (non-public) will need to have Splunk trust this certificate (or the Certificate Authority that issued the certificate), so that they can successfully use the SN SecOps Add-on (3921).

### Resolution

To update the Splunk Install Directory: 

Splunk Install Directory:

/opt/splunk/etc/apps/TA-ServiceNow-Secops/bin

This is the file that needs to modified:

/opt/splunk/etc/apps/TA-ServiceNow-Secops/bin/sn\_connect.py

Adjust Line 40 and 42 of "sn\_connect.py" python script to either

1.  Ignore SSL verification
2.  Create a new directory, Store CA certs in Directory, code path to the directory.
