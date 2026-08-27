---
title: "Troubleshooting \"[File] cannot be deleted\" errors in Wrapper log when attempting to AutoUpgrade MID server"
aliases:
  - KB0743708
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743708
kb_number: KB0743708
last_modified: 2024-04-07
---

## Troubleshooting "\[File\] cannot be deleted" errors in Wrapper log when attempting to AutoUpgrade MID server

  

### Issue

# Description

* * *

You observe the following symptoms:

-   MID server fails AutoUpgrade
-   Temporary service "Platform Distribution Upgrade" is still present
-   When attempting to start the "Platform Distribution Upgrade" service you note the service doesn't start and see errors in the Wrapper log
-   Errors repeat a message for "\[File\] cannot be deleted" until it timeouts
-   When logged in as the user for the service logon user you note that you are able to delete files in the directory

# Solution

* * *

This error comes from the UpgradeMain.CLASS file. CLASS files can be decompiled with software such as Eclipse Enhanced Class Decompiler.

Specifically this comes from the "missingOrCanDelete" function with lines 382-398.

What's occurring is that we attempt to open the files in the temp directory with Read/Write permissions and then close the file to verify if we can delete the file.

There are edge situations in which the client has configured the OS to allow for deletes, but not writes (ReadOnly) which result in the above code errors.

There are two solutions:

1.  Delete all the files in the indicated temp directory from the Wrapper log and restart the PDU service
2.  Remove any read/write restrictions on the files in the indicated temp directory and run the PDU service again

# Applicable Versions

* * *

All
