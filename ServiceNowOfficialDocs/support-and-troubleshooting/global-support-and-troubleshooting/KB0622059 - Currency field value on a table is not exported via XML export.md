---
title: "Currency field value on a table is not exported via XML export"
aliases:
  - KB0622059
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622059
kb_number: KB0622059
last_modified: 2024-04-07
---

## Currency field value on a table is not exported via XML export

  

### Issue

Currency field value on a table is not exported via XML export

Problem

* * *

After export, the record from any table contains currency field to XML file. When modifying the currency value in the XML file and import gain, the currency field value does not update.  

Symptoms

* * *

1\. Open the core\_company table.  
2\. Open company **ACME Africa**, and set profit to **$1234.00**.  
  
![](sys_attachment.do?sys_id=291f3026db0ab450e515c2230596197e)  
  
3\. Export the record to XML file. The profit is shown on the XML file.  
  
![](sys_attachment.do?sys_id=a91f3026db0ab450e515c2230596198f)  
  
4\. Modify the value for **Profit**, a currency field, to **$1000.00**. Save the record.  
  
![](sys_attachment.do?sys_id=651f3026db0ab450e515c223059619a6)  
  
5\. Import the XML file saved from step 3.  
  
![](sys_attachment.do?sys_id=691f3026db0ab450e515c223059619c2)

Note that the currency field value did not update.  

 ![](sys_attachment.do?sys_id=791f3026db0ab450e515c223059619dd)

Cause

* * *

The XML export feature is designed to work for exporting records from a table as is (raw data), without dependents such as currency records. This behavior is as intended.  
  
Resolution

* * *

Export/Import of currency fields should be done through other methods such as Excel/Csv/Import sets where the value of the currency field is exported and imported.  
  
Any method involving direct web services or XML has to separately transfer the fx\_currency\_instance table records first, and then the parent records (thus wanted record).
