---
title: "Configuring Issue ID using a data pill disables the Additional Fields option in Flow Designer for Jira"
aliases:
  - KB0818189
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818189
kb_number: KB0818189
last_modified: 2025-06-27
---

## Configuring Issue ID using a data pill disables the Additional Fields option in Flow Designer for Jira

  

### Issue

Learn how to configure an Update Issue action when using a data pill for the **Issue ID** hides the **Additional Fields** option. If you are using a static Issue ID in Jira, refer to this knowledge article. 

![image1](sys_attachment.do?sys_id=2a44db8b979e66d024a7739c1253af06)

### Release

All

### Resolution

To resolve this, add an action in the flow before the Update Issue action. In this example, the action is called Generate Encoded Query, which is part of Utility Actions Spoke.

1\. Go to Plugins and install Utility Actions Spoke.

![](/sys_attachment.do?sys_id=a244db8b979e66d024a7739c1253af1b)

2\. Once the spoke is installed, go to Flow Designer and create a new flow. 

3\. Create a trigger.

![](/sys_attachment.do?sys_id=3244db8b979e66d024a7739c1253af1d)

4\. Add an action called Generate Encoded Query. 

![](/sys_attachment.do?sys_id=3e44db8b979e66d024a7739c1253af20)

5\. Add the desired field. 

6\. Create an action. For example, Update Issue. 

In this example, the **Issue ID** field uses the data pill: Trigger - Record Created or Updated➛...➛Correlation ID

7\. Drag and drop the Encoded Query, Encoded Query ➛...➛ Encoded Query, into the Additional Fields option.

![](/sys_attachment.do?sys_id=ba44db8b979e66d024a7739c1253af22)

8\. Save and test

### Related Links

[Utility Actions Spoke](https://www.servicenow.com/docs/bundle/yokohama-integrate-applications/page/administer/integrationhub-store-spokes/concept/utilityact-spoke.html)

[Using data pills](https://developer.servicenow.com/dev.do#!/learn/learning-plans/xanadu/servicenow_application_developer/app_store_learnv2_virtualagent_xanadu_using_data_pills)
