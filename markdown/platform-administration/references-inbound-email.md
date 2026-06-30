---
title: References for Inbound email
description: Email object variables, user impersonations and inbound actions and examples for processing inbound email actions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/references-inbound-email.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Inbound email, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# References for Inbound email

Email object variables, user impersonations and inbound actions and examples for processing [[actions-inbound-email|inbound email actions]].

-   **[[r_AccessingEmailObjsWithVars|Accessing email object variables]]**  
An [[ia-inbound-email-il|inbound email]] action script contains the email object to access various pieces of an inbound email through variables. You can use the global variable *sys\_email* with inbound email actions.
-   **[[r_MatchingEmailToExistingUsers|Email user matching]]**  
When the instance receives an email message, the system searches for an existing user record with the same email address as the sender.
-   **[[r_ImpUserRunInboundActions|User impersonations and inbound actions]]**  
When the instance receives an email, it can take a variety of actions by impersonating the sender.
-   **[[r_AllowLockedUsersInbdEmailAct|Allowing locked out users to process inbound email actions]]**  
A property is available to allow locked out users to trigger inbound actions. For example, enabling the property can allow locked out users to reset their password and send email to the instance asking for assistance.
-   **[[r_RedirEmailDifferentAssignGrp|Redirecting email to the instance POP3 account]]**  
Configure other mailboxes to forward email to the instance's POP3 account.
-   **[[r_InboundEmailActionExamples|Inbound email action examples]]**  
Various examples of inbound email actions are available to help you build your own inbound email actions. These examples show how to set up inbound email actions to handle email replies, create \(log\) a problem record, request a change, and update an incident.
-   **[[t_IntegratingInboundEvents|Integrate inbound events]]**  
This example illustrates how to create a notification from an inbound JSON request.

**Parent Topic:**[[inbound-email-landing|Inbound email]]

## Related

- [[r_AccessingEmailObjsWithVars|Accessing email object variables]]
- [[r_MatchingEmailToExistingUsers|Email user matching]]
- [[r_ImpUserRunInboundActions|User impersonations and inbound actions]]
- [[r_AllowLockedUsersInbdEmailAct|Allowing locked out users to process inbound email actions]]
- [[r_RedirEmailDifferentAssignGrp|Redirecting email to the instance POP3 account]]
- [[r_InboundEmailActionExamples|Inbound email action examples]]
- [[t_IntegratingInboundEvents|Integrate inbound events]]
- [[inbound-email-landing|Inbound email]]
- [[actions-inbound-email|Inbound email actions]]
- [[ia-inbound-email-il|Inbound email]]
