---
title: "Product Setups for Microsoft Windows Server License Management Guided Setup page does not load completely"
aliases:
  - KB2574852
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2574852
kb_number: KB2574852
last_modified: 2025-11-27
---

## Product Setups for Microsoft Windows Server License Management Guided Setup page does not load completely

  

### Issue

SAM Workspace - Success Portal - Product Setups for Microsoft Windows Server License Management Guided Setup page not loading completely.

## Steps to Reproduce:

1\. Navigate to Workspaces > Software Asset Workspace > Success portal.  
2\. Select the Product Setups tab.  
3\. Select Microsoft Windows Server > Resume.  
4\. Click on "Prerequisites" and switch it to "Software Asset Management Configuration"  
5\. Click on View CAL or Add CAL

### Release

Yokohama

### Cause

This is happening because of the UI experience. If you switch to Next experience and launch the same guided setup, it works. Looks like the iframe does not support the UI without Next Experience. The URL used there redirects to nav\_to.do which might be causing the issue in the UI without Next experience turned on.

### Resolution

Switching to Next Experience resolves the issue.
