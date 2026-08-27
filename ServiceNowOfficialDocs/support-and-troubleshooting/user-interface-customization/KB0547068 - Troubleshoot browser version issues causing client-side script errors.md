---
title: "Troubleshoot browser version issues causing client-side script errors"
aliases:
  - KB0547068
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547068
kb_number: KB0547068
last_modified: 2026-03-24
---

## Troubleshoot browser version issues causing client-side script errors

  

### Issue

Troubleshoot client-side script errors caused by browser version incompatibilities or browser extensions conflicting with the ServiceNow platform.

### Symptoms

-   Field removed from form
-   Cannot change a field
-   Form is broken
-   UI policy not working
-   UI action not working
-   Client scripts not working
-   Form sections not loading
-   Fields not visible
-   Mandatory field not working

### Release

All releases

### Cause

-   Older or newer browser versions that were not accounted for at development time can cause client-side errors when certain scripts run.
-   Browser plugins or extensions can conflict with the ServiceNow platform.

### Resolution

When client-side scripts are not functioning as expected, try the following steps:

1.  Test using a different version of your current browser (newer or older).
2.  Test using a different browser type, such as Firefox or Chrome.
3.  Turn off browser plugins or extensions and retest to rule out conflicts with the ServiceNow platform.
4.  If the issue persists or you identify a discrepancy in browser behavior, open a case with ServiceNow Technical Support for investigation.

Example: In earlier versions of Internet Explorer (IE), the browser console was not available unless the developer tools were open. A script containing a **console.log** statement would cause a client-side error in those IE versions but work correctly in other browsers.

### Related Links

[Browser requirements for all Australia features and products](https://www.servicenow.com/docs/r/release-notes/rn-summary-browser-reqs.html "Browser requirements for all Australia features and products")
