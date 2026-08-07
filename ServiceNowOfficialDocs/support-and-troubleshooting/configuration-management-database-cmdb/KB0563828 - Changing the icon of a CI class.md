---
title: "Changing the icon of a CI class"
aliases:
  - KB0563828
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563828
kb_number: KB0563828
last_modified: 2025-04-07
---

## Changing the icon of a CI class

  

### Issue

Each cmdb\_ci class is associated with an icon that appears in the CI Relationship Related Item list of any CI that has a relationship to that particular CI. If no icon is defined, a default icon is used. Sometimes it is desirable to change the default icon of a new or existing CI class so it better represents the class.

Navigate to **System Definition > Modules**. 

1.  Ensure that the **Image (UI11)** column is visible on the list. If it is not visbile, personalize list columns and add it.
2.  Search for the CI class requiring a new icon.
3.  Double click on the empty I**mage (UI11)** field.
4.  Enter the path to an existing icon.  
    Alternatively, you can first add the new icon to the system by following the instructions in [Storing images in the database](https://docs.servicenow.com/csh?topicname=c_StoringImagesInTheDatabase.html&version=latest "Storing images in the database").
