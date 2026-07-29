---
title: "Email Notifications in Global Domain Apply to Records Across All Domains"
aliases:
  - KB0748040
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748040
kb_number: KB0748040
last_modified: 2024-04-26
---

## Email Notifications in Global Domain Apply to Records Across All Domains

  

### Issue

# Symptoms

There is a record that is in a non-Global domain, e.g. TOP/xyz.

An email notification is sent by a notification that is in the Global domain. The sending conditions in the notification have all been met.

It may have been expected that the email would not be sent since the affected record is not in the Global domain, but the notification is in the Global domain.  

# Release

Any Release

# Cause

This is working as designed.

# Resolution

The documentation is not clear on how this should work:

[https://docs.servicenow.com/csh?topicname=domain-separation-notifications.html&version=latest](https://docs.servicenow.com/csh?topicname=domain-separation-notifications.html&version=latest)

This use case is not defined under "How domain separation works in Notifications".  A request to update this documentation has been entered.

The documentation here should make it clear that notifications in the Global domain will be applied to all records no matter which domain they are created in.
