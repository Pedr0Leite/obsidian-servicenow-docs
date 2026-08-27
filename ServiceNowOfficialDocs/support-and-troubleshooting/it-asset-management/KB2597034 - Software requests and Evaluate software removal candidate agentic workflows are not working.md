---
title: "Software requests and Evaluate software removal candidate agentic workflows are not working"
aliases:
  - KB2597034
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2597034
kb_number: KB2597034
last_modified: 2025-11-12
---

## Software requests and Evaluate software removal candidate agentic workflows are not working

  

### Issue

After requesting software from a service catalog, the user is expecting the request to be visible in the SAM workspace, but surprisingly, it does not appear in the notifications tab, which can lead to confusion and uncertainty regarding the status of the request.

### Release

Zurich

[https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/sam-workspace-landing.html](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/sam-workspace-landing.html)

### Resolution

New software request -Request \[sc\_request\] - can be viewed in the "Alerts in the Activity center" of the Software Asset Workspace > Software Asset Overview, which serves as a centralized location for tracking and managing software requests.   
\-- These are the Software requests where the request state is pending approval, indicating that they require further review and authorization before proceeding.  
\-- Select to view the software request list in the classic Software Asset Management interface for a more traditional view of the request data.  
  
Find the screenshots below which are taken from our OOB instance, providing a visual representation of the process and outcomes, to help illustrate the steps involved.  
  
 ![](/sys_attachment.do?sys_id=8187adaf47743a10c2488d01426d431d)![](/sys_attachment.do?sys_id=a14725af47743a10c2488d01426d439f)

![](/sys_attachment.do?sys_id=214725af47743a10c2488d01426d43a1)![](/sys_attachment.do?sys_id=e54725af47743a10c2488d01426d43bc)![](/sys_attachment.do?sys_id=654725af47743a10c2488d01426d43be)

  
Do note, if you are requesting a Software catalog item that has a price <= $1000, the request will be automatically approved and will not appear in the "Alerts in the Activity center", as it does not require further approval. In the attached screenshots, I modified the price of the "Acrobat" item to $1001.10.

Following the same steps to reproduce, the request appeared in the "Alerts in the Activity center", demonstrating the system's response to requests with a higher price point.   
  
Refer to documentation for more information on the Software Asset Management workspace and its features.  
https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/sam-workspace-landing.html
