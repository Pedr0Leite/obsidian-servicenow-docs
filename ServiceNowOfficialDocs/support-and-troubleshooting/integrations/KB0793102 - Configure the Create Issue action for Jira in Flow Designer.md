---
title: "Configure the Create Issue action for Jira in Flow Designer"
aliases:
  - KB0793102
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793102
kb_number: KB0793102
last_modified: 2026-01-20
---

## Configure the Create Issue action for Jira in Flow Designer

  

### Summary

This process uses Jira Spoke with Flow Designer to create a Jira issue when a new incident is created in ServiceNow. 

### Release

New York

### Instructions

**Prerequisite**

Install and configure Jira Spoke so that it can be used as part of Flow Designer. See this knowledge article for specific steps: [How to set up Jira Spoke 2.5.1](https://hi.service-now.com/kb_view.do?sysparm_article=KB0792632)

**Configure Flow Designer**

1\. On your ServiceNow instance, go to **Flow Designer** > **Designer** > **Flows** \> **New.**

2\. Create a name for the flow, such as ServiceNow to Jira

3\. Select a trigger for the flow, for example, when an incident is created. 

![Select a trigger for the flow](/sys_attachment.do?sys_id=a27a7579472abe1077748d01426d43b0)

**Configure the action**

1.  Select the **Action** tab.
2.  In the left column, select **Jira**.
3.  From the menu that displays, select **Create Issue**.  
      
    This opens the **Create Issue** dialog box. 

![Select the Action tab. In the left column, select Jira. From the menu that displays, select Create Issue](/sys_attachment.do?sys_id=2e7a7579472abe1077748d01426d43b8)

**Select the Issue settings**

1.  The **Connection Alias** is automatically set to sn\_jira\_spoke.Jira providing Jira Spoke was set up as the prerequisite. 
2.  Select the **Project Key.** This defines in which Jira project the issue is created. The project key comes from the Atlasssian Instance (Jira > Projects). The following image uses the project key Snow-Jira-Test.  
      
    ![Select the Project Key. This defines in which Jira project the issue is created](/sys_attachment.do?sys_id=a67a7579472abe1077748d01426d43c1)  
      
    
3.  From the drop-down list, select the **Issue Type.  
      
    **\- In the default instance, choose from: Ask, Sub-Task, Story, Bug, or Epic.  
    \- If you created custom issue types in Jira, these will display in the list also.   
      
    
4.  Fill in the **Summary**, **Description**, and **Priority** fields (as shown in the following image)
5.  Select **Save**.   
      
    This flow now creates an issue in Jira whenever a new incident is created.  
      
    

![This flow now creates an issue in Jira whenever a new incident is created.](/sys_attachment.do?sys_id=627a7579472abe1077748d01426d43bd)

**Test the issue action**

To do this:

1.  Go to the flow you just created.
2.  Select **Test**.
3.  Select an incident record.
4.  Select **Run Test**.

![Go to the flow you just created. Select Test. Select an incident record. Select Run Test.](/sys_attachment.do?sys_id=ea7a7579472abe1077748d01426d4368)

1.  After the run is complete, under **RUNTIME VALUE**, verify that the correct test name is reflected and that the result shows **Success**. The following image shows a successful test run. 

![After the run is complete, under RUNTIME VALUE, verify that the correct test name is reflected and that the result shows Success](/sys_attachment.do?sys_id=6e7a7579472abe1077748d01426d43ab)

1.  Go to your Atlassian Jira instance. The issue just created is listed under the Project name.

![Go to your Atlassian Jira instance. The issue just created is listed under the Project name.](/sys_attachment.do?sys_id=d67a3579472abe1077748d01426d43a8)
