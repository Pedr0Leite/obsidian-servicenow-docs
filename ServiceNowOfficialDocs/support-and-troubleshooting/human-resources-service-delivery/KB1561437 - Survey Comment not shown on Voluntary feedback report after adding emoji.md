---
title: "Survey Comment not shown on Voluntary feedback report after adding emoji"
aliases:
  - KB1561437
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1561437
kb_number: KB1561437
last_modified: 2026-03-25
---

## Survey Comment not shown on Voluntary feedback report after adding emoji

  

### Issue

The customer reported that when adding emoji in the Voluntary survey, the comments stopped showing in the Voluntary Feedback Report

**Steps to Reproduce:**

_Pre-requisite:_

a. Install the latest version of Listening Posts (sn\_lp)

b. Activate voluntary survey: Listening Posts > Voluntary feedback > Voluntary survey

_Actual Steps:_

1\. Navigate to Employee Center Portal: [https://\[instance-name\].service-now.com/esc](https://[instance-name].service-now.com/esc)

2\. Click Give Feedback

![](/sys_attachment.do?sys_id=740e8bfe93823954f2167de86cba10a7 "Screenshot 2023-10-27 at 8.45.18 am.png")

3\. Select either

a. I like something

b. I don't like something

c. I have a suggestion

4\. Enter any emoji in the field "What would you like to tell us"

5\. Click Submit button

6\. Go back to the platform and navigate to Listening Posts > Voluntary feedback > Voluntary feedback report

**Expected Result:** View comment total will display and all the comments will will display

**Actual Result:** View comment is displaying as View Comments ({0}) and no comment displays

### Release

All release

### Cause

The issue was caused by the property "glide.util.xml.transformer.handle.utf16\_surrogate\_pairs" did not exist on the instance.

This property was introduced in Paris as part of PRB1385542, ONLY for new instances. Hence, instances that were provisioned before Paris would not have this property. 

### Resolution

Importing the property [glide.util.xml.transformer.handle.utf16\_surrogate\_pairs](sys_attachment.do?sys_id=780e8bfe93823954f2167de86cba10aa) will fix the issue.
