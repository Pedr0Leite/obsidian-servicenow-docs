---
title: "How to add special characters as an input in REST Web Service activity "
aliases:
  - KB0718637
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718637
kb_number: KB0718637
last_modified: 2025-01-03
---

## How to add special characters as an input in REST Web Service activity

  

### Issue

## Description:

This article explains how to configure the input values for 'REST Web Service' activity if they are intended to include special characters like French accent (è) for example.

## Procedure:

 Specify "Do not escape text" as the "Additional Attribute" to the input variable parameters of the activity that are expected to have the special characters.

For more information, please refer to our documentation below:

[https://docs.servicenow.com/csh?topicname=t\_CreateARESTWebServiceActivity.html&version=latest](https://docs.servicenow.com/csh?topicname=t_CreateARESTWebServiceActivity.html&version=latest)
