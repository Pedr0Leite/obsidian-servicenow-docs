---
title: "How to use email address filters to ignore any email from any sender?"
aliases:
  - KB0869547
area: Email / Notifications
tags:
  - servicenow
  - support-kb
  - email
  - email-filter
  - spam
  - deny-list
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869547
kb_number: KB0869547
last_modified: 2026-07-06
---

## How to use email address filters to ignore any email from any sender?

> Note: this instance's web fetch of the Now Support portal returned only the article's meta-description (the page requires an authenticated session to render the full body). This note summarizes the confirmed mechanism from that description plus corroborating docs/community sources — see `source_url` for the complete article.

### Question

An admin wants to ignore inbound email from one specific sender address, while continuing to process email from everyone else as normal.

### Answer (summary)

Use an **Email Address Filter** record (table `sys_email_filter`, list view `sys_email_filter_list.do`, also reachable from System Mailboxes → Administration → Filters). The base system ships with a default record named **"Ignore sender"**:

- Type: `Allow List`
- Domains: `*` (wildcard — allow inbound mail from every domain by default)
- Exceptions: a list of specific sender addresses that are carved *out* of that allow policy

Because the base policy is "allow everything," adding an address to the **Exceptions** list is what actually blocks/ignores it — the address is excluded from the allow rule, so inbound processing drops it (recorded as `received-ignored`) before any Inbound Email Action or record creation happens.

This is the supported, no-code way to build a sender deny list without writing a custom Business Rule or Inbound Email Action script.

### Caution

"Ignore sender" is a base-system record, so it can be reverted/overwritten on upgrade if flagged high-risk in a given release. Document any custom entries added to Exceptions (or clone the record) so they can be restored after an upgrade.

## Related

- [[KB0528852 - Transport Neutral Encapsulation Format (TNEF-encoded, winmail.dat or win.dat) messages aren't processed by the instance]]
- [[Set email address filters]]
- [[Community Discussion - Mails ignored by the Ignore sender email filter (postmaster, mailer-daemon)]]
