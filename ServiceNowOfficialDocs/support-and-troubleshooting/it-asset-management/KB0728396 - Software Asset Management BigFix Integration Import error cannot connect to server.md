---
title: "Software Asset Management BigFix Integration Import error cannot connect to server"
aliases:
  - KB0728396
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728396
kb_number: KB0728396
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Software Asset Management BigFix Integration Import error:

-   **cannot connect to server.**
-   **url 'https://<ip>:<port>/sam/processors?token=<token>' is not valid.**

# Release

* * *

All currently supported versions.

# Cause

* * *

The BigFix integration will create a record in the ecc\_queue for the MID server configured. The topic will be RESTProbe. The ecc\_queue output record will not be created if a MID server cannot be selected.

# Resolution

* * *

**Check if the ecc\_queue record was created for the MID server:**

1.  Navigate to the "ECC > Queue" table.
2.  Filter for records where Topic = "RESTProbe".
3.  Open record and check it contains the endpoint url.

If no records are found with "RESTProbe" topic, then a MID server could not be selected.

**To resolve the issue:**

1.  Check that the MID server has a record on ecc\_agent\_status table with the same name.
2.  Check the MID server IP range, Capabilities, and Applications configured. See Additional Information "MID Server selection" document.
3.  Attempt BigFix import again.

# Additional Information

* * *

-   [Set up IBM License Metric Tool (ILMT) and BigFix Inventory integration](https://docs.servicenow.com/csh?topicname=set-up-ibm-ilmt.html&version=latest "Set up IBM License Metric Tool (ILMT) and BigFix Inventory integration")
-   [MID Server selection](https://docs.servicenow.com/csh?topicname=c_MIDServerSelector.html&version=latest "MID Server selection")
