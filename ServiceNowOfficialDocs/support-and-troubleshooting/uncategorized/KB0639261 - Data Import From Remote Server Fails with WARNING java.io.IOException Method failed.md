---
title: "Data Import From Remote Server Fails with *** WARNING *** java.io.IOException: Method failed"
aliases:
  - KB0639261
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639261
kb_number: KB0639261
last_modified: 2024-08-16
---

## Data Import From Remote Server Fails with \*\*\* WARNING \*\*\* java.io.IOException: Method failed

  

### Issue

Data Import From Remote Server Fails with \*\*\* WARNING \*\*\* java.io.IOException: Method failed

  
  

# Problem

* * *

Importing data from a remote server fails and generates below exceptions. It might be a scheduled import or even you click Load All Records on the Data Source record.

com.glide.db.impex.datasource.DataSourceException: com.glide.db.impex.datasource.DataSourceException: java.io.IOException: Method failed:([https://remoteserver/filename)](https://129.195.234.94/locaux_fm.csv%29) null with code: 0   
at com.glide.processors.ImportProcessorWorker.loadDataSource(ImportProcessorWorker.java:181)   
at com.glide.processors.ImportProcessorWorker.startWork(ImportProcessorWorker.java:104)   
at com.glide.worker.AbstractProgressWorker.startAndWait(AbstractProgressWorker.java:86)   
at com.glide.worker.HierarchicalProgressWorker.startAndWait(HierarchicalProgressWorker.java:37)   
at com.glide.worker.ProgressWorkerThread.run(ProgressWorkerThread.java:53)   
Caused by: com.glide.db.impex.datasource.DataSourceException: java.io.IOException: Method failed: ([https://remoteserver/filename](https://129.195.234.94/locaux_fm.csv%29)[)](https://129.195.234.94/locaux_fm.csv%29) null with code: 0   
at com.glide.db.impex.datasource.DataSource.getFile(DataSource.java:312)   
at com.glide.db.impex.datasource.DataSource.getFile(DataSource.java:252)   
at com.glide.db.impex.CSVLoader.setDataSource(CSVLoader.java:127)   
at com.glide.db.impex.JDBCLoader.setImportDataSource(JDBCLoader.java:551)   
at com.glide.db.impex.datasource.CSVDataSource.getLoader(CSVDataSource.java:21)   
at com.glide.processors.ImportProcessorWorker.loadDataSource(ImportProcessorWorker.java:139)   
... 4 more   
Caused by: java.io.IOException: Method failed: ([https://remoteserver/filename](https://129.195.234.94/locaux_fm.csv%29)[)](https://129.195.234.94/locaux_fm.csv%29) null with code: 0   
at com.glide.protocol.http.HTTPURLConnection.connect(HTTPURLConnection.java:38)   
at com.glide.protocol.http.HTTPURLConnection.getInputStream(HTTPURLConnection.java:46)   
at com.glide.db.impex.datasource.DataSource.writeFile(DataSource.java:336)   
at com.glide.db.impex.datasource.DataSource.getFile(DataSource.java:305) 

# Cause

* * *

It appears after customers apply [ServiceNow Instance Hardening](https://support.servicenow.com/kb_view.do?sysparm_article=KB0550654#9.1 "ServiceNow Instance Hardening") KB0550654 and set **com.glide.communications.trustmanager\_trust\_all** system property false as a part of 9.1 Certificate Trust.

By default, ServiceNow trusts a certificate's Certificate Authority, CA, which ensures ServiceNow accepts self-issued certificates. When customers set this property false and their remote server is secured with a self-sign Certificate Authority, not a trusted CA, this import fails because the platform does not allow this.

# Solution

* * *

Customer can opt one of the following to fix this issue:

1.  Set system property **com.glide.communications.trustmanager\_trust\_all** as true.
2.  Or replace the self-signed certificate on their remote server with another one which is signed by a trusted CA.
