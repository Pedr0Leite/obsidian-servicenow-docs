---
title: "How to modify edit list view for Workflow Editor Welcome page"
aliases:
  - KB0686055
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0686055
kb_number: KB0686055
last_modified: 2025-01-07
---

## How to modify edit list view for Workflow Editor Welcome page

  

### Issue

# Description

* * *

This article describes how to display fields other than the default fields on the workflow editor Welcome page.

Note the following information:

-   The Workflow Editor Welcome page displays data from wf\_workflow\_version table and NOT the wf\_workflow table. To verify, right-click on a column name and choose **Configure > Dictionary**.
    
-   The wf\_workflow\_version table can be accessed separately to check the available fields.
    
-   Choose **Configure > List layout** to check which other tables are available to dot-walk to display fields from those tables.
    

# Procedure

* * *

1.  Navigate to **System UI > Lists**.
    
2.  Set the filter Table = wf\_workflow\_version AND View = Workflow Welcome.
    
3.  Click **New** to add a new list element with the following values:
    
    -   **Element**: Your desired field name, for example, checked\_out or workflow.sys\_updated\_by. (See the note in the previous section regarding tables available for dot-walking.)
        
    -   **Position:** Desired position of the field on the list view.
        
4.  Click **Submit**.
    

# Applicable Versions

* * *

All
