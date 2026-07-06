---
title: "SSH Private Key test credentials are failing with \"Authentication failed\"
aliases:
  - KB0693449
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693449
kb_number: KB0693449
last_modified: 2026-05-22
---

## SSH Private Key test credentials are failing with "Authentication failed"

  

### Issue

Under "SSH Private Key Credentials" type, add valid User name, password, SSH private key and optional SSH passphrase and click on "Test credentials" UI Action.Though all these information is accurate, the user can still see **"Authentication failed"** error message.

Along with the above, mid server logs would show an error message as below.

**`SSHProtocolEngine SEVERE *** ERROR *** Private key decode failure: Did not recognize PEM Header / Footer or unsupported algorithm`**

### Release

All

### Cause

The private key must be entered in the proper format to ensure it is correctly encrypted.

Copying and pasting SSH Private Key as a single line may lead to authentication failure. Usually, the private key should be copied exactly in the format as it is shown below. Whole SSH key is parsed to read the ending of header and starting of footer strings. The key to understanding this is the new line ASCII character ( \\n ).

\-----BEGIN RSA PRIVATE KEY-----  
  
  
Proc-Type: 4,ENCRYPTED  
DEK-Info: AES-128-CBC,16E71E389E846A79607EB5DAE36CD64C  
  
  
ffa+1dHRiZNDpmucGw9i4maaBAg/zgeCLy28PAEGhlNLeRiXHBZnZgmQ2Z/vdWCf  
A1QbWwdcMec4Lklr3ZezNK+ZzKx5Y6jODd2VSKErlS5ue5QlboKDZlXmES1ewxl1  
  
  
Ycl99/s7V0uzdNDjd+Se0vqTkLsfRDPPiQN4icmrpKUed8VKpA33CIiXyOqa5QTO  
wXsD4+BG9PCT1svSEZOtwNZK3AwxaW0bVpzhGTGJcXkdH96zV4JyuJ/5H17e634M  
sAzLPE5cAtUCKUHJ+FWmrxof93Y1Xux9JrS7J2NgbBQcdRChDZ/8E5DuXfJ2DztK  
k1Imtl1SH4Ffy3LOqK1r06bB5NdavqENEaHKAdbirZQWws03f2uZbrnuOfJ0hbe5  
DKCwOQjg3WfoENTmwSQ4ZqmeouU+fi1+GecYRrVGOtCY7da7tjFmwb/sDkAF+P/P  
k3FtyLewUcGrH8rsQHlEBEeOhWvDHivSqe1LCR/KX2XPM+XeHCwB4SksbrRVs1Mm  
BASFrr8enf5BmZ14iq+J9O0ajsLZ/6vOkD6Ido5Kc654PXh2gztoYx/9dz7QLnkW  
D7vrpz3+dTZlMcsqoP6Tgg9Q041VEpiahYxI07V99GHhhUJGbAZyg2qe7BknOT7D  
sYqkv30Sa8GZZg7zv9VXLAf9cd7UslDR+OPS5wYSxrQ1T8W6N6p9oZ3/mDti7Dp7  
5Fps+IPXnw3j4cDt51uEzz7v6+CYQT7GbBkcZIP00jrmd6D9WEt2pMVjWBT81hPT  
g4zTWqQfzi72bjOX/g5eof0ECk/+quauTc5pw4tXL6XHWzcFo731O2cLgvt0ciHw  
CEfaDFAl6dYXcm9oU8gvkAgtLLtxNm9w6eRRMhTleCoNIV2ct5S4l/AcQ2qaRPtq  
  
  
\-----END RSA PRIVATE KEY-----

### Resolution

-   User should enter the SSH Private Key in the appropriate format.
-   For any reason, if we are not copying the Private Key in the above format or If we are copying the SSH key as a single line, make sure to add **\\n** (new line ASCII character) string at the end of header ( -----BEGIN RSA PRIVATE KEY-----\\n ) and starting of footer ( \\n-----END RSA PRIVATE KEY----- ).
