---
title: "How to check if traps are received properly on to MID Server from BMC TrueSight"
aliases:
  - KB0778199
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778199
kb_number: KB0778199
last_modified: 2024-04-07
---

## Issue

After configuring SNMP Traps on the source, events are not being seen in the instance. Also, there are no traces of the events processing in the MID agent logs. 

## Resolution

1.  Make sure the MID WebService Event Collector is configured properly by following the documentation: [Event collection from BMC TrueSight](https://docs.servicenow.com/csh?topicname=event-collection-BMCTrueSight.html&version=latest "Event collection from BMC TrueSight")
2.  Confirm from the Wireshark that the packets are received in below format:
    -   `http://<MID_Server_IP>:<MID_Web_Server_Port>/api/mid/em/inbound_event?Transform=TransformEvents_bmcTrueSight`.
3.  Apply the below filter as shown in the screenshot:
    -   ![](sys_attachment.do?sys_id=6c0b837cdb04b0d016d2a345ca961995)
4.  If you see "Unauthorized" messages, this means that the Username/Password is configured incorrectly on the source end.
5.  Also, if the messages are received as expected by MID server, you will notice **HTTP 200 OK** message in the Wireshark.  
    -   ![](sys_attachment.do?sys_id=e40b837cdb04b0d016d2a345ca961994)
6.  Correct the credentials configured and re-check if the "Unauthorized" errors got disappeared.  
7.  If yes, the event processing should be good now.

## Additional Information

If the issue persists after following the steps advised, please reach out to [ServiceNow Technical Support](http://www.servicenow.com/support/contact-support.html "ServiceNow Technical Support")
