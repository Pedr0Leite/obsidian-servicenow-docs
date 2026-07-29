---
title: "How to apply any user preferences for all users"
aliases:
  - KB0695142
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695142
kb_number: KB0695142
last_modified: 2025-01-03
---

## How to apply any user preferences for all users

  

### Issue

  
  

# Description

* * *

This article details the steps that admins can take to apply any user preferences (such as homepage refresh value, list sorting order, related list loading, etc.) to all users.

# Procedure

* * *

1) As an admin navigate to User Administration > User Preferences > Click New

2) Determine which user preference would be applied to all users. In this case we'll be using 'home\_refresh' as an example (this is user preference that controls the homepage refresh rate)

3) Fill in the fields with the following values:

-   Name: home\_refresh
-   System: True/Checked
-   Type: String (change it according to what type of user preference is being used; refer to one OOB user preference of the same for proper type)
-   User: Leave this field empty
-   Value: 900 (change it according to which proper value is accepted; refer to one OOB user preference of the same for proper accepted values)

4) Submit the record

\*\*It might be necessary for users to log out and log back in to see the new effect

IMPORTANT: For users who already have their own user preferences (before the system user preference is applied) this won't apply to them as their own user preferences would always take precedence. For users who do not have their own first the system user preference would apply. But the users may always modify their user preferences after and those will then apply going forward.

# Applicable Versions

* * *

All versions

# Additional Information

* * *

[User preferences](https://docs.servicenow.com/csh?topicname=c_UserPreferences.html&version=latest "User preferences")
