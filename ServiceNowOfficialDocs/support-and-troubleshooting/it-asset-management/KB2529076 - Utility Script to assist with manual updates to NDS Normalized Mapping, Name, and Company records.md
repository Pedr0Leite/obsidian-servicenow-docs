---
title: "Utility Script to assist with manual updates to NDS Normalized Mapping, Name, and Company records"
aliases:
  - KB2529076
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2529076
kb_number: KB2529076
last_modified: 2026-05-12
---

## Utility Script to assist with manual updates to NDS Normalized Mapping, Name, and Company records

  

### Issue

After implementing the Normalization Data Services (NDS) Guided Setup you may find inconsistencies with your existing records on the Company\[core\_company\] table with various cases such as unexpected Normalized true/false flag, Normalized Mappings not present, incorrect Normalized Mappings, etc. requiring you to create or update the Normalized Mappings manually.

Depending on each customer's unique data set this could be a handful of Company records or a few thousand Company records that you may want to update.

This article has a custom Script Include attached with some helper functions that can be called from a background script to assist with these tasks and provides a few use cases with examples.

### Facts

The Attached Script Include NDSUtils needs to be imported to your instance for the background script examples in this article to work.

**When NDS is active:**

-   Company records that have Normalized Mapping record and the Normalized Name referenced on the mapping record is that company name, the Company record will be marked Normalized = true.
-   Company records that have Normalized Mapping record and the Normalized Name referenced on the mapping record is NOT that company name, the Company record will be marked Normalized = false.
-   Company records that do NOT have a Normalized Mapping record will marked Normalized = true.

### Release

All Releases

### Resolution

**I. Import the attached Script Include NDSUtils**

**1.** **Download** file [sys\_script\_include\_NDSUtils.xml](https://support.servicenow.com/sys_attachment.do?sys_id=00d50ffd877043942d5cbbb5cebb3574&sysparm_this_url=u_kb_template_kcs_solution_for_cs.do%3Fsys_id%3Dcdbd06f79340b2545736b25d6cba10ef%26sysparm_view%3D%26sysparm_domain%3Dnull%26sysparm_domain_scope%3Dnull%26sysparm_record_row%3D2%26sysparm_record_rows%3D2%26sysparm_record_list%3Dshort_descriptionCONTAINSnormal%255ekb_knowledge_base%253d124c2ca22bb9f1002f42729fe8da152e%255eORkb_knowledge_base%253d2eade0e22bb9f1002f42729fe8da1578%255eORkb_knowledge_base%253da5f38d0b2be931002f42729fe8da1594%255elatest%253dtrue%255eauthor%253da48b2ce2dbc584503bf6a851ca961980%255eORDERBYDESCworkflow_state) attached to this KB.

**2.** Go to the **Script Includes** \[sys\_script\_include\] table on your instance.

**3.** **Right Click** the **Column Headers** at the top of the list.

**4.** Click **Import XML**.

**5.** Click **Choose File** and select **sys\_script\_include\_NDSUtils.xml**.  

**6.** Click **Upload**.

**II. Use Cases**

**Use Case 1**: List all of the Company records that are marked Normalized is True and do not have a Normalized Mapping record.

**1.** Go to the **Company** \[core\_company\] table.

**2.** Open the **bread crumb filter**.

**3.** Choose field **Sys ID**.

**4.** Choose operator **Is One Of**.

**5.** Set below to the input field.

```
javascript: new NDSUtils().getNormTrueWithNoCDN();
```

**6.** Click **Run**

\- A list of all the Company records where Normalized is True and have no Normalized Mapping will be returned.

 _\*\* On instances with a high number of such records the script can take a long time to return the list, thus it can also take an Encoded Query like "nameSTARTSWITHA" as input to shorten the list to all Normalized Company records starting with A that don't have a Normalized Mapping._

```
javascript: new NDSUtils().getNormTrueWithNoCDN("nameSTARTSWITHA");
```

**Use Case 2:** Normalized Company and Normalized Name with no Normalized Mapping record linking the company to the normalized name.

**Example:** You find four Company records below that are marked Normalized is true and should be mapped to Normalized Name "Canon" but aren't because there's no Normalized Mapping record with that Company Name linking it to the Normalized Name.

-   Canon
-   Canon Production Printing
-   Canon U.S.A
-   Canon U.S.A.

• One of these Company records will be the one that has a Normalized Mapping referencing the Normalized Name which matches that Company Name.

• Open the records and check which one has related records under the Normalized Company Mappings and Normalized Company Names related lists.

• The other Company records will have empty Normalized Company Mappings and Normalized Company Names related lists as they don't have a Normalized Mapping record.

• Once you identify the Normalized Company Name record, go ahead and copy it's Sys Id as it'll be needed as an input for the script.

**Procedure**

**1.** Identify the Normalized Name that you want the Normalized Mapping records to reference and copy it's Sys ID.

**2.** On the Company \[core\_company\] table, query to filter only the records that you want to create Normalized Mappings to the Normalized Name for.

**3.** After the list has been filtered, right click on the breadcrumb filter and select **Copy Query.**

Example of a copied query:  "nameLIKEcanon^canonical=true"

**4.** Go to **System Definition > Scripts - Background**

**5.** Copy and paste the below script, adding the Normalized Name's Sys ID and the copied Encoded Query to the inputs before running the it.

```
// 1. Add inputs here
var normalizedNameSysId = "";
var encodedQuery = "";

// 2. Click Run Script

// Do not edit below this line
var ndsUtil = new NDSUtils();
var gr = new GlideRecord('core_company');
gr.addEncodedQuery(encodedQuery);
gr.query();
while(gr.next()){
	var companyName = gr.getValue("name");
	ndsUtil.createMapping(companyName,normalizedNameSysId);
}
// Do not edit above this line
```

**6.** Click **Run Script**.

**7.** After the script completes the Normalized Mapping records will be created.

**8.** Finally you need to back to **NDS Guided Setup** and rerun steps **Normalize CMDB (Configuration Items)** and **Normalize CMDB (Configuration Items) Models** which will update the Company records to Normalized is False and update any CIs or Models referencing those company records with the normalized company they're now mapped to.

**Use Case 3:** Create Normalized Mappings for Companies based on similarity with Names on existing Normalized Mapping records.

```
// Set Inputs
var encodedQuery = "";
var similarity = 80;
var createMaps = false;

// Please do not edit below this line
var encQ = "canonical=true^" + encodedQuery;
var gr = new GlideRecord('core_company');
var nds = new NDSUtils();
gr.addEncodedQuery(encQ);
gr.setLimit(100);
gr.query();
while(gr.next()){
var name = gr.getValue('name');
nds.possibleMatch(name,similarity,createMaps);
}
// Please do not edit above this line
```
