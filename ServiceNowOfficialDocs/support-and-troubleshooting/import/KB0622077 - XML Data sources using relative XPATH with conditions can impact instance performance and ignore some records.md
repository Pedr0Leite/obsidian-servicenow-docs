---
title: "XML Data sources using relative XPATH with conditions can impact instance performance and ignore some records"
aliases:
  - KB0622077
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622077
kb_number: KB0622077
last_modified: 2024-01-28
---

## XML Data sources using relative XPATH with conditions can impact instance performance and ignore some records

  

### Issue

XML Data sources using relative XPATH with conditions can impact instance performance and ignore some records

  
  

# Problem

* * *

Long XML files imported by a data source with XML format are unable to import some records when the XPATH field has been set with the following format:

//_path_\[_condition_\]

For example, //kb\_knowledge\[kb\_knowledge\_base='<sys\_id>'\] or //incident\[number='INC0010007'\]

![](sys_attachment.do?sys_id=fab96862db42b450e515c22305961945)  
 

# Steps to Reproduce

* * *

1.  Run a data source of type XML.
    
    For more information, see the documentation topic [Create a data source](https://docs.servicenow.com/).
    
2.  Set the XPATH to a relative path with a condition.
    
    For example, set **XPATH for each row** to //incident\[number='INC0010007'\]
    
3.  Click **Load all records**.
    
    Note that the records are not loaded and a a message appears on the data source:
    
    Relative XPATH expression is not recommended and can impact instance performance
    

# Cause

* * *

The XML data source import uses the XMLStreamDocument function, which in specific cases is not able to handle relative path with conditions, and returns null. Also, the use of a relative path involves extra overhead on the function.

# Resolution

* * *

To avoid both the search missing the date and to avoid performance issues on evaluating relative paths, use absolute paths, for example, /unload/incident\[number='INC0010007'\].

  
![](sys_attachment.do?sys_id=f2b96862db42b450e515c2230596196a)
