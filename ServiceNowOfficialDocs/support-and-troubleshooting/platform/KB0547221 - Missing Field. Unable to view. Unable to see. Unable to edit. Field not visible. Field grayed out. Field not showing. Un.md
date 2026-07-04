---
title: "Missing Field. Unable to view. Unable to see. Unable to edit. Field not visible.  Field grayed out. Field not showing. Unable to attach."
aliases:
  - KB0547221
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547221
kb_number: KB0547221
last_modified: 2024-04-30
---

## Missing Field. Unable to view. Unable to see. Unable to edit. Field not visible. Field grayed out. Field not showing. Unable to attach.

  

### Issue

Symptoms:

Field is missing on the form.

  

Field/Attachment/Choice Field/Button on a form does not appear/does not display/not visible/not showing/not editable/unavailable/missing/lost/can't see/unable to view/grayed out.

### Release

All

### Cause

Access controls for read rights are not granting access to a field.

\-- The user does not meet the filter condition of the ACL.

\-- The user does not meet the script condition of the ACL.

\-- The user does not have the defined roles of the ACL.

### Resolution

The first step to identifying a field not appearing on a form as an ACL issue is to use the debug security option to see if any ACL restrictions are occurring. Let's take the example of the work\_notes field which is on the task table (and extended tables). 

1.  To start with as an admin role user you will login and go to **System Diagnostics -> Session Debug -> Debug Security.**
2.  Impersonate a user that cannot see the field. In this case Joe Employee.
3.  View an affected record (incident in this case).  
    A large amount of security related statements will be displayed below the record. 
4.  Search for the field and operation (read, write, etc) that you are interested on the page by using the browser's search page function. In this case we search for **work\_notes/read**. You should see an entry that looks like this:  
    ![](sys_attachment.do?sys_id=b07e8cb8db48b0d0fec4fb24399619c9)  
      
    
5.  Click the link that is next to the failing ACL to open it in a separate tab. In this case the link text is **record/task.work\_notes/read**.  
    ![](/Note_25x.pngx "Note")**Note:** You will not be able to view the ACL because you are still impersonating a non-admin user.
6.  Switch back to your admin user account and refresh the tab with the ACL in it. 
7.  You can now see the ACL that is failing. Update this ACL script, condition, or filter values to allow access.

  

### Related Links

Community Article

[https://community.servicenow.com/community?id=community\_blog&sys\_id=e235c06cdbe7d050b1b102d5ca9619d7](https://community.servicenow.com/community?id=community_blog&sys_id=e235c06cdbe7d050b1b102d5ca9619d7)

  

Product Documentation

-   [ACL Debugging Tools](https://docs.servicenow.com/csh?topicname=c_AccessControlRulesDebug.html&version=latest)
-   [ACL Troubleshooting reference](https://docs.servicenow.com/csh?topicname=r_ACLTroubleshoot.html&version=latest)
-   [Create an ACL rule](https://docs.servicenow.com/csh?topicname=t_CreateAnACLRule.html&version=latest)
