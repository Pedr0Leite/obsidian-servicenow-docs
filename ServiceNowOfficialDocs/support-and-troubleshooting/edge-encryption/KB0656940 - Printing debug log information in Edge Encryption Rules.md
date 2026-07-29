---
title: "Printing debug log information in Edge  Encryption Rules"
aliases:
  - KB0656940
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656940
kb_number: KB0656940
last_modified: 2024-07-30
---

## Printing debug log information in Edge Encryption Rules

  

### Issue

Printing debug log information in Edge  Encryption Rules

  
  

# Overview

* * *

Edge Encryption provides the ability to encrypt the column data before the data is sent over the Internet to the instance. The data remains encrypted while stored in the instance. The encrypted data is sent back to the proxy application when requested. Finally, the encrypted data is decrypted by the proxy before being sent to the client in company's network. Using Encryption Configurations, the column and the corresponding table can be configured so that the data is encrypted for that column. 

In HTTP requests on the way to the instance, for example creating an incident using Record Producer, it may be necessary to identify and encrypt sensitive information. You can write encryption rules to identify, interpret, and encrypt data in such requests, mapping fields in the request to Glide table-field names on your instance.

Encryption rules are scripts executed on the Edge Encryption proxy server to map fields in a request to fields in a table on your ServiceNow instance. An encryption rule tells the Edge Encryption proxy server how to encrypt data in custom payloads.

An Encryption rule contains three parts:

1.  Condition
2.  Action
3.  Order

Without the encryption rule, if an attempt is made to insert the data through HTTP request into the encrypted column even when the call is made from the proxy network, the insert fails.

During the creation of the encryption rules it might be necessary to include debug statements in the Condition in order to check if the conditions are met and encryption rules is invoked

Since Encryption rules are written in JavaScript and are executed on the client proxy, Server side debug statements(Glide APIs) such as gs.log cannot be used in-order for debugging purpose.

In order to print log statements for debugging purpose in Edge Encryption Rules, **print** function can be used as shown the the screenshot below.

The log information is printed in the wrapper log in the logs folder  The log folder can be found under the Edge Encryption Server installation folder.

Please note gs.log or gs.print statements does not work inside the edge encryption rules.

The below screenshots demonstrates how to include the print statement and where to check in the logs.![](sys_attachment.do?sys_id=b7dae8e6db42b450e515c22305961999)
