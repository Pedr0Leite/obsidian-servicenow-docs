---
title: "Cloud Template Version is not getting activated"
aliases:
  - KB0778452
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778452
kb_number: KB0778452
last_modified: 2026-05-21
---

## Cloud Template Version is not getting activated

  

### Issue

Cloud Template Versions cannot be activated when there are duplicate parameters under variable sets in the Cloud Catalog item

### Release

Madrid

### Cause

1) When there are duplicate parameters under variable sets in the Cloud catalog item as shown in the screenshot below :

![](sys_attachment.do?sys_id=4de773611b950950d018c8ca234bcb02)

2) We see the below error in the system logs when we are trying to activate the Cloud template versions :

Java.lang.IllegalStateException: Duplicate key CatalogPropertyDTO{id='7dd43ca71b2f7b00e317ea0e6e4bcb81', globalPropertyId='', globalPropertyName='', name='formatter', parameterTypeId='null', parameterTypeName='null', defaultValue='', dataSource='null', dataSourceId='null', policy='', uiDataType='null', uiDataTypeId='20', helpText='', displayName='null', uiGroup='null', displayOrder=35, visibility=true, constraints='null', regex='', opUniqueId='null', stageResOpAttrId='null', bpStageOperationId='null', formBehaviorId='null', formUIGroup='null', stageResourceOpId='', stageResourceOpName='', formUIGroupId='null', mandatory=false, readonly=false, usePoolFilter=false, poolName='', poolId='', filterName='', filterId='', regexError=''} 

### Resolution

Remove the duplicate parameters under the variable sets and you will be able to activate the Cloud Template Version successfully
