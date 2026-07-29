---
title: Build Agent plugins
description: The plugins for Build Agent depend on whether you're using the free/trial version or premium version.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/build-agent-plugins.html
release: australia
topic_type: reference
last_updated: "2026-04-02"
reading_time_minutes: 1
keywords: [Now Assist, AI Agents, generative AI, agentic AI]
breadcrumb: [Configure, Build Agent, Agentic development on the ServiceNow AI Platform, Building applications]
tags:
  - application-development
  - type-reference
---

# Build Agent plugins

The plugins for [[build-agent|Build Agent]] depend on whether you're using the free/trial version or premium version.

Build Agent is available in both [[servicenow-studio-landing|ServiceNow Studio]] and the [[servicenow-ide-landing|ServiceNow IDE]].

**Note:** The trial app was formerly called "Build Agent" and has been renamed to "Build Agent \(Trial\)."

## Plugins for Build Agent \(Trial/free\)

Build Agent is available as a trial app on a freemium model. To install Build Agent \(Trial\), visit the [ServiceNow Store](https://www.servicenow.com/products/vibe-coding.html#benefits).

Two plugins are required:

1.  sn\_glider: the only required plugin for Build Agent in the Australia EA \(Australia patch 0\) version
2.  sn\_build\_agent: required for Australia Patch 1 and onward

## Plugins for Build Agent \(Paid\)

If you exceed the free interaction limit, you must wait 30 days for a reset, or install the paid version of Build Agent. For more information on how to install Build Agent, see [[install-build-agent|Install Build Agent]].

1.  For Australia Patch 1 and onward, the sn\_now\_creator plugin is required, which contains the sn\_build\_agent\_pro plugin.
2.  For the Australia EA \(Australia patch 0\) version, you must manually update ServiceNow Studio and the Unified Developer Core \(UDC\) in the ServiceNow Store before installing [[now-assist-for-creator-landing|Now Assist for Creator]].

**Parent Topic:**[[configure-build-agent|Configure Build Agent]]

## Related

- [[install-build-agent|Install Build Agent]]
- [[configure-build-agent|Configure Build Agent]]
- [[build-agent|Build Agent]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[servicenow-ide-landing|ServiceNow IDE]]
- [[now-assist-for-creator-landing|Now Assist for Creator]]
