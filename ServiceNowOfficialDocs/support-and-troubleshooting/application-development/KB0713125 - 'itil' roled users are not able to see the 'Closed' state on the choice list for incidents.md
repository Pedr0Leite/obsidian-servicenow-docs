---
title: "'itil' roled users are not able to see the 'Closed' state on the choice list for incidents"
aliases:
  - KB0713125
tags:
  - servicenow
  - support-kb
  - client-scripts
  - incident-management
  - roles
  - choice-list
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713125
kb_number: KB0713125
last_modified: 2024-04-18
---

## 'itil' roled users are not able to see the 'Closed' state on the choice list for incidents

  

### Issue

# Symptoms

* * *

When 'itil' roled users are accessing the incident form and attempting to change the state field to 'Closed', this option is not available to them.

# Release

* * *

All releases

#   

# Cause

* * *

This is caused by the following Client Script which checks whether users have the 'itil\_admin' role.

https://<instance-name>.service-now.com/sys\_script\_client.do?sys\_id=38c58af84657628200aeb11d8295f42c

# Resolution

* * *

1.  Open up the following Client Script - "(BP) Hide Choice - Closed"  
      
    https://<instance-name>.service-now.com/sys\_script\_client.do?sys\_id=38c58af84657628200aeb11d8295f42c  
      
    
2.  Change the 4th line to be the following:  
      
    if (g\_user.hasRole('itil'))  
      
    
3.  Save the record.

#

## Related

- [[KB0697413 - In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()]]
- [[KB0720671 - Generic error on form Submit canceled due to a script error - please contact your System Administrator]]
