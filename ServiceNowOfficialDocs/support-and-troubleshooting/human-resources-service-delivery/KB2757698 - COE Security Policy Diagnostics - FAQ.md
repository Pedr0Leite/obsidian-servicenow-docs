---
title: "COE Security Policy Diagnostics - FAQ"
aliases:
  - KB2757698
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2757698
kb_number: KB2757698
last_modified: 2026-02-23
---

## Text

## Table of Contents

-   [Overview](#mcetoc_1eivfhctq2g)
-   [Frequently Asked Questions](#mcetoc_1eivfhctq2h)
    -   [1\. What is this feature about and what is this not about?](#mcetoc_1eivfhctq2i)
    -   [2\. Why is my HR case not found in HR Case input field list?](#mcetoc_1eivfhctq2j)
-   [Additional Information](#mcetoc_1eivfhctq2l)

## Overview

COE Security Policy Diagnostics page allows HR administrators to analysee how COE Security Policies grants/denies access to a given HR Case for a given user.

## Frequently Asked Questions

### 1\. What is this feature about and what is this not about?

This feature is only to analyse how COE Security Policies are evaluated and grants/denies the access.

This feature is NOT for analysing the complete access of a user for HR Case records. It is possible that the access result from COE Security Plocy evaluation is different from actual access result. Use Platform Access Analyzer for complete access analysis.

### 2\. Why is my HR case not found in HR Case input field list?

It's possible that the current HR Administrator doesn't have the access to the case (possible due to COE Security Policies). In this scenario, you can do one of the following:

-   Try with a HR Admin user who has access to the case.
-   Try with a user who has both HR Admin and Admin roles. Out of the box, this user gets access to all cases regardless of COE Security Policy configuration.

## Additional Information

-   [Documentation](https://docs-preview.corp.service-now.com/bundle/australia-employee-service-management/page/product/human-resources/concept/coe-diagnostics-tool.html)
