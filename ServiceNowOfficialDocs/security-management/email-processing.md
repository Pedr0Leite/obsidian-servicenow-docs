---
title: Security Operations email processing
description: You can set up the integration of information from external detection systems, provide granularity in processing security operations records, handle unmatched emails, and prevent duplication of records using Email Processing.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/email-processing.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-concept
---

# Security Operations email processing

You can set up the integration of information from external detection systems, provide granularity in processing [[security-operations-landing-page|security operations]] records, handle unmatched emails, and prevent duplication of records using Email Processing.

Email Processing consists of these features:

|Feature|Description|
|-------|-----------|
|Email Parsing|Generate new Security Operations records from external system emails.|
|Duplication Rules|Identifies new email with known incidents and processes them appropriately.|
|Properties|Specifies accounts used as input in Email Parsing for security, vulnerability, and IoCs. Provides for granularity in processing Security Operations records.|
|Unmatched Emails|Lists emails that do not match any Security Operations record.|

-   **[[email-properties|Security Operations email properties]]**  
Email Properties specify which inboxes are used as input in Email Parsing to import information from external detection systems to create records for security, vulnerability, and IoCs. You can set up a general account for all external detection systems to use, or individual email accounts for [[sir-landing-page|Security Incident Response]], [[threat-intel-landing-page|Threat Intelligence]], or [[vuln-landing-page|Vulnerability Response]].
-   **[[email-parsing|Security Operations email parsing]]**  
Generate new Security Operations records from external detection systems using Email Parsing. This feature provides a method for integrating information from external [[tools|tools]] such as [[threat-intelligence-malware|malware]] detection, vulnerability detection, firewalls, threat intelligence, and more.
-   **[[umatched-emails|Unmatched Security Operations email events]]**  
Email events that do not match an email parser have their "matched" flag unset. You can view these email event records from the Unmatched Emails list, to reveal external detection systems whose emails are not yet parsed.

**Parent Topic:**[[sec-ops-common-functionality|Security Operations common functionality]]

## Related

- [[email-properties|Security Operations email properties]]
- [[email-parsing|Security Operations email parsing]]
- [[umatched-emails|Unmatched Security Operations email events]]
- [[sec-ops-common-functionality|Security Operations common functionality]]
- [[security-operations-landing-page|Security Operations]]
- [[sir-landing-page|Security Incident Response]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[vuln-landing-page|Vulnerability Response]]
- [[tools|Tools]]
- [[threat-intelligence-malware|Malware]]
