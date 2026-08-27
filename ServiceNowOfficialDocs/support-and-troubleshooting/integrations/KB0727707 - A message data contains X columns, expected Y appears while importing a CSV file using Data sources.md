---
title: "A message \"data contains X columns, expected Y\" appears while importing a CSV file using Data sources"
aliases:
  - KB0727707
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727707
kb_number: KB0727707
last_modified: 2024-04-07
---

## A message "data contains X columns, expected Y" appears while importing a CSV file using Data sources

  

### Issue

You will recognize the problem if:

-   The data is NOT imported into the target table
-   Error similar to "data contains 25 columns, expected 26" is observed

### Cause

There are inconsistent data columns in the CSV file being imported. In this occasion, while the CSV file was expected to contain rows of 26 data columns, some rows in the file were 25.

### Resolution

Validate the CSV file being imported to ensure that there are consistent columns within the CSV file.

1.  Remove the extra columns in the file
2.  Alternatively, add the expected columns to the incomplete rows

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: Ensure that the inconsistent CSV file is removed from the Data Source and the amended one is added after the changes are made</td></tr></tbody></table>

As a workaround, you may create the below system property to skip the non parseable row and load the correct rows. 

Name: **com.glide.csv.loader.ignore\_non\_parseable\_lines**  
Type: **true | false**  
Value: **true**  
Description: **If any row in a CSV file is non parseable for whatever reason, skip loading of that row and move on to the next one.**  
  
This will ignore the row that has a mismatch in column numbers and move on to the next row instead of stopping the load then and there.
