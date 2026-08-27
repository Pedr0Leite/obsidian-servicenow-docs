---
title: "Unable to see clickable links in survey questions"
aliases:
  - KB0852180
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852180
kb_number: KB0852180
last_modified: 2024-04-08
---

## Unable to see clickable links in survey questions

  

### Issue

Is it possible to add a clickable link to a survey question?

### Cause

No Out Of Box functionality exists in survey designer to create hyperlinks as part of a question.

### Resolution

Here are the other options and the steps for each:

I. Create the hyperlink in the Introduction of the survey.

1\. On the survey definition record, click on the 'Insert/Edit link' button in the editor:

![InsertLink](sys_attachment.do?sys_id=a1c47c45dbc0b0905a959c41ba961994 "InsertLink")

  

2\. In the dialog box, fill in the fields. **NOTE: Please have the TARGET field has a new window(\_blank) to avoid surveys being stuck or corrupted.** 

**![](sys_attachment.do?sys_id=29c47c45dbc0b0905a959c41ba961995)**

  

3\. After clicking the Ok button, it should look like this:

![](sys_attachment.do?sys_id=2dc47c45dbc0b0905a959c41ba9619af)

  

II. The second option is to add the URL to the Details field of the question.

1\. Open the survey in Survey Designer

2\. Click on the cog of the question to edit the Properties

3\. In the Details field, add the URL:

![](sys_attachment.do?sys_id=a1c47c45dbc0b0905a959c41ba9619b1)

4\. After exiting out of Properties, it should look like this:

![](sys_attachment.do?sys_id=2dc47c45dbc0b0905a959c41ba961992)

  

  

Here is a screenshot of how the survey will look to the user when both options have been applied to the survey. Please note that this has only been tested on the platform UI.

![](sys_attachment.do?sys_id=29c47c45dbc0b0905a959c41ba9619b2)
