---
title: "Troubleshooting JDBC connectivity and login to Microsoft SQL Server issues including SCCM Databases from MID Server"
aliases:
  - KB0748820
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748820
kb_number: KB0748820
last_modified: 2025-09-03
---

## Troubleshooting JDBC connectivity and login to Microsoft SQL Server issues including SCCM Databases from MID Server

  

### Issue

Importing data from Microsoft SQL Server via MID Server is very popular, but since this is an integration covering 2 endpoints (ServiceNow MID Server and MS SQL Server), it might be difficult to understand where the issue resides in case of an import failure.

This article will describe how you can validate the MS SQL Server connectivity from the MID Server host on Windows OS without the use of the ServiceNow platform. After following the steps described here, and if you have a successful connection, you will make sure that the SQL Server connection from the MID Server host is intact.

### Resolution

1\. Log in to your Windows MID Server host with the appropriate credentials.

If your SQL Server is enforcing "Integrated Windows Authentication" against your MS SQL Server, then login with the Windows user account that your MID Server is running under. You can gather this information from Windows Services applet after logging into Windows with admin privileges and by opening the MID Server service details:

![](sys_attachment.do?sys_id=5a1dbd78db8cb0d0471f9c41ba9619dc)

**Windows Integrated Authentication** option on ServiceNow data source is indicated with the flag "**Use integrated authentication**", but you should engage your SQL Server administrator to learn about the actual configuration on installed SQL Server.

If you have confirmed that you're not using integrated authentication, you can log in with any valid Windows user account.

  

**2.** Make sure you have enabled viewing filename extensions on File Explorer:

![](sys_attachment.do?sys_id=921dfd78db8cb0d0471f9c41ba96191d)

  

**3.** Create a new text file on your desktop by right-clicking on an empty area and navigating to **New** > **Text Document**:

![](sys_attachment.do?sys_id=1a1dfd78db8cb0d0471f9c41ba96191e)

  

**4.** Rename the file to have **.udl** extension:

![](sys_attachment.do?sys_id=9e1dfd78db8cb0d0471f9c41ba96191f)  

Windows will show a warning that the file might be unusable, but proceed with Yes:

![](sys_attachment.do?sys_id=161dfd78db8cb0d0471f9c41ba961921)

The file icon will change to a Data Link definition:

![](sys_attachment.do?sys_id=9a1dfd78db8cb0d0471f9c41ba961922)

  

**5.** Double-click on this file, and open the **Data Link Properties** dialog box. Populate the DB connection information that you have specified on the ServiceNow Data Source record.

If your SQL Server is enforcing Windows Authentication **and** you have logged into the MID Server host with the Windows credentials of the MID server process as mentioned in the 1st point, then you should select "**Use Windows NT Integrated security**":

![](sys_attachment.do?sys_id=121dfd78db8cb0d0471f9c41ba961924)

If your SQL Server is in Mixed Mode for authentication and you have specified a SQL Server account on the ServiceNow data source, then you should select "**Use a specific user name and password**":

![](sys_attachment.do?sys_id=961dfd78db8cb0d0471f9c41ba961925)

  

**6.** Click on **Test Connection**. If the connection successful, you should observe "**Test connection succeeded.**":

![](sys_attachment.do?sys_id=1e1dfd78db8cb0d0471f9c41ba961926)

This test concludes that your database connection information and credential validity are correct on the Microsoft SQL Server end.
