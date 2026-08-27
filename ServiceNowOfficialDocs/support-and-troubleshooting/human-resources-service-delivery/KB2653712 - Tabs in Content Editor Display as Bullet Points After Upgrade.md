---
title: "Tabs in Content Editor Display as Bullet Points After Upgrade"
aliases:
  - KB2653712
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2653712
kb_number: KB2653712
last_modified: 2025-12-17
---

## Tabs in Content Editor Display as Bullet Points After Upgrade

  

### Issue

After upgrading to Content Experience 32.0.5 and Content Publishing 33.0.9, the Tabs feature in the Content Editor no longer displays as horizontal tabs across the top, but instead appears as bullet points similar to Lists and Accordions.

### Release

Any

### Cause

The issue occurs when the Portal Preview → Service Portal URL suffix property does not match the actual portal suffix. This mismatch prevents required CSS files (e.g., `sc-bootstrap.scss`, `rce-canvas.css`) from loading, causing incorrect rendering of tabs.

### Resolution

-   Verify the Service Portal URL suffix property under Portal Preview settings.
-   Update the property to match the actual portal suffix used in the environment (e.g., `/escdevonly`, `/escuatonly`).
-   After correcting the property, clear cache and reload the portal to ensure CSS files load correctly.
-   Confirm that tabs render as expected after the update.
