---
title: "Error \"Error MessageDelete\" when trying to delete a survey instance"
aliases:
  - KB0959001
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0959001
kb_number: KB0959001
last_modified: 2024-03-16
---

## Error "Error MessageDelete" when trying to delete a survey instance

  

### Issue

When trying to delete a survey instance an error like this is displayed:  
  
Error MessageDelete of AINST0709719 not allowed because of a reference in record "Record" within the Assessment Instance Question file  
  

\*AINST0709719 is just an example number.

### Cause

Deleting survey instances is not recommended, especially if some surveys have already been taken. In that scenario we could find records with the answers that now are not related to a question or survey.

But in case a survey instance needs to be deleted, it is necessary to delete all its dependencies, that means all the questions on those survey instances need to be deleted first

### Resolution

The questions can be deleted manually or a background script can be run in order to do that.

Some guidance on how to code the script can be found on this [community post](https://community.servicenow.com/community?id=community_question&sys_id=bc3dc145db10e70854250b55ca9619a5).
