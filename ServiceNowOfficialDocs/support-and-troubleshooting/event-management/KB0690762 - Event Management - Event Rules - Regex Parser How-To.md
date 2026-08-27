---
title: "Event Management - Event Rules - Regex Parser How-To"
aliases:
  - KB0690762
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690762
kb_number: KB0690762
last_modified: 2024-04-07
---

## Event Management - Event Rules - Regex Parser How-To

  

### Issue

How to use Event Rules Regex Parser

  
  

# Description

* * *

This article is intended to help clarify some of the particulars and limitations regarding the Regex Parser

# Solution

* * *

-   Flags cannot be manually set. By default multi-line is not set, single-line is.
-   The following features are not currently supported:
    -   Setting flags
    -   Lookbacks  
          
        
-   Example of how to parse a multi-line event (working example vs. non-working examples):  
    
    em\_event Description:  
    "Stuff: Stuff  
    Value: some value  
    Target Hostname: domain.testing.com  
    Target IP Address: 10.10.1.1"
    
    Configure Event Rule to parse Description with:  
    "Hostname: (.\*\\n)" - Evaluation error (requires full text match)  
    "(.+?(?<=Hostname: ))(.+?$)(.\*)" - Evaluation error (Lookback not supported)  
    "(?m)(.+Hostname: )(.+?$)(.\*)" - Evaluation error (Manual flags not supported)  
    "(.+Hostname: )(.+?)(\\n.\*)" - Works
    
-   This will usually result in unwanted/unneeded capture groups. This is expected and you will just need to ignore using those capture groups for the Event Rules transform page.

# Applicable Versions

* * *

Post-Geneva

# Additional Information

* * *

-   Java regex tester: [https://www.freeformatter.com/java-regex-tester.html](https://www.freeformatter.com/java-regex-tester.html)
