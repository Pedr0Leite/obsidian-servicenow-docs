---
title: "Populating custom fields in Jira from ServiceNow - Flow Designer  Outbound"
aliases:
  - KB0815305
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815305
kb_number: KB0815305
last_modified: 2025-01-10
---

## Populating custom fields in Jira from ServiceNow - Flow Designer Outbound

  

### Issue

You would like to create a custom field in Jira and you would like that records coming from ServiceNow will populate this custom field.  
  
This article will show how to create a custom field in Jira and how to create a record from ServiceNow to Jira containing this custom field.

### Release

London onwards

### Resolution

For this scenario we will use the "Create Issue Action" for Jira.  
  
For the steps on how to perform this action please follow the articles: 

-   [How to set up Jira Spoke 2.5.1](https://support.servicenow.com/kb_view.do?sysparm_article=KB0792632 "How to set up Jira Spoke 2.5.1")
-   [How to Configure the Create Issue Action for Jira in Flow Designer](https://support.servicenow.com/kb_view.do?sysparm_article=KB0793102 "How to Configure the Create Issue Action for Jira in Flow Designer")

Steps for creating a custom field in Jira instance:  
  
1\. Click on the "Settings" button

![](/sys_attachment.do?sys_id=75e46978db497410471f9c41ba96197f)

2\. Here click "Issues"

![](/sys_attachment.do?sys_id=7de46978db497410471f9c41ba961982)

3\. Then click "Custom Fields"

![](/sys_attachment.do?sys_id=f1e46978db497410471f9c41ba96199f)

4\. Then click "Create Custom field"

![](/sys_attachment.do?sys_id=7de46978db497410471f9c41ba96197b)

5\. Select "Text Field (Multiline)

6\. Press Next.  
7\. Give it a name  
8\. Press "Create"  
9\. Select the screens (see example)

![](/sys_attachment.do?sys_id=71e46978db497410471f9c41ba96197a)

10.Press Update  
  
11\. Now test your field:  
  
12\. Click on the "Create" button

![](/sys_attachment.do?sys_id=f9e46978db497410471f9c41ba96195d)

13\. If your field does not appear in the form, make sure it is selected in the "Configure fields"

![](/sys_attachment.do?sys_id=79e46978db497410471f9c41ba96197d)

14\. Press "Create" or Cancel.

**In the next steps we will look at the way we populate this field, when creating a record from ServiceNow to Jira.**  
1\. Follow the steps for "Create Issue" exemplified in the above article, and make sure you add your custom field in the Additional Fields section

![](/sys_attachment.do?sys_id=79e46978db497410471f9c41ba961984)

2\. Press "Test".  
  
3\. Make sure the test ran successfully.  
  
4\. Check Jira and make sure your record has been created, with the custom field populated as in the image below:  
  
![](/sys_attachment.do?sys_id=71e46978db497410471f9c41ba961981)
