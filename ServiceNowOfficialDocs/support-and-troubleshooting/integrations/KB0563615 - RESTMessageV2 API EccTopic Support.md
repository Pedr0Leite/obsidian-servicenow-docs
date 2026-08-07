---
title: "RESTMessageV2 API EccTopic Support"
aliases:
  - KB0563615
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563615
kb_number: KB0563615
last_modified: 2025-09-21
---

## RESTMessageV2 API EccTopic Support

  

### Issue

# Overview

Starting with the Helsinki release, the RESTMessageV2 API includes the setEccTopic(String topic) and getEccTopic() methods.

These methods allow users to assign a custom probe business rule to handle REST responses. Assigning a custom probe business rule overrides all default ECC response handling for that RESTMessageV2 object, such as for asynchronous messages or messages sent via MID Server.

# API details

## setEccTopic(String topic)

Parameters:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Parameter</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Type</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Description</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">topic</td><td style="vertical-align: middle; text-align: left;">String</td><td style="vertical-align: middle; text-align: left;">The name of a business rule on the ECC Queue table that defines processing logic for the REST response.</td></tr></tbody></table>

Returns:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;">Type</td><td style="vertical-align: middle; text-align: left;">Description</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">None</td><td style="vertical-align: middle; text-align: left;">&nbsp;</td></tr></tbody></table>

Example:

var rm = new sn\_ws.RESTMessageV2();
rm.setEccTopic("CustomProbeBR");

**getEccTopic()**  
  
Parameters:  
  

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Parameter</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Type</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Description</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">None</td><td style="vertical-align: middle; text-align: left;">&nbsp;</td><td style="vertical-align: middle; text-align: left;">&nbsp;</td></tr></tbody></table>

Returns:

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;">Type</td><td style="vertical-align: middle; text-align: left;">Description</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">String</td><td style="vertical-align: middle; text-align: left;">&nbsp;The name of the ECC Queue topic that handles the response to this REST message.</td></tr></tbody></table>

Example:

var rm = new sn\_ws.RESTMessageV2();
var topic = rm.getEccTopic();
gs.log(topic);
