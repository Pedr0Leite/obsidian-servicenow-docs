---
title: "Troubleshooting Guide: MID Server"
aliases:
  - KB0597571
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597571
kb_number: KB0597571
last_modified: 2026-02-26
---

## Troubleshooting Guide: MID Server

  

### Issue

1.  **MID Server Upgrade Issues**
    -   **Symptoms**  
        -   MID Server status is **Down** in the MID Server list
        -   Discovery scans get stuck
        -   MID Server does not keep running
        -   MID Server status is **Up** but is not responding  
              
              
            
2.  **MID Server User Credential Issues**  
    -   **Symptoms**
        -   All MID Servers are down
        -   CIs are duplicated during Discovery
        -   MID Server keeps going down
        -   MID agent log is reporting 404, could not authenticate
        -   MID Server upgrade is hung
        -   Cannot restart MID Server

### Resolution

1.  **MID Server Upgrade Issues  
      
    **
    -   **Troubleshoot:** [Has the instance been recently upgraded manually or via QPP patch?](/kb_view.do?sysparm_article=KB0596459) 
    -   **Solution:** [Resolve communication issues between the MID and the instance](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597538)
    -   **Solution:** [Resolve local environment issues on the MID Server host](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597552)  
          
          
        
2.  **MID Server User Credential Issues  
      
    **
    
    -   **Troubleshoot:** [Is the MID Server user credential valid?](/kb_view.do?sysparm_article=KB0597574 "Is the MID Server credential valid?")
    -   **Solution:** [Resolve MID Server user credential issues](https://support.servicenow.com/kb_view.do?sysparm_article=KB0597570 "Resolve user credential issues on the MID")  
          
        
    
      
      
    

### Related Links
