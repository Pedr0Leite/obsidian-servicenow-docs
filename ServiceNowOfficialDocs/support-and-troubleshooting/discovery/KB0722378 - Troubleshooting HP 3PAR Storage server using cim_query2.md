---
title: "Troubleshooting HP 3PAR Storage server using cim_query2"
aliases:
  - KB0722378
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722378
kb_number: KB0722378
last_modified: 2024-04-07
---

## Troubleshooting HP 3PAR Storage server using cim\_query2

  

### Issue

# Description

* * *

Linux server which Discovered successfully doesn't show associated Storage Device & Storage Server in the Dependency View.

# Troubleshooting Steps

* * *

1\. ServiceNow has built a tool named "cim\_query2" using a query language.

2\. This cim\_query2 tool is the latest version which is modified from its previous version "cim\_query".

3\. To initiate this query builder you must call "cim\_query2.do" from the filter navigator, and the page opens as below,

![](cim_query2.do_homepage.jpgx)![](sys_attachment.do?sys_id=1ebaaca6db42b450e515c2230596197d)

4\. Proceed further querying storage server by filling on the required fields,

-   **IP Address**: IP address where SMI-S server hosted
-   **Namespace**: root/tpd
-   **MID Server**: MID server which could validate the target server
-   **Current Object**: TPD\_StorageSystem{Name='GenericSystem'} (which should be replaced by the identifier of the storage array
-   **Query**: CIM\_ManagedElement{CreationClassName='TPD\_StorageSystem',Name='0123456789ABCDEF'}

5\. Once upon querying, it should return respective volumes attached to it.

6\. If it doesn't return any Volumes, then the issue is related to SMI-S server which doesn't respond to cim query.

7\. In this situation, the target SMI-S server should be restarted in order to gather the required volume information.

8\. A sample query builder which was executed multiple times has returned volumes associated with the Storage server is as shown below,

![](sys_attachment.do?sys_id=12baaca6db42b450e515c22305961983)

In the above query, cyan background shows the query which was executed, 

"CIM\_ManagedElement{CreationClassName=‘TPD\_StorageSystem’,Name=‘2FF70002AC018A7D’}.CIM\_SystemDevice{ResultClass=CIM\_StorageVolume}"

where,

-   CIM\_ManagedElement{CreationClassName=‘TPD\_StorageSystem’,Name=‘2FF70002AC018A7D’} - executes a CIM "GetInstance" call for the named Object.
-   The "." indicates a CIM "Associators" call
-   CIM\_SystemDevice{ResultClass=CIM\_StorageVolume} - means to get SystemDevice associations to StorageVolumes.

\--> This query which I executed gets all Storage Volumes for the Storage Server.

# Alternate ways to query SMI-S server

* * *

1\. Use curl (Linux) or Invoke-WebRequest to post the correct XML to the SMI-S server  
\--> Check “XML Request” in cim\_query2 to get the correct XML to send.

2\. Use WBEMTest.

Docs: https://technet.microsoft.com/en-us/library/cc785775(v=ws.10).aspx

Executable: https://technet.microsoft.com/en-us/library/cc180684.aspx 

3\. Use CimNavigator from http://cimnavigator.com/  
\--> CimNavigator focuses on CIM, not SMI-S. It has trouble with SMI-S. I got some info from it by:

\> In 'Configure Host Connection' choose CIMOM Type "WBEMServices" or "OpenPegasus".  
\> After connecting choose namespace "root" under Edit/Namespaces.  
\> Go to Edit/Preferences/Associations, change Traverse (depth) to 1.  
\> Go to Tools/EnumerateInstances. Enumerate "CIM\_ManagedElement".  
\> Drag the 1st element onto the Associations Graph.  
\> Double click on any element to get it into the tree view.  
\> Select it in the tree view, switch to the "Properties" view.

# Additional Reference

* * *

Below are some useful references on,

1\. GetInstance: https://www.dmtf.org/sites/default/files/standards/documents/DSP200.html#2.3.2.2  
2\. Associators: https://www.dmtf.org/sites/default/files/standards/documents/DSP200.html#2.3.2.14  
3\. SMI-S ComputerSystem & Volume definition: https://www.snia.org/sites/default/files/SMI-Sv1.3r6\_Block.book\_.pdf (page 109)  
4\. Definition of StorageVolume: http://schemas.dmtf.org/wbem/cim-html/2.34.0/CIM\_StorageVolume.html
