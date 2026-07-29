---
title: "Form sections do not display as expected"
aliases:
  - KB0714803
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714803
kb_number: KB0714803
last_modified: 2024-04-18
---

## Form sections do not display as expected

  

### Issue

# Symptoms

* * *

Customer expects a form section to display from a UI action/script but it does not.

Script is using g\_form\_getSections()

#   

  
  

# Resolution

* * *

The customer had changed the form sections between environments. When referring to sections such as sections\[4\].style.display they are purely numerical and reordering form sections will cause irregular behavior. In this case a different tab would appear.

#
