---
title: "Clicking 'Map view' on 'Make a reservation' page [wsd_search] results in javascript errors "
aliases:
  - KB0966014
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0966014
kb_number: KB0966014
last_modified: 2024-08-21
---

## Clicking 'Map view' on 'Make a reservation' page \[wsd\_search\] results in javascript errors

  

### Issue

When clicking the 'Map View' on wsd\_search page, the map is not displayed instead it results in following error messages on the page:  
There is a JavaScript error in your browser console  
There was some error while trying to load the map. Please try again later.

Additionally, browser console contains following error 

js\_includes\_sp.jsx?v=05-26-2021\_0941&lp=Sun\_May\_02\_11\_05\_21\_PDT\_2021&c=32\_946:42488 Error: 401 Unauthorized  
at mappedin.js:11  
at h (mappedin.js:10)  
at Generator.\_invoke (mappedin.js:10)  
at Generator.next (mappedin.js:10)  
at i (mappedin.js:10)  
at l (mappedin.js:10)

In network tab, you shall observe following REST API call fails with 401 error

  
Request URL: https://INSTANCE\_NAME.service-now.com/api/sn\_wsd\_mappedin/api/bundleproxy?venue=<venue>&version=1.0.0  
Request Method: GET  
Status Code: 401 Unauthorized

### Release

Quebec Release

Workplace Reservation Management \[v1.6.1+\] & Workplace Service Delivery Integration with Mappedin \[v1.4.2+\]

### Cause

After the WSD June 2021 release, it is mandatory to add 'MappedIn Export Credentials' at

https://instance\_name.service-now.com/sys\_auth\_profile\_basic.do?sys\_id=2089f43b23531010fb0c949e27bf6544  
  
Either the credential is not filled or it is wrong. 

### Resolution

Provide correct credentials under 'MappedIn Export Credentials' record.

### Related Links

[https://docs.servicenow.com/bundle/quebec-employee-service-management/page/product/workplace-space-mapping/task/wsm-mappedin-credentials.html](https://docs.servicenow.com/bundle/quebec-employee-service-management/page/product/workplace-space-mapping/task/wsm-mappedin-credentials.html)
