---
title: "Updating Cases through email reply did not update the additional comments"
aliases:
  - KB0744909
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744909
kb_number: KB0744909
last_modified: 2024-04-07
---

## Issue

# Symptoms

When an email is replied to update the Case, the email is received but the email body comments not updated in the Additional comments.

# Release

Kingston, London

# Cause

The Out of the Box inbound email action "Update Case via reply" doesn't have the script statements to update the additional comments or the work notes.

# Resolution

1.  Open the Inbound Email Action - Update Case via reply add the below lines after the first line variable declaration statement or before the if loop.
2.  To add the email body in the additional comments add the below: current.comments = "reply from: " + email.origemail + "\\n\\n" + email.body\_text;
3.  To add the email body in the worknotes add the line current.work\_notes = "reply from: " + email.origemail + "\\n\\n" + email.body\_text;
