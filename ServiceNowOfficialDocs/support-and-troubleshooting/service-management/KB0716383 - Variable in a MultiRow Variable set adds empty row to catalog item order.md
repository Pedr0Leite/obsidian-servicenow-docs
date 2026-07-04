---
title: "Variable in a MultiRow Variable set adds empty row to catalog item order"
aliases:
  - KB0716383
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716383
kb_number: KB0716383
last_modified: 2024-04-07
---

## Variable in a MultiRow Variable set adds empty row to catalog item order

  

### Issue

The variable in a MultiRow Variable set adds an empty row to catalog item order

Error: 

 js\_includes\_table\_variable.jsx?v=09-11-2018\_1115&lp=Mon\_Aug\_13\_01\_08\_48\_PDT\_2018&c=29\_446:481 Uncaught TypeError: Cannot read property 'value' of undefined 

at e.getJSON (js\_includes\_table\_variable.jsx?v=09-11-2018\_1115&lp=Mon\_Aug\_13\_01\_08\_48\_PDT\_2018&c=29\_446:481) 

at e.serialize (js\_includes\_table\_variable.jsx?v=09-11-2018\_1115&lp=Mon\_Aug\_13\_01\_08\_48\_PDT\_2018&c=29\_446:353) 

at e.\_updateInputElement (js\_includes\_table\_variable.jsx?v=09-11-2018\_1115&lp=Mon\_Aug\_13\_01\_08\_48\_PDT\_2018&c=29\_446:341) 

at e.addRow (js\_includes\_table\_variable.jsx?v=09-11-2018\_1115&lp=Mon\_Aug\_13\_01\_08\_48\_PDT\_2018&c=29\_446:125) 

at saveDialog (catalog\_table\_variable\_dialog.do:442) 

at HTMLButtonElement.onclick (catalog\_table\_variable\_dialog.do:355) 

### Cause

We identified that customer had upgraded and some related macros that are part of plugin com.glideapp.servicecatalog.platform had been skipped during the upgrade 

sys\_ui\_macro\_f58f8ff40a0006d40090120a11a09057 approval\_summarizer\_sc\_req\_item com 

sys\_ui\_macro\_770989b10a0a0b0800b1333d892e2cdd catalog\_item 

sys\_ui\_macro\_da3431b43710300054b6a3549dbe5d4e catalog\_item\_additional\_cats 

### Resolution

Reverting to the Out of the Box System upgrade version for these files fixed this issue
