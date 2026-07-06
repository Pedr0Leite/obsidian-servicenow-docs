---
title: "MID Server won't start due to Root Certificate requirements - wrapper error \"The digital signature of the object did not verify\"
aliases:
  - KB0727033
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727033
kb_number: KB0727033
last_modified: 2024-04-07
---

## MID Server won't start due to Root Certificate requirements - wrapper error "The digital signature of the object did not verify"

  

### Issue

After installing or upgrading a MID Server, the MID Server may not start and the following error may be seen in the wrapper.log

2019/01/23 10:32:10 | --> Wrapper Started as Service  
2019/01/23 10:32:10 | Java Service Wrapper Standard Edition 64-bit 3.5.34  
2019/01/23 10:32:10 | Copyright (C) 1999-2017 Tanuki Software, Ltd. All Rights Reserved.  
2019/01/23 10:32:10 | http://wrapper.tanukisoftware.com  
2019/01/23 10:32:10 | Licensed to ServiceNow, Inc. for MID  
2019/01/23 10:32:10 |   
2019/01/23 10:32:10 | A signature was found in "<MID Server install folder>\\agent\\bin\\wrapper-windows-x86-64.exe", but checksum failed: (Errorcode: 0x80096010) The digital signature of the object did not verify. (0x80096010)  
2019/01/23 10:32:10 | Signer Certificate:  
2019/01/23 10:32:10 | Serial Number:   
2019/01/23 10:32:10 | 00 90 4d 8f d1 f3 86 8a ad 5f 17 e8 93 41 c3 08 f2   
2019/01/23 10:32:10 | Issuer Name: COMODO RSA Code Signing CA  
2019/01/23 10:32:10 | Subject Name: Tanuki Software Ltd.  
2019/01/23 10:32:10 | TimeStamp Certificate:  
2019/01/23 10:32:10 | Serial Number:   
2019/01/23 10:32:10 | 16 88 f0 39 25 5e 63 8e 69 14 39 07 e6 33 0b   
2019/01/23 10:32:10 | Issuer Name: UTN-USERFirst-Object  
2019/01/23 10:32:10 | Subject Name: COMODO SHA-1 Time Stamping Signer  
2019/01/23 10:32:10 | Date of TimeStamp : 2017/09/25 12:00:55  
2019/01/23 10:32:10 | The Wrapper will shutdown!

### Release

Mainly London and Madrid, after the Tanuki Java Wrapper version was upgraded to version 3.5.34, or New York or later with 3.5.36, but potentially any upgrade that includes a Tanuki wrapper version change where the Certificates compiled into their binaries have changed.

### Cause

The MID Server application runs inside a 3rd party Java wrapper provided by Tanuki. The executable files wrapper-windows-x86-64.exe and wrapper-windows-x86-32.exe are signed by a Certificate that depends on a **Root Certificate that may not be present on the Windows Server**.

-   London/Madrid use Tanuki Java Wrapper version 3.5.34, and New York uses 3.5.36, which are signed with an SHA-2 certificate, which depends on a COMODO root certificate.
-   Earlier ServiceNow versions used Tanuki Java Wrapper version 3.5.17, which is signed with a SHA-1 certificate, which depends on a USRTrust root certificate.

Since Wrapper version 3.5.34, the Wrapper binaries are dual signed with SHA-1 and SHA-2 hash algorithms to allow stronger verification at the OS level. On versions of Windows from Windows 7 and Server 2008 R2, SHA-2 is supported by the operating system for signed binaries, and so if the MID Server is installed on one of those Windows versions, then **the SHA-2 certificate in the binary must verify for it to run**, and that means the COMODO certificates up the chain must also be at the SHA-2 or higher level.

### Resolution

The [Tanuki troubleshooting documentation - "The Wrapper is reporting an error/warning about its signature when starting."](https://wrapper.tanukisoftware.com/doc/english/troubleshooting.html#9 "Tanuki troubleshooting documentation - \"The Wrapper is reporting an error/warning about its signature when starting.\"") clarifies this change, which occurred in their 3.5.28 version, and similar earlier ones.

The solution is to **ensure the latest COMODO root certificate is installed** for the Local Computer, or at least for the User that the MID Server service runs as (the "ServiceNow MID Server..." Service Logon user).

At the time of the Madrid release, a certificate with an expiry date of 1/19/2038 works fine, as shown in the mmc certificates screenshot below: 

![](/sys_attachment.do?sys_id=7d6da0e2db82b450e515c2230596193d)

**Note: The Tanuki support page may point you to an old Comodo download page** that will not work, and the clue that you have that is a 2020 expiry date and nothing listed in the Countersignatures section of the certificate details dialog box. Although the certificate chain appears to be all there, the MID Server will not start.

If you have this screenshot for the SHA-2 certificate, you will need to delete that older certificate, and import the latest one from Comodo. At the time of the Madrid release, the link was:  
[\[Root\] Comodo RSA Certification Authority (SHA-2) https://support.comodo.com/index.php?/Knowledgebase/Article/View/969/108/root-comodo-rsa-certification-authority-sha-2](https://support.comodo.com/index.php?/Knowledgebase/Article/View/969/108/root-comodo-rsa-certification-authority-sha-2 "https://support.comodo.com/index.php?/Knowledgebase/Article/View/969/108/root-comodo-rsa-certification-authority-sha-2")

![](/sys_attachment.do?sys_id=fd6da0e2db82b450e515c22305961942)
