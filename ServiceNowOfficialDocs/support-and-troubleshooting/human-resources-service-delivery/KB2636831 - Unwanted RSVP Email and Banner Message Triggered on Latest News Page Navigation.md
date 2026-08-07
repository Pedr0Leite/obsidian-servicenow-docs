---
title: "Unwanted RSVP Email and Banner Message Triggered on Latest News Page Navigation"
aliases:
  - KB2636831
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636831
kb_number: KB2636831
last_modified: 2026-01-01
---

## Unwanted RSVP Email and Banner Message Triggered on Latest News Page Navigation

  

### Issue

When users visit the Latest News page in the portal and navigate back:

-   An unwanted RSVP confirmation email is triggered.
-   An out-of-box (OOTB) info message “Thanks for your RSVP” appears at the top of the page, even though no RSVP action was taken.
-   Disabling the RSVP Confirm email notification stops the emails, but the banner message persists.

### Release

Any Release

### Cause

The issue is caused by the News Header widget when the Use Dataloader option is turned off.

### Resolution

1.  Navigate to the News Header widget instance in the portal configuration.
2.  Locate the Use Dataloader option in the widget settings.
3.  Enable Use Dataloader to prevent the RSVP email and banner message from triggering unexpectedly.
4.  Save the widget configuration and refresh the portal page.
5.  Verify:
    -   No unwanted RSVP email is sent.
    -   The “Thanks for your RSVP” banner does not appear when navigating back from the Latest News page.

Additional Info:

-   The issue is fixed in later releases under PRB1912242.
-   Enabling Use Dataloader is the recommended workaround for affected versions.
