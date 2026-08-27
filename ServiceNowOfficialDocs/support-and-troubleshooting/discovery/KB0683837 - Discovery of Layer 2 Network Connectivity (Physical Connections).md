---
title: "Discovery of Layer 2 Network Connectivity  (Physical Connections)"
aliases:
  - KB0683837
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0683837
kb_number: KB0683837
last_modified: 2024-12-11
---

## Discovery of Layer 2 Network Connectivity (Physical Connections)

  

### Issue

This knowledge base article covers how layer 2 discovery information is processed.

### Debugging procedure

-   Set the ’sa.discolog.sys\_log’ system property to true.
-   Run the following script in scripts-background: ​  
    -   var npm = new SNC.NetworkPathManager();
    -   npm.createPhysicalConnections(ciId);
-   In case of layer 2 connection between a server and a switch, the ciId should be the sys id of the server.​
-   In case of layer 2 connection between 2 switches, the ciId should be the sys id of one of the switches.
-   Look at the debug messages to understand why the connection was not created.
-   Note: The actual relation in the CMDB is created between the ports of the devices or between port of one device directly to another device (in case the target port was not found).
-   The algorithm is not creating a direct relation between the server and the network device or between 2 network devices.

### What are layer 2 connections?

-   layer 2 connections are physical connections between network devices and between network devices and other components, such a servers.
-   The layer 2 algorithm uses several strategies, together with information from various tables to create Connects to:Connected by relationships in the CMDB.
-   These relationships can be created between the ports of the devices or between port of one device directly to another device (in case the target port was not found).
-   The results can be viewed in the dependency view map by applying the ‘Physical Network Connections’ dependency type on the relevant device.
-   When applying this dependency type, we always see a dependency between the devices and not between their ports (even if the ‘Connects to::Connected by’ relation in the CMDB is actually between the ports of the devices).

### Required Plugins

-   Discovery plugin 

### How It Works

-   Prior to New York, a script action called ‘Create Layer 2 connections’ listened to the ‘discovery.device.complete’ event and triggered the layer 2 connections algorithm for each such event.
-   Starting from New York, we created a new event for layer 2 connections creation and created a separate event queue for this event.
-   The name of the event queue is ‘physical\_connections\_creation’ and the new event is called ‘physical\_connections.create’.​
-   A Script action named ‘Queue layer 2 connection calculations’ listens to the ‘discovery.device.complete’ event and creates a 'physical\_connections.create’ event with the CI sys Id as a parameter in the ‘physical\_connections\_creation’ event queue.
-   A new job named ‘Layer 2 Connectivity Creation’ is responsible for the processing of the ‘physical\_connections.create’ events.​
-   A Script action named ‘Create Layer 2 connections’ listens to these events and triggers the layer 2 connections algorithm for each such event.​
-   The purpose of this change is that the processing time of the layer 2 connections events will not influence the processing of other events and slow the event queue performance .​
-   This change was introduced via PRB1344266 (fixed in NY, MP6, LP10).​

-   In Orlando, we added an enhancement to reduce the amount of times the layer 2 connections algorithm is triggered.​
-   Instead of queuing the ‘physical\_connections.create’ event for each ‘discovery.device.complete’ event, the ‘Queue layer 2 connection calculations’ script action finds the last time the layer 2 connections algorithm was triggered for the CI reported in the event. Only if the period of time passed since the last time the algorithm was triggered is more than one day (configurable by ‘sa.create\_physical\_connections.minutes\_frequency’ property), a 'physical\_connections.create’ event is created for this CI.​
-   This change was introduced via PRB1359923 (fixed in O, NP4, MP9).​
-   The ‘Create Layer 2 connections’ script action (that listens to the ‘physical\_connections.create’ event) calls the java method NetworkPathManager.jsFunction\_createPhysicalConnections(String deviceId).​
-   This method finds the layer 2 connections and creates the relations of type ‘Connects to::Connected by’ in the CMDB.​
-   For ESX servers: there is a business rule called: "Create Layer 2 Connections from ESX" that calls the java method NetworkPathManager.jsFunction\_createPhysicalConnections(String deviceId).​

### Related Tables 

-   In order to create the layer 2 connections, we use the following tables:  
    -   discovery\_switch\_fwd\_table  
        -   The forwarding table of the switches
    -   discovery\_device\_neighbors  
        -   Used in order to find layer 2 connections between switches
        -   Contains a field called neighbor\_source which can be CDP or LLDP
    -   discovery\_switch\_spanning\_tree\_table  
        -   Used in order to find layer 2 connections between switches.
    -   discovery\_switch\_bridge\_port\_table  
        -   Used to map between port number in discovery\_switch\_fwd\_table and interface index.
