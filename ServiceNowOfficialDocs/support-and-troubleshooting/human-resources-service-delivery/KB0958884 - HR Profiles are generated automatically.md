---
title: "HR Profiles are generated automatically"
aliases:
  - KB0958884
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958884
kb_number: KB0958884
last_modified: 2026-02-12
---

## HR Profiles are generated automatically

  

### Issue

HR Profiles are generated automatically when a user without an HR profile raise an HR case

### Release

All release

### Cause

If the HR records producer calls script include 'hr\_ServicesUtil' it will make a call to 'hr\_CaseUtils' which uses script include 'hr\_Profile'.

The 'hr\_Profile', script include will find a profile with the requested user and return it, else, it will create a profile by createProfileFromUser.

### Resolution

This is an expected behaviour based on the hr\_ServicesUtil, hr\_CaseUtils, and hr\_Profile scripts.
