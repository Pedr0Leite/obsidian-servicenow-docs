---
title: "Set email address filters"
aliases:
  - Set email address filters
  - Email Address Filter
area: Email / Notifications
tags:
  - servicenow
  - product-doc
  - email
  - email-filter
  - spam
  - deny-list
  - allow-list
source_url: https://docs.servicenow.com/bundle/rome-servicenow-platform/page/administer/notification/task/set-email-address-filters.html
doc_type: product-documentation
last_modified: 2026-07-06
---

## Set email address filters

> Note: the live fetch of this docs.servicenow.com page returned no renderable body content for this instance (client-side rendered / blocked). This note captures the mechanism as verified directly against a live instance's "Ignore sender" record and cross-referenced against [[KB0869547 - How to use email address filters to ignore any email from any sender]] and community sources — confirm exact field labels against the current release's docs at `source_url` before relying on this for a build.

### What it is

Email Address Filters (table `sys_email_filter`) let an admin control, per sender address or domain, whether inbound email is processed or silently ignored — evaluated before Inbound Email Actions run, so a matched "ignore" record stops the email from ever creating or updating a record.

### Key fields observed on a record

- **Name** — descriptive label (e.g. "Ignore sender")
- **Type** — `Allow List` or `Deny List`. Allow List treats the Domains field as what's permitted, with Exceptions carved out as blocked; a Deny List would work the other way.
- **Domains** — one or more domains (or `*` for all domains) the Type applies to
- **Exceptions** — specific sender addresses excluded from the Type's rule. On an Allow List filter, entries here are the addresses that get ignored/blocked despite the general allow policy.

### Practical use: building a sender deny list

Since the base "Ignore sender" filter already ships as an Allow List with Domains `*`, the simplest way to block a specific sender is to add its address to that record's Exceptions list — no new filter record or scripting required. This is the mechanism behind a "block this sender" type of button on a case form: the button just needs to append the case's originating email address to this record's Exceptions field (with a duplicate check).

### Caution

The default "Ignore sender" record is a base-system record and may be reset on upgrade if ServiceNow revises it in a later release. Keep a record of custom Exceptions entries (or clone into a separate filter) so they survive an upgrade.

## Related

- [[KB0869547 - How to use email address filters to ignore any email from any sender]]
- [[Community Discussion - Mails ignored by the Ignore sender email filter (postmaster, mailer-daemon)]]
- [[KB0528852 - Transport Neutral Encapsulation Format (TNEF-encoded, winmail.dat or win.dat) messages aren't processed by the instance]]