-   Port tables:  
    -   cmdb\_ci\_network\_adapter
    -   dscy\_switchport
    -   dscy\_router\_interface
-   All the tables are populated during the horizontal discovery of the device.

### Layer 2 Connection Strategies  

-   **PhysicalHostConnectionStrategy** – Creates layer 2 connections between a discovered server, which is not a network device, and a network device.
-   **VMLayer2ConnectionStrategy** - Creates layer 2 connections between a VM and a network device.
-   **NetworkDeviceLayer2ConnectionStrategy** - Creates layer 2 connections between a network device and its neighbors.
-   **SpanningTreeLayer2ConnectionStrategy** - Creates a layer 2 connection between network device and the parent of the network device in the spanning tree.
-   **JavaScriptLayer2ConnectionStrategy** – Calls a java script function with empty implementation. We can add the function implementation on a customer instance in case we want to add another strategy. 

### PhysicalHostConnectionStrategy 

-   Creates layer 2 connections between a discovered server, which is not a network device, and a network device.
-   Prerequisites:  
    -   Horizontal discovery of the server
    -   Horizontal discovery of the network device.
-   Note: The discovery order matters. The switch needs to be discovered first in order the forwarding table, switch port table etc. will be populated. Then the server needs to be discovered. After the discovery of the server is complete, the layer 2 connections algorithm runs.
-   After the horizontal discovery was performed, we should validate the following:​  
    -   The network device has a forwarding table.​
    -   The server has ports (network adapters or router interfaces).

-   Step 1: Find the ports (network adapters and router interfaces) of the server.​  
      
    
-   Step 2: For each port, try to find if there is a layer 2 connection from the port:  
    -   Get the MAC address of the port.
    -   Navigate to discovery\_switch\_fwd\_table and search for records with this MAC address (and status field is not ‘self’).
    -   For each such record, search if there are more records in the forwarding table with the same switch (configuration item) and port but with different MAC addresses.
    -   Only in case there is only a single MAC on the port in the forwarding table of the switch, this switch is considered as a candidate (if we have more than one MAC it indicates that there is more than one source address so there is no layer 2 connection between the server and the switch).​
    -    In case the number of candidate switches does not exceed the value defined in sa.network.max\_candidate\_switches property (default is 2), create layer 2 connections to all the candidate switches.
-   Step 3: Try to find the port of the target switch and create the layer 2 connection  
    -   Navigate to discovery\_switch\_bridge\_port\_table and query this table by the switch (configuration item) and the port from the discovery\_switch\_fwd\_table.
    -   If a record found, get the interface index of the record.
    -   Query dscy\_switchport by the switch (configuration item) and interface index (interface number) in order to find the port.
    -   If the port was not found, Query dscy\_router\_interface by the switch (configuration item) and interface index (number) in order to find the port.
    -   If the port found in dscy\_switchport table or dscy\_router\_interface table has install status absent, the layer 2 connection is created directly to the switch and not to the port.
    -    In case the port of the switch was found, create a relation of type ‘Connects to::Connected by’ between the port of the server to the port of the switch. Otherwise, create a relation of type ‘Connects to::Connected by’ between the port of the server to the switch itself.
        

### VMLayer2ConnectionStrategy 

-   Creates layer 2 connections between a VM/ESX and a network device.​
-   Prerequisites:  
    -   Horizontal discovery of the network device.​
    -   vCenter discovery (horizontal discovery of the ESX and all the VMs that are on this ESX) - should be done twice. ​
-   Note: The discovery order matters. The switch needs to be discovered first in order the forwarding table, switch port table etc. will be populated. Then the vCenter discovery needs to be performed. After the discovery of the VM or ESX is complete, the layer 2 connection algorithm runs.​
-   After the horizontal discovery was performed, we should validate the following:​  
    -   The network device has a forwarding table.​
    -   The VM/ESX has ports (network adapters or router interfaces).​
    -   Each VM has **one of the** following:​  
        -   'virtualized by’ relation to the ESX
        -   ‘instantiated by’ relation to VMWare Virtual Machine Instance that has ‘registered on’ relation to the ESX​

-   Step1:  
    -   Find the ESX of the VM and find all the VMs on this ESX. ​
    -   Find the ports of the ESX and all the VMs (network adapters and router interfaces) and get the MAC addresses of those ports.​
    -   Find all the VMware Virtual machine instances of the ESX and get the MAC addresses of their VMware network adapters (cmdb\_ci\_vmware\_nic).​​

-   Step 2:  
    -   Find the ports (network adapters and router interfaces) of the VM.​

