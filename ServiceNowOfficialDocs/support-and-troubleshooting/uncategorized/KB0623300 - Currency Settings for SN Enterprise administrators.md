---
title: "Currency Settings for SN Enterprise administrators"
aliases:
  - KB0623300
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623300
kb_number: KB0623300
last_modified: 2024-04-07
---

## Currency Settings for SN Enterprise administrators

  

### Issue

-   Currency Settings for SN Enterprise administrators

### Resolution

# About currency configuration sets

* * *

Two main configuration sets run on the platform:, the currency settings for Service Catalog related functions, and the currency settings for the Financial Management plugins.

  

# Currency in Service Catalog

* * *

The instance can run in either Single Currency Model or Multiple Currency Model. The following Community posts provide a comprehensive description of these models:

-   [Converting amount & currency type based on locale](https://community.servicenow.com/community/service-automation-platform/blog/2016/01/13/getting-to-grips-with-currency-field)
-   [Using the Single Currency Model in your Instance](https://community.servicenow.com/community/service-automation-platform/blog/2016/01/20/getting-to-grips-with-the-currency-field-part-2)

While the Single Currency Model is relatively simple to understand, the Multiple Currency Model may cause confusion over time. The following factors determine which currency is used in the instance:

-   System Properties > System Localization. The instance Language and Locale codes drive the behavior, and en.US is used as default if left empty. The language and country code fields for the logged in user will override if present. Note that usually these fields are hidden. The browser's default settings will take effect when these fields are left empty.
-   System Localization => Currencies/Exchange Rates need to hold the corresponding used currencies conversion information.
-   sys\_locale needs to have corresponding locations. If not, the simplest way to make it available is to enable a hidden model named Load Locales under System Localization, and load the default samples.
-   Having done all of the previous, all currency data are stored using the system default currency, plus a record in the \[fx\_currency\_instance\] table if the data input is done in a currency other than the system default.
-   A currency globe icon is shown on each currency field in list views, and allows user's journal on different currencies.
-   If the current user is using a different currency from the system default, all the currency fields should be able to default to the user's currency as far as it has a default value, even if set to 0. If no default value is set, the currency will default to the system default.

# Currency in Project Portfolio Suite with Financials Management plugins

* * *

Currency in Project Portfolio Suite with Financials is controlled by the system property **com.glide.financial\_management.currency\_code**. If this property is not set, the application uses the system default. It does not matter which currency model of the Service Catalog is used.

It is important to note that although the financial applications allow users to input prices in different currencies, the calculations are always based onto the baseline currency specified by the **com.glide.financial\_management.currency\_code** property, or the system default. This baseline is always required for any currency or pricing aggregation performed by these plugins.
