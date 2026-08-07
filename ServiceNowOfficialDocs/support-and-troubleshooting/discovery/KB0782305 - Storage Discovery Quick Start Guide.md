---
title: "Storage Discovery Quick Start Guide"
aliases:
  - KB0782305
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782305
kb_number: KB0782305
last_modified: 2026-04-30
---

## Text

**Pre-requisites**

-   CIM server setup: Storage devices to be discovered should have SMI-S provider, for example CIM server having version 1.4+. SNMP shouldn't be used for storage discovery since it can only discover partial information about storage servers. Discovering storage via SMI-S will discover all of the storage infrastructure and relationships between storage components.
    
-   Connectivity: Ensure the connectivity between the MID Server and CIM server. For debugging any connectivity related issues, see the CIM Query section below.
    
-   Credentials: New CIM credentials need to be configured in the instance. **Note**: CIM server credentials could be different from the system hosting the prerequisite CIM server. For debugging any credential related issues, see the CIM Query section below.
    

**High level storage discovery flow**

**![](sys_attachment.do?sys_id=7fcdcd4e936803d0f2167de86cba1072)**

See detailed documentation [here](https://docs.servicenow.com/csh?topicname=c_Storage.html&version=latest).

**Troubleshooting using the CIM Query Tool**

The CIM Query tool can be useful for debugging connectivity and credentials related issues apart from various API responses from the CIM server.

The out-of-box tool in the instance: https://<INSTANCE\_NAME>/cim\_query2.do, allows you to obtain the results by querying the SMI-S server. Its looks similar to the below screen.

![](sys_attachment.do?sys_id=afcdcd4e936803d0f2167de86cba1019)

1.  Enter the IP address of the CIM server, namespace, and MID Server, then choose the desired heading and identifier.
    
2.  Query for the results.
    
    **NOTE**: Service Location Protocol (SLP) is an ad hoc protocol for retrieving and associating configuration information about the CIM server's exact interop namespaces. ServiceNow® Discovery retrieves the interop namespace of a CIM server via SLP and passes that information to the CIM Classify probe. Make sure to select the correct namespace while performing CIM queries. Alternatively, "Namespace" query can be used to retrieve all the namespaces for a given vendor.
    
3.  If there are any connectivity or credential related issues, the Query will fail. Correct the error reported and try to Query again.
    
    **NOTE**: The CIM Query option allows you to make queries that are not supported by the query language.
    

See the **Help** section at the top right of the CIM Query tool for more information.

![](sys_attachment.do?sys_id=f7cdcd4e936803d0f2167de86cba106a)

**Vendor specific details**

**NetApp storage discovery**

NetApp storage devices can be discovered either through native APIs or SMI-S.

-   Native API (ONTAPI).  
    -   Need to use storage server IPs and credentials for discovery.
    -   Follow this [link](https://docs.netapp.com/us-en/ontap-family/) for more information on ONTAP 
    -   There are two patterns: one for 7-mode systems and another for C- mode (Cluster mode) systems.

-   SMI-S  
    -   To discover NetApp devices via SMI-S, you need to provide SMI-S server's IP and SMI-S credentials.  
        

**FAQ on storage server discovery issues** 

**Q**: Can we have one CIM server across multiple storage vendors?

**A:** No. There is no SMI-S server that can be used for multiple vendors.

**Q:** If CIM-Classify probe doesn't return any response in the discovery.

**A1:** from CIM-Classify probe try changing the Probe parameter cim\_version from modern to legacy, if the parameter is already created.

**A2:** validate the added CIM credentials.

**Q:** 5,000 milliseconds timeout on connection http-outgoing-25 \[ACTIVE\]

**A:** 5000 milliseconds is the default value of the timeout probe parameters.     

     increase the value of probe parameters in the probe CIM - Classify

-   connection\_timeout
-   socket\_timeout

   If there is no probe parameter, create a new probe parameter and provide the value more than 5000ms

   refer to [KB0853483](/kb?id=kb_article_view&sysparm_article=KB0853483) for similar issue. 

**Q:** The target namespace does not exist

**Q:** Access to a CIM resource is not available to the client

****A:**** Run the query in the cim\_query2 tool from the servicenow instance. 

Provide IP address, namespace, mid server  and select any query to run. check for the response, if the repsonse has above mentioned errors.

run the same queries through postman either in the mid server or the target server. 

please find the attached postman queries [storage.postman\_collection.json.zip](/sys_attachment.do?sys_id=44ddcd4e936803d0f2167de86cba10e3&view=true "Attached by Pooja Halemani (NOW) 2021-08-11 00:33:39").

please modify the request by providing appropriate IP address, CIM credentials and the xml body for the query:

In the attached query the namespace is root/emc. this value should be replaced with the selected namespace along with CIMObject in the Request header.

In the Authorisation tab select basic auth and add the CIM credentials.

**XML query for Arrays:**

<?xml version="1.0" encoding="UTF-8"?>

<CIM CIMVERSION="2.0" DTDVERSION="2.0">

   <MESSAGE ID="329195" PROTOCOLVERSION="1.0">

      <SIMPLEREQ>

         <IMETHODCALL NAME="Associators">

            <LOCALNAMESPACEPATH>

               <NAMESPACE NAME="interop" />

            </LOCALNAMESPACEPATH>

            <IPARAMVALUE NAME="AssocClass">

               <CLASSNAME NAME="CIM\_ElementConformsToProfile" />

            </IPARAMVALUE>

            <IPARAMVALUE NAME="Resultclass">

               <CLASSNAME NAME="CIM\_ComputerSystem" />

            </IPARAMVALUE>

            <IPARAMVALUE NAME="ObjectName">

               <INSTANCENAME CLASSNAME="ECOM\_RegisteredProfile">

                  <KEYBINDING NAME="InstanceID">

                     <KEYVALUE TYPE="string" VALUETYPE="string">Array+1.3.0</KEYVALUE>

                  </KEYBINDING>

               </INSTANCENAME>

            </IPARAMVALUE>

         </IMETHODCALL>

      </SIMPLEREQ>

   </MESSAGE>

</CIM>

**XML query for NAS Head:**

<?xml version="1.0" encoding="UTF-8"?>

<CIM CIMVERSION="2.0" DTDVERSION="2.0">

   <MESSAGE ID="329198" PROTOCOLVERSION="1.0">

      <SIMPLEREQ>

         <IMETHODCALL NAME="Associators">

            <LOCALNAMESPACEPATH>

               <NAMESPACE NAME="interop" />

            </LOCALNAMESPACEPATH>

            <IPARAMVALUE NAME="AssocClass">

               <CLASSNAME NAME="CIM\_ElementConformsToProfile" />

            </IPARAMVALUE>

            <IPARAMVALUE NAME="Resultclass">

               <CLASSNAME NAME="CIM\_ComputerSystem" />

            </IPARAMVALUE>

            <IPARAMVALUE NAME="ObjectName">

               <INSTANCENAME CLASSNAME="ECOM\_RegisteredProfile">

                  <KEYBINDING NAME="InstanceID">

                     <KEYVALUE TYPE="string" VALUETYPE="string">NAS Head+1.4.0</KEYVALUE>

                  </KEYBINDING>

               </INSTANCENAME>

            </IPARAMVALUE>

         </IMETHODCALL>

      </SIMPLEREQ>

   </MESSAGE>

</CIM>

**Q:** Credentials bug with SMI-S server returning bad HTTP status code

**A:** refer the [KB0747645](/kb?id=kb_article_view&sysparm_article=KB0747645) for resolution

**Q:** CIM\_HostedAccessPoint - Invalid response from server

**A:** refer the [KB0853408](/kb?id=kb_article_view&sysparm_article=KB0853408) for resolution

**Q:** CMDB Identification Error: In payload missing minimum set of input values for criterion (matching) attributes from identify rule for table \[cmdb\_ci\_storage\_server\]. Add these input values in payload

**A:** refer the [KB0852915](/kb?id=kb_article_view&sysparm_article=KB0852915) for resolution

**Q:** HP 3PAR Mass Storage Array Discovery sets incorrect values in the Fibre Channel Port CI's Worldwide Node Name (WWNN) field

**A:** refer to [KB0852930](/kb?id=kb_article_view&sysparm_article=KB0852930) for resolution

Troubleshooting guide for HP 3PAR storage server can be found in [KB0722378](/kb?id=kb_article_view&sysparm_article=KB0722378)

More information on CIM Probe can be found [here](https://docs.servicenow.com/csh?topicname=r_CIMProbe.html&version=latest "here")

UI Action for displaying the storage relationships

1\. There is an ask from few customers to show the relationship between Storage Volumes, Server(VM Host), FC Disk and Storage Server(Arrays). "Show Used Volumes" UI action on the storage server form shows the relation between Storage Volumes, Server and FC Disk. Use the attached update(Show Used Volumes) set to import the UI action. PFA, update set (show used volumns.xml).

In the attached screenshot,  
"Volumes" are the storage Volumes,  
"Used by" is the server using the storage volume  
"As" are the disks on the server that are backed by the volume

![](sys_attachment.do?sys_id=c8ddcd4e936803d0f2167de86cba10b9)

  
2\. Few customers assume that the records in Storage Controller table are not actual storage controllers. But the fact is, in real world there is nothing called Storage Controllers. It is just the Servicenow term, customers can rename it by changing the label as per their convenience. We actually populate the entities that are in [http://schemas.dmtf.org/wbem/cim-html/2.34.0/CIM\_ProtocolController.html](http://schemas.dmtf.org/wbem/cim-html/2.34.0/CIM_ProtocolController.html)

**Interpreting the Information from CIM Classification**

-   After the classification completes, the classification scripts parse the result and verify if it is related to storage server or switch or fabric etc., based on this condition the respective probes will be triggered. Refer to "On classification script" under cim classifications for any of the records (discovery\_classy\_cim.do?sys\_id=6c83623337302000c7608c00dfbe5dda&sysparm\_record\_target=discovery\_classy\_cim&sysparm\_record\_row=2&sysparm\_record\_rows=4&sysparm\_record\_list=ORDERBYorder)
-   Each trigger probes under cim classification records has a condition script, the probe will be executed based on this condition. These values are assigned in the "On classification script" in cim classification.

**Namespace:**

-   Namespace groups the device partitions into groups
-   A device partition must only be associated with a single namespace at any one time
-   CIM defines an "interop" namespace that vendors aren't allowed to modify
-   Vendors can create their own namespaces and extend the class model however they want
-   In the CIM you start a query with the interop namespace. It will return an object that indicates its "true" namespace

For details about each namespace, refer to provider's documentation.

Please refer to below document for IBM Product

[https://www.ibm.com/support/pages/interoperability-namespace-list](https://www.ibm.com/support/pages/interoperability-namespace-list)
