---
title: "Determining if your ODBC driver is working correctly"
aliases:
  - KB0538948
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538948
kb_number: KB0538948
last_modified: 2024-05-01
---

## Determining if your ODBC driver is working correctly

  

### Issue

Determining if your ODBC driver is working correctly 

Symptoms

* * *

-   Cannot connect to the instance
-   Error message received during processing
-   Queried information lost
-   Connection dropped

Cause

* * *

The ODBC driver may not appear to be working correctly because too many records are being pulled in a query, there are missing ACLs, or a 3rd party application is interfering with the query.  

Resolution

* * *

First, test the ODBC driver. To do this, create the system DSN in the ODBC driver and click the **Test Connection** button. Details on how to test the ODBC Driver can be found [here](https://docs.servicenow.com/csh?topicname=t_TestingTheODBCDriver.html&version=latest "here"). 

Try running a test query that returns only one record from a table, such as a single incident. To do this, run **select** **short\_description** **from incident where** **number=‘<existing\_incident\_number>’;** and put the incident number you are sure exists on your instance instead of **<existing\_incident\_number>.** This shows if the driver is running correctly, regardless of ACL issues or number of records. 

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><span style="font-family: arial, helvetica, sans-serif;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="bottom" border="" hspace="" vspace=""></span></td><td style="vertical-align: middle; text-align: left;"><span style="font-family: arial, helvetica, sans-serif;"><strong>Note</strong>: <span style="font-size: 10pt;">The ODBC driver is not designed to pull a lot of data at a time, so any queries you run should account for this.</span></span></td></tr></tbody></table>

If testing a single record does not work, try running the same query and excluding 3rd party applications. 

To determine if the ODBC driver is working correctly by excluding 3rd party applications, follow these steps: 

1.  Open ISQL (this comes with the ServiceNow ODBC Driver).
2.  Connect to the instance using the steps identified in [Running Interactive SQL (ODBC)](https://docs.servicenow.com/csh?topicname=t_UsingInteractiveSQLWithODBC.html&version=latest "Running Interactive SQL (ODBC)") in the ServiceNow product documentation.
3.  If you have special characters in your username or password, use the following:  
      
    _Customconnect "DSN=your\_dsn\_name; UID=username;PWD=password"  
      
    _
4.  Issue a SELECT statement to retrieve the records you are pulling in through your specific application.
