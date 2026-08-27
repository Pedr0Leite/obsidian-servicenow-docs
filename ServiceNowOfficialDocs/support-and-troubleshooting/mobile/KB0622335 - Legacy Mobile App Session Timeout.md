---
title: "Legacy Mobile App Session Timeout"
aliases:
  - KB0622335
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622335
kb_number: KB0622335
last_modified: 2026-04-02
---

## Legacy Mobile App Session Timeout

  

### Issue

This discussion applies to the ServiceNow native mobile apps for iOS and Android. This does not apply to the ServiceNow mobile web experience or other mobile applications that integrate with ServiceNow.

### Resolution

### What settings determine session timeouts in the native mobile apps?

The native mobile app's session is determined by the greater of all these settings:

-   The OAuth refresh token lifespan for the `ServiceNow Mobile App` record in the `oauth_entity` table (defined in seconds)
-   The OAuth access token lifespan for the `ServiceNow Mobile App` record in the `oauth_entity` table (defined in seconds)
-   The web session timeout defined by the `glide.ui.session_timeout` system property (defined in minutes)
-   The integration session timeout defined by the `glide.integration.session_timeout` system property (defined in minutes). If this property is not defined, it will default to 5 minutes in Helsinki and 1 minute in Istanbul.

> **Note**: In order to validate changes to these settings are working, you must log out and back in to the ServiceNow Mobile app. This is a critical step that will ensure the app uses tokens and sessions with the updated lifespans instead of using previously granted tokens or sessions with different lifespans.

### What determines session inactivity in the native mobile apps?

Sessions are considered active if the app is in the foreground or if the app is processing a long running task in the background.

Any of the following actions are considered "backgrounding" the app:

-   Explicitly sending the app to the background
-   Locking the screen or having the screen go to sleep
-   Switching to a different app

Any of the following states are considered "actively running":

-   The app is visible on the screen (in the foreground) and the screen is unlocked
-   The app is processing a long running task even if the app is in the background (such as uploading or downloading a large attachment)

### How to validate session timeout settings are working in the native mobile apps?

In this example, we want the native mobile apps to log out after 30 minutes of inactivity.

Configure these settings on your instance:

-   Set the OAuth refresh token lifespan for the `ServiceNow Mobile App` record in the `oauth_entity` table to `1800` seconds
-   Set the OAuth access token lifespan for the `ServiceNow Mobile App` record in the `oauth_entity` table to `1800` seconds or less
-   Set the web session timeout defined by the `glide.ui.session_timeout` system property to `30` minutes or less
-   Ensure that the integration session timeout defined by the `glide.integration.session_timeout` system property is either not defined or set to 30 minutes or less. If this property is not defined, it will default to 5 minutes in Helsinki and 1 minute in Istanbul.

Test these timeout settings using the native mobile app:

-   Log out of your instance with the native mobile app. This is a critical step that will ensure the app uses tokens and sessions with the updated lifespans instead of using previously granted tokens or sessions with different lifespans.
-   Log in to your instance with the native mobile app
-   Send the app to the background (see _"What determines session inactivity in the native mobile apps?"_ above)
-   Wait 30 to 35 minutes
-   Launch the app and notice that the user has been logged out

### Related Links

It should be noted that setting system property glide.ui.session\_timeout will also apply to all desktop users.

It is currently not possible to configure a timeout that just applies to the mobile app.

If this is a requirement that you would like to be added to the product I suggest that you submit an idea using the new portal.  
Please see the following knowledge article that describe the new procedure for submitting new product enhancement requests:

KB0755878 Idea Management for customer enhancement requests  
[https://hi.service-now.com/kb\_view.do?sysparm\_article=KB0755878](https://hi.service-now.com/kb_view.do?sysparm_article=KB0755878)

Note: setting just the OAuth properties Refresh Token Lifespan and Access Token Lifespan will close the mobile app even if the user is actively using the app at the time.
