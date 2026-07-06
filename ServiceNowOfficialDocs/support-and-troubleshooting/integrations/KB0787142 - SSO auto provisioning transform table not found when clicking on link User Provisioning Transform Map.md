---
title: "SSO auto provisioning transform table not found when clicking on link \"User Provisioning Transform Map\"
aliases:
  - KB0787142
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787142
kb_number: KB0787142
last_modified: 2024-04-08
---

## SSO auto provisioning transform table not found when clicking on link "User Provisioning Transform Map"

  

### Issue

After clicking on link "User Provisioning Transform Map", it is expected that an existing Transform Map record will exist but a new Transform map is created.

### Cause

That is because options to use the transform map should be activated at least once to create the transform map

Options (tick boxes) should have been enabled at least once:

"Update User Record Upon Each Login"  
AND/OR  
"Auto Provisioning User "

### Resolution

Enable (and Disable again if functionality not ready yet)

"Update User Record Upon Each Login"  
AND/OR  
"Auto Provisioning User "
