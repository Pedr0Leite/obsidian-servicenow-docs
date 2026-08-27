---
title: "Troubleshooting ServiceNow instance ignoring email sent by another instance"
aliases:
  - KB0551482
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551482
kb_number: KB0551482
last_modified: 2026-03-23
---

## Issue

You build an email-based integration between two or more instances and send an email to another ServiceNow instance, but the receiving instance ignores emails coming from the sending ServiceNow instance.

Or, you receive an email that gets ignored because it contains the header "X-ServiceNow-Generated:true".

## Resolution

**Implement a Web Service Integration – recommended**

Customers implementing instance-to-instance integrations should use web service calls between the instances, which avoids the ambiguity inherent in trying to distinguish human-generated and system-generated inbound emails to drive an appropriate system response.

**Implement an Email-based Integration**

ServiceNow does not recommend integrations between instances via email notifications because it is fragile and easily broken.

A decision to integrate two instances in this manner must be considered with care.  It is imperative that you regression-test your instance-to-instance use cases. For example, simple changes to inbound email actions or filters can easily cause an automated email to slip through and create an incident, rather than execute the integration action you intended and tested when first deployed.

Before removing the inbound email filter or property header that prevents the email from being processed, customers must consider the automation scenarios possible when two instances email each other.  Some areas where things can go wrong are:

-   After initially validating that an implementation does not contain email loops for known tested workflows, you later make a change to inbound email actions or notifications that inadvertently introduce the issue. The person creating the updated functionality months after the initial integration may be unaware that the system handles both automated and manual email input and therefore accidentally introduces an email loop because the use case was not re-tested.
-   You define a corporate group email list outside of the ServiceNow instance (in MS Exchange, for example), and the instance's email address gets added to that group. A notification thus is configured to send to the group that includes the instance itself, causing an unintended email loop. This situation is time-consuming to diagnose and usually requires your email admin to be involved in resolving the incident.
-   The two instances may have overlapping watermark numbers. Inbound email processing will recognize the watermark and associate the email to the target record on the receiving instance.  This leads to email content about instance A getting attached to a target record in instance B, which now displays in the target record's work notes.  (This particular issue can be mitigated by the use of the [Random Watermark](https://docs.servicenow.com/csh?topicname=c_WorkingWithWatermarks.html&version=latest "Random Watermark") plugin in Jakarta and later.)
-   Once the ignore functionality is removed, email from any ServiceNow instance is now permitted.  Therefore you may experience an 'unintended integration' that results in an incident or outage.  (Consider modifying the email filter so that it also checks the 'from' address to ensure only email from a specific instance integration will be processed.) 

Test email between automated systems as follows:

1.  Define outbound email use cases.
2.  For each inbound receiving instance, define handling use cases.
3.  Remove the inbound filter on test instances that receive emails (or update the ignore headers property) to allow the instance to process emails sent by other ServiceNow instances.
4.  Test each instance's behavior to ensure that email loops do not occur.
5.  Send an email from a third instance if you have a subprod available.  Does this email from an unintended instance behave as you expect?

 **Note:** Make sure to retest email integration use cases after any changes to the email process on either instance.

Once you have tested this throughly see "My organization/customer is sending emails to my instance and they are marked as spam - what can I do?" section in [KB0549426](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549426) on how to modify Email Filters.
