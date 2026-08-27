---
title: "Add New Plan button not working from Resources Tab in Project Planning Console"
aliases:
  - KB0748874
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748874
kb_number: KB0748874
last_modified: 2024-04-07
---

## Add New Plan button not working from Resources Tab in Project Planning Console

  

### Issue

# Symptoms

  
'Add New Plan' Button not working from Resources in Planning Console.   
When you click the 'Add New Plan' Button in the Resource Finder list to create a new Resource Plan, nothing happens.   
The screen turns white and you see a continuos spinning circle.   
  
In the browser console an error is shown as below   
ERROR:   
  
js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:6283 TypeError: Cannot read property 'resource\_plan\_id' of undefined   
at js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:78398   
at js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:6295   
at r.$eval (js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:6309)   
at r.$digest (js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:6306)   
at r.$apply (js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:6310)   
at g (js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:6263)   
at T (js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:6268)   
at XMLHttpRequest.w.onload (js\_includes\_resource\_planner.jsx?v=04-02-2019\_1803&lp=Thu\_May\_09\_06\_53\_25\_PDT\_2019&c=24\_545:6269) 

TO REPRODUCE:

Open the Project  
Click the related link 'Planning console' on project form  
In planning console, click the 'Resources' tab  
in the resource finder list, you will see the button.

![](sys_attachment.do?sys_id=9b1ce82edb42b450e515c2230596192a)

# Release

London

# Cause

1\. The issue is caused by a custom Business Rule which is aborting the insert of the Resource Plan being created.   
  
2\. During debugging we reviewed the business rules that were executing before insert, see below   
09:56:01.974: Execute before insert business rules on resource\_plan:RPLN0017634 before engines (order <1000)   
business rule09:56:01.976: Global ==> 'Dates validation ' on resource\_plan:RPLN0017634   
business rule09:56:01.976: Global <== 'Dates validation ' on resource\_plan:RPLN0017634   
business rule09:56:01.978: Global ==> 'Check For Resource Based on Type' on resource\_plan:RPLN0017634   
business rule09:56:01.981: Global members\_list: => a67005240a0a8c08010497547966321b,c926d8420a0a8c0801430678b100aeb3,ef6a9032ff9d50445545114e40b9ad38,a670233a0a0a8c08007a182497b5972c   
business rule09:56:01.981: Global <== 'Check For Resource Based on Type' on resource\_plan:RPLN0017634   
business rule09:56:01.981: Global ==> 'Update task fields' on resource\_plan:RPLN0017634   
business rule09:56:01.994: Global <== 'Update task fields' on resource\_plan:RPLN0017634   
business rule09:56:01.994: Global ==> 'Populate planned hours from other types' on resource\_plan:RPLN0017634   
business rule09:56:01.995: Global <== 'Populate planned hours from other types' on resource\_plan:RPLN0017634   
business rule09:56:01.995: Global ==> 'Populate name when empty' on resource\_plan:RPLN0017634   
business rule09:56:01.996: Global short\_description: => RPLN0017634 - Res - Group IT Global Service Management   
business rule09:56:01.996: Global <== 'Populate name when empty' on resource\_plan:RPLN0017634   
business rule09:56:01.997: Global ==> 'Start date must be Sunday' on resource\_plan:RPLN0017634   
log09:56:01.997: Operation against file 'resource\_plan' was aborted by Business Rule 'Start date must be Sunday^86ab2a171b59b340f147c9506e4bcb72'. Business Rule Stack:Start date must be Sunday   
business rule09:56:01.997: Global <== 'Start date must be Sunday' on resource\_plan:RPLN0017634   
business rule09:56:01.997: Finished executing before insert business rules on resource\_plan:RPLN0017634 before engines (order <1000)   
  
3\. No further business rules were processed after the custom BR 'Start date must be Sunday' ran.   
  
4\. BR: Start date must be Sunday. In this BR, the last 2 lines of code are as below   
  
current.start\_date.setError('The Start date must be the starting Sunday of the week');   
current.setAbortAction(true); 

# Resolution

  
Inactivating this custom business rule fixes the issue. I tested this and was able to add new plan using the button. 

Customer was advised to review and revisit this with their developers to verify the Business Rule meets the business requirements.
