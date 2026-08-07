---
title: "SAM- How manual usage CSV upload (Copilot, Visio, Project Online) works and where data maps"
aliases:
  - KB2593337
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2593337
kb_number: KB2593337
last_modified: 2025-10-29
---

## SAM- How manual usage CSV upload (Copilot, Visio, Project Online) works and where data maps

  

### Summary

#### 1\. How the process starts

Customer exports usage CSVs for Project, Visio, and Copilot from the Microsoft 365 admin portal.

These CSVs are manually attached to the Microsoft 365 Integration Profile (`samp_sw_subscription_profile`).

#### 2\. Scheduled job execution

The scheduled job SAM – Collect Microsoft 365 Usage runs daily and performs these key actions:

<table><tbody><tr><td>1</td><td><code>captureManualReportUsageActivity(profile)</code></td><td>Reads and parses CSV attachments from the integration profile.</td></tr><tr><td>2</td><td><code>updateLastActivity(profile)</code></td><td>Updates the "Last activity" field for subscriptions if the product mapping matches usage data.</td></tr><tr><td>3</td><td><code>deleteAttachmentsForProfile(profile)</code></td><td>Deletes the uploaded attachments after processing.</td></tr></tbody></table>

#### 3\. File identification and handling

The job identifies which attachment belongs to which product (Project, Visio, or Copilot) by checking the filename pattern.

It extracts a timestamp from the filename to determine the most recent report.

If multiple CSVs are uploaded for the same product, only the newest one is processed.

If a previous import already contains newer data, older files are skipped.

#### 4\. Data processing and storage

The script reads each valid CSV file and, for every user row, captures the Last Activity Date and User Principal Name.

These details are recorded as usage activity within the Microsoft 365 usage logic managed by ServiceNow SAM.

After the data import completes, attachments are deleted automatically from the Integration Profile.

#### 5\. Verification

After the job runs, imported activity data can be validated by confirming that user usage and activity details appear under Software Usage / Last Activity for corresponding users.

Attachments will no longer be visible — this confirms ingestion was successful.

### Release

Xanadu and later

### Instructions

Upload Microsoft 365 usage CSVs for Copilot, Visio, and Project directly to your Microsoft 365 Integration Profile.

Allow the job “SAM – Collect Microsoft 365 Usage” to process them (or trigger it manually).

The system will:

Read and import the CSVs into usage activity data.

Update subscription last activity (if mapped products match).

Delete the attachments automatically after processing.

* * *

### Recommendations

Ensure filenames remain in Microsoft’s default format (e.g., `ProjectActivityUserDetail...csv`, `VisioActivityUserDetail...csv`).

Avoid renaming files, as filename patterns are used for product mapping.

Do not re-upload older files; only the most recent CSV per product is processed.

Expect the attachments to be deleted automatically once processed — this is normal and confirms the import was successful.
