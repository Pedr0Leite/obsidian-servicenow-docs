---
title: "Why am I unable to find a record that was created in an ATF (Automated Test Framework) test after it completes?"
aliases:
  - KB0687518
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687518
kb_number: KB0687518
last_modified: 2025-04-10
---

## Why am I unable to find a record that was created in an ATF (Automated Test Framework) test after it completes?

  

### Issue

# Symptoms

* * *

-   Unable to find records that were created during an ATF test.
-   Data created during the test seems to be unavailable.

# Release

* * *

Istanbul+

# Cause

* * *

ATF rolls back all changes it makes, because it is designed for testing functionality and not for generating data.

Any data created throughout that specific test will be erased upon test completion.

# Resolution

* * *

-   Records will not be available post-test, but they can be viewed while the test is still active (prior to rollback)
-   Users can add a validation step at the end of the test that will fail. As long as the validation evaluates to false, the test will wait patiently until the timeout. By default, the timeout is set to a maximum of 590 seconds (9.83 minutes).
-   More information is available here [https://community.servicenow.com/community?id=community\_blog&sys\_id=80f34f3bdbc02b44fece0b55ca961990](https://community.servicenow.com/community?id=community_blog&sys_id=80f34f3bdbc02b44fece0b55ca961990)
