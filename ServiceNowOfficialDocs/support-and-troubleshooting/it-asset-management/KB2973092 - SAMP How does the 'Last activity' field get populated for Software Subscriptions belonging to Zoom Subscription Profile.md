---
title: "SAMP: How does the 'Last activity' field get populated for Software Subscriptions belonging to Zoom Subscription Profile"
aliases:
  - KB2973092
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2973092
kb_number: KB2973092
last_modified: 2026-04-23
---

## SAMP: How does the 'Last activity' field get populated for Software Subscriptions belonging to Zoom Subscription Profile

  

### Issue

This KB is to explain in detail how the "Last activity" field gets populated for Software Subscriptions, specifically belonging to the Zoom Subscription Profile.

### Symptoms

We might notice that a few/all Software Subscriptions, that belong to the Zoom Subscription Profile, **may have the "Last activity" field EMPTY.**

### Facts

We track when a user hosts a meeting as the last activity for Zoom and when a user hosts a webinar as the last activity for Zoom webinar.  
We do not track last\_login\_time from the /users API as the parameter for last activity.

'Refresh Zoom Events' job is used to find 'meeting' and 'webinar' information for a user to update the Last Activity field on subscription.

Note: 'Refresh Zoom Events' Scheduled script will be available under \[sam\_saas\_sysauto\_script\] when the Zoom subscription profile is set up.

### Release

All

### Cause

When the '**Refresh Zoom Events**' Scheduled script is run, in the Outbound HTTP Log we do see something being populated in the Response Body under "meetings", especially for the Subscriptions that do have "Last activity" populated.

Working Example:

Response body:  
{"page\_size":300,"total\_records":2,"next\_page\_token":"","meetings":\[{"uuid":"Z0wRWectT+exXYtohXXXXX=\*\*body truncated\*\*  
https://<INSTANCE\_NAME>.service-now.com/sys\_outbound\_http\_log.do?sys\_id=<SYS\_ID>

And for the Subscriptions with EMPTY "Last activity"

Non-populating Example:

Response body:  
{"page\_size":300,"total\_records":0,"next\_page\_token":"","meetings":\[\]}  
https://<INSTANCE\_NAME>.service-now.com/sys\_outbound\_http\_log.do?sys\_id=<SYS\_ID>

The 'last\_activity' field was not populated for a few/all Zoom subscriptions because the Zoom API (GET /users/{userId}/meetings) returns empty 'meetings' arrays for users without upcoming scheduled meetings or Zoom API (GET /users/{userId}/webinars) returns empty 'webinars' arrays for users without upcoming webinars. The integration logic relies on this API to update 'last\_activity' based on meeting start times, but users without future meetings or with expired meetings did not trigger updates.

Logic is from "**SAMSaasZoomIntegration**" Script include under "**\_updateSubscriptionsFromEvents**" function  
https://<INSTANCE\_NAME>.service-now.com/sys\_script\_include.do?sys\_id=cbcb036567522300cdfacbb35685ef74

### Resolution

Given that:

-   "GET /users/{userId}/meetings" API only supports scheduled meetings
-   "GET /users/{userId}/webinars" API only supports scheduled webinars

You will need to make sure that there are scheduled meetings for the expected user subscription to populate the Last activity field.

### Related Links

1\. List meetings

get /users/{userId}/meetings  
List a meeting host user's scheduled meetings. For user-level apps, pass the me value instead of the userId parameter.

Prerequisites:

This API only supports scheduled meetings. This API does not return information about instant meetings.  
This API only returns a user's unexpired meetings.  
When type is set to upcoming, upcoming\_meetings, or previous\_meetings, only a maximum of 6 months of meeting data will be returned.  
Scopes: meeting:read:admin,meeting:read

Granular Scopes: meeting:read:list\_meetings,meeting:read:list\_meetings:admin

[Zoom: Zoom Meeting API - List Meetings](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetings "Zoom: Zoom Meeting API - List Meetings")  
[Zoom: GET /users/{userId}/meetings](https://developers.zoom.us/docs/api/meetings/#tag/meetings)

2\. List webinars

get /users/{userId}/webinars  
List all the webinars scheduled by or on behalf a webinar host. For user-level apps, pass the me value instead of the userId parameter.

Zoom users with a webinar plan have access to creating and managing webinars. Webinars let a host broadcast a Zoom meeting to up to 10,000 attendees.

Note This API only returns a user's unexpired webinars.

Prerequisites

A Pro or higher plan with the webinar add-on.  
Scopes: webinar:read:admin,webinar:read

Granular Scopes: webinar:read:list\_webinars,webinar:read:list\_webinars:admin

[Zoom: List webinars](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinars)  
[Zoom: GET /users/{userId}/webinars](https://developers.zoom.us/docs/api/meetings/#tag/webinars)

3\. ServiceNow Docs: Integrating with Zoom

[Docs: Software Asset Management - Integrating with Zoom](https://www.servicenow.com/docs/r/it-asset-management/saas-license-management/integrate-with-zoom.html?section=integrate-with-zoom "Docs: Software Asset Management - Integrating with Zoom")
