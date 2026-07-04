---
title: "How to eliminate Most Recent tags from Tagged Documents"
aliases:
  - KB0549863
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549863
kb_number: KB0549863
last_modified: 2024-01-28
---

## How to eliminate Most Recent tags from Tagged Documents

  

### Issue

Overview

* * *

When accessing Tagged Documents on the Edge, a Most Recent tag is populated with a number of different records.

The product documentation describes the tags as follows:

Most Active and Most Recent tags are maintained both at the system level and individually for each user. Modules or records tagged with the Most Recent tag cannot be removed by clicking the X icon. The Most Recent tag always shows the most recent modules or records. A Most Active tag contains the most active modules or records for the user who created the tag. A Most Active global tag contains the most active modules or records across all users. 

This information is populated automatically by the system, and no out-of-box capability has been provided to turn off the feature.

Solution

* * *

The following workaround can prevent the Most Recent tags from ever being populated.

1.  Create a new business rule on the label\_history table with the name 'Prevent most recent'.
2.  Under Advanced settings, set it to Before Insert.
3.  Include the following line as the script: current.setAbortAction(true); 
4.  Delete all the records in label\_history table.  
      
      
    

Documentation references

* * *

[Administering tags](https://docs.servicenow.com/csh?topicname=administering-tags.html&version=latest "Administering tags")

[Recently viewed and most viewed records](https://docs.servicenow.com/csh?topicname=c_Tags.html&version=latest "Recently viewed and most viewed records")
