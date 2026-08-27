---
title: "Storage-Level Encryption"
aliases:
  - KB0594570
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0594570
kb_number: KB0594570
last_modified: 2024-01-28
---

## Issue

  

# Overview

* * *

Storage-level encryption is a mechanism for customer data protection at rest. Storage-level encryption can be viewed as an additional or second-level of encryption for data that is already encrypted with **GlideEncrypter** data.

When enabled, storage-level encryption is used for the following data:

-   **password2** type fields in any table
-   Properties in the System Properties \[sys\_properties\] table of type **password1** or **password2**
-   Variables in the Values \[sys\_variable\_value\] table of type **password2**

For customers, storage-level encryption is transparent because it is performed on GlideRecord data.  
  

# Issues on older releases

* * *

Because this is a second level of encryption of already encrypted text, the problems listed below have been encountered in Geneva instances, resulting in the corruption of storage-encrypted data. These problems have been fixed since later Geneva and will not occur in any currently supported version.

-   [PRB668917](/nav_to.do?uri=problem.do?sys_id=de1f3a326fe2da401501f7307f3ee496 "PRB668917"), [PRB652074](/nav_to.do?uri=problem.do?sys_id=3b1777b66fe706c013568e4c2c3ee41c "PRB652074")
    
    Because the encrypted text is usually longer than the original, it might require a bigger column size to accommodate it; however, some **password2** fields are defined as just 40 characters, which is not long enough for double-encrypted text.
    
-   [PRB665720](/nav_to.do?uri=problem.do?sys_id=5776895d4f0e1e00f347524e0210c70f "PRB665720")
    
    Even though it is expected that the **password2** fields should be encrypted with GlideEncrypter, there are multiple cases when clear-text values are stored in **password2** fields.
    
    As a result, the older code did not properly handle such cases. For example, several incidents were related to saml2sp clear-text passwords that were corrupted into saml2so= (see PRB665720). The corruption occurs only for clear-text data where each character is Base64 and the value’s length is not a multiple of 4. Therefore, **password2** clear-text values with special characters like !, @, \*, %, & should not cause any issues.
    

![warning](/Warning_25x.pngx "Warning")**Warning**: Integrations that use data from **password2** fields can break if you do not change them. There are no warning messages in the logs related to this issue.  
  

# Planned and Scheduled Maintenance

* * *

You will be notified if maintenance is scheduled for your instance. In the case of **storage encryption**, there is maintenance planned that will make changes on your instance. This maintenance will:

-   Increase the length of **password2** type fields to 255 bytes for any password2 fields that were shorter than 255.
-   Encrypt clear-text data with a length that is not multiple of 4. 

After the maintenance runs, issues may occur if:

-   Customized scripts on **password2** fields that refer to clear-text values. These scripts might fail. See the **After the scheduled maintenance** section below for instructions on how to change your scripts.
    
-   Any system properties that have clear text values which are of type **password1** or **password2**.
    

### Before this scheduled maintenance:

Check with your instance administrator and your instance development team to see if you have customized scripts that run on **password2** fields. Make sure that the scripts do not assume that the values are in clear text.

Check the [system definition dictionary](https://docs.servicenow.com/csh?topicname=r_DictionaryEntryForm.html&version=latest "system dictionary") for **password2** columns and make sure they are over 255 bytes. You can filter the list of dictionary entries in the **System Definition > Dictionary** by filtering for entries of **Type** is **Password (2 Way Encrypted)** and **Max length** less than **255**. Change the Max Length to a value greater than 255. The maintenance will perform this task if you do not. This is not mandatory.

### After the scheduled maintenance:

If you do encounter issues after the planned maintenance, have your instance admin or development team look through all script customizations in business rules, script includes, etc., for script usages on **password2** fields. For example:

-   theGlideRecord.setValue('pwd2fieldName', 'some-value');
-   theGlideRecord.getValue('pwd2fieldName');

Replace these occurrences as by using GlideEncrypter as follows:

-   theGlideRecord.setDisplayValue('pwd2fieldName', 'some-value');
-   new GlideEncrypter().decrypt(theGlideRecord.getValue('pwd2fieldName');

  
Best Practices 

As a best practice, before enabling storage encryption, do the following:

1.  Look for all tables and password2 columns with a size less than 100 bytes.
2.  Increase the size to 255.
3.  Look for clear-text values stored in **password2** fields and system properties of type **password1** or **password2**.
4.  Encrypt located values with GlideEncrypter to avoid data corruption, which could occur after you enable storage encryption.

An example before this maintenance is performed:

1.  Table u\_test1 has a column u\_pwd with a size 40.
2.  u\_test.u\_pwd has a clear-text value “abc".
3.  u\_test.u\_pwd has a clear-text value “abcd".
4.  sys\_properties has a property of type **password2** with a clear-text value “xyz”.

After maintenance is performed:

1.  Table u\_test1.u\_pwd is altered, and its size becomes 255.
2.  The u\_test.u\_pwd value that was “abc” becomes “TGUdCrQRIt8=“ (encrypted with GlideEncrypter).
3.  The u\_test.u\_pwd value “abcd” does not change.
4.  sys\_properties with a clear-text value “xyz” becomes encrypted. For example,  {{dflt-gpaes}}wU2mS1Q/RtsHsgCPyOO7Bw==
