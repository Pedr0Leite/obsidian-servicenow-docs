---
title: Build Agent conversation change log
description: After Build Agent completes the changes you request, you can find information about the updates in the change log that automatically appears in an integrated tab in ServiceNow Studio.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/ba-conversational-change-log.html
release: australia
topic_type: concept
last_updated: "2026-04-02"
reading_time_minutes: 2
keywords: [Now Assist, AI Agents, generative AI, agentic AI]
breadcrumb: [Use, Build Agent, Agentic development on the ServiceNow AI Platform, Building applications]
---

# Build Agent conversation change log

After [[build-agent|Build Agent]] completes the changes you request, you can find information about the updates in the change log that automatically appears in an integrated tab in [[servicenow-studio-landing|ServiceNow Studio]].

Use the conversation change log to do the following actions:

-   View the changes you have made since a checkpoint
-   Roll back changes to the previous checkpoint
-   Approve and deploy changes to an update set

When viewing the conversation change log, you can also view update sets created by Build Agent from within the chat panel. Each checkpoint includes a button that opens the relevant update set in a new tab. For information on how the change log and checkpoints work with update sets, see [[ba-update-sets|Update sets and Build Agent]].

Checkpoints are groups of changes that you have made to an application that you can revert back to at any point during your conversation with Build Agent. Checkpoints are created automatically after you approve each task plan.

\[Omitted image "sn-studio-ba-convo-change-log.png"\] Alt text: The conversational change log shows changes Build Agent has made to an application

The change log displays the following:

1.  The **Files** list displays all the files that Build Agent updated during the course of your conversation.

    These categories mirror the ones in the ServiceNow Studio Navigator panel.

2.  The **Overview** section shows the actions Build Agent took based on the conversation.

    When there are multiple changes and checkpoints for the app, you can see a file diff viewer with precise changes.

3.  The menu at the top shows the checkpoint you're in. You can use the drop-down list at the end of the checkpoint name to select a different checkpoint to view.

    When there are multiple checkpoints, a **Summary** option appears, which shows changes from each checkpoint all together.

4.  In the corner, you can take actions by reopening the chat, restoring your app to a previous checkpoint, or opening the [[app-details-page|app details page]] for the app you're working in.

Changes from each checkpoint in the conversation are packaged together into an update set. You can find each update set on the **[[get-started-deployment|Deployment]]** tab on the ServiceNow Studio home page. For more information on deployment, see [[build-agent-deployment|Deploying what you built with Build Agent]].

**Parent Topic:**[[use-build-agent|Use Build Agent]]

## Related

- [[ba-update-sets|Update sets and Build Agent]]
- [[build-agent-deployment|Deploying what you built with Build Agent]]
- [[use-build-agent|Use Build Agent]]
- [[build-agent|Build Agent]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[app-details-page|App details page]]
- [[get-started-deployment|Deployment]]
