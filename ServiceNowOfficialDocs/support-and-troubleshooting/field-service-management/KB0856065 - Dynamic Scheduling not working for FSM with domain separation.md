---
title: "Dynamic Scheduling not working for FSM with domain separation"
aliases:
  - KB0856065
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856065
kb_number: KB0856065
last_modified: 2025-01-02
---

## Dynamic Scheduling not working for FSM with domain separation

  

### Summary

The Dispatch Groups are in domain – XYZ The Work Groups are in domain – ABC The locations are in customer domain - Top/ Cust. As soon as we put a customer company against a Work Order, the Dynamic Scheduling does not work due to domain mismatch. However, if we make the domains same for Dispatch Group Work Group and location , the logic works fine. Also note if we keep the company field blank, logic works as well, as there is no domain mismatch.

Business case-  
Customer domain Top/cust needed to be supported by the service provider domain Top/XYZ  
Given the details in the docs, it seems like the dispatch group and the workgroup needs to be in the same domain as the domain of the work order.  
This cant be the case for XYZ as the service providers need to support the customer and they will be in a separate domain.

Steps to reproduce  
Check the domain configuration  
XYZ domain which is the Service Provider domain  
Customer domain which is Cust  
Dispatch groups, workgroup records are in MSP domain that is ABC , and location and company are in Cust

### Related Links

FSM didn't add any specific domain separation and only support basic domain separation, WO is created in the company's domain is how general Domain Separation works. Please check here ([https://docs.servicenow.com/csh?topicname=c\_DomainAssignment.html&version=latest)](https://docs.servicenow.com/csh?topicname=c_DomainAssignment.html&version=latest%29) to see domain assignment.  
  
Since on a WOT record, it can not see the dispatch group from the other domain, that's also an expected behavior or general domain separation. There's some ways list in this Domain Visibility Doc: [https://docs.servicenow.com/csh?topicname=c\_DomainVisibility.html&version=latest](https://docs.servicenow.com/csh?topicname=c_DomainVisibility.html&version=latest)  
We can either use Contains Domain or Visibility Domain, however, Visibility Domain is a user-to-domain relationship and is explicitly granted. For this usecase, I think we can use Contains Domain which is a many-to-many, domain-to-domain relationship. When a domain is selected, you can see the data from that domain and its children. A contains domain lets you relate domains on an as-needed basis, so in this case, the dispatch group's domain should be contained by the customer's domain.
