---
title: "\"Changes - Current\" and \"Changes - Planned\" tabs on the event management dashboard"
aliases:
  - KB0750326
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750326
kb_number: KB0750326
last_modified: 2024-04-07
---

## Issue

# Description

This articles explains how to show the "Changes - Current" and "Changes - Planned" tabs on the event management dashboard on individual Service maps as well as explain what data will show up under each tab

# Procedure

1) In order to show the "Changes - Current" and "Changes - Planned" tabs, navigate to event management dashboard and drill down to the individual business service

2) On the top right corner , click on the hamburger icon as shown in the screenshot and enable "Changes - Current" and "Changes - Planned".

![](sys_attachment.do?sys_id=a2a8682edb02b450e515c2230596198c)

  

3) Now coming to the part where what exactly will show up under these tabs :

Changes - Current tab :

This tab will include all the changes corresponding to the CI 's in a business service where the conditions are actual start date will be less than a minute from the current time (the time when you have loaded the map) and has actual end date as empty. 

Changes - Planned tab : 

This tab will include all the changes corresponding to the CI 's in a business service where the conditions are planned start date should be greater than 1 minute from the current time and planned start date should be relatively on or before 7 days from now.

  

## Resolution

All
