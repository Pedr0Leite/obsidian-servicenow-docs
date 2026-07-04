---
title: "Need Complete elaboration on My List on CSM portal."
aliases:
  - KB0992695
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0992695
kb_number: KB0992695
last_modified: 2024-08-28
---

## Issue

  
1) Agent can see all the cases that has been created so far if he visits the /CSM portal(through MY List).  
  
2) External users can only see the cases submitted by them or opened on behalf of them(through MY List).  
  
3)The Number in my cases and all cases are same . we want to understand more on this.  
  
4) It is a question by us, Will "All Cases " in My cases would also reflect the cases based on Account.

For Ex:- I belong to a team who has three members and each one has submitted a case .  
So if i will login to CSM portal , will that be a case,  
where in "All Cases" I will get the total number ticket opened for the Account and in "My Cases " i will see only one case since i have submitted it.  
  

## Resolution

1) Agent can see all the cases that has been created so far if he visits the /CSM portal(through MY List) ?

**Answer :** Its not a good use case(scenario), agent will not go to portal unless having proxy roles

Read more here - [https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/concept/employee-create-case-for-customer.html](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/concept/employee-create-case-for-customer.html)  
and what agent does here - [https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/reference/r\_RolesInstalledWithCustomerService.html](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/reference/r_RolesInstalledWithCustomerService.html)

2) External users can only see the cases submitted by them or opened on behalf of them(through MY List).

**Ans:** Yes, check roles details here and what all can be seen - [https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/reference/r\_RolesInstalledWithCustomerService.html](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/customer-service-management/reference/r_RolesInstalledWithCustomerService.html)

3)The Number in my cases and all cases are same . we want to understand more on this.

**Ans :** No, assign case manager and case admin role and difference will shown when viewing only as customer role

4) It is a question by us, Will "All Cases " in My cases would also reflect the cases based on Account.  
For Ex:- I belong to a team who has three members and each one has submitted a case .  
So if i will login to CSM portal , will that be a case,  
where in "All Cases" I will get the total number ticket opened for the Account and in "My Cases " i will see only one case since i have submitted it.

**Ans :** Yes

**I would suggest for better understanding , play around with case manager and case admin roles to see differences**

**Note :** If a case has request as well with it then all cases will show cases and requests both  
but My list only cases  
my requests only requests
