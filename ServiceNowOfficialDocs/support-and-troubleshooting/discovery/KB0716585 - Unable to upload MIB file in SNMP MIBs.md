---
title: "Unable to upload MIB file in \"SNMP MIBs\"
aliases:
  - KB0716585
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716585
kb_number: KB0716585
last_modified: 2024-04-07
---

## Unable to upload MIB file in "SNMP MIBs"

  

### Issue

# Symptoms

* * *

Unable to upload MIB file in "SNMP MIBs". The documentation says a file must be uploaded without a file extension, but when I try to do so I get a prohibited file type error.  

# Release

* * *

All Versions

# Cause

* * *

The system property glide.ui.strict\_content\_types  which is restricting to load only the selective files into the instance                         
[https://docs.servicenow.com/csh?topicname=restrict-file-extensions.html&version=latest](https://docs.servicenow.com/csh?topicname=restrict-file-extensions.html&version=latest) 

In the instance, we have a certain list of values and hence a file without an extension is not allowed to upload into the system 

# Resolution

* * *

To upload SNMP MIB file,

1\. Save your file as ".txt" extension

2\. Add "txt" in the "glide.attachment.extensions" property if not available

3\. Follow the steps

    a) Navigate to MID Server > SNMP MIBs.

    b) Click New to create a new record.  
        The MID Server MIB File form opens to create a new ecc\_agent\_mib record.

    c) Use the following information to fill out the form:

             Name: The name of the MIB.  
             Version: The version of the MIB.  
             Source: Use this field to note where the MIB was acquired, such as a URL.  
             Description: The description that appears in the ecc\_agent\_mib table.  
             Active: This check box denotes whether the MIB module is enabled or disabled in the instance.

    d) Click the Add Attachment icon (attachment icon) in the upper right to attach the actual MIB file to the new record.

The MIB name must begin with an alphabetical character.  
Remaining characters must be one of the following: alphanumeric, hyphen ( - ), or underscore ( \_ ).  
The file name must not have an extension. You can reference the existing MIBs for examples. Use the actual name of the MIB for both the MIB record name and the attachment name, but it is not required.

4\. Now, upload the "FILE\_NAME.txt" extension file to the SNMP MIB file

5\. Do an update on the MIB file record so that the extensions will be cleared out using business rule "MIB filename compliance"

Business Rule Name: MIB filename compliance  
/nav\_to.do?uri=sys\_script.do?sys\_id=b7b95305ef11210003d778f775c0fb34

#   
Additional Information

* * *

Please refer to docs below

[https://docs.servicenow.com/csh?topicname=t\_LoadAMIBModule.html&version=latest](https://docs.servicenow.com/csh?topicname=t_LoadAMIBModule.html&version=latest)
