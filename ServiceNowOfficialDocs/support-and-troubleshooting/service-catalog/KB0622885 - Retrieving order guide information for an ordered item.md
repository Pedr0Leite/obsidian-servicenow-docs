---
title: "Retrieving order guide information for an ordered item"
aliases:
  - KB0622885
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622885
kb_number: KB0622885
last_modified: 2024-04-07
---

## Retrieving order guide information for an ordered item

  

### Issue

Retrieving order guide information for an ordered item | Best Practice

  
  

# Background

* * *

For releases prior to Helsinki, there is no way to determine on a base system whether a requested item was ordered via an order guide. One workaround is to use the current\_guide, current\_guide\_active, current\_guide\_serial values from the sc\_cart record to retrieve the order guide information. On the sc\_cart record, these fields are used internally to facilitate the order guide process: to track the current order guide in use (current\_guide), the current active catalog item (current\_guide\_active), variable values entered for the order guide (current\_guide\_serial) for applying the rule base and cascading variables to catalog items. Once the cart is checked out, these fields are not cleared and still contain values.

If a customization uses the mentioned fields to retrieve the order guide information, an item might incorrectly show that it has been ordered from an order guide. Therefore, using these values is not recommended. 

# Using the order guide field on the sc\_cart\_item and sc\_req\_item record

* * *

Releases from Helsinki onward include a new order\_guide field for the sc\_cart\_item and the requested item (sc\_req\_item) records. This field contains the order guide used to order the catalog item. If empty, the item was not ordered through an order guide. 

Because a request (sc\_request) record may contain requested items ordered through an order guide and not through an order guide, the order guide field is stored in the request item record rather than the request record. 

Because of the existence of this new field, prior customizations on the requested item record to store the requested item are no longer needed for releases from Helsinki onward. If prior customizations store the order guide information on the request record, update the customizations to retrieve order guide information from the order\_guide field of sc\_cart\_item or sc\_req\_item records instead.
