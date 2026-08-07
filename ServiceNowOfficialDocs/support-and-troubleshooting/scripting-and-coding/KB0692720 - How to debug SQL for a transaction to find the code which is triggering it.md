---
title: "How to debug SQL for a transaction to find the code which is triggering it"
aliases:
  - KB0692720
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692720
kb_number: KB0692720
last_modified: 2025-04-23
---

## How to debug SQL for a transaction to find the code which is triggering it

  

### Issue

This will help troubleshooting the exact SQL query which is resulting slow or incorrect, and the code which is calling the incorrect or unexpected SQL.

### Release

All releases

### Resolution

1.  In the Application Navigator, select '**Debug SQL (detailed)**' and '**Debug Log**' options. This will help you find the SQL for a specific transaction, as having the log is essential for debugging.  
      
    
2.  Open up the Chrome developer tools and switch to the Network tab. This tab will display all the network requests made by the application, allowing you to identify the specific network transaction that is causing the issue.  
      
    
3.  Reproduce the issue with developer tools and Debug SQL activated and take note of any slow network transactions. By reproducing the issue, you can see the network requests in real-time and identify the transaction that needs further investigation.  
      
    
4.  If the transaction is happening on a page or list load, you should see the SQL output below that page or list. This is because the SQL output is typically displayed along with the page or list load, making it easy to identify the SQL associated with the transaction.  
      
    
5.  If it is not happening on the page or list load, you will need to open a new page to '/ui\_page.do'. This is because the SQL output may not be displayed on the initial page load, and you may need to navigate to a different page to see the SQL output.  
      
    
6.  Search for the transaction name from the Network tab to identify the start of the transaction. This will help you narrow down the list of network requests and focus on the specific transaction that you are investigating.  
      
    
7.  If you are looking for slowness, find the slow transaction using the time value of the SQL output or look for SQL which is being very repetitive. If you see a lot of repetitive SQL, it could be making a bunch of quick queries, but in excess, which adds up to slowness.  
      
    
8.  To determine the Code which is triggering the SQL, click the small + at the end of the SQL statement to expand the Stack track for what triggered the SQL. This will show you the code that executed the SQL, allowing you to trace back to the source of the issue.  
      
    
9.  Normally, you can look for a **GlideRecord.query** line and then follow the code backward (down the call stack) from that to find the script, business rule, or Java file which is doing the GlideRecord query. This will help you identify the specific code that is causing the SQL query to be executed, allowing you to debug and fix the issue.  
      
    
10.  Any configurable code that is called in the stack trace will be shown in the format {table\_name}\_{sys\_id}. For example, if you see a stack trace line that has  "sys\_script\_fb678e75d4d1e1d88b1ff162390578f6" in it, this means that a record from the sys\_script table with sys\_id fb678e75d4d1e1d88b1ff162390578f6 was being executed. You can navigate to that table using the Application Navigator and entering {table\_name}.FILTER to open the list UI for that table. Then build a filter to match the sys\_id field to find that particular record. Alternatively, you can use the browser address bar to directly navigate to the relevant record directly with the format https://myinstance.com/{table\_name}\_list.do?sys\_id={sys\_id}. So, for example, if your instance name is acme.service-now.com, and you wanted to navigate to the sys\_script record from earlier, you would put https://acme.service-now.com/sys\_script.do?sys\_id=fb678e75d4d1e1d88b1ff162390578f6 into the address bar.

### Related Links

The transaction that is trigging the SQL shown in debug log should also present a similar message when the transaction has ended, with the time it took for that specific line of SQL to run, and the exact SQL query which is being run. You can hover over the ... between SELECT and FROM to see which fields are being queried.

This is an example of the Java files to look at to determine what is calling the glideRecord query that eventually runs this SQL:

![](sys_attachment.do?sys_id=d35f3c9e9701e290f03d739c1253aff0)

In your browser developer tools network tab you will see multiple requests, search for the one with the longest time spent waiting for a server response. Note that ServiceNow has a feature known as Session Synch that blocks server processing of a user's requests until the previous requests for that user have completed. This means that some requests that appear long running in the network tab may be _victims_ of a longer running request that started before them and was running simultaneously.

![](sys_attachment.do?sys_id=1b5f3c9e9701e290f03d739c1253aff2)
