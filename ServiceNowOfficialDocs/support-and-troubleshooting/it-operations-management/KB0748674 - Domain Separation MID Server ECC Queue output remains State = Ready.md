---
title: "Domain Separation: MID Server ECC Queue output remains State = Ready"
aliases:
  - KB0748674
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748674
kb_number: KB0748674
last_modified: 2026-05-19
---

## Domain Separation: MID Server ECC Queue output remains State = Ready

  

### Issue

ECC Queue \[ecc\_queue\] Output record State stays at "Ready", and "Processed" timestamp remains empty. However, other ecc\_queue similar output records perhaps with the same topic, mid server, and format in the source are quickly getting processed.

The instance is a MSP/Domain Separated one.

### Release

Any MSP Domain Separation enabled instance.

### Cause

Domain separation is the key to the issue. The ECC Queue has a Domain field, and the usual rules about record visibility applies. If the MID Server can't see the record, then it cannot pick up that job.

For example, the ecc\_queue topic was "RESTProbe" but it could have been any topic. The MID Server login user's sys\_domain was not in same sys\_domain as the RESTProbe ECC output record.

Other ecc\_queue output records with same topic, same mid server, same source, similar syntax in the name field, are getting processed as expected. The sys\_domain field value was "global" for these ecc\_queue output records.

MIDSERVER sys\_user record:

...   
<sys\_domain>2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b</sys\_domain>  
<sys\_domain\_path>!!!/!!#/!!!/!!!/</sys\_domain\_path>  
...   
<user\_name>MIDSERVERUSER</user\_name> 

Domain separated RESTProbe ecc\_queue output record:

<agent>mid.server.MIDSERVER</agent>   
<name>post</name>   
<processed/>   
<queue>output</queue>  
<source>http://source/subsource/actionname/action/</source>  
<state>ready</state>  
<sys\_created\_by>ADMIN</sys\_created\_by>  
<sys\_created\_on>2019-05-08 16:54:00</sys\_created\_on>  
<sys\_domain>1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a</sys\_domain>  
<sys\_domain\_path>!!!/!!#/!!!/</sys\_domain\_path>  
<topic>RESTProbe</topic> 

### Resolution

The MID Server records will get created in the same Domain as the login user set for that MID Server. MID Servers will tend to either be in

-   the Global domain, so that they can run jobs from, and see ecc\_queue output records from any domain.
-   or a leaf domain (the end of a branch, with no child domains), so that when the input ecc\_queue record retuns to the instance, the transaction to process it will be in the same domain as the output was. The jobs sensor will see the domain-specific data relevant to the job.

Using a MID Server in an intermediate domain often causes problems, and is not supported by some applications/integrations.

Changing the domain of a MID Server to match the job is problematic, because as well as changing the domain of the login user, all the MID Server's records will also need their domain changing to match. That is also likely to affect other features and integrations also using that MID Server.

So the solution is usually to ensure that the job that creates the e.g. RESTProbe is running as the correct domain to match the MID Server, so creates the ecc\_queue output record in the domain the MID Server can see.
