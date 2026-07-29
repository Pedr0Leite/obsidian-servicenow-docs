---
title: "Edge Encryption:  how to encrypt fields by running a Business Rule, Script Include, Scheduled Job or other background scripting"
aliases:
  - KB0815435
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815435
kb_number: KB0815435
last_modified: 2024-04-08
---

## Issue

Sample use case:

Have a scenario where new\_call records are created from an inbound email action, when a service desk agent opens the new\_call record and decides it's an incident, the u\_email\_address field should be copied from new\_call to the u\_ext\_email\_address column on the incident table.

Issue is that the u\_ext\_email\_address field on the incident table has an active edge encryption configuration and the u\_email\_address field on the new\_call table has no active edge encryption configuration and the copy fails. If you enable an edge encryption rule on the u\_email\_address field on the new\_call table then the inbound email action which creates the new\_call record fails because it's trying to insert data into an encrypted field. 

Error:

Invalid attempt to insert encrypted data into field: xxx in table xxx without going through an Edge Encryption proxy.

How can encrypted data end up in incident.u\_ext\_email\_address when copied from new\_call.u\_email\_address?

## Resolution

What can be done to handle this use case:

Add the Dictionary Attribute "Edge Encryption Clear Text Allowed" on the incident.u\_ext\_email\_address column (the column that has the active edge encryption configuration):  
  
[https://docs.servicenow.com/csh?topicname=r\_EdgeEncryptionDictAttributes.html&version=latest](https://docs.servicenow.com/csh?topicname=r_EdgeEncryptionDictAttributes.html&version=latest)  
  
Edge Encryption Clear Text Allowed \[edge\_encryption\_clear\_text\_allowed\]  
When set to true, allows server-side scripts to append non-encrypted data to an encrypted string within the field for user actions performed through the proxy server, or any server-side automated scripts, such as scheduled jobs.  
Value: true/false  
Target element: field  
Default value: false  
  
Then go to Edge Encryption Configuration -> Maintenance -> Scheduled Jobs and create a new scheduled job, e.g.:  
  
Name = encrypt incident.u\_ext\_email\_address  
Job type = Encryption  
Table = incident  
Column = u\_ext\_email\_address  
Run = Periodically  
Repeat interval -> could run this say every 10 seconds  
  
This will encrypt the incident.u\_ext\_email\_address columns by the running of the Encryption job.

Note that in this configuration UI updates (form view or list view updates) will not be allowed if NOT going through the Edge Encryption proxy for columns that have active Edge Encryption Configurations, i.e. you will see the error:

Invalid attempt to insert encrypted data into field: xxx in table xxx without going through an Edge Encryption proxy.
