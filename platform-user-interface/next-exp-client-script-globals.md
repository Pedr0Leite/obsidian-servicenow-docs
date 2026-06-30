---
title: Next Experience client-side scripting global variables
description: Next Experience global variables are used in client scripts to determine whether Next Experience is applied to a page.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/next-exp-client-script-globals.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Next Experience UI, Configure UIs and portals, Configure user experiences]
---

# Next Experience client-side scripting global variables

Next Experience global variables are used in client scripts to determine whether Next Experience is applied to a page.

-   **NOW.isUsingPolaris**

    Returns **true** if Next Experience is applied to the current page.

-   **NOW.isPolarisWrapper**

    Returns **true** if the page is running in the Next Experience Unified Navigation. This global variable exists only in the Unified Navigation.

    For more information about the Unified Navigation, see [[using-the-next-experience-global-header|Using the Next Experience Unified Navigation]].


Client script:

```
// Reload the current page in the unified navigator if not currently in the unified nav
if (NOW.isUsingPolaris && (!top.NOW || top.NOW.isPolarisWrapper !== "true")) {
    var currentPath = window.location.pathname + window.location.search;
    top.window.location.href = "/now/nav/ui/classic/params/target/" + encodeURIComponent(currentPath)
}

```

**Parent Topic:**[[next-experience-ui-admin|Configuring the Next Experience UI]]

**Related topics**  


[bundle-crapiref.PolarisUIScopedAPI]

## Related

- [[using-the-next-experience-global-header|Using the Next Experience Unified Navigation]]
- [[next-experience-ui-admin|Configuring the Next Experience UI]]
