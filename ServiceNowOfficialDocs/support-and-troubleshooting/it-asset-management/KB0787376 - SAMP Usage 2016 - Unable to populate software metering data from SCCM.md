---
title: "SAMP Usage 2016 -  Unable to populate software metering data from SCCM"
aliases:
  - KB0787376
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787376
kb_number: KB0787376
last_modified: 2026-06-19
---

## SAMP Usage 2016 - Unable to populate software metering data from SCCM

  

### Issue

-   When the data source is being executed, Job is pulling 0 records. Thus unable to populate software metering data from SCCM.  
      
    

![](sys_attachment.do?sys_id=042f9c49db0c70905a959c41ba961964)

### Release

ALL

### Cause

-   Stored Procedure not returning output. 
-   The query used in the Datasource is a Sample query, executing the data source **only** will not populate the data.

### Resolution

-   SAMP Usage 2016 job has a dependency on the reclamation rules. It requirs reclamation rules to be created with software products. These are the only set of products the usage will be fetched from SCCM.
-   In order to get the Software metering data from SCCM, run the "SAMP Usage 2016 Import" scheduled import which generates the SQL query on the fly using the reclamation rules.
-   This SQL query is generated using the "**getSQLStatement**" function of "**SAMPUsage2016Util**" script Include.   
      
    

![](sys_attachment.do?sys_id=8c2f9c49db0c70905a959c41ba961962)

-   Please make sure **to execute the parent "SCCM System 2016 Import" scheduled import job before executing the "SAMP Usage 2016 Import**". It will pull all the necessary Usage data from SCCM which is required for the later job.
-   Also, the process looks for **user\_name field on the sys\_user to compare against the user in the usage records from SCCM**. They both have to match (look at SAMPUsageUtil file to understand the lookup process).
