---
title: "Actionable notifications sent on MS Teams do not show complete short description and description"
aliases:
  - KB0965008
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0965008
kb_number: KB0965008
last_modified: 2024-05-22
---

## Actionable notifications sent on MS Teams do not show complete short description and description

  

### Issue

Actionable notifications sent on MS Teams do not show complete short description and description also do not have option to scroll and read the complete text. 

  

![](sys_attachment.do?sys_id=15aea2f6db34f01092bb0b55ca96194d)

### Resolution

Review the flow execution context which is responsible to post complete request payload to Adaptive card at MS teams end. Check if the payload is sent correctly. Sample message is below

  

{"type":"message","serviceUrl":"https://teamsproxy.service-now.com//teams/va/outbound/","originServiceUrl":"https://smba.trafficmanager.net/in/","channelData":{"tenant":{"id":"98126b57-e48d-4b10-b98a-6ef20e88d26b"}},"attachments":\[{"contentType":"application/vnd.microsoft.card.adaptive","content":{"$schema":"http://adaptivecards.io/schemas/adaptive-card.json","type":"AdaptiveCard","body":\[{"type":"Container","items":\[{"size":"medium","weight":"bolder","text":"Approval for: https://instancename.service-now.com/nav\_to.do?uri=%2Fproblem.do%3Fsys\_id%3D-1%26sysparm\_stack%3Dproblem\_list.do","type":"TextBlock"},{"maxLines":3,"text":"https://instancename.service-now.com/nav\_to.do?uri=%2Fproblem.do%3Fsys\_id%3D-1%26sysparm\_stack%3Dproblem\_list.do\\r\\nhttps://instancename.service-now.com/nav\_to.do?uri=%2Fproblem.do%3Fsys\_id%3D-1%26sysparm\_stack%3Dproblem\_list.do\\r\\nhttps://instancename.service-now.com/nav\_to.do?uri=%2Fproblem.do%3Fsys\_id%3D-1%26sysparm\_stack%3Dproblem\_list.do\\r\\nhttps://instancename.service-now.com/nav\_to.do?uri=%2Fproblem.do%3Fsys\_id%3D-1%26sysparm\_stack%3Dproblem\_list.do","type":"TextBlock","wrap":true},{"type":"FactSet","facts":\[{"title":"Number","value":"PRB0040005"},{"title":"State","value":"Requested"}\]},{"type":"ActionSet","actions":\[{"type":"Action.OpenUrl","title":"View details","url":"https://instancename.service-now.com/sp?id=approval&table=sysapproval\_approver&sys\_id=851b91501b907010951ac841604bcbaa"}\]}\]},{"type":"Container","items":\[{"text":"Provide a reason for rejections or add approval notes","type":"TextBlock"},{"isRequired":true,"isMultiline":true,"id":"approval\_note","placeholder":"When you reject something, let people know why","type":"Input.Text","maxLength":500},{"type":"ActionSet","actions":\[{"data":{"sysId":"851b91501b907010951ac841604bcbaa","action\_name":"approve","action\_identifier":"com.snc.ms\_teams","action\_handler":"sn\_now\_teams.MSTeamsMessageActionsApprovalHandler","table":"sysapproval\_approver"},"type":"Action.Submit","title":"Approve"},{"data":{"sysId":"851b91501b907010951ac841604bcbaa","action\_name":"reject","action\_identifier":"com.snc.ms\_teams","action\_handler":"sn\_now\_teams.MSTeamsMessageActionsApprovalHandler","table":"sysapproval\_approver"},"type":"Action.Submit","title":"Reject"}\]}\]}\],"version":"1.2"}}\]}

  

The adaptive card is having hard limit with specific size which is restricting the app to populate all the information at MS teams end. The maximum allowed length of MS Teams message is only 28 KB, below are the supporting docs.  
  
[https://docs.microsoft.com/en-us/microsoftteams/limits-specifications-teams#teams-and-channels](https://docs.microsoft.com/en-us/microsoftteams/limits-specifications-teams#teams-and-channels)  
  
[https://github.com/microsoft/BotFramework-Services/issues/228](https://github.com/microsoft/BotFramework-Services/issues/228)
