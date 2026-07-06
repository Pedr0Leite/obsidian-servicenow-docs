---
title: "Catalog client script is not hiding the container and the variables within the container"
aliases:
  - KB0745114
tags:
  - servicenow
  - support-kb
  - catalog-client-scripts
  - g_form
  - service-catalog
  - variables
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745114
kb_number: KB0745114
last_modified: 2024-04-07
---

## Catalog client script is not hiding the container and the variables within the container

  

### Issue

# Symptoms

Catalog client script is not hiding the container and the variables within the container.

# Release

Any supported release. 

# Cause

There are mandatory variables exists within the container and hence catalog client script is unable to hide the container and variables within it. 

# Resolution

Before hiding container variable with g\_form.setDisplay('variable',false) API, make sure, the mandatory variables within the container are set as non-mandatory via g\_form.setMandatory('variable',false) API.

# Additional Information

[Types of catalog variables](https://docs.servicenow.com/csh?topicname=r_VariableTypes.html&version=latest "Types of catalog variables")

## Related

- [[KB0726412 - Unable to change background color of reference field using g_form.getControl in client script]] - g_form API usage pitfalls
- [[KB0538917 - Determining if client script settings are incorrectly configured]] - broader client-script configuration troubleshooting

