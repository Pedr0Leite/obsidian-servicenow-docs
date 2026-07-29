---
title: "Discovery identification fails with error: Abandoned due to too many errors"
aliases:
  - KB0725605
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725605
kb_number: KB0725605
last_modified: 2024-04-07
---

## Discovery identification fails with error: Abandoned due to too many errors

  

### Issue

Pattern discovery of a device fails with error "**Abandoned due to too many errors**".

### Release

All currently supported releases.

### Cause

Multiple identification error when processing dependent CI(s) in the payload passed to the Identification and Reconciliation Engine.

### Resolution

Review the system logs, at the time of the error, to find the actual error causing the discovery to fail.

1.  Navigate to "System Logs > System Log > Errors".
2.  Filter for "Source = identification\_engine".
3.  Filter by created date to match the time the inputs were processed.

The review of the logs may lead to an error such as:

-   identification\_engine : IDENTIFICATION\_RULE\_FOR\_LOOKUP\_MISSING Identity Rule for table \[cmdb\_ci\_hardware\] missing Lookup Rule for class \[cmdb\_serial\_number\] 

From the above, we see the actual error in all caps is "IDENTIFICATION\_RULE\_FOR\_LOOKUP\_MISSING".

The next step is to search for the error/solution on the following link:

-   [Identification engine error messages](https://docs.servicenow.com/csh?topicname=id-engine-error-messages.html&version=latest "Identification engine error messages")

For the example error, we see the description/solution to be:

-   Description:The payload has a lookup class name, but the corresponding lookup rule is missing.
-   Resolution:Add lookup identifier entry with \[Search on table\] as \[_**abc**_\] for CI Identifier for table \[_**xyz**_\].
