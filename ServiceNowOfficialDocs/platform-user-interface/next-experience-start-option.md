---
title: Configure Next Experience start page options
description: Multiple start page options help you determine where best to start your day in Next Experience. Configure the landing page so that you and your users start on a page tailored to your needs in ServiceNow.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/next-experience-start-option.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
keywords: [next experience start page options]
breadcrumb: [Configure, Next Experience UI, Configure UIs and portals, Configure user experiences]
---

# Configure Next Experience start page options

Multiple start page options help you determine where best to start your day in Next Experience. [[configure-onboarding-modals|Configure]] the landing page so that you and your users start on a page tailored to your needs in ServiceNow.

There are several options for the page that opens when you launch ServiceNow® or select the logo at the top of the screen.

## Start page options

Any page can have redirect rules as the page is loading to take the user to a different page.

-   **Next Experience default landing page**

    The default landing page provides information to help orient you to your tasks. Variants of this page are available, depending on your setup. For more information, see [[exploring-your-next-experience-homepage|Exploring your Next Experience default landing page]].

-   **Configurable workspace home**

    Any page within a configurable workspace can be the start page. For more information about configurable workspace options, see [[c_set-up-configurable-workspace|Configuring Configurable Workspace]].

-   **User-selected landing page**

    You can select any page on the platform to be your start, based on a user preference. A user-selected landing page can be any page inside a configurable workspace as well. For more information, see [[configure-user-selected-start-page-preference|Configure a user-selected start page]].

-   **Admin-selected landing page**

    This option can be any page inside a workspace, but also a classic dashboard. The admin can include role-based logic to direct users to configurable workspaces. For more information, see

    -   [[use-ui16-landing-page-in-next-experience|Configure a Core UI global landing page in Next Experience enabled instances]]
    -   [[configure-per-user-ui16-landing-page-in-next-experience|Configure per-user landing pages in Next Experience]]
-   **Responsive dashboards**

    You can start with a responsive dashboard created in the classic environment to use an existing dashboard that isn't available in a configurable workspace. For more information, see [Set responsive dashboards as your home](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/t_SetDashboardsAsHome.md).

-   **Homepages**

    Homepages are a deprecated feature. Homepages from earlier releases are read-only from the Tokyo release. For information on converting homepages to Responsive dashboards, see [Homepage deprecation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/homepage-deprecation-help-tool.md).


## How to choose a start page

The different options for start pages serve different purposes. For example, choose a responsive dashboard for your start page if most of your data is in the classic environment, rather than in configurable workspaces.

## Upgrade considerations

When you upgrade to an instance with Next Experience enabled, it's best to convert homepages to responsive dashboards, so that you don't lose editing capabilities. In instances using Next Experience, legacy Homepages are turned off by default. For more information, see [Homepage deprecation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/homepage-deprecation-help-tool.md).

-   **[[ne-start-options-admin|Next Experience administrator start options]]**  
As an administrator, you can configure where users start when they log in to ServiceNow.
-   **[[ne-start-options-user|Next Experience user start options]]**  
As a user, you can specify where you want to start when you log in to ServiceNow.

**Parent Topic:**[[next-experience-ui-admin|Configuring the Next Experience UI]]

## Related

- [[exploring-your-next-experience-homepage|Exploring your Next Experience default landing page]]
- [[c_set-up-configurable-workspace|Configuring Configurable Workspace]]
- [[configure-user-selected-start-page-preference|Configure a user-selected start page]]
- [[use-ui16-landing-page-in-next-experience|Configure a Core UI global landing page in Next Experience enabled instances]]
- [[configure-per-user-ui16-landing-page-in-next-experience|Configure per-user landing pages in Next Experience]]
- [[ne-start-options-admin|Next Experience administrator start options]]
- [[ne-start-options-user|Next Experience user start options]]
- [[next-experience-ui-admin|Configuring the Next Experience UI]]
- [[configure-onboarding-modals|Configure]]
