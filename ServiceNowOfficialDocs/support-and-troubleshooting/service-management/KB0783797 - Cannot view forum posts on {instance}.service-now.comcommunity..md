---
title: "Cannot view forum posts on {instance}.service-now.com/community."
aliases:
  - KB0783797
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783797
kb_number: KB0783797
last_modified: 2024-05-16
---

## Cannot view forum posts on {instance}.service-now.com/community.

  

### Issue

Community forum posts are not visible to any user, including admins, why?

### Cause

The root cause of this issue was that the user had a custom implementation for the "CommunityContentDao" Script Include (SI) named "StarkIndustriesCommunityContentDao" which was using the releaseLock function of the "CommunityGlobalUtilSNC" SI.

### Resolution

As a reference, it was suggested that the user take a look at the "CommunityContentDao" SI, and resolve their customization issues.  
  
It was also suggested that the resolution to the customization also be applied to the following methods if used anywhere else in the customizations:

-   releaseLock()
-   addLock()

You can use the following methods in place of the above methods to achieve the same functionality (refer to CommunityContentDao, CommunityFeedbackDao, CommunityContentImpl for usage, respectively):

-   commentPosted()
-   feedbackPosted()
-   contentVisited()
-   updateAutoSysFields()
