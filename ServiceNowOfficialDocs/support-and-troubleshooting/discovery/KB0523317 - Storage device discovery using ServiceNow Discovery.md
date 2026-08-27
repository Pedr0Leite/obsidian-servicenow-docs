---
title: "Storage device discovery using ServiceNow Discovery"
aliases:
  - KB0523317
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523317
kb_number: KB0523317
last_modified: 2024-04-30
---

## Storage device discovery using ServiceNow Discovery

  

### Issue

Storage device discovery using ServiceNow Discovery 

  
  

# Overview

* * *

The Service Location Protocol (SLP) is required for Common Information Model (CIM) Discovery as it is part of the Storage Management Initiative Specification (SMI-S) stack.

Some storage devices may support the WBEM ("Web-based Enterprise Management") protocol, but may not support SLP.

# Procedure

* * *

SLP can be configured manually. Most modern flavors of Linux offer the SLP daemon as an available software package. An OpenSource package is also available for Microsoft Windows.

After installing, users can manually register the WBEM services on SLP using another common Linux tool, called **slptool**. Slptool is a command line tool to make SLPv2 User Agent (UA) requests that usually come with the SLP daemon package. It can be used for SLP lookup/advertisement in shell scripts or as a diagnostic tool.

To register a service, you simply provide a URL and list of attributes. An example can be extracted from a working SLP server by using the same tool.
