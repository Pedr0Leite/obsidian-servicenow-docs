---
title: "Move scoped application flows to another instance"
aliases:
  - KB0749925
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749925
kb_number: KB0749925
last_modified: 2026-03-30
---

## Move scoped application flows to another instance

  

### Issue

Learn how to create flows and subflows in a scoped application and move them between instances using the ServiceNow application repository. 

### Release

Beginning with the Vancouver release

### Resolution

#### **Create a flow or subflow in a scoped application**

In the source instance:

1.  Go to **ServiceNow** **Studio**, and then open the application you want to edit.
2.  Select **Create**.
3.  For the File Type, select **Automation**, and then choose either **Flow** or **Subflow**.
4.  Select **Continue**.
5.  Enter the flow properties, and then select **Build Flow**.
6.  Add your required parameters, such as trigger or actions.
7.  At the top right, select **Save**. 

#### **Move a flow or subflow to another instance**

Publish the application to the application repository:

1.  Go to **All > System Applications > My Company Applications**.
2.  Open the **In Development** tab.
3.  Open the application record to publish to the application repository.
4.  Select the **Publish to My Application Repository** link.
5.  Select **Submit**.

In the target instance: 

1.  Navigate to Flow Designer.
2.  Select **Flows** or **Subflows**.
3.  Verify your flow or subflow appears in the list.

### Related Links

[Flow Designer](https://docs.servicenow.com/csh?topicname=flow-designer.html&version=latest "Flow designer")

[Publish an application to the application repository](https://docs.servicenow.com/csh?topicname=t_PublishAppsToTheAppRepository.html&version=latest "Publish an application to the application repository")
