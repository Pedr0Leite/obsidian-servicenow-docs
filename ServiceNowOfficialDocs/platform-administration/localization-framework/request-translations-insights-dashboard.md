---
title: Request translations from Insights Dashboard
description: Request translations for Service Catalog items or Virtual Agent topics from the insights dashboard to localize them into the selected language based on their translation status.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/localization-framework/request-translations-insights-dashboard.html
release: australia
product: Localization Framework
classification: localization-framework
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Monitor the Localization Framework, Localization Framework, Translation and localization, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - localization
  - l10n
  - languages
  - translation
  - type-task
---

# Request translations from Insights Dashboard

[[request-translations-multiple-items|Request translations for Service Catalog items]] or Virtual Agent topics from the insights dashboard to localize them into the selected language based on their translation status.

## Before you begin

Role required: [[ia-localization-il|localization]]\_admin or localization\_requestor

## Procedure

1.  Navigate to **All** &gt; **[[localization-framework-landing|Localization Framework]]** &gt; **Insights Dashboard**.

    The dashboard provides **Catalog Items Translations** report and **Virtual Agent Topic Translations** report by default using which you can [[language-picker-ui|request translations]].

    If you have created a report for your custom artifact to display in the dashboard, you can also request translations for the custom artifacts. For more information, see [Create a report for custom artifact](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/t_CreateYourOwnReport.md).

2.  In the **Catalog Items Translations** report or **Virtual Agent Topic Translations** report, click the vertical bar of the language into which you want to request translations.

    For example:

    -   Select a language from the **Catalog Items Translations** report to request translations for the Service Catalog items in that language.
    -   Select a language from the **Virtual Agent Topic Translations** report to request translations for the Virtual Agent topics in that language.
    -   If you have a custom report created for an artifact, select a language from that report to request translations into the selected language.
3.  Select one or more documents from the localization insights list.

    -   You can click the **Select All** check box to request translations for all the items in the list.
4.  From the **Actions on selected rows** list, select **Request Translations**.

5.  Click **OK** in the Confirmation dialog box to submit the request.


**Parent Topic:**[Monitor the Localization Framework](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/localization-framework/monitor-localization-framework.md)

## Related

- [[request-translations-multiple-items|Request translations for Service Catalog items]]
- [[ia-localization-il|Localization]]
- [[localization-framework-landing|Localization Framework]]
- [[language-picker-ui|Request translations]]
