---
title: "How the Lenovo Hardware Warranty Integration Works in HAM"
aliases:
  - KB3112520
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3112520
kb_number: KB3112520
last_modified: 2026-06-23
---

## How the Lenovo Hardware Warranty Integration Works in HAM

  

### Summary

**ServiceNow HAM automatically retrieves hardware warranty data from Lenovo's external API and stores it against each eligible hardware asset record. The integration runs on a weekly schedule without any manual trigger.**

**1) Prerequisites**

**All three of the following must be in place before warranty data can populate.**

Hardware Asset Management plugin (sn\_hamp) must be active.

Lenovo Asset Warranty Spoke (sn\_lenovo\_spoke) must be installed.

A valid Lenovo API credential must be configured under the sn\_lenovo\_spoke.Lenovo connection alias using the Client ID and Client Secret issued by Lenovo.

**2) How It Runs**

The scheduled job is named "**Download Asset Warranty Information - Lenovo**" and runs on a weekly frequency. It triggers the Lenovo Asset Warranty Flow (sn\_itam\_common.lenovo\_asset\_warranty\_flow), which calls the Lenovo Warranty API and writes the results back to ServiceNow. The job logs each run to the **asset\_job\_log** table. Detail-level entries per asset are written to asset\_job\_log\_detail.

**3) Which Assets Are Included**

The flow queries the alm\_hardware table and applies four filters. An asset must pass all four to be included in the API call. Assets that fail any one filter are silently skipped with no error logged.

**Filter 1:** The asset's model manufacturer name must contain "lenovo".

**Filter 2:** The install status must not be 7 (Retired) or 8 (Missing).

**Filter 3:** The serial number field must not be empty.

**Filter 4:** The excluded\_from\_ham field must be false or empty.

**4) How Serial Numbers Are Sent to the API**

Eligible serial numbers are batched into URL query strings. Each batch is capped at 2,048 characters to stay within the Lenovo API's URL length limit. If the total number of eligible serials exceeds what fits in one request, the flow automatically splits them across multiple API calls.

**5) What the API Returns and What Gets Written**

The Lenovo API returns warranty entitlements keyed by serial number. For each serial in the response, the flow looks up the matching asset record in ServiceNow. If a match is found, warranty records are written to the sn\_itam\_common\_asset\_warranty table, one record per warranty entitlement returned for that serial.

The fields written are: External Warranty ID (the ID from Lenovo, used as part of the upsert key), Asset (reference to the alm\_asset record), Name, Description, Type (for example BASE or CONTRACT), Start Date, End Date, Active (boolean from Lenovo), Status, and Country.

All fields on **sn\_itam\_common\_asset\_warranty** are strictly read-only. They cannot be manually edited in the UI and are written exclusively by the integration job.

The upsert key is the combination of asset and external\_warranty\_id. If a record with that combination already exists it is updated. If not, a new record is created.

If the Lenovo API returns no data for a serial number, for example because the warranty has expired or the serial is unknown to Lenovo, no record is written and no error is logged. This is expected behaviour and means Lenovo has no warranty data to provide for that serial.

  
**6) Why Warranty Data May Be Missing for a Specific Asset**

There are four reasons a Lenovo asset may have no warranty records in ServiceNow.

**First**, the asset does not meet the eligibility filters. Verify the asset's manufacturer, install status, serial number, and excluded\_from\_ham field against the four filters described above.

**Second**, the serial number was added or corrected after the last job run. The job runs weekly. If a serial number is blank or incorrect when the job fires, no API call is made for that asset. Warranty data will not appear until the next weekly run after the serial is populated. There is no on-demand trigger.

**Third**, Lenovo's API returned no data for that serial. If the warranty is expired or the serial is not recognised by Lenovo, the API returns an empty response and ServiceNow writes nothing. To confirm this, check whether the warranty is visible in the Lenovo customer portal directly. If it is not visible there either, the serial may be incorrect or the asset may not be registered with Lenovo.

**Fourth**, the job has not yet run since the asset became eligible. Check the most recent job run date in asset\_job\_log. If the last run pre-dates when the asset became eligible, the data will appear after the next weekly run.

**7) How to Check the Job Run History**

Navigate to asset\_job\_log.LIST . Filter by job name "Download Asset Warranty Information - Lenovo". Each log entry shows the run date, status (Completed or Failed), and duration.

**8) Where Warranty Records Are Visible**

On a hardware asset record, warranty data is shown in the Asset Warranties related list (table: sn\_itam\_common\_asset\_warranty). Multiple warranty entitlement records may exist for a single asset, one per entitlement returned by Lenovo, such as a base warranty, battery warranty, or contract extension.
