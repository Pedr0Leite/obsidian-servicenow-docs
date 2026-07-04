---
title: "Unable to filter data on a list in Software Asset Workspace for a user with the sam_admin role"
aliases:
  - KB3088826
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3088826
kb_number: KB3088826
last_modified: 2026-06-15
---

## Text

**Short description**

A user with the sam\_admin role is unable to filter data on a list in Software Asset Workspace — filtering a column (commonly a reference field such as Discovery Model) returns no results even though matching data exists. This applies more broadly to any non-admin role on any application: after the May 2025 maintenance patch, querying a field requires a separate query-level ACL (query\_range / query\_match) in addition to read access. Users with the admin role are unaffected. Resolved in the Australia release.

**Symptoms**

-   A user with the sam\_admin role opens Software Asset Workspace, opens a List page (for example, Licensing / Software Installs), and filters a column (such as Discovery Model starts with a value) — the list returns zero rows although matching records exist.
-   More generally, any non-admin user filtering a list, report, or workspace list with a range or wildcard operator (CONTAINS, STARTSWITH, ENDSWITH, >, <, BETWEEN, LIKE, etc.) gets no results despite matching data.
-   The behavior is most commonly seen when filtering a reference field by its display value (a dot-walk query), but can occur on any field.
-   An information banner and/or a syslog entry appears. Depending on release:
    -   Current releases: **Part of the query on <tableName> has been ignored because of insufficient access for 'query\_range' operation on <tableName.fieldName>.**
    -   Older releases (UI): Part of the query on <tableName> has been ignored because of read security rules on <tableName.fieldName>.
    -   Older releases (syslog): Attempt to query against <tableName.fieldName> refused because of %s ACLs on that field.

-   The identical filter works when run as a user with the admin role.
-   An exact-match operator (is) may return rows while a range/wildcard operator (starts with, contains) returns none — confirming it is a query-level, not read-level, restriction.

**Environment**

-   All ServiceNow instances on releases that received the May 2025 Maintenance security patch, up to the Australia release (where it is resolved OOTB).
-   Any application or table — this is platform behavior, not specific to any product. Software Asset Workspace with the sam\_admin role is one common example.
-   Users with non-admin (role-scoped) access.

**Cause**

This is expected platform security behavior, not an instance misconfiguration.

The May 2025 Maintenance patch introduced two ACL operation types — query\_range and query\_match — to prevent unauthorized inference of data through range and wildcard query operators. Before this change, read access to a field was sufficient to also filter on it with those operators. After the change, query access is enforced separately from read access.

When a user's roles do not satisfy the applicable query\_range (or query\_match) ACL for the field being queried, the platform silently strips that part of the query rather than returning an error. The query then runs without the filtered condition, which typically yields no matching rows — producing the "no results" symptom.

Dot-walk and reference-field queries. When a reference field is filtered by its display value, the platform evaluates it as a dot-walk query of the form tableName.referenceField.field. In this case a query\_range ACL may be required on both:

-   tableName.referenceField (the reference field on the base table), and
-   referencedTable.field (the field on the referenced/lookup table).

If either is missing for the user's role, the predicate is stripped and the list returns no rows.

Why coverage can appear inconsistent. On the release where this enforcement was introduced, many query ACLs are not curated per table — they are generated from existing Read ACLs plus table-hierarchy rules. There is no one-to-one mapping between Read ACLs and Query ACLs, so some fields/lookup tables may lack usable query\_range coverage for a given non-admin role even though read access exists.

**Resolution**

Permanent fix — Australia release: This issue is resolved in the Australia release, where curated query\_range query ACLs are shipped out-of-the-box with the application plugins (rather than auto-generated from Read ACLs). After upgrading to Australia, standard non-admin roles can filter the affected lists without manual ACLs. Where a specific table's OOTB query ACL is still found missing for a standard role, ServiceNow addresses it as a product defect and ships the ACL. Use the workaround below only on releases prior to Australia.

Step 1 — Identify the exact field that is being blocked

Reproduce the filter as the affected user and read the UI banner or syslog message. The message names the specific <tableName.fieldName> whose query was ignored. For a reference/dot-walk filter, note both the reference field on the base table and the field on the referenced table.

Optionally use the Access Analyzer tool (plugin, available in sub-production) to confirm precisely which ACL is blocking the operation for the user on each table, so changes are targeted and verifiable.

Step 2 — Create the required query ACL(s)

Create a query\_range (and, if wildcard filters are also affected, a query\_match) ACL for each blocked field. Validate in a sub-production instance first.

Recommended pattern — Security-Attribute based (upgrade-safer; matches how ServiceNow ships these OOTB):

-   ACL Type: Record
-   Operation: query\_range (add a separate query\_match entry if needed)
-   Name: the field/table from the message (e.g. tableName.fieldName, and for dot-walk also referencedTable.field)
-   Security Attribute: HasRightsToReadAllDataIsTrue

This grants query access to exactly the users who can already read the data, and avoids hardcoding roles.

Alternative pattern — wildcard with explicit roles:

-   Name: <tableName>.\* (covers all fields on the table in one ACL)
-   Roles: the role(s) the affected users hold

The <table>.\* pattern reduces the chance of new field-specific errors resurfacing later.

Avoid adding conditional\_table\_query\_range ACLs in Store Apps unless the same table already has one in the Glide family; prefer a standard query\_range ACL with the HasRightsToReadAllDataIsTrue Security Attribute.

Step 3 — Validate

Re-run the original filter as the affected user and confirm results return and the banner no longer appears.

**Additional information**

-   query\_range / query\_match enforcement is enabled by design; insufficient query access drops the predicate silently rather than raising a hard error, which is why the symptom looks like "no data" rather than an access error.
-   HasRightsToReadAllDataIsTrue internally invokes Read ACL evaluation: on a table-level ACL it returns true only if the user can read all records on the table; on a table.field ACL it additionally requires read access to that field across those records.
-   Query ACLs are not strictly one-to-one with Read ACLs; inherited ACLs from parent tables and table-hierarchy rules also affect coverage.
-   **Upgrade note:** If you created custom query ACLs as a workaround on a pre-Australia release, the upgrade to Australia may detect the customization and load the new OOTB query ACLs inactive while keeping your custom ACLs active. After upgrading, review whether the OOTB ACLs now cover the affected fields, then retire your custom ACLs and activate the shipped set to return to the standard, upgrade-safe configuration.

**Related articles / references**

-   [KB2130442 — Troubleshooting query\_range ACLs (primary reference)](/kb?id=kb_article_view&sysparm_article=KB2130442)
-   [KB2046494 — May 2025 Maintenance Information](/kb?id=kb_article_view&sysparm_article=KB2046494)
