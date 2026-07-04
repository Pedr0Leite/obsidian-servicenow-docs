---
title: "How to resolve a large topology issue in business service maps"
aliases:
  - KB0596671
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596671
kb_number: KB0596671
last_modified: 2024-04-07
---

## How to resolve a large topology issue in business service maps

  

### Issue

# Problem

  
  
There is a limit on the maximum number of CIs and connections to be displayed on the service map. When this limit is reached, the described error appears.

# Symptom

In Service Mapping and Event Management products, when opening topology map/manual service map of Business Service, you may experience a problem when instead seeing the map, the following error message appears: "Cannot display the map. Topology too large."

# Solution

This section provides a procedure to verify whether the problematic map can be displayed by relaxing the maximum size limitations.

1.  Enter **sys\_properties.list** in the application navigator field.
    
2.  Click New and create a new property with the following values:
    
    **Name**: sa.map.LIMIT\_MAX\_GRAPH\_SIZE  
    **Type**: true|false  
    **Value**: false
    
3.  Click **Submit** to create the property.
    
4.  Navigate back to the problematic service map and verify whether the the map displays.
    
5.  If the problem is solved, navigate back to **sys\_properties.list**, and look up the recently created property by Name (sa.map.LIMIT\_MAX\_GRAPH\_SIZE).
    
6.  Change the property value to **true**.
    
    To have working service maps, ensure a more accurate configuration.
    
7.  If you are on the Helsinki release:
    
    1.  In a Chrome browser window, navigate to the problematic map.
        
    2.  Open the developer tools.
        
        ![](/sys_attachment.do?sys_id=118c24aedb42b450e515c223059619d1)
        
    3.  Choose Console tab.
        
        ![](/sys_attachment.do?sys_id=dd8c24aedb42b450e515c223059619dc)see attached image "Filter console chrome").
        
    4.  Click the filter icon.
        
    5.  In the filter input field, type **nNodes**.
        
        You should see the message **SA\_LOG:: MAP\_PERF\_DEBUG: nNodes: <_number_\>, nEdges: <_number_\>**.
        
    6.  Copy down the numbers for nNodes and nEdges.
        
8.  Navigate to **sys\_properties.list** and click New.
    
9.  Create a new property with the following values:
    
    Name: **sa.map.MAX\_NODES\_FOR\_LAYOUT**  
    Type: **integer**  
    Value: The value for **nNodes + 1**. (If not available, try the number 1000.
    
10.  Click Submit.
     
11.  Create another property with the following values:
     
     Name: **sa.map.MAX\_EDGES\_FOR\_LAYOUT**  
     Type: **integer**  
     Value: The value for **nEdges + 1**. (If not available, try the number 10000.)
     
12.  Click **Submit**.
     
13.  Navigate back to the problematic map to verify whether the problem solved.
