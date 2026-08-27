---
title: Opt out of data sharing for Now Assist
description: Data sharing improves ServiceNow AI products. You can opt out of data sharing from the Now Assist Admin console Settings page.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/opt-out-of-data-sharing-for-now-assist.html
release: australia
topic_type: task
last_updated: "2026-01-23"
reading_time_minutes: 2
keywords: [Opt out, Now Assist, data sharing, Admin console, settings page, account]
breadcrumb: [Data sharing and processes, Now Assist Admin Settings, Exploring Now Assist Admin, Now Assist, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-task
---

# Opt out of data sharing for Now Assist

Data sharing improves ServiceNow AI products. You can opt out of data sharing from the [[platform-now-assist-landing|Now Assist]] Admin console Settings page.

## Before you begin

**Important:** Data sharing is not available for GCC or self-hosted instances. You don't need to opt out because data sharing is never enabled. If you have any questions, reach out to your account representative.

If you do not have a data steward, see [[assign-data-steward-role|Assign the data steward role]] documentation.

Role required: sn\_generative\_ai.data\_steward

**Note:** The **Opt out** button appears only if you’ve installed at least one Now Assist application or plugin. For a list of all Now Assist applications, see [[exploring-now-assist-platform|Exploring Now Assist Admin]].

## About this task

By opting out of the ServiceNow customer data sharing program, you can no longer provide data to improve ServiceNow AI products. By sharing data with the ServiceNow AI development program, you provide relevant data to help improve prediction accuracy, user experience, tailor products to your business needs, and reduce hallucinations for your activated [[now-assist-skills|Now Assist skills]].

You can choose to opt out a ServiceNow instance from data sharing from the Now Assist Admin console if you don't want to participate. Repeat the opt-out process for all instances that use the Now Assist functionality.

Opting out can take up to five business days to process.

**Note:** You must opt out of data sharing to turn off ServiceNow ability to gather Customer data for AI and data products.

## Procedure

1.  Change the current session scope by selecting the Globe icon in the top right next to the search bar and setting Application Scope to [[generative-ai-controller|Generative AI Controller]].

2.  Navigate to **All** &gt; **Now Assist Admin** &gt; **Settings**.

    If you’re already in the Now Assist Admin console, select the **Settings** tab.

3.  In the Settings panel, select the **Data sharing and processing** &gt; **Data sharing** tab.

    \[Omitted image "naa-data-sharing.png"\] Alt text: Account panel in [[configure-now-assist-admin-settings|Now Assist Admin Settings]] that shows the features that are included with your license. It also provides a data sharing opt-out button.

4.  Select **Opt Out**.

5.  In the confirmation window, select **Opt Out**.


## Result

Your data sharing preference is saved on the instance. If you want to opt back in to data sharing, you must consult with your account executive.

**Parent Topic:**[[now-assist-data-sharing-and-processes|Data sharing and processes]]

## Related

- [[assign-data-steward-role|Assign the data steward role]]
- [[exploring-now-assist-platform|Exploring Now Assist Admin]]
- [[now-assist-data-sharing-and-processes|Data sharing and processes]]
- [[platform-now-assist-landing|Now Assist]]
- [[now-assist-skills|Now Assist skills]]
- [[generative-ai-controller|Generative AI Controller]]
- [[configure-now-assist-admin-settings|Now Assist Admin Settings]]
