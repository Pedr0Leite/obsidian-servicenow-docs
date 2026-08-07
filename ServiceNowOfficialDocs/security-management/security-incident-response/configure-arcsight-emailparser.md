---
title: Configure HPE Security ArcSight ESM - Email Parser integration
description: HPE Security ArcSight ESM - Email Parser integration uses email notifications from ESM to drive enrichment, and response workflows.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/security-incident-response/configure-arcsight-emailparser.html
release: australia
product: Security Incident Response
classification: security-incident-response
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [HPE Security ArcSight ESM - Email Parser integration, Security Incident Response integrations, Security Incident Response, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - sir
  - security-incidents
  - investigation
  - soar
  - type-task
---

# Configure HPE Security ArcSight ESM - Email Parser integration

[[arcsight-emailparser-integration|HPE Security ArcSight ESM - Email Parser integration]] uses [[tisc-email-notifications|email notifications]] from ESM to drive enrichment, and response workflows.

## Before you begin

Role required: sn\_si\_admin

## About this task

An HPE Security ArcSight ESM - Email Parser template is provided to use for the integration. It must be configured and activated before the integration takes place. Updating the parser activates it.

## Procedure

1.  Navigate to **All** &gt; **[[security-operations-landing-page|Security Operations]]** &gt; **Integrations** &gt; **Integration Configurations**.

    The available security integrations appear as a series of cards.

2.  In the HPE Security ArcSight ESM - Email Parser card, select **Configure**.

3.  In the **HPE Security ArcSight ESM - Email Parser Configuration** dialog box, select the **Configure Email Parser** link.

4.  Select the **ArcSight ESM** link to edit the settings in the template email parser provided.

    At a minimum, fill in the `Email is from` field. To create you own email parser, see [[parsing-emails|Create email parsers in Security Operations]].

5.  Check the **Active** box.

6.  Select **Update** in the **Email Parser** form.

    The email parser is active. You do not need to return to **Integration Configurations**.

## Related

- [[parsing-emails|Create email parsers in Security Operations]]
- [[arcsight-emailparser-integration|HPE Security ArcSight ESM - Email Parser integration]]
- [[tisc-email-notifications|Email Notifications]]
- [[security-operations-landing-page|Security Operations]]
