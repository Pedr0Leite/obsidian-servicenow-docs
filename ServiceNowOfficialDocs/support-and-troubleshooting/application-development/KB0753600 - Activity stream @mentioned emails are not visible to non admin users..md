---
title: "Activity stream @mentioned emails are not visible to non admin users."
aliases:
  - KB0753600
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753600
kb_number: KB0753600
last_modified: 2024-04-07
---

## Activity stream @mentioned emails are not visible to non admin users.

  

### Issue

# Symptoms

If a non admin user @mentions another non admin user in the activity stream for the record, both the users are not able to see the email in sys\_email table. 

# Release

Any supported version

# Cause

Script in table level read ACL for sys\_email table checks for the user's access to live\_notification table for @mentioned emails. If the script fails, it would restrict the user from seeing @mentioned emails in sys\_email table.

# Resolution

Create table level ACL on live\_notification table according to the requirement so that the user has access to live\_notification table.
