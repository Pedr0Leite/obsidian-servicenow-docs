---
title: "Fix Script for Duplicate Hardware Models referencing non existent Company records"
aliases:
  - KB2533993
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2533993
kb_number: KB2533993
last_modified: 2026-05-12
---

## Fix Script for Duplicate Hardware Models referencing non existent Company records

  

### Summary

-   When Normalization Data Services (NDS) is implemented incorrectly or it's Guided Setup wasn't completed you may experience duplicate Model \[cmdb\_model\] records being created where the Model Name and Model Number are the same and the Manufacturer appears to be (empty). 
-   However, grouping these duplicate model records by Manufacturer or showing the XML of the record shows that there's a Sys Id with no display value in the model's manufacturer field. Because there's no display value, the Manufacturer field on the mode list 'appears' to be (empty).
-   If you query the Company \[core\_company\] table for a record with the Sys Id from the Model's manufacturer field, you'll find there's no such record, and thus the Model record is referencing a non existent Company record.
-   This is typically a 'symptom' of an incorrect/incomplete NDS setup resulting in Company records with invalid unique Hash values or their Normalized field incorrectly set to true or false.
-   When Company records are in this state, Discovery or any other data source that uses the MakeAndModel API to get existing or create new Models for CIs being brought into the CMDB will query NDS for a normalized Company record for the discovered manufacturer name and will create a new Company record if a 'normalized' company isn't returned.
-   Due to incorrect/incomplete NDS setup, the MakeAndModel API will try to create a new Company record that already exists and the insert of the new company record will  fail with a UNIQUE Key Violation in the backend DataBase.
-   This leaves the Sys ID for the Company record that was being created in the Model's manufacturer field and no Company with that Sys ID created.
-   This occurs each time that same Manufacturer and Model are discovered, and a duplicate Hardware Model is created.

The custom Script Include attached to this article has helper functions that can be called from a background script to use the below strategies to try and get the Manufacturers of the Models using the Model's name and then update the Model with that Company \[core\_company\] record.

**1.** Look for the Model's name on the SNMP OID Classification \[discovery\_snmp\_oid\] table and return the Manufacturer.  
**2.** Look for other Model records with same Model name AND have the existing Company/Manufacturer.  
**3.** A Model's Display Name is usually the manufacturer name + the model name, so try and parse the manufacturer name from the Display name.  
**4.** Finally, if no Manufacturer found then the script will log which Models need to be verified and set manually. 

### Facts

The Attached Script Include **ModelCleanUpUtil** needs to be imported to your instance for the background script examples in this article to work.

### Release

All Releases

### Instructions

**I. Import the attached Script Include ModelCleanUpUtil**

**1.** **Download** file [sys\_script\_include\_ModelCleanUpUtil.xml](https://support.servicenow.com/sys_attachment.do?sys_id=6863437d877c03942d5cbbb5cebb3530&sysparm_this_url=u_kb_template_kcs_how_to_for_cs.do%3Fsys_id%3Dc1ceac2897947a58f03d739c1253afe6%26sysparm_view%3D%26sysparm_domain%3Dnull%26sysparm_domain_scope%3Dnull%26sysparm_record_row%3D1%26sysparm_record_rows%3D15%26sysparm_record_list%3Dshort_descriptionCONTAINSscript%255ekb_knowledge_base%253d124c2ca22bb9f1002f42729fe8da152e%255eORkb_knowledge_base%253d2eade0e22bb9f1002f42729fe8da1578%255eORkb_knowledge_base%253da5f38d0b2be931002f42729fe8da1594%255elatest%253dtrue%255eauthor%253da48b2ce2dbc584503bf6a851ca961980%255eORDERBYDESCnumber) attached to this KB.

**2.** Go to the **Script Includes** \[sys\_script\_include\] table on your instance.

**3.** **Right Click** the **Column Headers** at the top of the list.

**4.** Click **Import XML.**

**5.** Click **Choose File** and select **sys\_script\_include\_ModelCleanUpUtil.xml**.  

6. Click **Upload**.

**II. Running the Script** 

**1.** Go to the **Model** \[cmdb\_model\] table.

**2.** Filter the table for records where **Manufacturer Is Not Empty** AND **Manufacturer.Name Is Empty** to get all of the Models referencing a non existent Company.

**3.** **Add further filter conditions** to split the number of records to be updated into smaller batches.

For Example: Name Starts with A

**4.** After the list has been filtered, **right click on the breadcrumb filter** and select **Copy Query**.

Example of a copied query:  "manufacturerISNOTEMPTY^manufacturer.nameISEMPTY^nameSTARTSWITHA"

**5.** Go to System **Definition > Scripts - Background**

**6.** Copy and paste the below script and add the copied **Encoded Query** to the input **before** running it.

```
// 1. Add an Encoded Query from the Model [cmdb_model] table 
var encodedQuery = ""; 

// 2. Click the 'Run Script' button

// Please do not edit below this line
var modelCleanup = new ModelCleanUpUtil();
modelCleanup.fixHardwareModels(encodedQuery);
// Please do not edit above this line
```

**7.** Click **Run Script.** 

**8.** After the script completes refresh the filtered Models list and check the results.

**9.** Any remaining Models still referencing an non existent Company will need to be verified manually.

**III. Updating multiple Models after verifying the Company manually.**

**After** you've identified the manufacturer.

**1.** Go to the **Model** \[cmdb\_model\] table.

**2.** **Filter** the table for records where **Manufacturer Is Not Empty** AND **Manufacturer.Name Is Empty**.

**3.** Add further filter conditions to specify **only the records that are going to be updated with that Manufacturer.**

**4.** After the list has been filtered, **right click on the breadcrumb filter** and select **Copy Query**.

**5.** Go to **System Definition > Scripts - Background**

**6.** Copy and paste the below script and add the **Manufacturer Name** and the copied **Encoded Query** to the input **before** running it.

```
// 1. Add the Manufacturers Name and the  Encoded Query from the Model [cmdb_model] table below
var manufacturerName = "";
var encodedQuery = ""; 

// 2. Click the 'Run Script' button

// Please do not edit below this line
var modelCleanup = new ModelCleanUpUtil();
modelCleanup.directlyUpdateMfr(manufacturerName,encodedQuery);
// Please do not edit above this line
```

7\. Click **Run Script**. 

8\. After the script completes refresh the filtered Models list and check the results.
