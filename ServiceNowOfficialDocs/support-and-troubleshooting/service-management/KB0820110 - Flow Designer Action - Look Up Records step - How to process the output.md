---
title: "Flow Designer Action - Look Up Records step - How to process the output"
aliases:
  - KB0820110
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820110
kb_number: KB0820110
last_modified: 2024-06-23
---

## Flow Designer Action - Look Up Records step - How to process the output

  

### Issue

We have documentation for "Look Up Records step" but it doesn't cover how to process the output.

[Look Up Records step](https://docs.servicenow.com/csh?topicname=lookup-records-action-designer.html&version=latest "Look Up Records step")

To process the output, 

1.  Select Look Up Records
2.  From the Action Outline, select Add a new step.
3.  Select Script.
    
    4\. In your script you will need to use a while loop as shown below.
    

```
//Iterate through the list of User recordswhile(inputs.userRecords.next()) {}
```

\------

To know how to configure Look up records step" and "Output" Please refer to below documentation. (From step 9)

[Create a custom action to generate an array of objects from a list of records](https://docs.servicenow.com/csh?topicname=create-custom-action-array-objects.html&version=latest)
