---
aliases:
  - "Workspace App Shell UX Page Properties"
area: "Workspace"
source: notion-export
tags:
  - workspace
  - app-shell
  - ui-builder
  - next-experience-ui
---

# Workspace App Shell UX Page Properties

## Table of Contents

---

---

---

[Overview](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#overview)

[Workspace UX Page Properties](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#workspace)

[Header Configuration](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#header)

[Navigation Configuration](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#navigation)

[Search Configuration](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#search)

[Tabs Configuration](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#tab)

[Main Configuration](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#main)

[Record Page UX Page Properties](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#record)

[List Page UX Page Properties](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#listprop)

[Appendix](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#appendix)

---

---

---

# Overview

The intention of this article is to act 
as a reference when creating a workspace experience via either UI 
Builder, or Studio and configuring Workspace app shell properties. It's 
important to note, that when creating a workspace experience from App 
Engine Studio, that the starter workspace experience generated will 
automatically create and configure some of these for you.

Some of the page properties in this 
article can be configured in UI Builder via Experience Settings, which 
provides a GUI interface to change basic experience settings. When 
building a new workspace experience via UI Builder or Studio, you can 
also use UI Builder to input experience settings, and the associated UX 
Page Properties will be generated for you.

[](https://www.servicenow.com/community/image/serverpage/image-id/154333i6749906C013DD879/image-size/large?v=v2&px=999)

Before we discuss UX Page Properties, 
let's touch base on what an App Shell is. An App Shell is a record that 
defines the root components that go into the header, toolbar, and 
footer. It has data resources to get the information it needs to render 
the components that are utilized within the app shell. This article 
specifically discussed the **Agent Workspace App Shell**, which is used for our new configurable workspace experiences.

The Agent Workspace App Shell is comprised of two protected components: **sn-canvas-header** and **sn-canvas-toolbar**.
 These components utilize metadata from UX Page Property records in 
order to show certain settings, such as search, notifications, toolbar 
items, etc. Customers cannot modify these components directly, but can 
control settings via UX Page Properties.

UX Page Properties are records that 
contain metadata for the app shell configuration. This allows for the 
app shell to point to these records that developers can configure 
instead of hardcoding this information directly in the app shell 
components. This article will discuss the workspace app shell, which 
contain the header and sidebar/toolbar components. As mentioned above, 
when setting up workspaces from App Engine Studio, some of these 
properties will automatically be generated for you, but when using 
methods that are not App Engine Studio you will have to define all of 
the necessary UX Page Properties manually.

[](https://www.servicenow.com/community/image/serverpage/image-id/154319i469AF78FBDE55750/image-size/large?v=v2&px=999)

---

# Workspace UX Page Properties

| **UX Page Property**
 | **Description**
 |
| --- | --- |
| [chrome_header](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#header) | Adds a header to the experience, inside 
of the header configuration you can define public and private page 
configurations. You can use this property to turn on/off features such 
as Search, Notifications, and User Preferences. You can also perform 
these configurations via UI Builder > Menu > Edit Experience Settings > Utilities
 |
| [chrome_toolbar](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#navigation) | Adds a left-side navigation toolbar to 
the experience. Can be used to display custom buttons on the sidebar. 
You can also perform these configurations via UI Builder > Menu > Edit Experience Settings > Side Navigation
 |
| [global_search_configurations](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#search) | This is an instance of sys_search_context_config.You can also perform these configurations via UI Builder > Menu > Edit Experience Settings > Utilities
 |
| [chrome_main](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#main) | Controls performance settings for 
experience. Manages client side cache side in terms of number of unique 
instances of the canvas screen. The specific configuration specified in a
 chrome_main page property will be supplied to the canvas screen which 
determines the screen macroponents which are rendered via the client 
side cache.
 |
| [chrome_tab](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#tabs) | Provides tabs specific contextual information, you can define here the + symbol for new record types you would like to create.
 |
| [routeConfigId](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#routeconfig) | Defines dynamic routing behavior. This is one of the records in the sys_ux_dynamic_route_config table.
 |

## Header Configuration (chrome_header)

---

**Note:** Some
 of these configurations will not apply to workspace experiences with 
Next Experience turned on as the workspace utilizes the Next Experienced
 Unified Navigation header instead of the dedicated header component 
that the Agent Workspace App Shell utilizes when Next Experience is not 
turned on. For more information see the article [Next Experience Architecture and Terminology.](https://community.servicenow.com/community?id=community_article&sys_id=27d55ca2db9dd990dd886c8e13961942)

**privatePage**

> Configuration information for an authenticated user.
> 
> 
> type: **object**
> 

**privatePage.searchEnabled**

> Indicates to the header that a slot 
should be created for a search component. Note that search functionality
 is not determined by this property. The sn-canvas-header component 
simply creates an empty slot of name "search-input" that can be used to 
insert a search component.
> 
> 
> type: **boolean**
> 

**privatePage.userPrefsEnabled**

> Indicates to the header that a user icon
 should be created. This corresponds to the user Menu on the right-hand 
side of the header. If no menu children are specified, an avatar will 
display. Otherwise a dropdown menu is included.
> 
> 
> type: **boolean**
> 

**privatePage.notificationsEnabled**

> Indicates to the header that a slot 
should be created for a notification bell component. Note that the 
notification bell component is not determined or created by this 
property. The sn-canvas-header component simply creates an empty slot of
 name "notificationTrigger" that can be used to insert something like an
 notification bell.
> 
> 
> type: **boolean**
> 

**privatePage.currentScreenLinkConfiguration**

> Indicates to the header the positioning 
and role of of the currentScreenLinkConfiguration. This will tell the 
header where in the user drop-down-menu to add the link/button to edit 
the screen configuration. Note that this property does not provide the 
actual URL to the header, it simply provides information regarding the 
position (numeric value) in which the button should appear in the user 
drop down list, and the role for which this button should be available 
to.
> 
> 
> type: **object**
> 

**privatePage.globalTools**

> Provides configuration information for 
the buttons that appear on the right-hand side of the header, including 
the contents of the user-drop-down menu.
> 
> 
> type: **object**
> 

**privatePage.globalTools.collapsingMenuId**

> Indicates which child, by position, of 
the primaryItems list that should be used as the configuration for the 
user-drop-down menu. Keep in mind that this ID, or index, applies to the
 primaryItems list once it bas been sorted by each element's position 
property.
> 
> 
> type: **number**
> 

**privatePage.globalTools.primaryItems**

> A list of items/buttons that should appear on the most right-hand side positions of the header. See Menu Item schema below.
> 
> 
> type: **array**
> 
> **_roles**
> 
> > List of roles required to see or 
> interact with this item. This information is used on the server and it 
> never makes it to the component. If the current user role does not 
> appear in this array, this menu item is removed from the configuration.
> > 
> > 
> > type: **array**
> > 
> 
> **label**
> 
> > Object representing the label of button/item.
> > 
> > 
> > type: **string**
> > 
> 
> ```
> "label": {"translatable":true, "message":"Button Title"}
> ```
> 
> **icon**
> 
> > Name of Now Design System (NDS) icon.
> > 
> > 
> > type: **string**
> > 
> 
> **position**
> 
> > Numerical number defining the relative location of a specific item to other items.
> > 
> > 
> > type: **number**
> > 
> 
> **primaryDisplay**
> 
> > Indicates whether to display item icon 
> and/or label or none when an item is displayed in the global tools. 
> Options include:'none', 'label', 'icon', and 'both'. Not supported if an
>  item is within a menu (e.g., the user drop-down-menu).
> > 
> > 
> > type: **string**
> > 
> 
> **alert**
> 
> > Represents an alert configuration for 
> menu items. It will contain a table and filter property to get aggregate
>  counts from a specific table.
> > 
> > 
> > type: **object**
> > 
> 
> ```
> "alert": {
>     "table": "task",
>         "filter": "assigned_to=46c6f9efa9fe198101ddf5eed9adf6e7"
> }
> ```
> 
> **value**
> 
> > An object containing keys specific to the type of the item. See examples below, under the "type" property.
> > 
> > 
> > type: **object**
> > 
> 
> **type**
> 
> > The type of this menu item. Type can be one of 'navigation', 'menu', 'action', 'toggle', 'divider'.
> > 
> > 
> > type: **string**
> > 
> > 'navigation' represents external navigation and its value represents input into sn-nav-item
> > 
> 
> ```
> {
>     "label": {"translatable": true, "message": "Logout"},
>     "type": "navigation",
>     "position": 400,
>     "primaryDisplay": "none",
>     "value": {
>     "type": "external", //sn-nav-item's type property
>         "opensWindow": false, //sn-nav-item's opens-window property
>         "value": {"href": "#logout"} //sn-nav-item's item-value property
> }
> }
> ```
> 
> > 'menu' indicates that this item will have children of its own.
> > 
> 
> ```
> {
>     "label": {"translatable": true, "message": "Submenu"},
>     "type": "menu",
>     "position": 300,
>     "primaryDisplay": "none",
>     "value": {
>     "children": [] //a list of Items
> }
> }
> ```
> 
> > 'action' represents an internal navigation or action
> > 
> 
> ```
> {
>     "label": {"translatable": true, "message"; "Dispatch"},
>     "type": "action",
>     "position": 200,
>     "primaryDisplay": "none",
>     "value": {
>     "name": "DISPATCH_ACTION_NAME",
>         "payload": {
>         "payloadKey": "payloadValue"
>     }
> }
> }
> ```
> 
> > 'toggle' represents a true/false user preference.
> > 
> 
> ```
> {
>     "label":{"translatable":true, "message":"Show Ribbon"},
>     "type":"toggle",
>     "value":{
>     "_meta":{
>         "_type":"userPreferences", //identifies that this is a toggle/user preference item
>             "_path":"userPrefName", //the path in _value and _default to find the name and default value of the user preference
>             "_value":{
>             "userPrefName":"workspace.showRibbon" // name of the user preference
>         },
>         "_default":{
>             "userPrefName":"true" //default value of user preference
>         }
>     }
> }
> }
> ```
> 
> > 'divider' Visual divider (horizontal line) to seperate menu sections
> > 
> 
> ```
> {
>     "label": "Display Preferences",
>     "type": "divider",
>     "position": 0,
>     "primaryDisplay": "none"
> }
> 
> ```
> 

**privatePage.globalTools.secondaryItems**

> A list of items/buttons that should 
appear on the right-hand side of the header, but to the left of the 
privatePage.globalTools.primaryItems. See Menu Item schema below.
> 
> 
> type: **array**
> 

### 

### [Chrome Header Example JSON (Appendix)](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#header%20example)

---

**publicPage**

> Configuration data for un-authenticated users.
> 
> 
> type: **object**
> 

**publicPage.searchEnabled**

> Indicates to the header that a slot 
should be created for a search component. Note that search functionality
 is not determined by this property. The sn-canvas-header component 
simply creates an empty slot of name "search-input" that can be used to 
insert a search component.
> 
> 
> type: **boolean**
> 

**publicPage.actionButtons**

> A list of items that will appear on the 
right-hand side of the header when the user is not authenticated. The 
schema of these items do not follow the same format as the 
privatePage.globalTools secondaryItems and primaryItems. Take a look at 
the example at the bottom of this page to get an idea of the information
 needed: "bare" is an indicator if the button should appear as a 
bordered button or clickable text, "label" is will be the text within 
the button, and "value" is the information needed when dispatch an 
action.
> 
> 
> type: **array**
> 

**publicPage.menuEnabled**

> Indicates to the header that a slot 
should be created for a a navigation menu component (sn-canvas-menu). 
Note that menu functionality is not determined by this property. The 
sn-canvas-header component simply creates an empty slot of name 
"navigation-menu" that can be used to insert a menu component (for 
example, sn-canvas-menu). This property should be set to true, if a menu
 is desired for either a publicPage (authenticated user) or a 
privatePage (unauthenticated user).
> 
> 
> type: **boolean**
> 

**publicPage.logoRoute**

> Route/link attached to the logo when there is no authenticated user. Meant to be the route to have the user login.
> 
> 
> type: **object**
> 

```
"logoRoute": {
    "type":"route",   //sn-nav-item's type property
    "value": {
        "route": "home", // sn-nav-item's item-value property
        "fields": {}
    }
}
```

## Navigation Configuration (chrome_toolbar)

---

The chrome_toolbar UX Page Property adds
 a left-side navigation to the experience. You can have multiple 
chrome_toolbar records, each record merges into one property. The order 
property is used to sort the icons into the desired order.

**id**

> Defines the button id.
> 
> 
> type: **string**
> 

**label**

> Defines the button value.
> 
> 
> type: **string**
> 

**icon**

> Defines the icon displayed.
> 
> 
> type: **string**
> 

**order**

> Defines the order displayed in toolbar from top to bottom
> 
> 
> type: **number**
> 

**badge**

> Defines the badge information. It contains count， configurations，and type property.
> 
> 
> type: **object**
> 

**presence**

> Presence of the user, displayed with an 
indicator icon in the corner of the toolbar button. It contains status, 
configurations object and type. Status can be one of 'available, 'busy',
 'away', 'offline'.
> 
> 
> type: **object**
> 

```
 "presence":  {
        status: "available",
        configurations: {
            table: "sys_user_presence"
            filter: "user_available=true^user=6816f79cc0a8016401c5a33be04be441"
        },
        type: "record"
    }
```

**availability**

> Defines the button availability criteria
 based on user roles, plugin activation. It contains roles and plugin 
property. Example below: The inbox button must be available for user 
with awa_agent or awa_admin roles and agent chat plugin(com.glide.interaction.awa) is activated.
> 
> 
> type: **object**
> 

```
"availability": {
      "roles": ["awa_agent","awa_admin","admin"],
      "plugin": "com.glide.interaction.awa"
    }
```

### [Chrome Navigation Example JSON (Appendix)](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#navigation%20example)

## Search Configuration (global_search_configurations)

---

**globalSearchViewConfigId**

> Points to a Global Search Configuration 
record, contains references to global search configurations to be 
consumed by search components.
> 
> 
> type: **object**
> 

```
{
"globalSearchViewConfigId": "97a574ea53c0130084acddeeff7b12a6",
"globalSearchRoute": "search"
}
```

**globalSearchDataConfigId**

> Points to a Search Application Configuration record, i.e. sys_id of the record.
> 
> 
> type: **string**
> 

### 

## Tabs Configuration (chrome_tab)

---

### 

[](https://www.servicenow.com/community/image/serverpage/image-id/154305iCD7B7B8583E0173A/image-size/medium?v=v2&px=400)

**contextual**

> Routes can hold sub tabs. To create a 
sub tab, targetRoute must be set current (if the current active route is
 a contextual route) or any contextual route so a sub tab is created 
under that tab corresponding to the route. Indicating the values listed 
in the contextual array will open a sub tab as defined by the list 
routes.
> 
> 
> type: **array**
> 

**newTabMenu**

> Create new records directly from the tab bar. If newTabMenu is empty, the + symbol in the tab bar is not shown.
> 
> 
> type: **array**
> 
> **newTabMenu.label**
> 
> > Indicates the new tab label to be displayed.
> > 
> > 
> > type: **string**
> > 
> 
> **newTabMenu.routeInfo**
> 
> > Represents the configuration of the item selected to be dispatch when the button is clicked.
> > 
> > 
> > type: **object**
> > 
> 
> **newTabMenu.condition**
> 
> > Represents the configuration of the item selected to be dispatch when the button is clicked.
> > 
> > 
> > type: **object**
> > 
> 
> [](https://www.servicenow.com/community/image/serverpage/image-id/154315iF4FCE3661B061F03/image-size/large?v=v2&px=999)
> 

**maxMainTabLimit**

> Maximum number of main/session/L1 that 
an experience can hold per session. If number of tabs exceeds the limit,
 new main tabs will not be created.
> 
> 
> type: **integer**
> 

**maxTotalSubTabLimit**

> Maximum number of total tabs (main, 
primary, and sub tabs) that an experience can hold per session. If 
number of tabs exceeds the limit, new tabs will not be created.
> 
> 
> type: **integer**
> 

**primaryRoute**

> An experience can only have one primary 
tab renders at any point in time, it's always the first tab if it 
exists. Primary tab switches between primaryRoutes defined in the 
primaryTab property. See properties for primary routes below.
> 
> 
> type: **string**
> 
> **primaryRoute.< primaryRoutes >**
> 
> > Indicates the metadata for the 
> primaryRoute nested object tab. This configuration is used to create a 
> primary tab, and switch/activate the primary tab between primaryRoutes 
> when a corresponding route is active. The object name indicates the 
> route the object properties bind totype: object
> > 
> 
> **primaryRoute.< primaryRoutes >.badge**
> 
> > Represents the badge information. It contains count， configurations，and type property.type: object
> > 
> 
> **primaryRoute.< primaryRoutes >.icon**
> 
> > Indicates the icon displayed.type: string
> > 
> 
> **primaryRoute.< primaryRoutes >.isHighlighted**
> 
> > Indicates if the current primary route object tab is highlighted.type: boolean
> > 
> 
> **primaryRoute.< primaryRoutes >.isSelected**
> 
> > Indicates if the current primary Route object tab is selected.type: boolean
> > 
> 
> **primaryRoute.< primaryRoutes >.label**
> 
> > Indicates the new tab label to be displayed.type: string
> > 
> 
> **primaryRoute.< primaryRoutes >.routeInfo**
> 
> > Represents the route information associated to the chrome tabs object.type: object
> > 
> 
> **primaryRoute.< primaryRoutes >.status**
> 
> > Indicates the status of the primary route object.type: string
> > 

### 

### [Chrome Toolbar Example JSON (Appendix)](https://www.servicenow.com/community/next-experience-articles/workspace-app-shell-ux-page-properties/ta-p/2331956#toolbar%20example)

### 

## Main Configuration (chrome_main)

---

**maxCachedPageCount**

> Indicates the total number of sn-canvas-screen instances live in DOM per experience.
> 
> 
> type: **integer**
> 

**maxActivePageCount**

> Indicates the number of active sn-canvas-screens within the dom how many are active (not in the now-mode='suspended' state).
> 
> 
> type: **integer**
> 

**timeLeftWarning**

> Indicates the amount of time, in minutes, before the client side warning is displayed for the actual session timeout.
> 
> 
> type: **integer**
> 

## 

Chrome Main Example JSON

In a scenario where there **maxCachedPageCount** is 5, and the **maxActivePageCount** is 3:

- 
    - 5 screens will be cached (maximum)
    - 3 screens will be active
    - 2 screens will be suspended

```
"chrome_main": {
    "maxCachedPageCount": 5,
    "maxActivePageCount": 3,
    "timeLeftWarning": 15
}
```

## Route Configuration (routeConfigId)

---

This UX Page Property points to a sys_id
 of a record on the Route Configurations (sys_ux_dynamic_route_config) 
table. A Route Configuration record will have related Route Mapping 
records. With no mappings, the record/table/sysId page should open in a 
new primary/sub tab. If a mapping exists for the current experience 
record, it should map given the route with table and sys_id payload 
values to open a new primary tab/sub tab with the route and payload as 
defined. You'll notice our product workspaces may have their own records
 in this table, and that workspaces generated from App Engine Studio use
 a base COE Route Config record. If you're building a workspace 
manually, and are not sure what is needed here, try re-using the COE 
Route Config record.

---

# Record Page UX Page Properties

These UX page Properties are independent of the app shell. They are bound to the Record page > Glide Form data resource.

| **UX Page Property**
 | **Description**
 |
| --- | --- |
| actionConfigId | Uses a string value of a Sys ID from the
 UX Action Configurations (sys_ux_action_config) table to show 
declarative actions on the record page.
 |
| headerConfigId | Uses a string value of a Sys ID in the Form Header (sys_aw_form_header) table to show a form header for the experience.
 |
| ribbonConfigId | Uses a string value of a Sys ID in the 
UX Ribbon Configurations (sys_ux_ribbon_config) table to show a ribbon 
for the experience.
 |
| highlightedViewConfigId | Uses a string value of a Sys ID in the UX Highlighted Value Configurations (sys_ux_highlighted_value_config) table.
 |
| view | Specifies the view for the table when a 
view rule for the table is not defined. An example is the workspace view
 for the CSM/FSM Configurable Workspace experience.
 |
| viewRuleConfigId | UX View rule configuration ID. Accepts a
 string value of a sys_id located on the Workspace View Rules 
(sysrule_view_workspace) table. 
 |

[](https://www.servicenow.com/community/image/serverpage/image-id/154313iFB5715374B71F17B/image-size/large?v=v2&px=999)

---

# List Page UX Page Properties

| **UX Page Property**
 | **Description**
 |
| --- | --- |
| listConfigId | Uses a string value of a Sys ID from the UX List Menu Configuration (sys_ux_list_menu_config) table to populate the list menu. |

[](https://www.servicenow.com/community/image/serverpage/image-id/154325iD2132406FE684FAA/image-size/large?v=v2&px=999)

## 

---

## Appendix

### Chrome Header Example JSON

```jsx
{
  "privatePage":{
    "searchEnabled": true, //Should header provide a slot for a search bar
    "userPrefsEnabled":true,  //
    "notificationsEnabled":true,
    "currentScreenLinkConfiguration": {
       "roles": ["admin"],
       "position": 250
    },
    "globalTools":{
      "collapsingMenuId":0,
      "primaryItems":[
        {
          "label":{"translatable":true, "message":"UserMenu"},
          "icon":"user",
          "type":"menu",
          "primaryDisplay":"icon",
          "value":{
            "children":[
              {
                "_roles":[
                  "workspace_admin"
                ],
                "label":{"translatable":true, "message":"Configure Workspace"},
                "type":"navigation",
                "position":200,
                "primaryDisplay":"none",
                "value":{
                  "type":"external",
                  "opensWindow":"true",
                  "value": {
                    "href": "/nav_to.do?uri=/sys_ux_app_config.do?sys_id=89153225530010107388ddeeff7b122f"
                  }
                }
              },
              {
                "label":{"translatable":true, "message":"Settings"},
                "type":"menu",
                "position":100,
                "value":{
                  "children":[
                    {
                      "type": "divider",
                      "label": "Display Preferences",
                      "primaryDisplay": "none"
                    },
                    {
                      "label":{"translatable":true, "message":"Show Ribbon"},
                      "type":"toggle",
                      "value":{
                        "_meta":{
                          "_type":"userPreferences",
                          "_path":"userPrefName",
                          "_value":{
                             "userPrefName":"workspace.showRibbon"
                          },
                          "_default":{
                            "userPrefName":"true"
                          }
                        }
                      }
                    },
                    {
                      "label":{"translatable":true, "message":"Show Sidebar"},
                      "type":"toggle",
                      "value":{
                        "_meta":{
                          "_type":"userPreferences",
                          "_path":"userPrefName",
                          "_value":{
                            "userPrefName":"workspace.showAgentAssist"
                          },
                          "_default":{
                            "userPrefName":"true"
                          }
                        }
                      }
                    },
                    {
                      "label":{"translatable":true, "message":"Wrap List Text"},
                      "type":"toggle",
                      "value":{
                        "_meta":{
                          "_type":"userPreferences",
                          "_path":"userPrefName",
                          "_value":{
                            "userPrefName":"workspace.wrapListText"
                          },
                          "_default":{
                            "userPrefName":"false"
                          }
                        }
                      }
                    },
                    {
                      "type": "divider",
                      "label": {"translatable":true, "message":"Notifications"},
                      "primaryDisplay": "none"
                    },
                    {
                      "label":{"translatable":true, "message":"Show Banners"},
                      "type":"toggle",
                      "value":{
                        "_meta":{
                          "_type":"userPreferences",
                          "_path":"userPrefName",
                          "_value":{
                            "userPrefName":"workspace.notifications.showPopups"
                          },
                          "_default":{
                            "userPrefName":"true"
                          }
                        }
                      }
                    },
                    {
                      "label":{"translatable":true, "message":"Show Badge Count"},
                      "type":"toggle",
                      "value":{
                        "_meta":{
                          "_type":"userPreferences",
                          "_path":"userPrefName",
                          "_value":{
                            "userPrefName":"workspace.notifications.showBadgeCount"
                          },
                          "_default":{
                            "userPrefName":"true"
                          }
                        }
                      }
                    }
                  ]
                }
              },
              {
                "label":{"translatable":true, "message":"Logout"},
                "type":"navigation",
                "position":300,
                "value":{
                  "value":{
                    "href": "/logout.do"
                  },
                  "type":"logout"
                }
              }
            ]
          }
        }
      ],
      "secondaryItems":[]
    }
  },
  "publicPage":{
    "searchEnabled":false,
    "menuEnabled": true,
    "actionButtons": [
      {
          "label": {"translatable":true, "message":"Requests"},
          "value": {
              "type": "route",
              "value": {
                  "route": "requests",
                  "fields": {}
                  }
          }
      },
      {
          "label": {"translatable":true, "message":"Login"},
          "value": {
              "type": "AUTH_ROUTE_BINDING",
              "binding": {
                  "address": ["loginModal"],
                  "default": "/login.do"
              }
          },
          "bare": true
      },
      {
          "label": {"translatable":true, "message":"Register"},
          "value": {
              "type": "AUTH_ROUTE_BINDING",
              "binding": {
                  "address": ["register"],
                  "default": "/login.do"
              }
          },
          "bare": false
      }
    ]
  }
}
```

### Chrome Navigation Example JSON

```jsx
[
  {
    "id": "home",
    "label": {"message": "Home", "translatable": true},
    "icon": "home-outline",
    "viewportInfo": {},
    "routeInfo": {
      "route": "home"
    },
    "group": "top",
    "badge": {},
    "order": 100,
    "presence": {},
    "availability": {}
  },
  {
    "id": "list",
    "label": {"message": "List", "translatable": true},
    "icon": "list-outline",
    "viewportInfo": {},
    "routeInfo": {
      "route": "list"
    },
    "group": "top",
    "order": 200,
    "badge":{},
    "presence": {},
    "availability": {}
  },
  {
    "id": "call",
    "label": {"message": "Call",  "translatable": true},
    "icon": "phone-outline",
    "routeInfo": {},
    "viewportInfo": {
      "route": "cti",
      "fields": {
        "opened": false
      },
      "viewportElementId": "wsCornerDialog"
    },
    "group": "bottom",
    "order": 300,
    "badge":{},
    "presence": {},
    "availability": {}
  }
]
```

### Chrome Toolbar Example JSON

```jsx
{
  "tabConfig": {
    "primaryRoute": {
      "home": {
        "badge": null,
        "icon": "home-outline",
        "isHighlighted": true,
        "isSelected": true,
        "label": "Home",
        "routeInfo": {
          "route": "home"
        },
        "status": ""
      },
      "list": {
        "badge": null,
        "icon": "list-outline",
        "isHighlighted": false,
        "isSelected": false,
        "label": "List",
        "routeInfo": {
          "route": "list"
        },
        "status": ""
      },
      "inbox": {
        "badge": {
          "count": 2
        },
        "icon": "inbox-outline",
        "isHighlighted": false,
        "isSelected": false,
        "label": "Inbox",
        "routeInfo": {
          "route": "inbox"
        },
        "status": "available"
      }
    },
    "contextual": ["record"],
    "newTabMenu": [
      {
        "label": "New Interaction",
        "routeInfo": {
          "route": "record",
          "fields": {
            "table": "interaction",
            "sys_id": "-1"
          }
        },
        "condition": {
          "tableDescription": {
            "table": "interaction",
            "canCreate": true
          }
        }
      },
      {
        "label": "New Incident",
        "routeInfo": {
          "route": "record",
          "fields": {
            "table": "incident",
            "sys_id": "-1"
          }
        }
      }
    ],
        "maxMainTabLimit": 5,
        "maxTotalSubTabLimit": 10
  }
}
```

## Related

- [[Workspace]]
- [[How to use UI Actions in Workspaces]]
- [[Workspace for a custom app forms]]
- [[Using Applicability in Next Experience Themes to s]]