---
title: "How the authentication model works in ServiceNow"
aliases:
  - KB0518896
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0518896
kb_number: KB0518896
last_modified: 2026-03-18
---

## Issue

This article describes how the ServiceNow authentication model works, including the authentication sequence, session management with the Remember Me feature, cookie behavior, and session expiration rules.

## Resolution

The following diagram illustrates the authentication sequence:

![Authentication Sequence Diagram displaying the process of authenticating a user upon login.](/Auth_sequence_diagram.pngx "Authentication Sequence Diagram")

#### Legend

-   **GlideServlet**: Handles system initialization and all servlet transactions (doPost and doGet methods).
-   **GlideServletTransaction**: Handles semaphore checks, times out long-running transactions, and similar operations.
-   **GlideServletUITransaction**: Processes actions (Update, Insert, Delete, and so on), then renders lists and forms.
-   **GlideRecord**: High-level interface to the database.
-   **User**: Represents a user loaded from the sys\_user table.
-   **GlideSession**: Tracks a session. All user and background interactions have a session. Sessions have roles and locale specifications.

#### Session management

Selecting the Remember Me check box keeps you logged in until you manually log out. Your browser must have secure cookies enabled to use this feature.

When you select the Remember Me check box at login, the following cookies are stored on your computer:

1.  `glide_user`: SCv2:token (Base64 encoded; user\_name is added for non-production environments) — long-lived cookie
2.  `glide_user_session`: Same as above — session cookie

The token is a 32-character GUID in the form of a 32-character hex value. This token is also stored in the sys\_user\_token table along with the user\_name.

These cookies automatically authenticate you on subsequent visits. The token is retrieved from the cookie and compared against the sys\_user\_token table to confirm it is still valid. If it is valid, the user\_name associated with the token in the sys\_user\_token table is used to log in.

#### Session expiration

The HTTP session remains active for 30 minutes (Tomcat default) or until the browser is closed, whichever comes first. If the HTTP session is active, user information is retrieved from it. Otherwise, the system uses the token from the cookie.

The cookie lifetime is normally set to 2^31 − 1 seconds (approximately 68 years). For users with time-limited credentials (for example, user@snc or user@snc.role1,role2,...), the lifetime is set to one day.

When you log out, these cookies are destroyed and you must log in again for subsequent visits. The corresponding token in the sys\_user\_token table is invalidated by updating the timestamp to sysdate.
