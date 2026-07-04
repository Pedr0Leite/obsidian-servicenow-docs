---
title: "Update Set Preview Troubleshooting"
aliases:
  - KB0535263
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535263
kb_number: KB0535263
last_modified: 2023-12-19
---

## Update Set Preview Troubleshooting

  

### Issue

This article provides common Update Set preview issues and troubleshooting steps to resolve them.  
  

### Symptoms

-   Update Set Preview is blank
-   Cannot see Update Set Preview
-   Update Set Preview does not show all updates

### Resolution

#### If preview is blank

If a preview is showing completely blank, generally this is a result of a change within the **UpdateSetPreviewer** code from one platform version to another. To resolve this, you will need to identify what the change is and manually edit the XML code with the new requirements in order for the Update Set to preview correctly within the new version.

#### If preview does not show all updates 

When a preview does not show all updates included within an update set, generally the root cause is one of two options: 

-   There is a bug within the UpdateSetPreviewer.
-   There is a corruption of one or more updates within the Update Set.

Attempt to replicate the preview issues by exporting and importing the Update Set via XML into a demo, using the same version as the customer instance. If the issue can be replicated, perform the following steps on the Demo instance. If you cannot replicate the issue, then the following steps will need to be performed on the customer instance, after first gaining permission:

1.  Remove the first 10 updates from the set and re-preview. If the preview now shows all expected updates, then the corruption is within the updates you removed. If the preview still shows a decreased number of updates than what is expected, remove another 10 updates, re-preview and repeat, until you have located the group that includes the bad update/s.
2.  Once the corruption has been narrowed down to a single group, delete and reimport the update set and then remove one update at a time from the group you previously identified as having the corrupted update/s. Re-preview the update set after each removal until you have found the corrupted item and the remaining items preview as expected.
3.  Once the corruption has been located, the customer will need to re-capture this update within a new update, in order to promote it to the target instance.
