---
title: "Flow input/output data type \"Password (2 Way Encrypted)\" and REST capabilities passing via REST into header not being decrypted"
aliases:
  - KB0954949
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954949
kb_number: KB0954949
last_modified: 2025-04-23
---

## Text

How to correctly pass data in their Flow via REST per the "Password (2 Way Encrypted)" Flow action, as the data would not decrypt, having already attempted the following:

-   Encrypt their plain-text password manually with GlideEncrypter
-   Turn the variable into a password 2 way variable with GlideActionUtil.setEncryptedOutput(val)
-   Drag and drop this into a REST message

The correct way to encrypt and use a string for authentication between a Script Step and a REST Step is as follows in this example script:

(function execute(inputs, outputs) {  
var pw = inputs\['password'\];  
var username = inputs\['username'\];  
var cleartext = GlideStringUtil.base64Encode(username + ":" + pw);  
outputs\['unencrypted'\] = cleartext;  
var encrypted = new GlideEncrypter().encrypt(cleartext);  
outputs\['encrypted'\] = sn\_fd.GlideActionUtil.setEncryptedOutput(encrypted);  
})(inputs, outputs);

  
To clarify:

-   Inputs are both string types
-   The unencrypted output is a string type
-   The encrypted output is of Password2 type

In the Developer's REST step, it contained the following correct header, Authorization: Basic <encrypted pill>.
