---
title: "Handling special characters via the MID Server "
aliases:
  - KB0621052
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621052
kb_number: KB0621052
last_modified: 2026-05-07
---

## Issue

An outbound web service routed through a MID Server cannot handle special characters if the MID Server is not properly configured. For example, when a form field contains an ampersand (&) and is submitted via a REST call, the MID Server automatically encodes the & symbol to `&amp;`, causing the receiving system to receive an incorrect value.

## Resolution

Complete all three steps below in order to resolve this issue.

Step 1 — Configure UTF-8 encoding on the MID Server

1.  On the MID Server host machine, open the following file in a text editor: `C:\<MID Agent Dir>\conf\wrapper-override.conf`
2.  Locate the last line that starts with `wrapper.java.additional.xx` where `xx` is a number (for example, 1, 2, or 3).
3.  Make a note of the value of `xx`.
4.  Add a new line immediately after it using the next sequential number. For example, if the last line was `wrapper.java.additional.1`, add the following new line: `wrapper.java.additional.2=-Dfile.encoding=UTF-8`

Step 2 — Add the REST capability to the MID Server

1.  In your ServiceNow instance, navigate to MID Server > Capabilities.
2.  Select the REST capability.
    -   If the REST capability does not exist, select New and create a capability with the name REST and a value of `service-now`.
3.  Select Submit.
4.  Reopen the REST capability record.
5.  In the MID Servers related list, select Edit.
6.  Move one or more MID Servers to the Selected list.
7.  Select Save.

Step 3 — Restart the MID Server

Restart the MID Server service on the host machine to apply the configuration changes.

To verify the fix, re-run the REST call and confirm that the ampersand (&) is no longer encoded as `&amp;` in the ECC Queue payload

## Additional Information

-   KB0539838 — Using special characters in an MID Server config.xml file
-   KB0718637 — How to add special characters as input in a REST Web Service activity
-   [MID Server product documentation](https://docs.servicenow.com/bundle/latest/page/product/mid-server/concept/mid-server-landing.html)
