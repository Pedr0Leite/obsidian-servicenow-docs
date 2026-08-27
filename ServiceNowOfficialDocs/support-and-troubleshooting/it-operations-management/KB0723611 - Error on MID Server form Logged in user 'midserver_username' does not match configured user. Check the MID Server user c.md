---
title: "Error on MID Server form: \"Logged in user '<midserver_username>' does not match configured user. Check the MID Server user configuration.\" "
aliases:
  - KB0723611
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723611
kb_number: KB0723611
last_modified: 2024-04-07
---

## Issue

Post cloning MID Server is down with an error message "Logged in user '<midserver\_username>' does not match configured user. Check the MID Server user configuration."

**Sample Error Message:**

Logged in user 'XYZ' does not match configured user. Check the MID Server user configuration.

  

## Resolution

1.  Log on to the host machine as a local admin or the MID Server user
2.  Navigate to the /agent directory where the MID was installed
3.  Edit the config.xml file
4.  Search for the parameter: mid.instance.username 
5.  Copy the value of that parameter into your buffer
6.  Return to the target instance
7.  In the text editor, navigate to Organization > Users Search for User ID = \[the name in your buffer\]
8.  After completing the above 7 steps, manually enter the password in the config.xml for the value of the parameter mid.instance.password  
    **Note:**  The password for the user saved in the target instance should match the password manually entered in above step.
9.  Save the config.xml file and restart the MID Server Service from the host machine
