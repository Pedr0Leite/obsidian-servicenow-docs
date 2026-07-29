---
title: "Unable to establish connectivity to Postgresql data source from ServiceNow"
aliases:
  - KB0790097
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790097
kb_number: KB0790097
last_modified: 2025-04-10
---

## Unable to establish connectivity to Postgresql data source from ServiceNow

  

### Issue

Unable to establish connectivity to Postgresql data source from ServiceNow.

This article explains how to set up the Data Source and troubleshoot any connectivity issues.

### Resolution

Follow the documentation for 'JDBC drivers for unsupported database formats'.

Extend the available JDBC driver options by creating a new choice list entry to specify the JDBC driver Java package name.

1.  Navigate to System Import Sets > Administration > Data Sources.
2.  Click New.
3.  In the Data Sources form, right-click the Format field label, and select Show Choice List from the pop-up menu
4.  Click New in the list of choices.
5.  Provide the following values to create the new database choice. Look at the existing drivers for examples.
    
    -   **Table**: sys\_data\_source
    -   **Label**: Database name that appears as an option in the Format choice list, for example: **Teradata**.
    -   **Value**: Package name and class of the driver. For example, the value for TeraData is **com.ncr.teradata.TeraDriver**.
    
6.  Click Submit.(check  screenshot  below)
    
    The new data source now appears in the list of available JDBC formats.
    
    ![](sys_attachment.do?sys_id=e6571aaa47e202d0b6d8aa25126d430b)
    
    ## Install a driver on a MID Server
    
    You can install a new JDBC driver JAR file to a MID server to access database formats that are not supported by default.
    
    1.  Navigate to MID Server > JAR Files.
    2.  Click New.
    3.  Complete the following fields:
        
        -   **Name**: A unique and descriptive name for identifying the file in the instance.
        -   **Version**: A version number for the file, if one is available.
        -   **Source**: Location of the JAR file for reference purposes. Source information is not used by the system.
        -   **Description**: Short description of the JAR file and its purpose in the instance.
        
    4.  Click the paper clip icon in the banner and attach the JAR file to the record.
        
        ![](/sys_attachment.do?sys_id=f2b95eaa936682d0e7eef35d6cba101d)
        
    5.  Click Submit.
    6.  Restart the MID Server service.
        
        The platform makes the JAR file available to any MID Server configured to communicate with the instance.
        
        **Now configure the data source with the right connection parameters .**
        
        If there are any issue such as below:
        
        _MID Server reported error: java.sql.SQLException: com.snc.automation\_common.integration.exceptions.InvalidConnectionParameterException: Unable to load JDBC driver: Postgresql_
        
        Verify that the connection can be made successfully outside servicenow by running the below java program .This could be run from Eclipse IDE
        
        ```
        import java.sql.Connection;import java.sql.DriverManager;import java.sql.SQLException;public class doIt {public static void main(String a[]){try{Class.forName("org.mariadb.jdbc.Driver");//For customer: Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver"); (try{Connection con = DriverManager.getConnection("jdbc:mysql://<database>:<port>/<databasename>","<username>","<password>");//For customer: "jdbc:sqlserver://<DBSERVER>:1500;selectMethod=cursor;databaseName=CM", "<username>", "<password>")System.out.println("Connected Successfully");} catch (SQLException ex) {System.out.println(ex);}} catch (ClassNotFoundException ex) {System.out.println("Driver not found.");}}} //end
        ```
