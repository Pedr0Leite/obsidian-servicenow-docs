---
title: "JWT Token is incorrectly formatted, and can not be decoded..invalid token (SAMP Adobe Integration Profile)"
aliases:
  - KB1001921
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1001921
kb_number: KB1001921
last_modified: 2024-11-29
---

## JWT Token is incorrectly formatted, and can not be decoded..invalid token (SAMP Adobe Integration Profile)

  

## Issue

-   While integrating the Adobe Subscription API, the error appears and Credentials test fails even the Configuration is successfully configured on the Adobe console

## Error

-   "Connection Failed. JWT Token is incorrectly formatted, and can not be decoded..invalid token."

![](sys_attachment.do?sys_id=3c2c687cdbb04554b5d6e6be13961935)

## Cause 

-   The signature part in JWT token is null. Based on our code, the variables passed in to generate signature are all from the customer side, and the code has been working fine for previous cases. Could you please ask the customer to confirm they followed the steps from our documentation and maybe try to set it up again

## **Documentation**

-   Product Documentation: [Integrate with Adobe Cloud](https://docs.servicenow.com/bundle/rome-it-asset-management/page/product/software-asset-management2/task/set-up-adobe-subscription.html "Integrate with Adobe Cloud")
-   Knowledge Article: [Adobe integration configuration Step-By-Step](/kb?id=kb_article_view&sysparm_article=KB1001915 "Adobe integration configuration Step-By-Step")
-   Adobe Documentation: [Service Account Connection](https://www.adobe.io/developer-console/docs/guides/authentication/ServiceAccountIntegration/ "Service Account Connection")
