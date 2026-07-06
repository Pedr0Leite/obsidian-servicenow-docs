---
title: "How to set Event Rule regex expression to be case-insensitive for Event Management"
aliases:
  - KB0749814
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749814
kb_number: KB0749814
last_modified: 2024-04-07
---

## How to set Event Rule regex expression to be case-insensitive for Event Management

  

### Issue

# Description

When configuring Event Rule, to transform information in fields - regex mode, the regex engine is case-sensitive by default.

For example, for string:

Test\[Test\]PRiority:P2\[Test\]

Below filter won't return any result:

.\*Priority:P(\\d).\*

It's necessary to wrap both uppercase and lowercase of each character in square brackets to complete the OR operator. 

For example, for string:

Test\[Test\]PRiority:P2\[Test\]

Below filter will return the number 2:

.\*\[P|p\]\[R|r\]\[I|i\]\[O|o\]\[R|r\]\[I|i\]\[T|t\]\[Y|y\]:P(\\d).\* 

# Applicable Versions

Post London

# Additional Information

[Configure an event rule to customize alert content](https://docs.servicenow.com/csh?topicname=t_EMComposeOuput.html&version=latest "Configure an event rule to customize alert content")
