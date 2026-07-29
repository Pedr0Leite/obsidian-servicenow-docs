---
title: "How to trace an Oracle DB unlicensed install"
aliases:
  - KB0870831
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870831
kb_number: KB0870831
last_modified: 2025-01-03
---

## How to trace an Oracle DB unlicensed install

  

### Summary

This article explains how the Oracle Database license metrics are calculated and how to trace an unlicensed install. 

-   **The Oracle DB Named User Plus (NUP) License Metric calculation is as follows:** 

-   -   **For Oracle DB Enterprise Edition:**

Highest of the below two:

-   -   -   Physical host CPU Count x No. of Cores per CPU x Core Factor x Metric Attribute (_Minimum Users Per Processor_)
        -   Number of Client Access Records per Physical Server 

-   -   **For Oracle DB Standard Edition:**

Highest of the below two:

-   -   -   Physical host CPU Count x Metric Attribute (_Minimum Users Per Processor_)
        -   Number of Client Access Records per Physical Server

  

-   **For Oracle DB Per Processor License Metric Calculation:** 

-   -   **For Oracle DB Enterprise Edition:** Physical host CPU Count x No. of Cores per CPU x Core Factor  
        
    -   **For Oracle DB Standard Edition:** Physical host CPU Count   
        

### Release

Paris

### Instructions

How the calculation is done for a physical host:

-   The license calculation starts with the Software Installation record in cmdb\_sam\_sw\_install table. 
-   If the Software Installation is installed on a Virtual Server then we will need to find the Physical Server and get a list of all Software Installations installed on it. This is done by:  
    -   From the related lists of the virtual server, find the name of the physical server 
    -   navigating to System Definitions > Database Views > samp\_vminstall\_on\_pinstall view > Try it
    -   Filter: _Child_ is <physical\_server\_name> and _Normalized Product_ is <DB Server>
    -   You will get a list of all the Software installation records on that physical server. Now, add _sys\_id_ field to the form and copy the list of _sys\_ids_.

-   If however, the Software Installation is on a Physical Server, then just note the _sys\_id_ of this installation record.
-   Get the list of Oracle DB instances that are linked to those installations by navigating to Oracle Instances cmdb\_ci\_db\_ora\_instance table and filter on: _Software Install_ is <sys\_ids\_from the previous\_step>
-   Note the _sys\_ids_ of those oracle instances
-   Finally, open the Client Access samp\_sw\_client\_access table and filter on: _Database Instance_ is <sys\_ids\_noted\_from\_previous\_step>
-   Add the _Total user count_ of all the records and that will give you the total number of Client Access Records.
-   Finally add this to the calculation provided earlier to see the number of licenses needed.

### Related Links

-   In Pre-Paris releases, the license is calculated per _Oracle_ _Instance_ instead of per _Physical Server._
-   At least 1 [Client Access](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/task/t_AddAClientAccessRec.html "Client Access") record is **needed** in order to calculate the NUP license for that Physical server. Client Access records are created manually. This can be done by querying the _oracle\_dba\_users_ table to identify which applications/devices/users are accessing the Oracle database server instance.
