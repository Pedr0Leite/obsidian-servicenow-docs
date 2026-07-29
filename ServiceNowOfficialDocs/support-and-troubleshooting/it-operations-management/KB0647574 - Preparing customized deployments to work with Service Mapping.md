---
title: "Preparing customized deployments to work with Service Mapping"
aliases:
  - KB0647574
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647574
kb_number: KB0647574
last_modified: 2024-04-07
---

## Issue

# Description

This article helps preparing customized deployments to work with Service Mapping. The procedures described below are optional and necessary only for deployments on customized instances.  
  
  

# Discovery source property is customized or outdated

### Cause

If you customized the Choices \[sys\_choice\] table, it may contain outdated values for the discovery source which do not support Service Mapping. 

### Solution 1

1.  In the ServiceNow instance, navigate to **System Definitions > Choice Lists**.
2.  Filter the table using these settings:  
    -   Element contains discovery
    -   Element equals discovery\_source
    -   Language equals en
    -   Table equals  cmdb\_ci
3.  Verify that the Value column contains the following values and that the spelling is as appears below:  
    -   ServiceWatch
    -   ServiceNow (not service-now)
4.  If these values are missing add them.
5.  If the spelling of the values is wrong, correct it. 

### Solution 2

-   Navigate to the System Properties \[sys\_properties\] table.
-   Filter the table using this setting: **Name** equals \*discovery.source. The glide.discovery.source\_name property is displayed.
-   Verify that the value for this property is set to ServiceNow.
-   If the value is not ServiceNow, change it to ServiceNow.
-   Save the property.  
      
      
    

# Some CI attributes in the Configuration Item \[cmdb\_ci\] table are mandatory

### Cause

If you have customized the Configuration Item \[cmdb\_ci\] table to make some attributes mandatory, and the discovery process does not set these attributes, the discovery fails.

### Solution  

-   Verify that there are no attributes that are defined as mandatory in the ServiceNow instance:
-   In the ServiceNow instance, navigate to **System Definitions > Script-Background**.
-   Enter the following script in the **Run script** pane:

var gr = new GlideRecord('sys\_dictionary');  
gr.addQuery('name', 'CONTAINS', 'cmdb');  
gr.addQuery('mandatory', true);  
gr.query();  
while (gr.next()) {  
        var updateName = gr.sys\_update\_name;  
                var updateGr = new GlideRecord('sys\_update\_xml');  
                updateGr.addQuery('name',updateName);  
                updateGr.query();  
                if (updateGr.hasNext()) {  
                                gs.log("Table: " + gr.name + "; Field: " + gr.element);  
                }  
}

3\. Click **Run Script**.

4\. Check the output. If there are mandatory attributes, they are listed by the CI type table. 

Notice that if a mandatory attribute is defined for a CI type that serves as a parent for other CI types, the child CI types inherit this mandatory attribute.

5\. There are a few ways of resolving the problem if there are mandatory attributes. Discuss them with the customer.   
  
  

# Status attributes for host CIs are manually modified

### Cause

Before starting the top-down discovery, Service Mapping checks if the device hosting the application CI exists in the CMDB and what this device status. The status information is stored as the following attributes in the Configuration item \[cmdb\_ci\] table:

-   Status
-   Operational status 

In the base system, Service Mapping is configured to ignore all hosts that are either

-   Not operational -   The Operational status \[operational\_status\] value is set to a value other than 1 (Operational).
-   Absent - The status \[install\_status\] column value is 100 (absent). 

If you have modified these attributes in the Configuration item table to have customized values, Service Mapping may not discover the CI whose status or operational status is different from the default values. 

### Solution

Add customized values to the system property that Service Mapping uses to decide if to run top-down discovery for the CI with these values.

1.  In the ServiceNow instance, navigate to the System Properties \[sys\_properties\] table.
2.  Click **New**.
3.  In the **Name** field, enter _sa.active\_operational\_status_ for the Operational status or sa.inactive\_install\_status for the Status.
4.  In the **Value** field, enter all the values considered by the system valid for running the top-down discovery. It is a comma-separated list of integers.
5.  Click **Submit**.

For example, if you have modified the Operational status to add the _Active_ setting with the value of 7, enter the following string in the Value field for the _sa.active\_operational\_status_ property_:7,1,3,4,5,6_

_![](sys_attachment.do?sys_id=97a8a82edb02b450e515c22305961939)_

# OOB relationships are removed

### Cause

Service Mapping is dependent on OOB relationships being present in the CMDB. The relationships is created by the CMDB plugin, and Service Mapping is depending on the sys\_id's to be the OOB sys\_id's. If they are removed, Service Mapping will fail.  
  

### Solution 1

Restore from 'Deleted Records':  
\- Go to the 'Deleted Records' table.  
\- Filter on the table 'cmdb\_rel\_type'.  
\- Select all the OOB ones.  
\- Click on 'Undelete record'.  
  

### Solution 2

Import from another instance:  
\- Go to an OOB instance on the same family and patch.  
\- Export the OOB relationships from 'cmdb\_rel\_type'.  
\- Import the relationships into the instance with the missing records, into the 'cmdb\_rel\_type' table.
