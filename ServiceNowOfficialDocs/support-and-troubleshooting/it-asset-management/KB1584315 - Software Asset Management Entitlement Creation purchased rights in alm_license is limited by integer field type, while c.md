---
title: "Software Asset Management : Entitlement Creation : \"purchased rights\" in alm_license is limited by \"integer\" field type, while customer can have huge value that can only be contained by  \"Long\" type"
aliases:
  - KB1584315
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1584315
kb_number: KB1584315
last_modified: 2023-12-11
---

## Software Asset Management : Entitlement Creation : "purchased rights" in alm\_license is limited by "integer" field type, while customer can have huge value that can only be contained by "Long" type

  

### Issue

Software Asset Management : Entitlement Creation : "purchased rights" in "alm\_license" table is limited by "integer" field type, while customer can have huge value that can only be contained by  "Long" type  
  

### Release

This issue will be available for all Software asset management (SAM) customer's and are creating entitlement with purchase rights going beyond the integer limit of "2,147,483,647"

### Cause

This issue will be available for all Software asset management (SAM) customer's and are creating entitlement with purchase rights going beyond the integer limit of "2,147,483,647".

Open Entitlement page  
Create entitlement with purchased rights more than "2,147,483,647" , it will get changed to ""2,147,483,647" as the data type is = Integer.

### Resolution

To Remediate the above issue,  customers need to replace the below table's columns from "Int" to "Long".  
  
Below are the steps to be followed, based on the customer who is implementing the changes.

Category 1   
For new customer's which are starting SAM journey and are planning to use the large quantity as purchase rights with quantity more than "2,147,483,647".  
  
Steps : they can simply change table's column - data type from "Int" to "Long" , if the data is not available in this columns of tables. If data is available it will not allow direct updates from UI.  
  
Note : If data deletion / recreation is not possible, Kindly follow the steps provided in Category 2.  
  

Category 2   
Customer who are already live and wants to uptake new large quantity number for future use.  
  
Steps :   
For the tables they want to change the column from "Int" to "Long"

1.  Created a temp column with "Long" data type
2.  Copied values from actual - "Int" column to temp - "Long" column
3.  Clear actual column values
4.  Changed the data type of column of actual column from "Int" to "Long"
5.  Copy back the values from temp column to actual column.
6.  Delete the temp column.
7.  Save.

Please find the list of tables and columns which are required to be changed as part of "Integer" to "Long" and it's application for both category 1 and 2 customers.

< SAP Tables >  
  
SAP License Metric Measurement - "samp\_sap\_license\_metric\_measurement"

Column Name :

1.  Usage 

SAP engine Usage - "samp\_sap\_sw\_client\_access"

Column Name :

1.  Usage

  
Import Set table - "imp\_samp\_sap\_license\_metric\_measurement "

Note : imp\_samp\_sap\_license\_metric\_measurement - usage column is string so no change required.

Entitlement Table - "alm\_license"

Column Names :

1.  Active rights
2.  Purchased rights
3.  Number of packs
4.  Quantity
5.  Rights per license pack
6.  Total units
7.  Allocations available

< Reconciliation Tables >

License Metric Results - "samp\_license\_metric\_result"  
  
Column Names :

1.  Allocated in Use
2.  Allocated not in use
3.  Allocations needed
4.  Licenses available
5.  Not allocated
6.  Not allocated in use
7.  Rights consumed
8.  Rights needed
9.  Rights Owned
10.  Rights Used
11.  Rights Available
12.  Unlicensed SAP users

Remediation Options  - "samp\_remediation\_option"

Column Names :

1.  Rights Needed
2.  Actionable rights
3.  Rights Not allocated
4.  Unlicensed installs
5.  Unlicensed options
6.  Unlicensed rights
7.  Unlicensed sap users

Rights Used By  Table -  "samp\_entitlement\_result"

Column Names :

1.   Allocated in Use
2.  Not allocated in use
3.  Allocations needed
4.  Allocated not in use
5.  Rights Used

Rights Needed By Table - "samp\_remediation\_result'

Column Name :

1.  Rights Needed

  
< Purchase Order Tables >

Receiving Slip Line  -  "proc\_rec\_slip\_item"

Column Name :

1.   Quantity

Purchased order Line Items - "proc\_po\_item"

Column Names :

1.  Ordered Quantity
2.  Received quantity
3.  Remaining quantity

### Related Links

Customer's should ensure the below jobs / process to be stoped while performing the steps for changing the data type from "Int" to "Long".

1.   Reconciliation job
2.   Entitlement creation manual / Automated / playbook 
3.   Entitlement Import job
4.   SAP Import Data jobs

  
Note: If customer's faces any issues while following the above steps, Kindly reach out to ServiceNow support team for help and guidance.
