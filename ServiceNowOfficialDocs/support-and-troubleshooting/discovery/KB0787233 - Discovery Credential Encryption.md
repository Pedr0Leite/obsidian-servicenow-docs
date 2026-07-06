---
title: "Discovery Credential Encryption"
aliases:
  - KB0787233
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787233
kb_number: KB0787233
last_modified: 2024-04-08
---

## Issue

**Credential Encryption Steps on MID Server:**

1.  When a brand new MID server starts up it generates a unique RSA public/private key pair.
2.  The MID Server connects to the instance for the first time with the public key.
3.  At this point, the MID server is untrusted, no credentials will be transferred to the MID server in this state.
4.  A MID server admin manually validates the MID server if trusted.
5.  Then MID server can request credentials as it is trusted.
6.  The instance encrypts the credentials with the public key of the mid server, only the specific MID with the private key can decrypt this.

**FAQs:**

1.  What encryption type is used? (3DES, AES128, AES256, other)  
      
    -   **Encryption Type:** RSA 2048  
          
        
2.  Where is the fixed key located?  
      
    -   **The key is located in Keystore:**  
          
        -   Keystore is a located at /<midserver installation directory>/agent/keystore/
        -   Each file in this directory is password protected  
              
            
3.  What security measures are in place protected that fixed key, and who has access to it?  
      
    -   Anyone who has access to the directory can access these files but needs a password which only the mid server has to decrypt them.
    -   From Orlando , Keystore directory is locked for everyone except MID Server admin.
4.  Is that key unique per instance?  
      
    -   The public/private keypair is unique per MID Server.
