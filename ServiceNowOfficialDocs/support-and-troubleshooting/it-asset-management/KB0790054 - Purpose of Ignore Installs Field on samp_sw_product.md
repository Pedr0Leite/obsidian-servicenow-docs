---
title: "Purpose of Ignore Installs Field on samp_sw_product"
aliases:
  - KB0790054
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790054
kb_number: KB0790054
last_modified: 2024-04-08
---

## Issue

There is an ignore installs field on the samp\_sw\_product and the samp\_custom\_sw\_product tables. This article provides some background on the use of this field.

## Resolution

1) The main purpose of the ignore installs field is that based on the field we determine if we need to populate the normalized product attribute on the software installation records which is used for reconciliation purposes.  
  
2) If the ignore installs is set to false on the software product record, we populate the normalized product attribute on the software installation record.  
  
3) If the ignore installs is set to true, we do not populate the normalized product on the software installation record.  
  
4) Additionally, if the ignore installs is true, we cannot see the show matching discovery model UI action on the Software model record  
  
  
5) Below are the business rules which use the ignore\_installs field :  
  
https://<Instance\_name>.service-now.com/sys\_script\_list.do?sysparm\_query=sys\_idIN9ec2b34d37101000deeabfc8bcbe5d43,ba0b3db20b7222005b38650d37673aaa,bd6141ed73231300278a97f8faf6a7ed  
  
  
6) Below are the script includes which use the ignore\_installs field :  
  
[https://<Instance\_name](https://\<Instance)\>.service-now.com/sys\_script\_include\_list.do?sysparm\_query=sys\_idIN1a16787b73631300278a97f8faf6a788,1cfa67f587602300ede6f64936cb0b39,30bbdf9587f52300923aa75fe5cb0b97,33aa34170b3022002d53650d37673a5b,6761b0dd0b1232001a17650d37673a77,f238a9387f012200fa0d328c4efa914a
