---
title: "Discover license consumption of Microsoft RDS CAL (Additive CAL) for Windows Server via Software Asset Management Publisher Pack for Microsoft"
aliases:
  - KB1947810
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1947810
kb_number: KB1947810
last_modified: 2025-03-12
---

## Issue

How can we calculate the license consumption for RDS Additive CAL and maintain it in the SAM Workspace.

## Resolution

Although Microsoft provides a seperate license for additive CAL (RDS- Remote Desktop Services CAL), the additive CALs are not supported via ServiceNow discovery.  
  

The procedure on how to setup Microsoft Server Software Base CAL as well as additive CAL on ServiceNow SAM Professional is provided in the below ServiceNow community article:  
[https://www.servicenow.com/community/sam-blog/microsoft-server-software-cal-setup-on-servicenow-sam-pro/bc-p/3191699#M326](https://www.servicenow.com/community/sam-blog/microsoft-server-software-cal-setup-on-servicenow-sam-pro/bc-p/3191699#M326)  
  
The article also highlights that since ServiceNow doesn't automatically discover Additive CAL usage like RDS CALs, obtain usage reports from your Windows Server administrator and manually record this information in SAM Pro.
