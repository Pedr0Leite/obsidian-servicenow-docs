---
title: Configure Auto-Responder notifications
description: Configure the Auto-Responder feature for sharing relevant content in email notifications for deflecting cases.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/config-auto-responder.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Machine learning solutions, Implement Intelligence, Configure, Customer Service Management]
---

# Configure Auto-Responder notifications

Configure the Auto-Responder feature for sharing relevant content in email notifications for deflecting cases.

## Before you begin

Role required: admin

Activate the Predictive [[intelligence-csm|Intelligence]] for [[c_CustomerServiceManagement|Customer Service Management]] plugin \(com.snc.csm\_ml\). For more information, see [Activate a plugin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_ActivateAPlugin.md) and [[predictive-intelligence-for-csm|Predictive Intelligence for CSM solution definitions]].

## About this task

When you install and activate the Predictive Intelligence for Customer Service Management plugin \(com.snc.csm\_ml\), the following related plugins are also activated:

-   Customer Service plugin \(com.sn\_customerservice\)
-   Predictive Intelligence for [[osp-contextual-search|Contextual Search]] plugin \(com.snc.contextual\_search\_ml\)
-   Email Notification Script for Contextual Search Results plugin \(com.snc.adv\_cxs\_results\_email\_script\)

You can also configure the Auto-Responder feature for tasks other than customer service cases. For more information, see [[config-auto-responder-other-tasks|Configure Auto-Responder for tasks other than cases]].

## Procedure

1.  Follow the steps in this link: [[enable-auto-responder|Enable Auto-Responder]].

2.  Follow the steps in this link: [[train-sol-defn-auto-responder|Train the similarity solution for finding Auto-Responder notification content]].

3.  Follow the steps in this link: [[config-context-auto-responder|Configure the search context for Auto-Responder]].

4.  Follow the steps in this link: [[config-limit-auto-responder|Limit the number of articles in Auto-Responder notifications for cases]].

5.  Follow the steps in this link: [[use-extension-point-auto-responder|Include advanced contextual search results in Auto-Responder notifications]].

    **Note:** By default, any knowledge articles viewed in the last 30 days by the user are not included in the email notification. You can use the getViewedContent extension point to modify the filter out by the duration of the last viewed content.

6.  Follow the steps in this link: [[enable-text-based-auto-responder|Enable text search recommendations in Auto-Responder notifications]].

7.  Follow the steps in this link: [[config-auto-responder-channels|Include cases logged using specified communication channels in Auto-Responder notifications]].

8.  Follow the steps in this link: [[config-auto-responder-custom-portal|Include knowledge articles from custom portals in Auto-Responder notifications]].

    **Note:** When you configure the Auto-Responder feature to use a custom portal, the default configuration for the customer service portal and consumer service portal are not used. Ensure that you use this configuration when you have your own custom portal and don't want to use the customer service portal or consumer service portal.


**Related topics**  


[[auto-responder-case|Using Auto-Responder for case deflections]]

## Related

- [[predictive-intelligence-for-csm|Predictive Intelligence for CSM solution definitions]]
- [[config-auto-responder-other-tasks|Configure Auto-Responder for tasks other than cases]]
- [[enable-auto-responder|Enable Auto-Responder]]
- [[train-sol-defn-auto-responder|Train the similarity solution for finding Auto-Responder notification content]]
- [[config-context-auto-responder|Configuring the search context for Auto-Responder]]
- [[config-limit-auto-responder|Limit the number of articles in Auto-Responder notifications for cases]]
- [[use-extension-point-auto-responder|Include advanced contextual search results in Auto-Responder notifications]]
- [[enable-text-based-auto-responder|Enable text search recommendations in Auto-Responder notifications]]
- [[config-auto-responder-channels|Include cases logged using specified communication channels in Auto-Responder notifications]]
- [[config-auto-responder-custom-portal|Include knowledge articles from custom portals in Auto-Responder notifications]]
- [[auto-responder-case|Using Auto-Responder for case deflections]]
- [[intelligence-csm|Intelligence]]
- [[c_CustomerServiceManagement|Customer Service Management]]
- [[osp-contextual-search|Contextual search]]
