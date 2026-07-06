---
title: "Post csv file using REST API is creating duplicate data sources "
aliases:
  - KB0815455
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815455
kb_number: KB0815455
last_modified: 2025-01-03
---

## Post csv file using REST API is creating duplicate data sources

  

### Summary

We can post the CSV file directly to the import set. But some cases it is creating new data sources with the file names which we sent in the postman tool

Below is the URL format which we use to send the attachment :

[https://<instance>.service-now.com/sys\_import.do?sysparm\_import\_set\_tablename=<table\_name>&sysparm\_transform\_after\_load=<true>](https://\<instance\>.service-now.com/sys_import.do?sysparm_import_set_tablename=\<table_name\>&sysparm_transform_after_load=\<true\>)  
  
Please refer below sample image to send the request with attachment using the POSTMAN :  
  
![](/sys_attachment.do?sys_id=105368cddb8874d0b55f0b55ca9619bd)

### Related Links

Please refer below different scenarios of creating new data source or using existing data source 

scenario 1:-  
\=======  
I have a data source already created and attached one file to it. Now I am sending a new request with a different file name like  " test.csv", so it is created a new Data Source with the file name "test.csv".  
  
scenario 2:-  
\=======  
Now from the postman, I am sending again one more request with the same file which I used in step 1 "test.csv", in this case, it is not created a new data source it is pointed to the existing data source "test.csv".  
  
scenario 3:-  
\=======  
if we change the file name to "test1.csv" and if send rest from "postman" it is creating a new data source with new file name "test1.csv"
