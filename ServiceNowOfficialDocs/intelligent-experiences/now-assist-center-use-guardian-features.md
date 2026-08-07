---
title: Use Now Assist Guardian features in Now Assist Center
description: Use Now Assist Guardian features in the Now Assist Center workspace to detect offensive content, prompt injection attacks, and sensitive topics in generative AI interactions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/now-assist-center-use-guardian-features.html
release: australia
topic_type: task
last_updated: "2026-04-09"
reading_time_minutes: 2
keywords: [Now Assist, Now Assist Center, Gen AI, Generative AI]
breadcrumb: [Using other Now Assist applications from Now Assist Center, Use, Now Assist Center, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-task
---

# Use Now Assist Guardian features in Now Assist Center

Use [[platform-now-assist-landing|Now Assist]] Guardian features in the [[now-assist-center-workspace|Now Assist Center workspace]] to detect offensive content, prompt injection attacks, and sensitive topics in generative AI interactions.

## Before you begin

The following applications must be installed before performing this task:

-   [[now-assist-center-landing-page|Now Assist Center]]

    For more information, see [[now-assist-center-install|Confirm installation of Now Assist Center]].

-   Now Assist Admin console

    For more information, see [[install-configure-essential-now-assist-plugins|Install and configure essential Now Assist plugins using Now Assist Center]].


Role required: sn\_na\_center.nac\_admin

## About this task

Follow these steps to use Now Assist Guardian capabilities from Now Assist Center.

Now Assist Guardian provides safety and governance [[controls|controls]] for AI-generated content. It monitors AI interactions for potentially harmful, offensive, or policy-violating content.

In Now Assist Center, the integration of Now Assist Guardian includes multi-tabbing support for working with safety and governance controls without leaving the application context.

For more information on Now Assist Guardian, see [Now Assist Guardian](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/now-assist-guardian.md).

## Procedure

1.  Navigate to **All** &gt; **Now Assist Center** or **Workspaces** &gt; **Now Assist Center**.

2.  Select **Admin** \(\[Omitted image "icon-now-assist-center-nav-admin.png"\] Alt text: Admin icon. \) in the [[now-assist-center-side-navigation-bar|side navigation bar]].

    The Admin tab opens showing Now Assist Admin options.

3.  Select one of the options under **Now Assist Guardian** to configure.

    Now Assist Guardian provides three guardrails. Each guardrail has a different scope.

<table id="choicetable_bs2_qzh_w3c"><thead><tr><th align="left" id="d177991e226">

Guardrail

</th><th align="left" id="d177991e229">

Description

</th></tr></thead><tbody><tr><td id="d177991e235">

**Prompt injection detection**

</td><td>

This guardrail attempts to override LLM instructions or expose restricted information. It applies to all generative AI applications and features.

 Select **Prompt injection** to open the Prompt injection tab.

 For more information on how to configure this guardrail, see [Configure prompt injection attack protection](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/configure-prompt-injection-attack-protection.md).

</td></tr><tr><td id="d177991e260">

**Offensiveness detection**

</td><td>

This guardrail detects offensive or harmful content in AI inputs and outputs. It applies to specific [[now-assist-skills|Now Assist skills]] and workflows.

 Select **Offensiveness** to open the Offensiveness tab.

 For more information on how to configure this guardrail, see [Activate offensiveness protection for generative AI](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/activate-offensiveness-protection-for-generative-ai.md).

</td></tr><tr><td id="d177991e288">

**Sensitive topic filters**

</td><td>

This guardrail filters subjects not suited for AI responses, such as workplace safety or employee compensation. It applies to Virtual Agent conversational skills only \(available for HR Service Delivery and Customer Service Management\).

 Select **Sensitive Filters** to open the Filters tab.

 For more information on how to configure this guardrail, see [Configure sensitive topic filters](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/configure-sensitive-topic-filters.md).

</td></tr></tbody>
</table>
**Parent Topic:**[[now-assist-center-using-other-applications|Using other Now Assist applications and features from Now Assist Center]]

## Related

- [[now-assist-center-install|Confirm installation of Now Assist Center]]
- [[install-configure-essential-now-assist-plugins|Install and configure essential Now Assist plugins using Now Assist Center]]
- [[now-assist-center-using-other-applications|Using other Now Assist applications and features from Now Assist Center]]
- [[platform-now-assist-landing|Now Assist]]
- [[now-assist-center-workspace|Now Assist Center workspace]]
- [[now-assist-center-landing-page|Now Assist Center]]
- [[controls|Controls]]
- [[now-assist-center-side-navigation-bar|Side navigation bar]]
- [[now-assist-skills|Now Assist skills]]
