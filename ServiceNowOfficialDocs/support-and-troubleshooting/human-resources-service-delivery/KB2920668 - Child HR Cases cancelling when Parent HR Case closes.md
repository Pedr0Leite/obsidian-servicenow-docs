---
title: "Child HR Cases cancelling when Parent HR Case closes"
aliases:
  - KB2920668
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2920668
kb_number: KB2920668
last_modified: 2026-03-27
---

## Child HR Cases cancelling when Parent HR Case closes

  

### Summary

**Issue**: Child HR Cases are cancelling when the Parent HR Case closes.

**Cause**: This is working as designed, OOB expected behavior. 

The OOTB functionality is implemented by the "Cancel or Close Case Cleanup" Business Rule, which calls the cleanupChildRecordsForCase method in the hr\_utils Script Include. The script within this method sets the child cases to "Cancelled" if they are still open.

There is no OOTB way or configuration to carry on the current state of child cases. 

How to Change this behavior: To achieve desired outcome, ServiceNow best practices (avoiding direct modification of OOTB scripts), the recommended approach involves creating custom configurations.

You can create your own business rule and script includes to control the state of the HR child cases when the parent is closed. 

### Release

All
