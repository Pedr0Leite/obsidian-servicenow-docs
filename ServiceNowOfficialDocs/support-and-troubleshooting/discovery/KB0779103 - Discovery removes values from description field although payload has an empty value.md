---
title: "Discovery removes values from description field although payload has an empty value"
aliases:
  - KB0779103
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779103
kb_number: KB0779103
last_modified: 2024-04-08
---

## Issue

On a windows server CI, a manually updated value for the field description is empty after a discovery scan.

## Resolution

The above described behavior is expected.

If you want to prevent this from happening, create a custom business rule which checks to see if the update on the description field is empty, if empty, it prevents discovery from making the update. Below are the details of how you can create this custom business rule:

1\. Navigate to Business rule >new

-   Name: Discovery\_field update
-   Table:cmdb\_ci\_win\_server
-   active: checked
-   advanced:checked

2.For tab "when to run", select the following

-   when: before
-   update is checked
-   Filter condition :description changes

3.For tab "advanced", use the below code:

  
       (function executeRule(current, previous /\*null when async\*/) {  
  
        // Add your code here  
       if (current.short\_description === "")  
      {  
          current.short\_description = previous.short\_description;  
       }  
  
       })(current, previous);  
  

4\. Click Submit
