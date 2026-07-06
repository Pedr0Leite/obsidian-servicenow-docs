---
title: "Agent Intelligence ML Solution training fails with error \"Error while training solution\" followed by  an error related to \"dedup task failed\" or \"data is not sufficient for model creation\""
aliases:
  - KB0691436
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691436
kb_number: KB0691436
last_modified: 2024-04-12
---

## Agent Intelligence ML Solution training fails with error "Error while training solution" followed by an error related to "dedup task failed" or "data is not sufficient for model creation"

  

### Issue

# Symptoms

* * *

When training an Agent Intelligence ML Solution Definition defined against the \[incident\] table, the Solution State is updated with "Error while training solution". If a Training Progress bar is displayed you can observed one of these two errors:

-   Step 2. Preparing Data: Training terminated due to Exception. Executing dedup task failed. text columns can not be null or empty  
    or
-   Step 3. Training Solution: Training terminated due to Exception. Model creation failed because data is not sufficient for model creation. Consider increasing time window for training data set.  
    or
-   Step 3. Training Solution: Training terminated due to Exception. Solution training failed as either the data used is not sufficient or the input field is not predictive of the output field."

# Release

* * *

Kingston, London

# Cause

* * *

The data set provided to the trainer is not valid. It does not have enough data or there is enough data but its quality is not good enough.

# Resolution

* * *

1.  It is advised to have a data set of at least 50k Incidents, although 100k would be an even better amount. A data set is the number of Incidents matching the selection criteria defined on the Solution Definition. If there are not enough Incidents, consider increasing the time window to select more Incidents.  
      
    
2.  The quality of the model built by the trainer relies on the quality of the data which is provided:
    -   The Incidents should be linked to **at least** 2 different values for the Output Field (usually the Category or the Assignment Group).  
        
    -   There should not be any Incidents with an empty Input Field (usually the Short Description) or an empty Output Field (usually the Category or the Assignment Group).
    -   The values for the Input Field (usually the Short Description) should be of good quality. Incidents created artificially (by script, etc) are usually not of good quality as their short descriptions are the same or look almost the same. Real Incidents should be used.