-   Step 3: For each port, try to find if there is a layer 2 connection from the port:  
    -   Get the MAC address of the port.​
    -   Navigate to discovery\_switch\_fwd\_table and search for records with this MAC address, status field is not ‘self’ and Absent=false. ​
    -   For each such record, search if there are more records in the forwarding table with the same switch and port but with MAC addresses that don’t belong to the ESX or one of its VMs. Count the number of such exceptional MAC addresses.​
    -   Only in case the number of exceptional MAC addresses is low (max 3 MAC addresses that are max 51% of all MAC addresses of the ESX and VMs), this switch is considered as candidate. The logic regarding the number of candidate switches allowed is the same as described in PhysicalHostConnectionStrategy.

-   Step 4: Try to find the port of the target switch and create the layer 2 connection  
    -   The same logic as in PhysicalHostConnectionStrategy.

### NetworkDeviceLayer2ConnectionStrategy 

-   Creates layer 2 connections between a network device and its neighbors (other network devices).
-   Prerequisites:  
    -   Horizontal discovery of the network devices (switches or routers) – should be done twice.​

-   After the horizontal discovery was performed, we should validate the following:​  
    -   discovery\_device\_neighbors table was populated for at least one of the switches.​

-   Step 1: Find the ports of the switch.
-   Step 2: For each port, try to find if there is a layer 2 connection from the port:  
    -   Navigate to discovery\_device\_neighbors table and query the table by the switch (configuration item) and the port (origin interface).
    -   Look at the neighbor address and neighbor interface of the record.
    -   Ignore records that their neighbor interface is with install status = absent.
    -   If we have exactly one neighbor with neighbor address or neighbor interface or both, we will create a layer 2 connection.
-   Step 3: create a layer 2 connection  
    -   In case the neighbor interface exists, create a relation of type ‘Connects to::Connected by’ between the origin interface to the neighbor interface. Otherwise, create a relation of type ‘Connects to::Connected by’ between the origin interface to the switch with the neighbor address.

### JavaScriptLayer2ConnectionStrategy 

-   JavaScriptLayer2ConnectionStrategy is calling to createConnections (hostId) function in Layer2ConnectionStrategy script include.
-   The implementation of this function is empty and can be replaced by any other implementation on a customer instance in case we want to add another strategy or override an existing strategy.

### System properties to enable/disable the feature

-   By default the layer 2 connections algorithm is active.
-   We can disable it by setting the ‘sa.create\_physical\_connections.active’ property to false. ​
-   On PRB1359923 (fixed in O, NP4, MP9), we added more system properties that enable executing the layer 2 algorithm only for certain types of devices:​  
    -   sa.create\_physical\_connections.vm.active​
    -   sa.create\_physical\_connections.network\_device.active​
    -   sa.create\_physical\_connections.physical\_host.active​  
        ​
        

### Known Problems 

-   Layer 2 connection is not presented in the dependency view (‘Connects to::Connected by’ relation exists in the cmdb, but does not appear in the dependency view when applying the ‘Physical Network Connections’ dependency type):  
    -   Run the following script in scripts-background:​  
        -   var npm = new SNC.NetworkPathManager();​
        -   npm.getNetworkNeighbors(<host\_sys\_id>);​
    -   If you get error which is similar to the following: ‚Syntax Error or Access Rule Violation detected by database (Unknown column 'cmdb$par10.a\_ref\_8' in 'where clause’)’, open a task to Persistence team (see similar cases/tasks: CSTASK008547, TASK475910).​

-   "Layer 2 Connections Creation" cause memory issue:  
    -   As already mentioned above, this process may be disabled by setting "sa.create\_physical\_connections.active" property to false. This will be a good enough solution in case customer doesn't use layer 2 featuer, and will ensure no memory is spent over a process the customer is not interested in.
    -   Alternatively, go to event queue table (if you get there from navigator, just remove all filters).
    -   Filter by "name=physical\_connections.create".
    -   Sort by "Processing duration". If you see some records with really high value, this is your suspect.
    -   Look at the value of "Parm 1" in the suspected records. This is a sys\_id. Search for it in cmdb\_ci table. This is where you might find the problem. In one case we found  sys id of a computer with more than 20K network adapters. The computer itself wasn't discovered a long period which indicated a problem in this ci.

### Running the layer 2 algorithm from Scripts-Background

-   Run the following script in scripts-background: ​  
    -   var npm = new SNC.NetworkPathManager();
    -   npm.createPhysicalConnections(ciId);
-   In case of layer 2 connection between a server and a switch, the ciId should be the sys id of the server.​
-   In case of layer 2 connection between 2 switches, the ciId should be the sys id of one of the switches
-   To see the debug messages, set the ’sa.discolog.sys\_log’ property to true before executing the algorithm. ​
