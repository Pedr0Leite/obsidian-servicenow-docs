---
title: "When notification is sent, email is not showing hyperlink for the  incident number "
aliases:
  - KB0743780
tags:
  - servicenow
  - support-kb
  - notifications
  - dictionary
  - display-value
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743780
kb_number: KB0743780
last_modified: 2024-04-26
---

## When notification is sent, email is not showing hyperlink for the incident number

  

### Issue

When notification is sent, email is not showing hyperlink of a incident number

### Cause

OOB script displays hyperlink based on Display Value. Display value was false for "Number" column on incident table.

### Resolution

Right click on "Number" field in incident table > Configure dictionary > Check the "Display" checkbox for 'Number' column to fix the issue.

## Related

- [[KB0727617 - Access referenced fields in a notification record against the Approval table]] - notification body configuration
- [[KB0725194 - Approval emails are not being generated for requested items]] - notification troubleshooting

