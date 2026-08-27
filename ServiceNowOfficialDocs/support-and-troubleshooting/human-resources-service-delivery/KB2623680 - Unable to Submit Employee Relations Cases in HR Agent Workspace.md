---
title: "Unable to Submit Employee Relations Cases in HR Agent Workspace"
aliases:
  - KB2623680
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2623680
kb_number: KB2623680
last_modified: 2025-12-14
---

## Unable to Submit Employee Relations Cases in HR Agent Workspace

  

### Issue

Users are unable to submit new Employee Relations COE cases via HR Agent Workspace. After filling in details and clicking Submit, the page shows no progress.

-   Issue occurs for multiple users and is reproducible with and without impersonation.
-   Case creation is inconsistent and sometimes works after configuration changes.

### Release

Xanadu

### Cause

The impersonation check property and related ACLs were preventing mandatory fields from being visible on the HR Case creation page. When required fields are hidden, the Submit button remains inactive, blocking case creation.

### Resolution

Perform the following steps to resolve the issue:

#### Step 1: Navigate to System Properties

-   Go to System Properties in your instance.
-   Locate the property:  
    check\_impersonation\_on\_acl\_evaluation\_in\_hr\_app  
    (Impersonation Check for ACL Evaluation in HR App).

#### Step 2: Disable the Property

-   Set the property value to false.
-   Click Save.

#### Step 3: Verify Mandatory Fields

-   Go to HR Case Creation Configuration.
-   Ensure all mandatory fields configured for case creation are also present on the form layout.
-   Add missing fields if necessary.

#### Step 4: Clear Cache

-   Navigate to System Diagnostics > Cache.
-   Clear the cache to refresh configurations.

#### Step 5: Test Case Submission

-   Open HR Agent Workspace.
-   Create an Employee Relations case and click Submit.
-   Confirm that the case is created successfully.
