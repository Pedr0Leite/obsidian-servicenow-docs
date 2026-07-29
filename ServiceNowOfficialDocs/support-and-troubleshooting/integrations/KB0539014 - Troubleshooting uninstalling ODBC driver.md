---
title: "Troubleshooting uninstalling ODBC driver"
aliases:
  - KB0539014
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0539014
kb_number: KB0539014
last_modified: 2024-05-01
---

## Troubleshooting uninstalling ODBC driver

  

### Issue

Troubleshooting uninstalling ODBC driver

Symptoms

* * *

-   Uninstall will not complete
-   Error message received after uninstalling 

  
Cause

* * *

If you try to uninstall a previous version of a driver and receive an error message, some registry keys may need to be deleted to complete the uninstall.  

Resolution

* * *

If you are trying to upgrade to a new release and are attempting to uninstall the previous version of your driver, you may receive the following error message: 

![](/errormessage.pngx)

To correct this:

1.  Go to **Start > Search programs** **and file** and type _regedit_ in the search field.
2.  The **Registry Edit** application opens.
3.  Do one of the following:
    -   For 64 bit machine, navigate to **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\**.
    -   For 32 bit machine, navigate to **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall**.
4.  Delete the key that was displayed in the error dialog. In this example, it is {0B338284-2241-42A6-B7FC-9036BE730CEA}.
5.  Also, conduct a search for the keys containing ServiceNow and be sure to delete them.
