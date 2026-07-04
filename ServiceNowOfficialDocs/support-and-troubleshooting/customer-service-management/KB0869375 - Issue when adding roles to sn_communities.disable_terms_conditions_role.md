---
title: "Issue when adding roles to sn_communities.disable_terms_conditions_role"
aliases:
  - KB0869375
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869375
kb_number: KB0869375
last_modified: 2026-03-22
---

## Issue when adding roles to sn\_communities.disable\_terms\_conditions\_role

  

### Issue

Customer want to disable pop up to accept T&C before accessing community

### Release

All

### Resolution

Out of box, widgets "Communities T&C Blocker" and "Terms and conditions" are responsible for creating a community profile record and adding 'sn\_communities.community\_user' role to the sys\_user record. Apart from this, it will populate the \`accepted\_tc\`, \`accepted\_tc\_date\`, and \`accepted\_tc\_on\` fields on the newly created community profile record.  
  
The property that we have used here (\`sn\_communities.disable\_terms\_conditions\_role\`) will be used to disable the Terms & Condition popup during initial login (to community) and redirect the user to the Community Home page. Which means this property will be used to skip the creation of community profile record, skip granting community user role action, and accepting terms and conditions.  
  
If you want to skip the T&C dialog for all the snc\_external users. To achieve this requirement with the above property, you have to create all the necessary prerequisites upfront.  
  
Generally, we will have two types of snc\_external users  
1) self-registered users: By default, we will not see T&C popup for these users as the user accepts them during their sign-up.  
2) Platform users with role snc\_external:  
\>>>> Whenever a platform user with the role \`snc\_external\` is being switched to the \`community\` portal then we will run into this issue. As the observed behavior is an Out of box behavior we can achieve the requirement through the following customization.  
A) Create a community profile record and live\_profile record upfront, before the user switching to the Community portal  
B) Grant the role \`sn\_communities.community\_user\` to user  
C) Update fields \`accepted\_tc\`, \`accepted\_tc\_date\`, and \`accepted\_tc\_on\` fields on community profile record.
