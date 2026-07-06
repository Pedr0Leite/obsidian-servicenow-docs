---
title: "Which features do MID Servers not support, depending on whether it is running on a Linux or Windows Host"
aliases:
  - KB0755179
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755179
kb_number: KB0755179
last_modified: 2025-02-14
---

## Which features do MID Servers not support, depending on whether it is running on a Linux or Windows Host

  

### Issue

Some ServiceNow features use MID Servers, and additionally rely on features of the host operating system, or 3rd party applications that only support certain operating systems.

The following table lists known limitations, which will dictate which Host OS the MID Server will need to be installed on. This list is not comprehensive, and does not include anything that would be expected to work on both Windows and Linux:

<table style="border-collapse: collapse; width: 100%; height: 119px;" border="1"><tbody><tr style="height: 13px;"><td style="width: 16.6667%; height: 13px;">&nbsp;</td><td style="width: 33.3333%; height: 13px; text-align: center;">Windows MID Server</td><td style="width: 33.3333%; height: 13px; text-align: center;">Linux MID Server</td></tr><tr style="height: 13px;"><td style="width: 16.6667%; height: 13px;">MID Server</td><td style="width: 33.3333%; height: 13px; text-align: center;">Yes</td><td style="width: 33.3333%; height: 13px; text-align: center;">Multiple installs on the same host not supported.<br>All Capabilities except:<br>PowerShell<br>WMI</td></tr><tr style="height: 27px;"><td style="width: 16.6667%; height: 27px;">Discovery</td><td style="width: 33.3333%; height: 27px; text-align: center;">Yes</td><td style="width: 33.3333%; height: 27px; text-align: center;">All Probes except:<br>Host Discovery of Windows devices.<br>Application Discovery of Windows Applications via Powershell APIs (MSSQL, IIS, etc.)&nbsp;&nbsp;</td></tr><tr style="height: 13px;"><td style="width: 16.6667%; height: 13px;">Orchestration</td><td style="width: 33.3333%; height: 13px; text-align: center;">Yes</td><td style="width: 33.3333%; height: 13px; text-align: center;"><p>All templates except Powershell.</p><p>Activities not supported:<br>AD Activity Pack<br>Exchange Activity Pack<br>SCCM activity pack</p><p>Plugins not supported:<br>Password Reset Orchestration Add-on<br>Client Software Distribution&nbsp;</p></td></tr><tr style="height: 13px;"><td style="width: 16.6667%; height: 13px;">IntegrationHub</td><td style="width: 33.3333%; height: 13px; text-align: center;">Yes</td><td style="width: 33.3333%; height: 13px; text-align: center;">Spokes not supported:<br>Microsoft AD spoke<br>Microsoft SCCM spoke</td></tr><tr style="height: 13px;"><td style="width: 16.6667%; height: 13px;">Patterns for Service Mapping / Horizontal Discovery</td><td style="width: 33.3333%; height: 13px; text-align: center;">Yes</td><td style="width: 33.3333%; height: 13px; text-align: center;">Pattern Steps not supported:<br>Get registry key<br>LDAP query<br>WMI method invocation<br>WMI query</td></tr><tr style="height: 27px;"><td style="width: 16.6667%; height: 27px;">Data collection and discovery using Netflow for Service Mapping</td><td style="width: 33.3333%; height: 27px; text-align: center;">No</td><td style="width: 33.3333%; height: 27px; text-align: center;">Yes</td></tr></tbody></table>
