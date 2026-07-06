---
title: "Issue with FTPS Data Source - TLS Resumption"
aliases:
  - KB0792687
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792687
kb_number: KB0792687
last_modified: 2024-02-07
---

## Issue with FTPS Data Source - TLS Resumption

  

### Issue

The customer is facing an issue with the **File Transfer Protocol** (FTPs) data source with TLS Auth. They are getting a Secure Sockets Layer (SSL) handshake error while importing a .csv file.

Added a certificate of FTP server as well but no luck.

**Steps to reproduce:**

1.  Data source
2.  Load 20 Records

Will get an error as "**com.glide.db.impex.datasource.DataSourceException: java.io.IOException: Connection has been shutdown: javax.net.ssl.SSLHandshakeException: Remote host closed connection during handshake**"

### Release

NA

### Cause

-   Customer is using the below setting  'Require TLS session resumption' while communicating to ServiceNow :  
    ![](sys_attachment.do?sys_id=8fd2428497d339100ed83bbe2153af97)
-   There is an issue with the FTP Client at ServiceNow end :
    
    The error in the log is: (from 3rd party)  
      
    (000700) 12/18/2019 15:51:17 PM - (not logged in) (103.23.65.12)> TLS connection established  
    (000700) 12/18/2019 15:51:17 PM - (not logged in) (103.23.65.12)> USER servicenow  
    (000700) 12/18/2019 15:51:17 PM - (not logged in) (103.23.65.12)> 331 Password required for servicenow  
    (000700) 12/18/2019 15:51:17 PM - (not logged in) (103.23.65.12)> PASS \*\*\*\*\*\*\*\*\*\*\*\*\*  
    (000700) 12/18/2019 15:51:17 PM - servicenow (103.23.65.12)> 230 Logged on  
    (000700) 12/18/2019 15:51:17 PM - servicenow (103.23.65.12)> PROT P  
    (000700) 12/18/2019 15:51:17 PM - servicenow (103.23.65.12)> 200 Protection level set to P  
    (000700) 12/18/2019 15:51:18 PM - servicenow (103.23.65.12)> PASV  
    (000700) 12/18/2019 15:51:18 PM - servicenow (103.23.65.12)> 227 Entering Passive Mode (52,64,250,91,195,167)  
    (000700) 12/18/2019 15:51:18 PM - servicenow (103.23.65.12)> RETR /LMSExtract\_20191217\_030003.csv  
    (000700) 12/18/2019 15:51:18 PM - servicenow (103.23.65.12)> 150 Opening data channel for file download from server of "/LMSExtract\_20191217\_030003.csv"  
    (000700) 12/18/2019 15:51:18 PM - servicenow (103.23.65.12)> 450 TLS session of data connection has not resumed or the session does not match the control connection  
    (000700) 12/18/2019 15:51:18 PM - servicenow (103.23.65.12)> QUIT
    

  
  
  
  

### Resolution

When the customer unchecked the setting 'Require TLS session resumption' while communicating to ServiceNow, the issue with the  FTPS data source is resolved.

**NOTE:**

ServiceNow does not support TLS Resumption and currently has no plans to do so. We strongly recommend using SFTP over FTPS as FTPS is no longer supported by some firewall vendors.

### Related Links

Not requiring session resumption allows session stealing attacks. The problem with FTP is that the data connection does not authenticate the client: Imagine you a want to upload a new version of your website. To initiate the transfer your client sends the PASV command followed by the STOR command. The server opens a port and waits for the client to connect to it and upload the file. Now an attacker comes along and figures out the port the server listens on. He connects to the port before you can and uploads a piece of malware to your website.  
  
TLS session resumption prevents this, it acts as a form of authentication. If the TLS session of the data connection matches the session of the control connection, both the client and the server have the guarantee that the data connection is genuine. Any mismatch in sessions indicates a potential attack.
