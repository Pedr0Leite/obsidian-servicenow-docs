---
title: "Legacy Read ACLs preventing HR agents from viewing fields on HR Cases"
aliases:
  - KB0999321
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999321
kb_number: KB0999321
last_modified: 2025-09-03
---

## Issue

Different fields including Number and State on HR Cases are not visible to the HR agents.

## Resolution

The following OOB **Read ACLs** have Not been shipped OOB since the London release. However, these ACLs were never deleted on existing instances, to avoid causing unexpected behaviour.

If your instance still has such ACLs, they should be deactivated or deleted after thorough testing to make sure that none of your custom functionality is affected:

<table style="border-collapse: collapse; width: 63.6108%; height: 298px;" border="1"><tbody><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;"><strong>Name</strong></td><td style="width: 49.9348%; height: 15.4px;"><strong>Sys_id</strong></td></tr><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;">sn_hr_core_case.assignment_group</td><td style="width: 49.9348%; height: 15.4px;">6fb29497531122003585c3c606dc34a4</td></tr><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;">sn_hr_core_case.collaborators</td><td style="width: 49.9348%; height: 15.4px;">fd2374c50b9332008cd6e7ae37673aec</td></tr><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;">sn_hr_core_case.hr_service</td><td style="width: 49.9348%; height: 15.4px;">efb732b2534132003585c3c606dc3440</td></tr><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;">sn_hr_core_case.number</td><td style="width: 49.9348%; height: 15.4px;">62e2d497531122003585c3c606dc3459</td></tr><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;">sn_hr_core_case.short_description</td><td style="width: 49.9348%; height: 15.4px;">dc03d497531122003585c3c606dc34c1</td></tr><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;">sn_hr_core_case.state</td><td style="width: 49.9348%; height: 15.4px;">330fbaaf531122005a18c3c606dc34bd</td></tr><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;">sn_hr_core_case.subject_person</td><td style="width: 49.9348%; height: 15.4px;">a9f7b2b2534132003585c3c606dc3468</td></tr><tr style="height: 15.4px;"><td style="width: 50.0446%; height: 15.4px;">sn_hr_core_case.sys_updated_on</td><td style="width: 49.9348%; height: 15.4px;">36db3ef6534132003585c3c606dc343b</td></tr></tbody></table>
