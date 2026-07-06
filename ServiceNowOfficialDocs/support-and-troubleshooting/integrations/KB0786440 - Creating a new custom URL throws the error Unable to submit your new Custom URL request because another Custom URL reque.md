---
title: "Creating a new custom URL throws the error \"Unable to submit your new Custom URL request because another Custom URL request for your instance is still in progress.\""
aliases:
  - KB0786440
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786440
kb_number: KB0786440
last_modified: 2024-04-08
---

## Creating a new custom URL throws the error "Unable to submit your new Custom URL request because another Custom URL request for your instance is still in progress."

  

### Issue

If you're trying to creating a new Custom URL on the instance, it may fail to be created and will throw the below error:

"Unable to submit your new Custom URL request because another Custom URL request for your instance is still in progress."

### Cause

This may happen if you previously created a custom URL but the job for provisioning it has not yet completed.  
Custom URL jobs may take up to 6 hours to complete and polling for custom URL job completion occurs every 30 minutes.

### Resolution

You need to wait for the provisioning of the custom URL job that's in progress to complete before creating another custom URL.
