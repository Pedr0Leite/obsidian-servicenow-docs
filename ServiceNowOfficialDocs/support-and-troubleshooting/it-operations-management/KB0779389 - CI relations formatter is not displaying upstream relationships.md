---
title: "CI relations formatter is not displaying upstream relationships"
aliases:
  - KB0779389
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779389
kb_number: KB0779389
last_modified: 2025-04-08
---

## Issue

-   Relationships are present in cmdb\_rel\_ci table but are not visible in "upstream" relationships under relationship formatter.

![](sys_attachment.do?sys_id=c8bd8b74dbc434d0471f9c41ba961928)

-   cmdb\_rel\_ci showing the relationships:

![](sys_attachment.do?sys_id=44bd8b74dbc434d0471f9c41ba961927)

-   The above example, the table has almost 16 entries matching the filter criteria and all the 16 relationships are expected under the relationship formatter.

## Resolution

-   Please delete the orphan records manually or refer to the below script to delete the records.

var gr = new GlideRecord('cmdb\_rel\_ci');  
gr.addEncodedQuery('parent.sys\_class\_path=NULL^ORchild.sys\_class\_path=NULL^ORtype.parent\_descriptor=NULL^ORtype.child\_descriptor=NULL');  
gr.deleteMultiple(); 

-   **Note: Above script will delete data and need to be tested/verfied by SME before using.**

## Additional Information

Please reach out to [Technical Support](http://www.servicenow.com/support/contact-support.html "Technical Support") if there are any questions.
