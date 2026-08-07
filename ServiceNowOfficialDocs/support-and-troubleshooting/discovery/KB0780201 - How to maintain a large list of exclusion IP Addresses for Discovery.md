---
title: "How to maintain a large list of exclusion IP Addresses for Discovery"
aliases:
  - KB0780201
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780201
kb_number: KB0780201
last_modified: 2024-09-26
---

## Issue

In cases where a customer would like a large list of IP Addresses to be excluded from discovery, we have found that it is not possible to create a list and associate it with a mid server, however it is possible to create one that can be created and associated with any Discovery schedule. It is one central list and need not be recreated for each schedule. It is done by importing a spreadsheet of the IP Addresses into a user defined table, creating a transform map and applying that transform map to the table where the list is stored Maintenance on the data involves two steps but is fairly straightforward.

## Resolution

**Step 1: Create a Blank Discovery Schedule**

You will need to create a blank Discovery Schedule in order to house the list that you will create. Create the schedule, assign a mid server, and right click in the gray area to save.

**Step 2: Create a New Discovery Range Set**

This is the initial step to get to the list that we will eventually create. There will be a hierarchy based on this object:

Discovery Range Set->Discovery IP Range->List Items

**Step 3: Create a Discovery IP Range**

After creating this, copy the Sys ID of this record. It will be used in the transform map

**Step 4: Create a Dummy List Item Entry**  
Add an ip address entry to this list as a dummy record. In our case we will add this to the related list for excludes, but keep in mind that there is one for includes as well. It is in a different table and the entire logic of this exercise could easily be applied for includes if you chose that related list instead.You will note that the table that this record is in for excludes is discovery\_range\_item\_exclude. That is the table that the transform map will eventually write to.

**Step 5: Load Data**

Navigate to Load Data, create a user defined table, choose the csv/excel import file

example user defined table: u\_load\_exclude\_ip\_addresses   
 

**Step 6: Create a Transform Map**

Choose Source(u\_load\_exclude\_ip\_addresses)/Target Tables(discovery\_range\_item\_exclude)Click Save

**Step 7: Click Mapping Assist**

Map in the source field(s) match to the target table, click save

**Step 8: Add the Parent Field top the related list of field mappings**

Click New

On the new record click the checkbox for "use source script"

Paste the sys id of the parent object(copied to the clipboard from step 3) between the quotes in the script

Change Target Field to "Parent"-click submit

**Step 9: Transform**

Click Transform, click the transform button

\*To Delete any records you must delete them directly from discovery\_range\_item\_exclude  
\*To Add Records navigate to Load Data  and import a new spreadsheet with the new IPs to the same user defined table (u\_load\_exclude\_ip\_addresses in our example) and rerun the transform map. It should only import the new records and not the old ones that have already been imported.

## Additional Information

Full testing should be done to verify that no unknown scenarios could possibly affect this.
