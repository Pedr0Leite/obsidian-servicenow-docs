---
title: "Not able to authenticate from Agent Mobile App on Android phones using WorkspaceONE browser from Vmware Airwatch"
aliases:
  - KB0792430
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792430
kb_number: KB0792430
last_modified: 2024-04-08
---

## Not able to authenticate from Agent Mobile App on Android phones using WorkspaceONE browser from Vmware Airwatch

  

### Issue

Accessing Servicenow from Mobile Agent on the Vmware Airwatch using WorkspaceONE browser doesn't authenticate or redirect to the SSO authentication page and throws an exception "installation of snapauth plugin is required "

This is observed on fewer versions of the WorkspaceONE browser which are later than 7.9.20 (560) 4.11 version. 

Steps to reproduce:

i) Install Servicenow classic App on Android mobile 

ii)  Open the App on Vmware Airwatch app on your mobile 

iii) Try to login and you will get re-directed to WorkspaceONE browser on the mobile to open Servicenow

iV) This doesn't display the login page instead shows an error "installation of snapauth plugin is required"

Note: issue is NOT observed when you open Servicenow directly from the WorkspaceONE browser instead of the Mobile App. Issue is also restricted to Android Operating Systems

### Release

Madrid Patch 7a

### Cause

The issue is with the version of WorkspaceONE browser with version released after 7.9.20 (560) 4.11 

### Resolution

"Web - Workspace ONE" released a new updated version on Dec 31st 2019, and this version works as expected with the Air watch and should be able to successfully login to Servicenow from Mobile App using WorkspaceONE browser

Please try this newest version of Airwatch Browser: https://play.google.com/store/apps/details?id=com.airwatch.browser
