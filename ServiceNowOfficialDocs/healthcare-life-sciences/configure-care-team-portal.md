---
title: Embedding Care Team Portal in Epic Hyperspace via Hyperdrive
description: Configure the Care Team Portal by embedding it into Epic Hyperspace via Hyperdrive and enabling SMART on FHIR authentication.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/healthcare-life-sciences/configure-care-team-portal.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Care Team Portal, Healthcare Operations, Healthcare and Life Sciences]
tags:
  - healthcare-life-sciences
  - type-concept
---

# Embedding Care Team Portal in Epic Hyperspace via Hyperdrive

Configure the [[care-team-portal-landing|Care Team Portal]] by embedding it into Epic Hyperspace via Hyperdrive and enabling SMART on FHIR authentication.

1.  [[configure-iframe-portal|Configure iFrame embedding for Care Team Portal]]

    For the Care Team Portal to successfully launch in Hyperspace via Hyperdrive, the portal must be configured to work within an iFrame.

2.  [[hcls-cto-enabling-oidc|Enable Multi-Provider SSO for your ServiceNow instance]]

    Ensure that Multiple Provider SSO is enabled and configured correctly for Care Team Portal to authenticate with Epic Hyperspace via Hyperdrive.

3.  [[hco-copy-script-include-global|Copy HCLS Script Includes to Global Scope]]

    Copy the MultiSSO\_OIDC\_CTO and OAuthUtilEpic script includes to the global scope so they are available for later configuration steps.

4.  [[hco-authenticate-portal|In Epic: Build the FHIR App to Authenticate with ServiceNow]]

    Set up your FHIR app in Epic with the correct configurations to allow single sign-on for Epic users to access the Care Team Portal inside Epic Hyperspace via Hyperdrive.

5.  [[create-identity-provider-hco|Create and Configure an Identity Provider in ServiceNow to Authenticate with Epic]]

    Set up and configure an Identity Provider in your ServiceNow instance to authenticate with Epic.

6.  [[hco-configure-epic-integration|In Epic: Configure Epic Hyperspace Integration]]

    Configure the Epic integration records \(FDI, Activity, and Menu\) so that a button in Epic launches the ServiceNow Care Team Portal.

7.  [[hco-update-variables-portal|Capture Additional Data From Epic Within ServiceNow Record Producers]]

    Capture additional data from Epic within ServiceNow record producers by configuring variables that map to the Epic authorization token.

## Related

- [[configure-iframe-portal|Configure iFrame embedding for Care Team Portal]]
- [[hcls-cto-enabling-oidc|Enable Multi-Provider SSO for your ServiceNow instance]]
- [[hco-copy-script-include-global|Copy HCLS Script Includes to Global Scope]]
- [[hco-authenticate-portal|hco authenticate portal]]
- [[create-identity-provider-hco|Create and Configure an Identity Provider in ServiceNow to Authenticate with Epic]]
- [[hco-configure-epic-integration|hco configure epic integration]]
- [[hco-update-variables-portal|Capture Additional Data From Epic Within ServiceNow Record Producers]]
- [[care-team-portal-landing|Care Team Portal]]
