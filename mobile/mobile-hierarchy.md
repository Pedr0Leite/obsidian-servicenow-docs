---
title: Mobile hierarchy
description: Learn the components of ServiceNow mobile and how they work together to assist you in configuring, modifying, and creating applications.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/mobile-hierarchy.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Building mobile apps, Mobile Platform]
---

# Mobile hierarchy

Learn the components of ServiceNow® mobile and how they work together to assist you in configuring, modifying, and creating applications.

## Components of the ServiceNow mobile framework

This image represents the structure of the ServiceNow mobile framework. The next sections detail specific areas of the overall hierarchy, and descriptions of individual components.

\[Omitted image "mobile-app-core-foundation.png"\] Alt text: Diagram showing the foundation elements of mobile apps.

## Mobile App Configuration

\[Omitted image "mobile-hierarchy-callout-1.png"\] Alt text: Components of the Native Client.

-   **Mobile app**

    A part of the ServiceNow® [[mobile-config-navigation|Mobile Platform]], there are 2 mobile apps: the [[now-mobile-app|Now Mobile app]] and the [[mobile-experience|Mobile Agent app]]. Each app focuses on a persona, which means the app experiences are tailored to support the tasks of specific roles in your organization. Each mobile app can have one or more mobile app configurations. For more information, see the following "Mobile app config" section.

-   **Mobile app config**

    When users download a ServiceNow Mobile Platform application, they are prompted to log in with their credentials. When a user logs in to the instance, they are presented an experience that is created by a single mobile app config. The mobile app config that defines the user's experience depends on conditions defined in the config.

-   **[[sg-mobile-tab-bar|Navigation bar]]**

    Each mobile app config has a navigation bar that appears at the bottom of the screen. A navigation bar can have up to five icons, called navigation bar tabs. By default, navigation bars have a notification and settings navigation bar tab. For information about how to create a navigation bar, see [[config-sg-application-menu|Configure the navigation bar and navigation tabs]].

-   **Navigation bar tabs**

    Each tab in the navigation bar represents a screen or launcher screen. When you add more than five tabs to the navigation bar, a **More** tab appears. Tapping the **More** tab opens a list view showing additional tabs.

    For information on how to create navigation bar tabs, see [Configure the navigation bar and navigation tabs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/config-sg-application-menu.md).

-   **Launcher screens**

    Launcher screens serve as landing pages or home pages for your users. Launcher screens contain a configurable header, and sections to provide access to screens in several formats. You can also configure launcher screens with a search bar and [[sg-config-quick-actions|quick actions]], which give your users access to commonly used functions.

    For more detail on launcher screens, see [[sg-mobile-applet-launcher|Launcher screens]].

-   **Screens**

    Screens provide your users a method to view and modify data on your instance. Screens can display information as lists, maps, records, and other formats. You can find more detail on screen components in the next section.


## Screens

\[Omitted image "mobile-screens.png"\] Alt text: List of all available [[mobile-screens-landing|mobile screens]].

-   **Screen segments**

    Screens contain one or more screen segments, which display information from your instances to your users. Screen segments represent the lists, calendars, maps, and records your users see within the app. If a screen has more than one screen segment, your users can switch between screen segments using a tabbed interface.

    Screen segment records for lists, calendars, and maps are located on the screen segment \[sys\_sg\_item\_stream\_segment\] table. Screen segment records for record screens are on the record screen segment \[sys\_sg\_form\_segment\] table.

-   **Icons**

    Each screen has an icon. This icon represents the screen when it is displayed in a launcher screen or the navigation bar.

    Icon records are located on the Icons \[sys\_sg\_icon\] table.

    For more information on icons, see [[sg-mobile-icon|Mobile icons]].

-   **Item streams**

    An item stream is the source for the data shown in your screen. An item stream gets its data from a single source, called a data item. You can associate more than one item stream to a screen segment to include data from multiple tables. For example, you could create two item streams to display items from both the incident \[incident\] and request item \[sc\_req\_item\] tables in a single list.

    Item streams are also associated with one or more item configurations. These item configurations provide a pattern controlling how the data appears in your screen segment.

    Item stream records are located in the item stream \[sys\_sg\_item\_stream\] table.

-   **Data items**

    Data items provide the data presented in a screen. A data item is a dataset correlated with a table in an instance. A data item can include a filter condition to restrict what data the item returns. Associate data items with screens so that the screens can transform the dataset into human-readable information.

    Data items are located on the data items \[sys\_sg\_data\_item\] table.

    For more detail on data items, see [[sg-data-item|Data items]].

-   **Item configurations**

    Item configurations provide a pattern for data in your screen, and control how your data appears within a screen segment. For more detail on how an item configuration controls the appearance of your data, see the item configuration section.

    Item configurations are located on the item configuration \[sys\_sg\_master\_item\] table.

-   **More information**

    For more information, See:


## Screen segments

\[Omitted image "mobile-launcher-screens.png"\] Alt text: A hierarchical diagram of the available mobile launcher screens.

-   **Screens**

    Screen types determine what a screen looks like and how your users are able to interact with it. You can create these screen types:

    -   [[calendar-screen|Calendar]]
    -   [[chart-screen|Chart]]
    -   [[form-screen|Form]]
    -   [[grouped-list-screen|Grouped list]]
    -   [[list-screen|List]]
    -   [[map-screen|Map]]
    -   [[url-screen|URL]]
    In addition to these types, you can add the following screens to segments in your record screen:

    -   Details screen
    -   Activity stream screen
    -   Related list screen
    -   Embedded list screen
-   **Functions**

    Your users can use functions to perform tasks in the mobile app such as assigning a task, or navigating between records. Actions can also interact with your mobile device to send emails, navigate using map software, or make a phone call.

    Functions are located on the Function \[sys\_sg\_button\] table.

    For more information on functions, see [[sg-studio-mobile-button-types|Mobile functions]].

## Related

- [[config-sg-application-menu|Configure the navigation bar and navigation tabs]]
- [[sg-mobile-applet-launcher|Launcher screens]]
- [[sg-mobile-icon|Mobile icons]]
- [[sg-data-item|Data items]]
- [[calendar-screen|Calendar screen]]
- [[chart-screen|Chart screen]]
- [[form-screen|Record screen]]
- [[grouped-list-screen|Grouped list screen]]
- [[list-screen|List screen]]
- [[map-screen|Map screen]]
- [[url-screen|Mobile web screen]]
- [[sg-studio-mobile-button-types|Mobile functions]]
- [[mobile-config-navigation|Mobile Platform]]
- [[now-mobile-app|Now Mobile app]]
- [[mobile-experience|Mobile Agent app]]
- [[sg-mobile-tab-bar|Navigation bar]]
- [[sg-config-quick-actions|Quick actions]]
- [[mobile-screens-landing|Mobile screens]]
