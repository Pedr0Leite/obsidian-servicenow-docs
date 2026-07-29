---
title: "SAMP Citrix publisher: Data regarding the applications published to Citrix is not being retrieved from the discovery of Citrix system."
aliases:
  - KB0859528
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859528
kb_number: KB0859528
last_modified: 2024-04-08
---

## Issue

Data regarding the applications published to Citrix is not being retrieved from the discovery of Citrix Delivery Controller.

## Resolution

Below data is collected from Delivery controller pattern extension step: Discover Published Applications And Machine Access  
https://<instance-name>.service-now.com/sa\_pattern\_list.do?sysparm\_query=nameSTARTSWITHdeli&sysparm\_view=  
  
Delivery Group: samp\_citrix\_delivery\_group  
Citrix Machine: .service-now.com/samp\_citrix\_machine  
Published Application to Delivery Group: .service-now.com/samp\_citrix\_application\_m2m\_delivery\_group  
Delivery Group Access: .service-now.com/samp\_citrix\_delivery\_group\_m2m\_user\_adgroup  
ADGroup Member table: This is empty  
samp\_citrix\_adgroup\_m2m\_user  
  
For data to be populated in above table few configurations must be enabled as below:  
1\. Active Directory PowerShell module must be active on the delivery controller.  
2\. Applicative credentials for the Domain Controller should be present (to read active directory).  
  
In the pattern extension "Discover Published Applications And Machine Access", the step "29. Parse formatted Group Member table" is where the data is being updated from the data we get from the step "27. Get Groups and Users".
