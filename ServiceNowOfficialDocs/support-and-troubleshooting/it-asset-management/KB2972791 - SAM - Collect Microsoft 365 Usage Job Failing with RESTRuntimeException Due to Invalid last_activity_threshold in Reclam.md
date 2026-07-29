---
title: "SAM - Collect Microsoft 365 Usage Job Failing with RESTRuntimeException Due to Invalid last_activity_threshold in Reclamation Rule"
aliases:
  - KB2972791
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2972791
kb_number: KB2972791
last_modified: 2026-04-22
---

## Issue

The scheduled job "SAM - Collect Microsoft 365 Usage" fails repeatedly. The following error may appears in the job log

ERROR \*\*\* Script: SamCollectUsageO365: Error: CaptureM365AppsUsageReport: Error: com.glide.rest.util.RESTRuntimeException: Response body was requested to be saved as attachment. It's not available through getBody() anymore.

## Resolution

Navigate to the samp\_sw\_reclamation\_rule table and identify the reclamation rule associated with the Microsoft 365 .

Open the record and verify the last\_activity\_threshold field. Even if the UI shows a valid value (e.g., 30), confirm the underlying XML by checking the record's XML view.

If the XML shows an unsupported value (e.g., 60), set the field to a supported value: 30, 90, or 180 days.

Force save the record (right-click the form header and select Save, or use the context menu force save option). This corrects the XML to match the selected value.

Re-run the SAM - Collect Microsoft 365 Usage job and confirm it completes successfully in samp\_job\_log.
