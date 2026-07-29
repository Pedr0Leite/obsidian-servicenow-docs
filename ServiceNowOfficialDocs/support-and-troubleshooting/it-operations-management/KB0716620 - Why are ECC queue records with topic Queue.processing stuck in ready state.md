---
title: "Why are ECC queue records with topic Queue.processing stuck in ready state?"
aliases:
  - KB0716620
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716620
kb_number: KB0716620
last_modified: 2025-01-03
---

## Issue

# Description

* * *

The ECC queue table has records with topic as queue.processing and they seem to be stuck in a ready state.

# Procedure

* * *

The mid server sends records to the instance with topic as queue.procesisng to indicate that it is working on processing a request.

These records are marked processed by a business rule "ECC Queue - mark outputs state". In this business rule at line 26 

var sys\_table\_name = gr.getValue('sys\_table\_name');

the sys\_table\_name is gathered for the queue.processing record in ECC Queue table. The property of sys\_table\_name will be accessible for the ecc\_queue table only if the table is in table rotation.

If this table is removed from table rotation, the value of sys\_table\_name will be NULL and hence the records in the ECC queue will be stuck in ready state.

In order to fix this, please add the ecc\_queue table back to the table rotation. The out of box record for ecc\_queue in table rotation is as follows:

![](sys_attachment.do?sys_id=b06c286edb42b450e515c2230596198e)

# Applicable Versions

* * *

London
