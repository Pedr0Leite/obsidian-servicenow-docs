---
title: "Modify the Knowledge Article Link that is populated when we click on Attach button from Contextual Search Results"
aliases:
  - KB0717995
tags:
  - servicenow
  - support-kb
  - client-scripts
  - knowledge-management
  - contextual-search
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717995
kb_number: KB0717995
last_modified: 2025-01-03
---

## Modify the Knowledge Article Link that is populated when we click on Attach button from Contextual Search Results

  

### Issue

# Description

* * *

Modify the Knowledge Article Link that is populated when we click on Attach button from Contextual Search Results

# Procedure

* * *

1\. The Knowledge Article Link is populated from the Script include cxs\_knowledge which is read-only and cannot be edited.

2\. However, we can still modify the link by creating an onChange Client Script on the comments field which is populated with the Knowledge Article link when we click the “Attach” button from the contextual search results.

3\. Here is an Example client script on Comments fields for overriding the link to view in Portal:

function onChange(control, oldValue, newValue, isLoading, isTemplate) {

  if (isLoading || newValue === '') {

  return;

  }

  if(newValue.includes('kb\_view')){

     g\_form.setValue('comments', newValue.replace('kb\_view.do?sys\_kb\_id', 'sp?id=kb\_article&sys\_id'));

     }

  } 

# Applicable Versions

* * *

Any

## Related

- [[KB0711972 - oldValue returns empty value instead of the previous value for onChange client scripts]]
- [[KB0696067 - How to restrict the record producer's contextual search results to a particular knowledge base]]
