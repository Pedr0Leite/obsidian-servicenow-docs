---
title: Generate an encoded query string through a filter
description: You can generate an encoded query string through a filter on any list and paste the string into a URL query or a reference qualifier.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/t\_GenEncodQueryStringFilter.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Encoded query strings, Filters and breadcrumbs, Lists in the classic environment, Working in the classic environment, Working in Core UI, Configure UIs and portals, Configure user experiences]
tags:
  - platform-user-interface
  - type-task
---

# Generate an encoded query string through a filter

You can generate an encoded query string through a filter on any list and paste the string into a URL query or a [[onboarding-modals-reference|reference]] qualifier.

## Before you begin

Role required: none

## Procedure

1.  Open a list of records.

2.  [[t_CreatingFilters|Construct the filter]].

3.  Click **Run**.

4.  Right-click the end of the filter breadcrumb and select **Copy query** from the context menu.

    \[Omitted image "FilterToQuery2.png"\] Alt text: Copy the query

    If you are in split mode in List v3, right-click the blue filter text in the left pane.

5.  Copy the query to your system clipboard.

6.  Use the query string to [[navigate-using-url|Navigate to a record or module using a URL]] or an [Reference qualifiers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_ReferenceQualifiers.md).

    When you use the CONTAINS operator on a list filter, the system translates the filter to a LIKE query. For example, if you filter for active records with numbers that contain 123, the URL is `https://InstanceName.service-now.com/incident_list.do?sysparm_query=active%3Dtrue%5EGOTOnumberLIKE123`.


**Parent Topic:**[[c_EncodedQueryStrings|Encoded query strings]]

**Related topics**  


[Reference qualifiers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_ReferenceQualifiers.md)

[Navigate to a record or module using a URL](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/navigate-using-url.md)

## Related

- [[t_CreatingFilters|Create a filter in List]]
- [[navigate-using-url|Navigate to a record or module using a URL]]
- [[c_EncodedQueryStrings|Encoded query strings]]
- [[onboarding-modals-reference|Reference]]
