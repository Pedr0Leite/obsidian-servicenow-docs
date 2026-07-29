---
title: "[SAMP\NDS] Queries related to Normalization Data Services"
aliases:
  - KB0827882
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827882
kb_number: KB0827882
last_modified: 2024-04-08
---

## \[SAMP\\NDS\] Queries related to Normalization Data Services

  

### Issue

-   Post activating "Normalization Data Services" plugin and configuring around there are 2 scenarios noted, 

**Scenario-1:**

-   How is the related list 'Normalized Company Mapping' being set on the "core\_company" form?

**Steps to reproduce:**

1\. Login to the instance  
2\. Navigate >> Normalized Company Names >> Click New and add the name as "Normalized Company"  
3\. In the Related links under Normalized Mappings >> Click New and created 2 mappings as

a. Normalized Company  
b. Not Normalized Company

4\. Navigate >> core\_company and Click new and create Core Companies as

a. Normalized Company  
b. Not Normalized Company

5\. For the core\_company that are created, the Normalized Company mapping is not being set.

![](sys_attachment.do?sys_id=3ba2f08ddb8cb8d066e0a345ca9619ae)

**Scenario-2**:

-   Why doesn't normalization seem to work on Asset (when it does work on Configuration Item)?

**Steps to reproduce:**

1\. Login to the instance  
2\. Navigate >> Linux Server >> Create one CI record with Manufacturer as "Adobe"  
\==> Could see the Manufacturer changes to "Adobe Systems" i.e. it gets changed to Normalized "Adobe Systems"

![](sys_attachment.do?sys_id=37a2f08ddb8cb8d066e0a345ca9619b1)

3\. Similarly, goto alm\_hardware table and create a new asset for Linux Server and select Company = "Adobe"  
\==> Could see the Company field will not get Normalized i.e. doesn't change to "Adobe Systems"

![](sys_attachment.do?sys_id=bfa2f08ddb8cb8d066e0a345ca9619af)

  

### Release

-   Instance with Normalization Data Services plugin enabled.

### Cause

-   For scenario 1 - The "Normalized Company Mapping" records to populate it should satisfy the three conditions (briefed in Resolution section) to be shown in the related list of "core\_company".
-   For scenario 2 - OOTB Business Rules normalize the manufacturer on CI and model respectively and not the Assets.

### Resolution

**Scenario -1:**

-   The related list 'Normalized Company Mapping' under core\_company form is using ‘Relationships’ - ‘Normalized Company Mapping’  
    \- Table - sys\_relationship, Name - Normalized Company Mapping
-   Similarly for related list 'Normalized Company Name’ under core\_company form is using ‘Relationships’ - ‘Normalized Company Name’  
    \- Table - sys\_relationship, Name - Normalized Company Name
-   i.e. The "Normalized Company Mapping" records, which satisfy the following three conditions will be shown in the related list of core\_company.

1\. 'Name' of core\_company should be as the value of 'Normalized Name' column on "Normalized Company Mapping" record  
2\. Value of 'Table' column on "Normalized Company Mapping" record should be 'core\_company'  
3\. Value of 'Field' column on "Normalized Company Mapping" record should be 'name'

**Scenario -2:**

-   OOTB "Normalization Data Services" plugin provides two business rules,

a. Canonicalize Manufacturer Company CI, and  
b. Canonicalize Manufacturer Company Model.

-   These business rules normalize the manufacturer on CI and model respectively and not the Assets. It is OOTB behavior.
