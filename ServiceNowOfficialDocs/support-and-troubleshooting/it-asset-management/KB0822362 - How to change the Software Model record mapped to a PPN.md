---
title: "How to change the Software Model record mapped to a PPN "
aliases:
  - KB0822362
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0822362
kb_number: KB0822362
last_modified: 2025-01-03
---

## How to change the Software Model record mapped to a PPN

  

### Summary

This Knowledge article explains how to map a specific PPN to a new Software Model. 

### Release

All Versions

### Instructions

1.  Make sure that the Entitlement Definition (**DMAP**) you want is mapped to the correct PPN in the Product Definition Table _samp\_sw\_product\_definition_
2.  Make sure that the Software Model you want to keep has all the PPN specifications (Edition,Version and Language)
3.  Update the Software Model you want to keep with the needed DMAP. This automatically move the Entitlements, Allocations and published Catalog Item to that Software Model from the unneeded Software Model
4.  You can now delete the unneeded Software Model after deleting the entitlements attached to it.

### Related Links

Please note that the Software model record UI allows the update of the DMAP as long as the new DMAP belongs to the same Software Model Product.
