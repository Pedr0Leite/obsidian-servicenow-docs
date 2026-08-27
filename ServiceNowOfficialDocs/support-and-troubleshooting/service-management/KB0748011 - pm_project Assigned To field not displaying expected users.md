---
title: "pm_project \"Assigned To\" field not displaying expected users"
aliases:
  - KB0748011
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748011
kb_number: KB0748011
last_modified: 2024-04-07
---

## pm\_project "Assigned To" field not displaying expected users

  

### Issue

# Symptoms

* * *

In a Project, after selecting an ‘assignment group’ in the Project form, the assigned to should be limited to those who are a member of the group. 

However not all group members are available to be selected as "Assigned to" even though they are a Group member. 

# Release

* * *

All Releases

# Cause

* * *

This is the Out-Of-Box expected behavior.

The "Assigned To" field on the "pm\_project" table has a dictionary override that is set to use the following reference qualifier: 

pm\_project 

https://xxxxxxxx.service-now.com/nav\_to.do?uri=sys\_dictionary\_override.do?sys\_id=5f25463c9f211200598a5bb0657fcf5f%26sysparm\_view=advanced 

javascript:var util = new ProjectManagementUtils(); util.assignedToRefQual(current, SNC.PPMConfig.getProjectRole('user',current.getTableName()),true); 

This reference qualifier is calling "assignedToRefQual" function on the script include "ProjectManagementUtils". This process will eventually call "SNC.PPMConfig.getProjectRole" which is looking for the it\_project\_user role. 

# Resolution

* * *

1\. Align your configuration to meet the out of the box design. To do this, follow the below 

a. Ensure your expected member records are Active. Activate User record by checking the Active flag. 

 b. Ensure the Users have the relevant role ‘it\_project\_user’

 This should allow the users display in the Assigned\_to field. 

2\. Alternatively, changing this OOB behavior requires customization, by not using the reference qualifier. As an example, unchecking "Override reference qualifier" on the "assigned\_to" dictionary override for the "pm\_project" table will revert the behavior to the "task" table dictionary definition, meaning that all group members that have the "itil" role will be listed.
