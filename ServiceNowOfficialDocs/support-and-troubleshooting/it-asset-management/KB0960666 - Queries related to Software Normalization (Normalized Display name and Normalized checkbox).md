---
title: "Queries related to Software Normalization (\"Normalized Display name\" and \"Normalized\" checkbox)"
aliases:
  - KB0960666
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960666
kb_number: KB0960666
last_modified: 2024-03-26
---

## Queries related to Software Normalization ("Normalized Display name" and "Normalized" checkbox)

  

### Issue

-   Why the "Normalized display name" on the software installation record, is not a concatenation of the normalized values ?  
      
    
-   What is the purpose of the "Normalized" checkbox on the records under "cmdb\_sam\_sw\_install" table ?  
      
    ![](/sys_attachment.do?sys_id=ae0b65b8db3be0101cd8a345ca961979)  
    

### Release

-   Paris and below

### Resolution

-   It is observed that the "Normalized display name" is the same as the "Display name" for the records under "cmdb\_sam\_sw\_install" table. Why the "Normalized display name" is not a concatenation of the normalized values ?  
      
    -   The concatenation feature is added in Quebec. For pre Quebec releases, it's a legacy column. So it's expected to have that field the same as "Display name".  
          
        
-   What is the purpose of the "Normalized" checkbox on the records under "cmdb\_sam\_sw\_install" table ?  
      
    -   "Normalized" is a legacy column, and it is not used anymore.
