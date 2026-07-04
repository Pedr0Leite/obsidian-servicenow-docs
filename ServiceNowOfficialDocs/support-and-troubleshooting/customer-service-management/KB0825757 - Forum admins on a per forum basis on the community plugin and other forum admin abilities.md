---
title: "Forum admins on a per forum basis on the community plugin and other forum admin abilities"
aliases:
  - KB0825757
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0825757
kb_number: KB0825757
last_modified: 2024-08-28
---

## Forum admins on a per forum basis on the community plugin and other forum admin abilities

  

### Issue

The community admin role can act as admin for each forum on the community plugin. How can you make a user be a forum admin for just one forum (and the subsequent sub forums) 

  
Example: There are two forums (ie 'FORUM A' and 'FORUM B'). How can we make a user be an admin for 'FORUM A' but not for 'FORUM B'

Steps to reproduce

1.  Install community plugin
2.  Log in as forum admin
3.  Go to Community -> Administration -> Forums
4.  Click on multiple forums
5.  Observe that you can edit all forums

### Cause

This is not out of the box behaviour and is therefore not documented on the product but it is possible

### Resolution

Possible solutions. In any case make sure the forum admin does not have the admin role

Solution 1

1.  Create two new forums (ex. 'FORUM A' and 'FORUM B')  
    2\. Add a forum permission to one (ex create a new one called 'SN TEST A Admin group' on 'FORUM A')  
    3\. Add a member to 'SN TEST A Admin group'  
    4\. This member is an admin of the 'FORUM A' group but cannot see 'FORUM B' in the platform, nor on the community portal

If there is a sub-forum, the forum admin will need to be added to each one of those. These forum permissions do not transfer to subforums.

If a user has the role "sn\_communities.community\_moderator" which gives control over community they may be able to see multiple forums.

  
Solution 2

1.  Go to forum and forum exceptions, assign a particular user with forum admin permission.
2.  This may be simple but if they are more than one user who can administer a forum, a new entry needs to be created here.
3.  But with the second option, just adding users to a particular forum user is enough.

### Related Links

Here is a list of a few of the actions that cannot be done by a forum admin:

1.  Cannot create new forums but can configure the forum (supported content types permission, forum users etc..)
2.  Cannot update content types and feed back types at the community level.
3.  Cannot configure video configuration
4.  Cannot configure profile field mapping, moderation settings, community properties
5.  Cannot ban a user.
6.  Featuring content in forums and content movement between forums can be done within the forums for which they are an admin.
7.  The feature required roles can be added to get the below features for forum admin, but these will have an affect at the community level, so it’s not recommended to assign the roles to forum admin
8.  Cannot create case from question  
    1.  knowledge harvesting
    2.  gamification setting
9.  Can moderate the content in the forum

Heres the link to overview of community roles:  
[https://docs.servicenow.com/csh?topicname=communities-roles.html&version=latest](https://docs.servicenow.com/csh?topicname=communities-roles.html&version=latest)

For more detailed feature/config related info look in to the documentation  
[https://docs.servicenow.com/csh?topicname=servicenow-communities.html&version=latest](https://docs.servicenow.com/csh?topicname=servicenow-communities.html&version=latest)  
[https://docs.servicenow.com/csh?topicname=configure-communities.html&version=latest](https://docs.servicenow.com/csh?topicname=configure-communities.html&version=latest)
