---
title: "Outbound REST message fails due to incorrect escaping in variable substitutions"
aliases:
  - KB0692465
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692465
kb_number: KB0692465
last_modified: 2024-04-07
---

## Outbound REST message fails due to incorrect escaping in variable substitutions

  

### Issue

Variable substitution in outbound REST fails to escape quotes (" ") and incorrectly prints it as " "&quot;" causing the request the fail. 

### Cause

For example, when we have 4 variable substitutions for an outbound REST message with values in quotes (" ").   
The escape type for all these 4 are set to "_**No Escape**_". 

When we click on 'Test', the content is wrong. 

Content when the test run failed:

  

{

"workflowArgs": 

{

"applicationId" : &quot;8a4890db539c40b901539c48a9da000e&quot;, 

"emplId" : &quot;31690&quot;, 

"snTicketId" : &quot;39ff79664fc726001b1ae3414210c70a&quot;,

"accountArgs" : {&quot;Role&quot;: \[&quot;8a4890db542b436301543b69570c4069&quot;\]}

}

}

### Resolution

If the escaping is incorrect for the variable substitutions, you would need to apply the below solution:

**Change the escape type of the affected variable substitutions from "NO ESCAPE" to "ESCAPE XML".** 

Content when the test run is successful: 

  

{

"workflowArgs": 

{

"applicationId" : "8a4890db539c40b901539c48a9da000e", 

"emplId" : "31690", 

"snTicketId" : "39ff79664fc726001b1ae3414210c70a", 

"accountArgs" : {"Role": \["8a4890db542b436301543b69570c4069"\]} 

} 

}
