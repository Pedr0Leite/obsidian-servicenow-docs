---
title: "Is it recommended to have Parent Instance and Child instances on different versions in Team Development?"
aliases:
  - KB0754144
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754144
kb_number: KB0754144
last_modified: 2024-04-07
---

## Is it recommended to have Parent Instance and Child instances on different versions in Team Development?

  

### Issue

Is it recommended to have Parent Instance and Child instances on different versions in Team Development?

### Release

All Releases

### Resolution

The answer to that question is a No. It is expected that the sub-development instances are on the same software version as the parent development instance.

The way we suggest to set up a Team Dev environment is as follows:   
1\. Have a parent development instance on the same software version, such as Madrid, as the target instance, such as production.   
2\. \[Recommended\] Clone the production instance to the parent development instance.   
3\. Provision sub-development instances on the same software version as the parent development instance.   
4\. (Optional) Log in to the parent development instance and clone it to the sub-development instances.   
5\. On each sub-development instance: \*Define remote instance connections to other instances in the hierarchy that this instance needs to push and pull with.   
    \*Select the parent instance.   
    \*Pull all changes from the parent instance.   
    \*Grant access rights to appropriate developers.   
  
The parent instance must be on the same release family as the local instance. For example, a development instance on the Madrid release family must have a parent instance also on the Madrid release family. If you select a parent from a different release family, the Team Development dashboard displays an error message and prevents you from pulling changes and reconciling. If you select a parent from a different patch release, the dashboard displays a warning message but allows you to pull changes and reconcile. 

### Related Links

In addition to the above information, please find below a useful documentation that is helpful   
[https://docs.servicenow.com/csh?topicname=t\_SelectTheParentInstance.html&version=latest](https://docs.servicenow.com/csh?topicname=t_SelectTheParentInstance.html&version=latest)
