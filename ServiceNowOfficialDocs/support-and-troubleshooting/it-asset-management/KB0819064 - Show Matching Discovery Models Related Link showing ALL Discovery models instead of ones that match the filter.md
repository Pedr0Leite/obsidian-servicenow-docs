---
title: "\"Show Matching Discovery Models\" Related Link showing ALL Discovery models instead of ones that match the filter"
aliases:
  - KB0819064
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819064
kb_number: KB0819064
last_modified: 2024-04-08
---

## Issue

In order to match a software package which was found by discovery with a software model that you generate, you will need to define his software model so that it matches the the discovery models of their installs.

You can verify what discovery models will be picked up by their software model by clicking the link "Show Matching Discovery Models" in the Related Links section.

However, when doing triggering this action, the URL does not show any filter query being performed and instead of providing a list of matching Discovery Models, we get a list of ALL the Discovery Models.

## Resolution

To resolve this, please add the relevant fields which are retrieved from the script of the UI Action to the Form. 

Out of the Box, all these fields should be present on the form.

To do this, go on the Software Model, click on the Burger Icon on the left handside and go on Configure > Form Layout
