---
title: "Mails are ignored by the filter \"Email ignored by 'Ignore sender' filter\""
aliases:
  - Ignore sender filter postmaster mailer-daemon
area: Email / Notifications
tags:
  - servicenow
  - community
  - email
  - email-filter
  - spam
  - deny-list
source_url: https://www.servicenow.com/community/developer-forum/mails-are-ignored-by-the-filter-quot-email-ignored-by-ignore/m-p/1507995
doc_type: community-discussion
last_modified: 2026-07-06
---

## Mails are ignored by the filter "Email ignored by 'Ignore sender' filter"

ServiceNow Developer Forum thread (Jan 2019, still referenced in later releases) discussing a side effect of the base-system **Ignore sender** Email Address Filter (see [[Set email address filters]] and [[KB0869547 - How to use email address filters to ignore any email from any sender]]).

### Issue reported

A customer's replies to ServiceNow (approval emails) were silently dropped with the log reason `Email ignored by 'Ignore sender' filter`. The default filter ignores any inbound email where the sender/header contains `mailer-daemon` or `postmaster`.

Root cause in this case: the customer's outbound mail server introduced itself in the SMTP HELO handshake as `postmaster@customer.com`, which matched the ignore condition even though the actual sender was a real person replying to an approval request — the HELO identity, not the visible From address, tripped the filter.

### Guidance from the thread (accepted answer + replies)

- Don't disable the default "Ignore sender" filter outright — it exists to stop mail loops and bounce/auto-reply storms (`mailer-daemon`/`postmaster` messages) from generating unwanted incidents or approvals.
- If a legitimate sender's mail server happens to identify itself with `postmaster`/`mailer-daemon` in its HELO, a workaround is to create a **new** email filter that matches specifically against the message headers/sender field causing the false positive, rather than modifying the base condition — and to keep the original "Ignore sender" filter active for other domains.
- Before rolling out a filter change, test on a non-production instance first, since a mis-scoped change can either let bounce-storm mail back in (mail loop risk) or continue blocking legitimate senders.

### Relevance to building a "deny list" feature

This thread is a useful caution when building anything (like a case-form button) that writes into this same filter mechanism: the ignore condition can match on header content (like SMTP HELO), not just the visible From address, so a naive "add this sender's email to Exceptions" implementation should be tested against real headers, not just the display address, to confirm it behaves as expected.

## Related

- [[KB0869547 - How to use email address filters to ignore any email from any sender]]
- [[Set email address filters]]
- [[KB0528852 - Transport Neutral Encapsulation Format (TNEF-encoded, winmail.dat or win.dat) messages aren't processed by the instance]]
