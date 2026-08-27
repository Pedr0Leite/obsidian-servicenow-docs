---
title: "Enabling the Reference float functionality on an extended table"
aliases:
  - KB0523768
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523768
kb_number: KB0523768
last_modified: 2025-01-30
---

## Enabling the Reference float functionality on an extended table

  

### Issue

Enabling the Reference float functionality on an extended table

  
  
  
Overview

* * *

The **Edit** button is available for related lists that represent many-to-many and one-to-many relationships. The **Edit** button appears on a one-to-many relationship if the **Reference floats** option in the dictionary entry is selected for the reference field. For example, if the **Edit** button is made available in the **Incident** related list on the **Problem** form, it allows users to assign incidents to a problem via the interface.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" width="26" height="25" align="baseline"></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: If your related list represents a many-to-many relationship, right-click the related list header, select <strong>Personalize &gt; List Control</strong>, and click the <strong>Enable Edit</strong> button to make the <strong>Edit</strong> button available on the related list.</td></tr></tbody></table>

Procedure

* * *

To enable the reference float functionality on a one-to-many related list:

1.  1.  Navigate to the related list that is missing the **Edit** button.

  

1.  1.  Open a record from the related list.

  

1.  1.  Right-click the field that creates the relationship with the parent table and select **Personalize > Dictionary**. For example, when troubleshooting the **Task SLA** related list on the **Incident** form, the **Task** field is the field that creates the relationship with the Incident \[incident\] table.  
          
        The Dictionary Entry form appears.  
          
        
    2.  Select the **Reference floats** option.
        
        ![](/sys_attachment.do?sys_id=51fb6ceadb42b450e515c22305961925 "Reference Floats")
        

  

1.  1.  Click **Update**.

  

1.  Return to the parent form and verify that the **Edit** button appears in the related list.
    
    ![](/sys_attachment.do?sys_id=5dfb6ceadb42b450e515c22305961934 "Edit Button")
