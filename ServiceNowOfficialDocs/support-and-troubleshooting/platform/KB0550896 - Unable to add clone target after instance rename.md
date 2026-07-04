---
title: "Unable to add clone target after instance rename"
aliases:
  - KB0550896
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550896
kb_number: KB0550896
last_modified: 2023-10-18
---

## Issue

A clone target could be unavailable to clone over after an instance(clone target) has been renamed.

While trying to add the instance with its new name you could encounter an error like; "Error MessageTarget instance already exists (cannot create new record)"

## Resolution

In order to rename the clone target records after an instance rename, there is an easy workaround any administrator on the instance should be able to perform.

#### Approach 1

You can execute the below script after supplying the 3 instance variables on the /sys.scripts.do page as user with the (security\_)admin role.

renameCloneTarget();  
function renameCloneTarget() {  
 var old\_instance\_name = 'insertOldInstanceNameHere';  
 var instance\_id = 'insertInstanceIDhere';  
 var new\_instance\_name = 'insertNewInstanceNameHere';  
 var target = new GlideRecord('instance');  
 target.addEncodedQuery('source=false^instance\_id='+instance\_id+'^instance\_urlLIKE'+old\_instance\_name);  
 target.setLimit(1);  
 target.query();  
 while (target.next()) {  
  gs.info('Renamed clone target instance "'+old\_instance\_name+'" with ID instance\_id '+instance\_id+' to > "'+new\_instance\_name+'"');  
  target.instance\_name = new\_instance\_name;  
  target.instance\_url = 'https://'+new\_instance\_name+'.service-now.com';  
  target.update();  
 }  
}

#### Approach 2

1.  Navigate to **Clone Targets** list.
2.  Find the clone target which was renamed, **DO NOT OPEN the record.**
3.  Double click on the **Instance URL** value for that record, it should allow you to edit the text for Instance URL.
4.  Change the Instance URL to reflect the new instance name
5.  Click the green checkmark to save the record.
6.  Schedule a new clone. 

#### Approach 3

1.  Remove all entries for the clones to the old instance name from the clone history list. You may need to configure the delete button to show for admins.
2.  Remove the clone target record. You may need to configure the delete button to show for admins.
3.  Add the clone target with the new name. 

#### Approach 4 not recommended but if all else fails

1.  Navigate to **Clone Targets**.
2.  Export the clone target that needs renaming to XML; 
3.  Change the following fields to reflect the new instance name using a text editor:  
    -   <instance\_name>
    -   <instance\_url>  
        As long as the target instance URL is OK the rest of the fields, like db properties, get updated via the soap service from the clone automation.
4.  Import the updated XML  
    (If the right-click option to "Import XML" does not show then navigate to **Retrieved Update Sets > Import Update Set from XML** (this way no business rules run when updating the record, this also means you can no track the update))
5.  Schedule a new clone.
