---
title: "Multiple login.failed events / User getting locked out after 3 failed attempts"
aliases:
  - KB0749501
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749501
kb_number: KB0749501
last_modified: 2024-04-07
---

## Issue

# Symptoms

Multiple failed logins events (login.failed) are getting created for single failed login. Which is resulting the faster account lock out which is having a default threshold of 5 defined in the script action : SNC User Lockout Check

# Release

All versions

# Environment

Instance is having Multi SSO plugin activated

# Cause

The Event "login.failed " is getting called in the installation exits.

In the "MultiSSOLogin" or any other customised installation exits you may see the event is calling as shown below

### EventManager.queue("login.failed", "", userName, t == null ? null : t.getRemoteAddr());

# Resolution

After validating you can comment out the **EventManager.queue("login.failed", "", userName, t == null ? null : t.getRemoteAddr());** and test the same. This will prevent the creation of additional **"login.failed"**event in the event log
