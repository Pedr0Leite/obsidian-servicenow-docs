---
title: "Encryption text fields are not supported by inbound actions"
aliases:
  - KB0647661
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647661
kb_number: KB0647661
last_modified: 2024-04-07
---

## Encryption text fields are not supported by inbound actions

  

### Issue

Encryption text fields are not supported by email inbound actions 

Problem

* * *

Encryption is a process that scrambles information into a format that unauthorized parties cannot decode or use. Encryption text fields enable yoiu to encrypt the data stored on the field. It is available only for users with the role associated to the Encryption context.  

![Encryped text is not supported by inbound actions](sys_attachment.do?sys_id=002cac2edb42b450e515c223059619d8 "Encryped text is not supported by inbound actions")

Symptoms

* * *

If email inbound actions are set to populate the encrypted text fields, the following symptoms occur:  

-   The data could be store in clear text in the encrypted text field but it is not visible on the form.
-   The data could be stored on the fields with the encryption context but null as the encrypted value.
-   System logs could show "Input length must be multiple of 16 when decrypting with padded cipher: javax.crypto.IllegalBlockSizeException: Input length must be multiple of 16 "

Cause

* * *

Impersonation does not change the encryption contexts available to a user. Even while impersonating, you have only the encryption contexts available to you originally. Because inbound actions follow an implicit impersonation to the users associated to the sender of the email, the encryption context is not available for inbound actions for encryption or decryption.

Resolution

* * *

The use of encrypted fields is limited within the context of the associated role. It should not be used on email inbound actions because an implicit impersonation is involved. Consider using different integration methods (for example, REST messages) to populate the encrypted data where the impersonation is not required.

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="text-align: center;"><img title="Note" src="/Warning_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="text-align: left;"><strong>Warning</strong>: Impersonation does not change the encryption contexts available to a user. Even while impersonating, you have only the encryption contexts available to you originally.</td></tr></tbody></table>
