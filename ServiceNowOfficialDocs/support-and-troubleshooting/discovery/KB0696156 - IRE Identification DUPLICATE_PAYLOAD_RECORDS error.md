---
title: "IRE Identification DUPLICATE_PAYLOAD_RECORDS error"
aliases:
  - KB0696156
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696156
kb_number: KB0696156
last_modified: 2025-09-30
---

## IRE Identification DUPLICATE\_PAYLOAD\_RECORDS error

  

### Issue

The identification and reconciliation engine (IRE) performs identification relying on identification rules. Based on the data passed to the IRE and the identification rules, the identification engine should find the correct configuration item (CI) in the configuration management database (CMDB). The IRE should be used when updating or creating CIs. Using the IRE leads to a consistent CMDB with no duplicates. 

Discovery patterns collect data from CIs and update the CMDB. However, it is possible that duplicate records within the same payload can be passed to the IRE. DUPLICATE\_PAYLOAD\_RECORDS error will be thrown when duplicate records are passed on the same payload to the IRE. DUPLICATE\_PAYLOAD\_RECORDS can be removed from a payload via steps in the pattern. This KB outlines a simple method of removing such duplicates. 

Example error:

DUPLICATE\_LOOKUP\_PAYLOAD Found duplicate Lookup items (0 and 1) in the payload index 22 using fields serial\_number,serial\_number\_type: no thrown error 

### Resolution

 A simple way to remove duplicates is to use the DuplicateRemover script. The steps would be:

1.  Determine the table in the payload with the duplicates. In the example above the table was cmdb\_serial\_number, the fields mentioned in the error will help in determining the correct table.
2.  Add a step to the pattern where operation = "Set Parameter Value".
3.  Fill out the Value with the script to remove the duplicates such as:  
    
    EVAL(
    javascript:
    // This table will be the new table without the duplicates
    var tableWithoutDuplicates = '';
    
    // Pass the table\_to\_remove\_duplicates\_from, and the columns to use for identification, to the DuplicateRemover
    tableWithoutDuplicates =  DuplicateRemover.removeDuplicates(${table\_to\_remove\_duplicates\_from},\["column\_1","column\_2"\]);
    
    // Replace original table with new table duplicates free
    CTX.setAttribute("table\_to\_remove\_duplicates\_from",  tableWithoutDuplicates);
    );
    
4.   The step should now look as such:  
    ![](sys_attachment.do?sys_id=4529a8eb47a3659011eaf24c736d4330)
5.  Save the step and publish the pattern.

**Notes:**

-   In most cases, it is best to add the step to remove duplicates right after the table with the duplicates is created.
-   The name in the step image above, $temp\_unique\_service, can be any name that does not match a variable already in use in the pattern.
-   The script will have to be updated to contain the correct table name and columns.
-   The columns mentioned in the script, column\_1, and column\_2, are what the script will use to determine what a duplicate is and should be replaced accordingly. If the rows for an example CI identifiable by only a column, let's say serial\_number, then only one column would be necessary as such:  
    
    tableWithoutDuplicates =  DuplicateRemover.removeDuplicates(${cmdb\_serial\_number},\["serial\_number"\]);
    

### Related Links

(1) Set sys\_properties record glide.cmdb.logger.source.identification\_engine to "info,warn,error,debug"  
(2) Run the following script:  
var eccRecord = new GlideRecord('ecc\_queue');  
eccRecord.get(''); // put the sys id of the input ecc queue  
var sp =new SncSensorProcessor(eccRecord);  
sp.process();  
(3) Review the output  
  
[Debugging Identification and Reconcilliation Engine using scripts in scripts background](https://hishowcase.service-now.com/kb?id=kb_article_view&sysparm_article=KB0793220)

[Identification and Reconciliation Components and Process](https://docs.servicenow.com/csh?topicname=c_CompsandProcessIDandReconcil.html&version=latest "Identification and Reconciliation Components and Process")

[Identification Engine Error Messages](https://docs.servicenow.com/csh?topicname=id-engine-error-messages.html&version=latest#d363848e812 "Identification Engine Error Messages")

['MSSql DB On Windows'  Pattern's "Collect MSSQL Components Info" shared library throws DUPLICATE\_RELATED\_PAYLOAD Found duplicate Related items (1 and 25) in the payload index 1 using fields binary\_path,service\_name,service\_type](https://support.servicenow.com/kb_view.do?sysparm_article=KB1116160 "KB1116160")

[Could not find host item in Identification engine output payload](https://support.servicenow.com/kb_view.do?sysparm_article=KB0744602 "Could not find host item in Identification engine output payload")
