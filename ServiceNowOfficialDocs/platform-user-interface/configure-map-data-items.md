---
title: Configure map data items
description: Add map data items to render data on your Map Page using the Classic Environment.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/configure-map-data-items.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create an advanced Map Page, Map pages, User interface configuration, Working in Core UI, Configure UIs and portals, Configure user experiences]
tags:
  - platform-user-interface
  - type-task
---

# Configure map data items

Add map data items to render data on your Map Page using the Classic Environment.

## Before you begin

Role required: admin

## About this task

Create a container for your map data items first, then [[configure-onboarding-modals|configure]] and select the data items for your Map Page.

## Procedure

1.  Navigate to **All** &gt; **System Map Page** &gt; **Map Data Items**.

2.  Click **New**.

3.  On the form, fill in the fields.

    |Field|Description|
    |-----|-----------|
    |Name|Name for the map data item.|
    |Table|Table for the condition. For example, select the Choice \[sys\_choice\] table.|
    |Condition type|Condition using declarative or scripted conditions.|
    |Conditions|Declarative conditions for your map data item.|
    |Application|Optional application scope for the map marker, if other than Global.|

4.  Click **Submit**.


## Map Data Item form

Select the options in the table to successfully create a map data item. Use this configuration with the examples in [[set-up-map-filters|Add a map filter]] and [Configure a map filter data mapping](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/set-up-map-filters.md) to successfully create a map filter.

|Field|Description|
|-----|-----------|
|Name|Enter `Incident state`.|
|Table|Select Choice \[sys\_choice\].|
|Condition type|Select **Declarative**.|
|Conditions|Input the following into the fields: `Element is state` and `Table is task`.|
|Application|Skip this field.|

## What to do next

Create [[configure-map-markers|map markers]] for your map.

**Parent Topic:**[[create-advanced-map-page|Create an advanced Map Page]]

## Related

- [[set-up-map-filters|Add a map filter]]
- [[configure-map-markers|Create a map marker]]
- [[create-advanced-map-page|Create an advanced Map Page]]
- [[configure-onboarding-modals|Configure]]
