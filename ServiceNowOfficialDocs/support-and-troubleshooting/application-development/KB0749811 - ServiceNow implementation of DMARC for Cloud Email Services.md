---
title: "ServiceNow implementation of DMARC for Cloud Email Services"
aliases:
  - KB0749811
  - ServiceNow implementation of DMARC for Cloud Email Services
tags:
  - servicenow
  - support-kb
  - dmarc
  - email-security
  - spf
  - dkim
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749811
kb_number: KB0749811
last_modified: 2025-08-25
---

## ServiceNow implementation of DMARC for Cloud Email Services

  

### Issue

ServiceNow is making use of the DMARC (RFC 7489) standard to further improve our email security. There should be no need for customers to alter any of their existing instance email configurations to take advantage of the DMARC policy. Additionally, customers should not need to alter the configurations of their email infrastructure because of the ServiceNow DMARC policy.

It may be necessary to make changes to customer email services to take full advantage of the ServiceNow DMARC policy. We advise that you contact your email administrator if desired.

### Overview of DMARC

DMARC (_Domain-based Message Authentication, Reporting, and Conformance_) is an email authentication protocol. It is designed to give email domain owners the ability to protect their domain from unauthorized use, commonly known as _email spoofing_. The purpose and primary outcome of implementing DMARC is to protect a domain from being used in business email compromise attacks, phishing emails, email scams, and other cyber threat activities.

Once the DMARC DNS entry is published, any receiving email server can authenticate the incoming email based on the instructions published by the domain owner within the DNS entry. If the email passes the authentication, it will be delivered and can be trusted. If the email fails the check, depending on the instructions held within the DMARC record, the email could be delivered, quarantined, or rejected.

DMARC extends two existing mechanisms, **Sender Policy Framework** (SPF) and **DomainKeys Identified Mail** (DKIM). It allows the administrative owner of a domain to publish a policy in their DNS records to specify which mechanism (DKIM, SPF, or both) is employed when sending email from that domain; how to check the _From:_ field presented to end-users; how the receiver should deal with failures - and a reporting mechanism for actions performed under those policies.

### Release

All versions

### Resolution

### ServiceNow's DMARC Policy

The ServiceNow DMARC policy will only apply to emails sent with a _From:_ address that contains the **@service-now.com** domain. Our policy will consist of the following TXT (\_dmarc.service-now.com) record in the service-now.com domain.

_v=DMARC1; p=none; rua=mailto:dmarcaadmin@service-now.com; ruf=mailto:dmarcfadmin@service-now.com; sp=none; fo=1; ri=86400_

### The Policy Explained Field by Field

-   **v=DMARC1;**  
    -   This is the identifier that the receiving server looks for when it is scanning the DNS record for the domain it received the message from. If the domain does not have a TXT record that begins with v=DMARC1, the receiving server will not run a DMARC check.

-   **p=none;**  
    -   This part tells the receiving server what to do with messages that fail DMARC. In this case, the policy is set to "none." This means that the receiving server will take no action if a message fails DMARC. This can still be valuable for a sender, because DMARC sends reports that alert the domain administrator of any DMARC failures

-   **rua=mailto:dmarcaadmin@service-now.com;**  
    -   This part tells the receiving server where to send aggregate reports of DMARC failures. These aggregate reports are sent daily to the administrator of the domain that the DMARC record belongs to. They include high-level information about DMARC failures but do not provide granular detail about each incident. This can be any email address you choose.

-   **ruf=mailto:dmarcfadmin@service-now.com;**   
    -   This portion of the DMARC record tells the receiving server where to send forensic reports of DMARC failures. These forensic reports are sent in real-time to the administrator of the domain that the DMARC record belongs to. These forensic reports contain details about each individual failure. This email address must be from the domain that the DMARC record is published for.

-   **sp=none;**  
    -   This part would tell the receiving server >what DMARC policy to apply to sub-domains.

-   **fo=1;**  
    -   Defines the error reporting policy the sending MTA requests from the receiving MTA.

-   **ri=86400**  
    -   Defines the reporting interval in seconds.

### Upcoming Changes to the DMARC Policy

#### Policy Change from "none" to "quarantine"

-   **Notification**:  On or before February 3rd, 2020, ServiceNow will notify our customers of the policy change from "none" to "quarantine". 
-   **Change:** On April 3rd, 2020, ServiceNow will modify our DMARC policy from "none to "quarantine".

#### Policy Change from "quarantine" to "reject"

-   **Notification**:  On or before April 4th, 2020, ServiceNow will notify our customers of the policy change from "quarantine" to "reject". 
-   **Change:** On June 4th, 2020, ServiceNow will modify our DMARC policy from "quarantine to "reject".

#### What these policy changes mean to our DMARC policy

#### Policy: NONE

-   With NONE, the policy does not dictate any action to the email receiver, so the email is expected to reach the mailbox of the recipient with no modification. This policy is used for reporting how many emails are received without DMARC compliance and from what sources.

#### Policy: **Quarantine**

-   With QUARANTINE, the policy dictates that any non-compliant email (i.e. originating from a source not mentioned in ServiceNow records) should be placed in a special quarantine, such as the junk/spam folder. Depending on the email recipient configuration, other actions, such as modifying the subject of the email with a warning text, may also be configured. Any email received this way should be analyzed by your email administrators to track the origin. 

#### Policy **Reject**

-   With REJECT, the policy dictates that any non-compliant email (i.e. originating from a source not mentioned in ServiceNow records) should be rejected and not delivered to the recipient's mailbox. These emails will be bounced and returned to the sender.

### Related Links

[Indicator templates for controls](https://www.servicenow.com/docs/csh?topicname=indicator-templates-for-ctrls.html&version=latest "Indicator templates for controls")

[KB1709711 - DMARC Policy Enforcement for Inbound Mail](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1709711 "DMARC Policy Enforcement for Inbound Mail")

## Related

- [[KB0695182 - Using DKIM for Emails from the service-now.com Domain]]
- [[KB0725655 - Only ServiceNow Mail Servers are allowed to send emails for service-now.com domain]]
- [[KB0535456 - How to configure Sender Policy Framework (SPF) records for ServiceNow email delivery]]
- [[KB0817647 - Forwarded emails and SPAM SPF_SOFTFAIL or SPF_HARDFAIL]]
