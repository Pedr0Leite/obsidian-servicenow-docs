---
title: "Invalid XML schema error is observed while resolving WSDL generated from ServiceNow."
aliases:
  - KB0794095
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794095
kb_number: KB0794095
last_modified: 2024-04-08
---

## Invalid XML schema error is observed while resolving WSDL generated from ServiceNow.

  

### Issue

Invalid XML schema error is observed while resolving WSDL generated from ServiceNow.

The error looks like below on the Web Service Client:

![](/sys_attachment.do?sys_id=1e12e849db0cb4d04cfbeeb5ca96191f)

This issue has been reported for Web Service Clients like BusinessWorks, Cold Fusion and there might be some others too.

### Release

All

### Cause

Some web service clients require complex-types to have a name attribute parsed properly. They do not accept an element name and complex type name.

In OOB instance, by default the WSDL schema will look like the following

<xsd:complexType name="incidentgetKeysType">  
  

### Resolution

This is resolved by adding the following system property -

Name: _glide.wsdl.complextypenames_

Type: String

Value: False

  
This omits complex-type name attributes in generated WSDL documents

The Complex Type attribute after adding this property as mentioned above will look like the following in the WSDL:

<xsd:complexType>
