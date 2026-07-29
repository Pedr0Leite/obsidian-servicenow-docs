---
title: "Data not transferred from one form to another when content of description is more than 4000 characters"
aliases:
  - KB0695409
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695409
kb_number: KB0695409
last_modified: 2024-04-07
---

## Data not transferred from one form to another when content of description is more than 4000 characters

  

### Issue

# Symptoms

* * *

Data not transferred from New Call to request when request initiated from call and content of description is long if it has more than 4000 characters.

# Release

* * *

ALL

# Cause

* * *

System property "glide.tiny\_url\_min\_length" changes the url to tiny support url if the number of characters exceeds the specified value in the property. 

# Resolution

* * *

\-- By default the value of property "glide.tiny\_url\_min\_length" is 1024 characters, so when we are trying to pass description with more than 1024 characters, the url will change as below

Decoded url: [http://<instance-name>/nav\_to.do?uri=/com.glideapp.servicecatalog\_cat\_item\_view.do?sysparm\_tiny=f4498c6ccccc2300964faf77e5defea3](http://10.11.88.155:16001/nav_to.do?uri=/com.glideapp.servicecatalog_cat_item_view.do?sysparm_tiny=f4498c6ccccc2300964faf77e5defea3)

\-- So when we try to get the "sysparm\_additional\_information" query parameter in our client script, it will return undefined.

\-- Tiny url creates an entry in the "sys\_tiny\_url" table, and as you can see it passes the sys\_id of that record in the above URL

\-- To handle this scenario you need to fire an Ajax call on "sys\_tiny\_url" table and fetch the record with sys\_id, there you will get the value of the field that has long valu..

# Additional Information

* * *

Here you can read more about 'Examples of navigating by URL':

[https://docs.servicenow.com/csh?topicname=r\_NavigatingByURLExamples.html&version=latest](https://docs.servicenow.com/csh?topicname=r_NavigatingByURLExamples.html&version=latest)
