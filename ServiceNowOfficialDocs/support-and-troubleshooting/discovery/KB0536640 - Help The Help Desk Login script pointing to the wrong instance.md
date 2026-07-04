---
title: "Help The Help Desk Login script pointing to the wrong instance"
aliases:
  - KB0536640
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0536640
kb_number: KB0536640
last_modified: 2025-01-05
---

## Help The Help Desk Login script pointing to the wrong instance

  

### Issue

When using Help The Help Desk, the configuration items are not being updated on the instance.

Further investigation shows that the Help The Help Desk Login script has the wrong instance name in the following section of code:

// The variable should point to your instance URL, such as https://demo.service-now.com   
var server = "https://wrong-instance-name.service-now.com/";

### Cause

The value of the system property **glide.servlet.uri** is the most likely cause of this issue.

The property may be set at an incorrect value after a clone operation onto the target instance.

### Resolution

The instance name in the Help The Help Desk Login script is dynamically generated on the instance from the system property **glide.servlet.uri**.

Review the value of this property and set the value accordingly:

1.  In Scripts-Background, run this script:
    
    gs.info(gs.getProperty('glide.servlet.uri'));
    
2.  It should be: [https://correct-instance-name.service-now.com/](https://correct-instance-name.service-now.com/)  
      
    
3.  If it is not, please open up a Case with Support.
