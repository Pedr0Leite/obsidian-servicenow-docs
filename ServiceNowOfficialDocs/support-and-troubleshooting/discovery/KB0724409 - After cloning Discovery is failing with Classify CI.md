---
title: "After cloning Discovery is failing with Classify CI"
aliases:
  - KB0724409
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724409
kb_number: KB0724409
last_modified: 2024-04-07
---

## After cloning Discovery is failing with Classify CI

  

### Issue

# Symptoms

* * *

Discovery was working until the instance was cloned over.  Discovery is working on one instance but it does not work on another instance.  The failure is during the classification phase.

# Release

* * *

All

# Cause

* * *

The credentials maybe tied to a particular mid server.  That mid server may not exist or attached to this particular instance you trying to run discovery from.  Discovery will fail because the active mid server does not have the correct credentials to use for discovery.

# Resolution

* * *

1.  Go to the Credentials table discovery\_credentials

2.  Select the credential which should work for the CI that you're trying to discover

3.  Look at the Applies to Section.  Check to see if it set use a particular mid server.  

4.  If it's set to use a particular mid server. Make sure you see the mid server that's can access the target device is listed there, or change the applies to "All MID servers". 

5\. If you see sys\_id instead of name, those mid server does not exist in this environment. You can remove them from the list.
