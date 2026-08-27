---
title: "[SAMP-CDS] Purpose of \"stage_*\" fields on samp_sw_product and possibility of customization"
aliases:
  - KB0852545
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852545
kb_number: KB0852545
last_modified: 2025-01-02
---

## \[SAMP-CDS\] Purpose of "stage\_\*" fields on samp\_sw\_product and possibility of customization

  

### Summary

This article will explain the purpose of different fields _**stage\_\***_ (Like _stage\_categories_, _stage\_description_, etc) on the table _**samp\_sw\_product**_ table. And also the possibility of customization/utilization of them for customizations.

![](/sys_attachment.do?sys_id=2167f801db0878d0fec4fb24399619ea)

**Question #1**: Purpose of fields stage\_\* fields on table samp\_sw\_product?

**Answer**:

Stage\_\* columns were added to Orlando for supporting content updates. These columns are used to store the latest values downloaded from CDS during content download job. There is a job that compares the stage column with the corresponding actual column to figure out if a value has changed for a product. If yes, then the job propagates this change to all the impacted downstream entities and finally copies the value from stage to actual column.  
  
**Question #2**: Can we customize these columns?  

**Answer**:

Stage columns are not supposed to be customized.
