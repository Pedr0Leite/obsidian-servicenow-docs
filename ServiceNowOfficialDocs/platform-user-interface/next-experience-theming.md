---
title: Working with themes in Next Experience
description: Themes enable you to tailor the visual experience for your users, helping to update the look and feel to be more like your brand.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-user-interface/next-experience-theming.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Configure, Next Experience UI, Configure UIs and portals, Configure user experiences]
tags:
  - platform-user-interface
  - type-concept
---

# Working with themes in Next Experience

Themes enable you to tailor the visual experience for your users, helping to update the look and feel to be more like your brand.

Quickly create, edit, preview, and publish themes to your experiences using Theme Builder. See [[configuring-next-experience-with-theme-builder|Configure Next Experience with Theme Builder]] for more information.

**Important:** Theming applies to the classic environment in [[lists-configurable-workspace|Lists]], [[form-configurable-workspace|Forms]], and Dashboards. Custom components don't reflect theming.

## Theming at a glance

-   Theming is the ability to customize the Next Experience Design System to reflect your product or brand.
-   Theming means styling various aspects of the ServiceNow® platform while maintaining the overall look and feel.
-   Theming typically involves changing the colors to your company brand colors but can also include typography, imagery, shape and form.

## Next Experience default themes

New customers launching on Zurich will have the Next Experience Coral theme enabled by default on their instance.

Existing customers upgrading from a previous release will continue to see the theme they've applied to their instance prior to upgrade, for example the Next Experience Polaris theme or a theme created in Theme Builder. Use [[tb-apply-theme|Theme Builder to publish Coral theme to your instance]] or [[configure-presentation-order-of-themes|add Coral theme to the Next Experience UX Parent App Theme table.]]

\[Omitted image "next-exp-coral-polaris.png"\] Alt text: Theme preference with Polaris and Coral themes displayed.

\[Omitted image "next-exp-coral-record-light.png"\] Alt text: Record page with Coral theme light variant applied.

\[Omitted image "next-exp-coral-record-dark.png"\] Alt text: Record page with Coral theme dark variant applied.

## Theme record

This image shows the default Polaris theme, which is read-only. You create your own themes and styles to be used by experiences in your instance by either cloning the Polaris or Coral theme or [[create-custom-theme-using-theme-builder-record|by cloning a Theme Builder theme record]]. If you clone either the Polaris or Coral theme, you also must clone the styles under UX Theme Styles and make changes to those styles, as desired. At least one Core type style must be defined.

\[Omitted image "comp-theme-overview.png"\] Alt text: Next Experience Polaris UX theme main record with Applicability, Order, Style and Type columns highlighted

## Theme styles

You can [[configure-onboarding-modals|configure]] a theme to match your company brand look and feel in ServiceNow. When you configure a theme, you adjust the color schemes, fonts, and images of your applications. On the Theme Builder Theme form, you configure Order, Style, and Type settings.

-   **Order**

    Style records with higher-order values override styles with lower values. The base system styles all have the order 0. If you meet the Applicability constraint, styles with higher values override the base system styles. If not, the lower-value style is used.

-   **Style**

    Style records define reusable styles that together comprise a theme. Core styles include color, shape and form, typography, and imagery. Variants are a different version of the theme, commonly different colors, that users can select in preferences. The most common use of variants is for accessibility purposes, particularly to account for color blindness. If you decide to use a dark theme, consider selecting the Polaris or Coral theme or [[tb-edit-color-palette|create a dark alternate color palette in Theme Builder]].

-   **Type**

    Styles can be of either the Core type or the Variant type. Core styles are active by default. Users can choose from available variants from their Theme user preference, and those variant styles override the core style. Theme Builder doesn’t automatically generate dark theme variants; however, you can create a dark alternate color palette with limited customization. For more information, see [Add an alternate color palette](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/tb-edit-color-palette.md). The Polaris and Coral themes include a Dark Theme variant that is available on instances with Next Experience enabled.


-   **[[guided-tours-theme-builder|Guided tours in Theme Builder]]**  
Learn about Theme Builder [[guided-tours|guided tours]], including how to access and take them to build your knowledge of Theme Builder.
-   **[[dark-mode-theme-builder|Dark mode in Theme Builder]]**  
Learn how to switch to dark mode in Theme Builder.
-   **[[theme-builder-get-help-now|Get help with Theme Builder]]**  
To get help with Theme Builder, your ServiceNow instance, plugins, permissions, and more, watch a short video to contact the ServiceNow admin who works in your company.
-   **[Configuring Next Experience with Theme Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/configuring-next-experience-with-theme-builder.md)**  
Reflect your company's brand on your ServiceNow instance by managing, editing, and implementing Next Experience themes in an easy, efficient, and upgrade-safe way using Theme Builder. Theme Builder is included as a core plugin with the Next Experience and is available by default.
-   **[[tb-working-in-dark-theme|Working with the dark theme]]**  
The dark theme emits less blue light, making the display easier for your eyes and less disturbing in low-light settings. The dark theme is supported for configurable workspaces, lists, forms, dashboards, and reports.
-   **[[themeable-empty-state-images|Working with theme-able empty state images]]**  
Add theme-able empty state images to customize empty states and improve the user experience. Empty states include guidance or actions for users to add or create content.
-   **[[config-next-experience-themes-prefs|Configuring Next Experience themes and preferences]]**  
Theming in Next Experience applies to individual experiences. As an admin user, you can configure the variables for colors, shapes, fonts, and other aspects of the user experience.
-   **[[edit-login-features-u-n|Configure login theming in Next Experience]]**  
Configure Next Experience login illustrations and welcome text to provide a login experience that reflects your branding.
-   **[[customize-login-background|Customize the Next Experience login background illustration]]**  
Customize and change the background illustration applied to your Next Experience login page.
-   **[[customize-ne-login-background-color|Customize the Next Experience login background color]]**  
Customize and change the background color applied to your Next Experience login page.
-   **[[remove-gradient-from-login-page|Remove the gradient from the Next Experience login page]]**  
Remove the gradient from the Next Experience login page and restore the solid color of your default theme.

**Parent Topic:**[[next-experience-ui-admin|Configuring the Next Experience UI]]

## Related

- [[configuring-next-experience-with-theme-builder|Configuring Next Experience with Theme Builder]]
- [[tb-apply-theme|Publish your themes with Theme Builder]]
- [[configure-presentation-order-of-themes|Publish multiple themes in Next Experience]]
- [[create-custom-theme-using-theme-builder-record|Create a custom theme by cloning a Theme Builder theme record]]
- [[tb-edit-color-palette|Add an alternate color palette]]
- [[guided-tours-theme-builder|Guided tours in Theme Builder]]
- [[dark-mode-theme-builder|Dark mode in Theme Builder]]
- [[theme-builder-get-help-now|Get help with Theme Builder]]
- [[tb-working-in-dark-theme|Working with the dark theme]]
- [[themeable-empty-state-images|Working with theme-able empty state images]]
- [[config-next-experience-themes-prefs|Configuring Next Experience themes and preferences]]
- [[edit-login-features-u-n|Configure login theming in Next Experience]]
- [[customize-login-background|Customize the Next Experience login background illustration]]
- [[customize-ne-login-background-color|Customize the Next Experience login background color]]
- [[remove-gradient-from-login-page|Remove the gradient from the Next Experience login page]]
- [[next-experience-ui-admin|Configuring the Next Experience UI]]
- [[lists-configurable-workspace|Lists]]
- [[form-configurable-workspace|Forms]]
- [[configure-onboarding-modals|Configure]]
- [[guided-tours|Guided Tours]]
