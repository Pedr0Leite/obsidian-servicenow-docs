---
title: "Topic Category and Topic Details are Null upon selection of HR Service"
aliases:
  - KB0779006
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779006
kb_number: KB0779006
last_modified: 2025-09-18
---

## Topic Category and Topic Details are Null upon selection of HR Service

  

### Issue

This article will be useful in scenarios where administrators are creating HR Cases from Email where HR Services are to be selected after the HR Case is created

### Resolution

In OOTB design Topic Category and Topic Details are selected on basis of HR Service Selected while creating the HR Case (HR Service is a mandatory field).

However while creating HR Case from email the Inbound Action sets hard coded value to the HR Service.

In scenarios where customer creates their custom inbound action and HR Service is selected manually, then in order to set the Topic Category and Topic Details fields we need to update the OOTB Business rule - Set Values of Topic Fields to run on Update (By default this business rule runs in Insert only).

  

  

### Related Links

\-> Custom Inbound Email action is defined to create Payroll case. That action does not set the HR service while creating case.  
OOB solution defaults topic details only while inserting the case based on HR service details. Business rule on case table - "Set values on Topic fields" sets the topic details.  
  
\-> If customer is having implementation is such a way that payroll case is always created with out a service and service is associated manually, then OOB provided BR logic has to be extended to on change of HR service also.
