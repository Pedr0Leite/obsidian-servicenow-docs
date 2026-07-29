---
title: "Sensor error when processing Horizontal Pattern"
aliases:
  - KB0747648
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747648
kb_number: KB0747648
last_modified: 2024-04-07
---

## Issue

# Symptoms

During Discovery using patterns, we might encounter an error in the ecc\_queue input such as below :

Sensor error when processing Horizontal Pattern: -----------------------------

Stack:com.snc.sw.resulthandlers.HorizontalDiscoveryResultHandler.updateDeviceHistory(HorizontalDiscoveryResultHandler.java:580)

com.snc.sw.resulthandlers.HorizontalDiscoveryResultHandler.analyzeIdentificationEnginePayload(HorizontalDiscoveryResultHandler.java:551)

com.snc.sw.resulthandlers.HorizontalDiscoveryResultHandler.jsFunction\_analyzeIdentificationEnginePayload(HorizontalDiscoveryResultHandler.java:483)

# Release

Any

# Cause

1) The issue here is that we might see a NPE when calling the updateDeviceHistory method in the HorizontalDiscoveryResultHandler.java Class.

2) In this method, we are trying the grab the host name of the host items in the identification output payload, in order to update the Device history table.

3) These Host Items include the main CI type in the pattern as well as any Class that extends from cmdb\_ci\_hardware.

4) In the scenario where we are not able to grab the host name or the IP address of the Host Items present in the identification engine payload, the above error is thrown

# Resolution

1) Make sure the name or IP address is populated in the pattern for the main CI type as well as the CI's that extend cmdb\_ci\_hardware.
