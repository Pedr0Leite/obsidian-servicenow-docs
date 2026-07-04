---
title: "SAMP - Software Subscriptions Do Not Have Software Models After Being Imported With SaaS Integration"
aliases:
  - KB2099185
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2099185
kb_number: KB2099185
last_modified: 2026-05-12
---

## SAMP - Software Subscriptions Do Not Have Software Models After Being Imported With SaaS Integration

  

### Issue

Software Subscription \[samp\_sw\_subscription\] records are created with no Software Model.

These Software Subscription records won't be reconciled when "Software License Reconciliation" is run.

**Expected Behavior:**

Software Subscription \[samp\_sw\_subscription\] records created from a  'SAM - Import User Subscriptions' schedule job have a reference to their Software Model record.

**Actual Behavior:**

Software Subscription \[samp\_sw\_subscription\] records created from a  'SAM - Import User Subscriptions' schedule job have an (empty) Software Model reference.

### Symptoms

-   The Software Model \[software\_model\] field on the Software Subscription \[samp\_sw\_subscription\] record will be (empty).
-   The Display Name of the Software Subscription \[samp\_sw\_subscription\] record will be the same value as it's Subscription Identifier \[subscription\_identifier\] field.

### Facts

-   During the Import User Subscription jobs the Subscription Identifier for each Software Subscription is used to lookup a matching record on the Subscriptions Product Definition \[samp\_sw\_subscription\_product\_definition\] table.
-   The Subscriptions Product Definition \[samp\_sw\_subscription\_product\_definition\] table is a SAMP Content table and is populated by the SAM - Content Download jobs.
-   The matching record on the Subscriptions Product Definition table references a DMAP (Discovery Map) record with that Software Subscription's Display Name, Publisher, Product, and Software Model to be created.
-   If no record is found on the Subscriptions Product Definition table matching the Software Subscription record's Subscription ID, then the Display Name of the Software Subscription record is set with value of it's Subscription ID and no Software Model is created for it.

### Release

All Releases

### Cause

The Import User Subscription job was run before the Content for the Subscriptions Product Definition completed downloading/updating.

The expected records with the Software Subscription's Subscription Identifiers are not on the the Subscriptions Product Definition \[samp\_sw\_subscription\_product\_definition\] table to be used to identify the Software Subscription and create it's Software Model record due to the Content not having completed fully downloading or having applied the latest content updates to the Subscriptions Product Definition table.

### Resolution

1\. Go to the Data Services: Download Schedules \[cds\_client\_schedule\] table and find the record where the 'Table' field is "samp\_sw\_subscription\_product\_definition".

2\. Open the job/record and click Execute Now.

3\. After the job completes, reload the Subscriptions Product Definition \[samp\_sw\_subscription\_product\_definition\] table

4\. Verify that records with the Subscription Identifiers are now present.

5\. Run the Import User Subscription job again.

\*\* If the Software Identifiers are still missing after the latest Content download has completed, then please open a request to the ITAM Content team.
