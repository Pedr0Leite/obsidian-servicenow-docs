---
title: "Make Additional Information Field Mandatory"
aliases:
  - KB0812348
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812348
kb_number: KB0812348
last_modified: 2024-04-08
---

## Make Additional Information Field Mandatory

  

### Issue

You have reported an issue whereby you have created an Incident Resolution User Satisfaction Survey in which you have used image scale to check if the user has Happy, Not Happy or Average response.  
You have also enabled Additional Information Field and named it 'Comments, if Any'.  
  
Your requirement is that - Depending upon the response of the user (let's say user selects Not happy), that field should be made mandatory.  
This is to force user to mention why he is NOT Happy.  
  

Steps to reproduce:  
  
Go to Surveys -- Select 'Incident Resolution User Satisfaction Survey'

\-- Go to Survey Designer

\-- Click on 'Preview' in top right corner dropdown

\-- Select red face image with Not Happy mentioned below it.  
  
  
If we select this image, the 'Comments, if Any:' field should be made Mandatory.

### Cause

The current behavior described is by design.  
I have looked into your issue and determined that this feature is working as intended.  
Unfortunately there is no OOB way to have the 'Additional information label' be a mandatory dependent field.

### Resolution

  
1\. OOB we have provided the means to meet your requirement by adding another Question type for e.g. this could be a string.  
This question can be defined to be dependent upon the selection/s in your image scale question.  
It can also be defined to be mandatory.  
  
The above will meet your requirement and is the standard and expected configuration provided to achieve this.  
  
  
  
2\. For your specific requirement of having the 'Additional information label' be a mandatory dependent field you can raise an enhancement request if you would like this functionality to be added to our product, which will be reviewed by our internal resources.
