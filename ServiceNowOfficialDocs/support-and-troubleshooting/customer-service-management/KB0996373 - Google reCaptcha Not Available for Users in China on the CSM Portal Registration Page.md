---
title: "Google reCaptcha Not Available for Users in China on the CSM Portal Registration Page"
aliases:
  - KB0996373
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996373
kb_number: KB0996373
last_modified: 2026-07-02
---

## Google reCaptcha Not Available for Users in China on the CSM Portal Registration Page

  

### Issue

Users based in mainland China encounter issues with the self-registration captcha on the CSM portal registration page. Google reCaptcha is blocked for traffic originating from China, preventing affected users from completing the registration process.

### Release

All

### Cause

Google reCaptcha is not accessible in mainland China due to regional internet restrictions that block Google services. As a result, any CSM portal registration page that relies on Google reCaptcha will fail to load the captcha challenge for users in China, making self-registration unavailable for those users without a workaround.

### Resolution

The following workarounds are available depending on your organization's requirements:

1.  **Disable Google reCaptcha globally** — Set the System Property `sn_customerservice.captchaEnabled` to `false`. This disables reCaptcha for all users globally and removes the captcha requirement from the registration page. Note that disabling captcha has security implications and should be reviewed and approved according to your organization's security governance process.
2.  **Create a separate portal page for users in China** — Create a dedicated portal page or widget for users in China that bypasses Google reCaptcha. This can be done by customizing the existing customer registration widget on the `csm_registration` portal page and configuring it to skip the captcha step for a China-specific portal route.
3.  **Replace Google reCaptcha with a China-accessible alternative** — Replace Google reCaptcha with a China-friendly alternative such as [recaptcha.net](https://www.recaptcha.net). Note that this approach requires reviewing and customizing all related CSM logic that references Google reCaptcha, including Widgets, Script Includes, and System Properties, and may require significant implementation effort.
