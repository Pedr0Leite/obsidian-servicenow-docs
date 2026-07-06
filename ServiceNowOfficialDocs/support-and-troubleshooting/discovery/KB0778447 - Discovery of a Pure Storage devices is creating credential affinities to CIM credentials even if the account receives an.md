---
title: "Discovery of a Pure Storage devices is creating credential affinities to CIM credentials even if the account receives an \"Access Denied\" error."
aliases:
  - KB0778447
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778447
kb_number: KB0778447
last_modified: 2024-04-08
---

## Issue

When you have multiple CIM credentials and When we try to run a scan of an IP address for a Pure Storage device, Discovery appears to randomly select a CIM credential to try first. In most cases, this is the wrong CIM credential. During the discovery, the CIM cred is tried to logon but fails with an "Access Denied" error. Instead of moving on to another CIM cred, Discovery is creating a Credential Affinity for the failed credential and then stopping the discovery as "Active, couldn't classify". So, future scans of that IP fail as it is using the bad Credential Affinity. 

## Resolution

You can also use the following workaround :  
  
1) Navigate to the mid server script include "CimQuery"   
  
Line no 340 Replace  
  
if (responseTxt.indexOf('Invalid Credential') > 0)  
  
with  
  
if ((responseTxt.indexOf('Invalid Credential') > 0) || (responseTxt.indexOf('CIM\_ERR\_ACCESS\_DENIED') > 0))  
status = 401;
