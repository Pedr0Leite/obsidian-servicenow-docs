---
title: "Description field shows the text without line breaks on the Incident record"
aliases:
  - KB0791099
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791099
kb_number: KB0791099
last_modified: 2024-04-07
---

## Description field shows the text without line breaks on the Incident record

  

### Issue

When an incident is created through email, the requirement is to have the body of the email in the description field. In an attempt to accomplish this using an Inbound Action , an issue is observed where the email body is populated in the incident description with the text but without line breaks.

### Release

Any Release

### Cause

Piece of code used in the "create incident" inbound action to achieve the goal 

\=======

current.description=email.body\_text

\=======

When you look at the type of the description field, there are chances it was modified to HTML instead of string based on individual customer requirement. This is one of the reason for the text in the description field on the incident record without the line breaks.

### Resolution

We have 2 paths to resolve the problem

Solution1:

i) Configure the type of Description field on the incident table to string

ii) Use the below code in the "create incident" inbound action

current.description=email.body\_text

Solution 2:

i) Configure the type of Description field on the incident table to HTML

ii)Use the below code in the "create incident" inbound action

current.description = email.body\_html;

With this solution, you should be able to view the email body in the description field of an incident record with proper line breaks
