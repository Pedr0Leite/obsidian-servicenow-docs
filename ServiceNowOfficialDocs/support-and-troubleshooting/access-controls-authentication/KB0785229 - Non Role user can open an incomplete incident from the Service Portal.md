---
title: "Non Role user can open an incomplete incident from the Service Portal"
aliases:
  - KB0785229
tags:
  - servicenow
  - support-kb
  - acl
  - acl-script
  - service-portal
  - incident
  - create-acl
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785229
kb_number: KB0785229
last_modified: 2026-04-06
---

## Non Role user can open an incomplete incident from the Service Portal

  

### Issue

**Issue:**  
Non Role user can open an incomplete incident from the Service Portal  
  
**Steps to Reproduce:**  
\- Log into instance  
\- Impersonate as user with read only roles  
\- Go to URL: https://<instance\_name>.service-now.com/sp/?id=form&table=incident&filter=active%3Dtrue&sys\_id=-1&v=  
\- Notice user is able to submit incident  
  

### Release

Any

### Cause

**Most Probable Cause:**  
\- User doesn't have any roles assigned.  
\- Checked the create ACL on incident table and there is no restriction added for any roles. (https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=80a7a096c0a8016662c872762163bbdc)

### Resolution

If you want to make incident form read only on the portal for the user : create a role and assign to the user.  
On the create ACL above, you need to add a script check if the user has the new created role and set the answer to false. (https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=80a7a096c0a8016662c872762163bbdc)  
Example code below:

\[code\]<pre><code>answer = true;<br/>if (gs.hasRole('new\_restriced\_role'))<br/> answer = false;<br/>if(pm.isActive('com.snc.incident.mim') &amp;&amp; current.major\_incident\_state == 'accepted'){<br/> if(gs.hasRole('major\_incident\_manager'))<br/> answer = true;<br/> else<br/> answer = false;<br/>}<br/></code></pre>\[/code\]

You can go to the Portal and check now, "save" button will be hidden restricting the user to submit incident.

## Related

- [[KB0750886 - ACL script is failing at script include function call]] — syntax reference for writing correct ACL scripts
- [[KB0693899 - On Service Portal the record producer form  does not display all subcategories option  for users with no role]] — another Service Portal issue affecting users with no role
- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — background on how create ACLs are evaluated
