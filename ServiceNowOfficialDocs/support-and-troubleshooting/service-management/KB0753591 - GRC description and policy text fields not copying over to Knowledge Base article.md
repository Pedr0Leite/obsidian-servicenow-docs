---
title: "GRC  description and policy text fields not copying over to Knowledge Base article"
aliases:
  - KB0753591
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753591
kb_number: KB0753591
last_modified: 2024-04-07
---

## GRC description and policy text fields not copying over to Knowledge Base article

  

### Issue

The issue is caused by using single quotes in article body. Please find the sample text statement:

<table style="border-collapse: collapse; width: 100%; height: 191px;" border="1"><tbody><tr><td style="width: 100%;"><em>To ensure information security events and weaknesses associated with information systems are communicated in a manner allowing timely corrective action to be taken, all employees, contractors and third-party users should be made aware of the procedures for reporting the different types of events and weaknesses that might have an impact on the security of organizational assets.</em><br><br><br><em>Information Security is responsible for monitoring the incident response program and offering suggestions for enhancements when necessary.</em><br><br><em>Incident Response Plan</em><br><br><em>A documented Incident Response Plan and procedures shall be in place to report security incidents or system malfunctions to management.</em><br><br><em>Reporting Information Security Events and Weaknesses</em><br><br><em>All Denny’s personnel and related third parties are required to note and report any observed or suspected security issues, potential incidents, or weaknesses in systems or services to Information Security.</em><br><br><em>User Responsibility Discovering Weaknesses</em><br><br><em>Denny’s personnel should not attempt to prove suspected security weaknesses. Testing weaknesses, with the exception of items approved by IT Management, might be interpreted as a potential misuse of the system and could also cause damage to the information system or services.</em></td></tr></tbody></table>

Scenario:

1.  Navigate to any published policy   
      
    2\. Once it is published, it should create a kb article, with the content, however, it is creating the article but the article body is empty. 

### Cause

It is the single quote (Denny's) in the policy text that is causing the problem. The property glide.html.sanitize\_all\_fields property is missing in the instance.

### Resolution

Once the glide.html.sanitize\_all\_fields property is created with value "**true**" the issue is solved.

### Related Links

[Available system properties London](https://docs.servicenow.com/csh?topicname=r_AvailableSystemProperties.html&version=latest "Available system properties London") 

Also additionally, If you have the glide.html.sanitize\_all\_fields property set to true, then create a policy with policy text having a single table cell, then view xml, you can see the policy\_text field has this data,  
  
"<!\[CDATA\[  
<table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr><td style="width: 100%;"> </td></tr></tbody></table>  
\]\]>"  
  
now if you set this property to false, create a policy with policy text having a single table cell, when you view xml, you see this,  
  
"<!\[CDATA\[  
<table style="border-collapse: collapse; width: 100%;" border="1"> <tbody> <tr> <td style="width: 100%;">&nbsp;</td> </tr> </tbody> </table>  
\]\]>"  
  
It looks like with glide.html.sanitize\_all\_fields set to false, the policy text field has an extra "&nbsp;", which cause error when we call the GlideJellyRunner script.  
  
I noticed that there's another property glide.translated\_html.sanitize\_all\_fields, properly for translated html fields.
