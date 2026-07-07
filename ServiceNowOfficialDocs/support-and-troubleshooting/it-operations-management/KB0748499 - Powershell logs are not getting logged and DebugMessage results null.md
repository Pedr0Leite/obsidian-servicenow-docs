---
title: "Powershell logs are not getting logged and DebugMessage results \"null\"
aliases:
  - KB0748499
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748499
kb_number: KB0748499
last_modified: 2024-04-07
---

## Powershell logs are not getting logged and DebugMessage results "null"

  

### Issue

# Symptoms

Powershell logs are not getting logged and DebugMessage results "null"

![](sys_attachment.do?sys_id=d1ab28aadb42b450e515c22305961953)

-   **Expected Result**: Upon selecting debugMessages under Response drop down list, it should display Debug information details.
-   **Actual Result**: Upon selecting debugMessages under Response drop down list, it displays null.

# Release

-   All Releases  
      
    

# Steps to Reproduce

-   Navigate through table: wf\_element\_activity
-   Search any record of type Powershell in Activity Designer and click on Test Inputs.
-   Fill all mandatory fields and click ok.

![](sys_attachment.do?sys_id=d5ab28aadb42b450e515c22305961958)

# Cause

-   The MID property "mid.property.powershell.log\_info" is missing.

# Resolution

-   Navigate through MID Server>Properties
-   Click New and create the record with the following information and Submit.  
      
    -   **Name**: mid.property.powershell.log\_info
    -   **Value**: true
    -   **MID Server name**: <Name of the MID Server>
