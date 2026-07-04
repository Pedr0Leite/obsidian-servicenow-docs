---
title: "After external user completes registration by clicking \"Register Now\", there is no 'Login' option available on the VAM portal for the user to login"
aliases:
  - KB0953121
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953121
kb_number: KB0953121
last_modified: 2024-01-11
---

## After external user completes registration by clicking "Register Now", there is no 'Login' option available on the VAM portal for the user to login

  

### Issue

In VAM portal, after user completes the registration by clicking "Register Now" there is no 'Login' option available for the user to login back. On the Registration Page there is a login link that says "Already have an account?", however, when this link is clicked it brings you back to the portal home page where there is still only "Register Now" link.

### Cause

VAM portal uses 'La Jolla'  theme which was missing in the instance. Because of which 'Login' is missing on the home page.

### Resolution

Go to VAM portal record -> /sp\_portal.do?sys\_id=903eb8e553212010733addeeff7b1246

Ensure Theme is set to 'La Jolla'
