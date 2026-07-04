---
title: "Determining if you have the latest ODBC driver version"
aliases:
  - KB0538945
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538945
kb_number: KB0538945
last_modified: 2024-05-01
---

## Determining if you have the latest ODBC driver version

  

### Issue

Determining if you have the latest ODBC driver version

Symptoms

* * *

-   Cannot connect to the instance
-   Error message received during processing
-   Queried information lost
-   Precision errors received
-   Connection dropped

   
Cause

* * *

A common cause of ODBC driver issues is not having the latest ODBC version installed. If you do not have the latest version, uninstall the old version and install the new one.  

  
Resolution

* * *

To verify that your instance is running the latest ODBC version, check the build date and time of the ODBC driver. To do this, use **CheckVersion** located in the _Service-Now\\ODBC\\ip\\tools_ folder. This is an executable Windows host script that reports the build date and time of the current ODBC driver. Use the scrpt to determine which build of the ODBC driver is running. If the **CheckVersion** tool is absent, the ODBC driver is out of date and should be uninstalled and reinstalled. For more information, see [ODBC Driver](https://docs.servicenow.com/csh?topicname=c_ODBCDriver.html&version=latest "ODBC Driver") in the ServiceNow product documentation.  
  
Starting with the ODBC driver version 1.0.9 you can view the version of the installed driver in the Microsoft Windows **Programs And Features** control panel.  
  
Prior to ODBC driver version 1.0.7.1, the only way to identify the version is:  

1\. Go to _<installations\_folder>\\ODBC\\ip\\oajava\\service\_now_. 

2\. Open glide-odbc.jar as an archive. 

3\. Navigate to _META-INF_ folder. 

4\. Open _MANIFEST.MF_ file. 

5\. Look for the buildVersion or Implementation-Version property.
