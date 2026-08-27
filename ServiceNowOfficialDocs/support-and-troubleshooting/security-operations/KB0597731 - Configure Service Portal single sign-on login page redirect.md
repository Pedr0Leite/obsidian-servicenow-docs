---
title: "Configure Service Portal  single sign-on login page redirect"
aliases:
  - KB0597731
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597731
kb_number: KB0597731
last_modified: 2025-09-08
---

## Issue

Service Portal works with single sign-on (SSO) to redirect users to your primary Identity Provider (IDP) or display external login options. This article explains how to configure authentication requirements and redirect users to Service Portal after login:

-   Require authentication for every Service Portal
-   Make Service Portal your default login page
-   Conditionally redirect to Service Portal after login
-   Debugging

## Resolution

#### Require authentication for every Service Portal

Some companies want their portal content available to only authenticated users. To do this, activate the Service Portal plugin (Service Portal for Enterprise Service Management).

Activating this plugin provides the $sp in sys\_public.list and all modules for Service Portal.

Set the following values:

-   Page: $sp
-   Active: true

When unauthenticated users access \[instance\]/sp or \[instance\]/$sp.do, they are redirected to the platform configured login page. This is particularly useful for organizations with complex SSO environments.

#### Make Service Portal your login page

To make Service Portal the login page for your instance:

-   Set the system property glide.entry.page.script to the new SPEntryPage().getLoginURL().

**Configure the SPEntryPage**

SPEntryPage uses /sp/ as the portal path for redirects. To change this path:

1.  Edit the SPEntryPage script include
2.  Change the assigned portal to your preferred portal\_suffix.

**Note:** After modifying this script include, it will not be upgraded with future updates. 

[![](/sys_attachment.do?sys_id=c0de08be47732ad4c2488d01426d4334)](https://github.com/service-portal/documentation/blob/master/assets/sso/portal_suffix.png)

#### **Conditionally redirect to Service Portal after login**

Set the system property glide.entry.first.page.script to new SPEntryPage().getFirstPageURL().

The getFirstPageURL function does the following: 

1.  Redirects to [login\_redirect.do](http://login_redirect.do) in order to break out of the frameset (if one exists).
2.  Redirects to Service Portal if the user has no roles, or to the full platform for all other users.

You can customize this behavior within the SPEntryPage script include.

**Note:** After modifying this script include, it will not be upgraded with future updates. 

#### **Debugging**

To view debug output from SPEntryPage and see the session variables for redirects:

1.  Verify the system property glide.entry.first.page.script is set to the new SPEntryPage().getFirstPageURL().
2.  Open the SPEntryPage script include. 
3.  Find and set **this.logVariables** to **true**.
4.  In a different browser (or incognito or inPrivate session), log in.
5.  To view the log output, go to **System Logs** > **System Log** > **All** or by going directly to: /syslog\_list.do?sysparm\_query=level%3D0%5EORDERBYDESCsys\_created\_on&sysparm\_first\_row=1&sysparm\_view=
