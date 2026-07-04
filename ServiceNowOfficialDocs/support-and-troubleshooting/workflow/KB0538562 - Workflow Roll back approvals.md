---
title: "Workflow: Roll back approvals "
aliases:
  - KB0538562
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538562
kb_number: KB0538562
last_modified: 2025-11-17
---

## Workflow: Roll back approvals

  

### Issue

**Workflow: Rollback approvals** 

**Summary**

The Workflow Editor allows the designer to roll back the workflow and restarts at different points of a process. 

If there are Approvals in the rollback path, they will be set to **Not Yet Requested**, even if they had been previously approved. 

If the Rollback To Activity transitions directly to an Approval, that approval will be set to **Requested**, even if it has been previously approved.

All activities that are in the **Rollback To** transition path are already executed and in the **Activity History** Related List of the Workflow Context. The status of these activities will be set to **Restarted**.

Once the workflow begins to re-execute from the point of rollback, all the newly executing activities will have an individual record on the **Activity History** Related List. Because of this, it is possible to see the entire execution of the workflow in a linear format using the Timeline feature in the **Workflow Context**.

### Release

### Resolution

   

**ServiceNow approval workflow**

In many business process definitions, approvals are requested before work can be performed. However, approvals can also be requested as work is progressing. In the event that subsequent approvals are rejected or tests or tasks fail, the Workflow Editor offers the Rollback To activity. This Activity allows the process designer to return to an earlier place in a process and restart. The Rollback To Activity will adjust the state of User Approvals and Tasks that are part of a rolled back set of activities.

1\. In the Workflow Editor, click the **Open** button. Find and select the **K14 Rollback Example One** workflow. Your screen should look like this:

![In the Workflow Editor, click the Open button. Find and select the K14 Rollback Example One workflow](sys_attachment.do?sys_id=5ffc1b8193d5ba10057c7de86cba1005)

2\. Select the **Gear Menu > Properties**. Your screen should look like this:

  ![Select the Gear Menu > Properties](sys_attachment.do?sys_id=dbfc1b8193d5ba10057c7de86cba100a)

Notice that this workflow is on the **Change Request** Table**. Change Request** is a Task table. Because this workflow is based on a Task table, there are more approval options that can be included in the workflow. Notice also that this workflow is configured to run only when the Priority field is set to **4 – Low**. 

3\. Close the Workflow Properties window using the X in the upper right-hand corner of the form.

4\. Expand the **Approvals Category** the Activities Tree. 

![Expand the Approvals Category the Activities Tree.](sys_attachment.do?sys_id=effc1b8193d5ba10057c7de86cba10c1)

The new Approval Activities appear in the Activity Tree for Task tables because they rely on columns in the Task table for their execution.

5\. Select the **Gear Menu > Check Out**. The Workflow is now checked out to you and is ready to edit. 

6.  Click the **Rollback To** Activity in the **Approvals** folder.

 ![  Click the Rollback To Activity in the Approvals folder.](sys_attachment.do?sys_id=6bfc1b8193d5ba10057c7de86cba10c5)

8\. Fill out the form as shown: Name: **Approvals Rolled Back**

9\. Click the **Submit** button**.**

10\. Select the **Gear Menu** > **Expand Transitions.**

![Select the Gear Menu > Expand Transitions.](sys_attachment.do?sys_id=63fc1b8193d5ba10057c7de86cba10e2)

11\. On the **Reject Approval Two Log Message** Activity, select the transition from the **Always** node and draw a transition to **Rollback To** Activity.

12\. On the **Rollback To** Activity, select the **Always** node and draw a transition to the **Approval One** Activity.

13\. Arrange the activities so all the transition lines are clear.

![Arrange the activities so all the transition lines are clear.](sys_attachment.do?sys_id=abfc1b8193d5ba10057c7de86cba10e5)

**About the rollback to approval records**

The **Rollback To** Activity will walk back through the executed transitions until it finds the Workflow Activity that the **Rollback To** transition arrow is pointing to.  As the **Rollback To** Activity is walking back through the model, if it encounters an Approval it will set that approval state to **Not Yet Requested** if it is not the Workflow Activity that the **Rollback To** transition is pointing to. Once the approval value is reset, the **Rollback To** Activity will continue back along the transition path until it finds the Activity it is pointing to. If that activity is also an Approval, then that Approval will be set to **Requested.**  These changes of approval state are made directly to the User Approval record in the database. 

 ![About the rollback to approval records](sys_attachment.do?sys_id=e3fc1b8193d5ba10057c7de86cba10e9)

**Rollback to and the executing records** 

If a **Rollback To** is transitioning, all the activities encountered in the **Rollback To** transition have all executed and are stored as Finished in the Activity History Related List of the Workflow Context.  As the **Rollback To Activity** encounters activities, their state in the Activity History Related List of the Workflow Context is set to restart.

1\. Return to the Main tab of the ServiceNow instance.

2. **Change > Create New**.

3\. Right-click in the form header and select **Save**.

4\. With tabs active, scroll down the form and find the **Approvals** Related List. 

![With tabs active, scroll down the form and find the Approvals Related List](sys_attachment.do?sys_id=2bfc1b8193d5ba10057c7de86cba10f9)

5. **Right-Click > Approve**.

![ Right-Click > Approve.](sys_attachment.do?sys_id=e3fc1b8193d5ba10057c7de86cba10fd)

Notice that a second Approval, **K14-Approver Two**, appears in the list. This is the Approval that transitions to the **Rollback To** activity. Let's verify this.

6\. Select **Show Workflow** from the Related Links list.

Your workflow should look like this:

![A second Approval, K14-Approver Two, appears in the list](sys_attachment.do?sys_id=13fc1b8193d5ba10057c7de86cba1066)

The green Activity is the current Activity. Notice the Reject Condition transitions to the Rollback To.

7\. Close the browser tab of the **Workflow Context** view.

8\. Find the **Requested** Approval for the K14 Approver Two in the Related List of the Change Request.

9. **Right-Click > Reject**.

![Right-Click > Reject.](sys_attachment.do?sys_id=17fc1b8193d5ba10057c7de86cba106a)

QUESTION: Why is the state of K14-Approver Two not **Rejected**?

QUESTION: Why is the state of K14-Approver Two not **Requested**?

QUESTION: Why is the state of K14-Approver One **Requested**?

10\. Select **Workflow Context** from the Related Links list.

11\. Select the **Workflow Activity History** Related List.

Your list should look like this:

![Completed correct list](sys_attachment.do?sys_id=1bfc1b8193d5ba10057c7de86cba106e)

Notice the State of some of the Activities is **Restarted**. These restarted Activities are the Activities that were in the transition path between the **Rollback To** Activity and the **Approval One** Activity. To verify this, select the **Show Workflow** link from the Related Links list on the Workflow Context form.

Your workflow should look like this:

![Completed correct workflow](sys_attachment.do?sys_id=1ffc1b8193d5ba10057c7de86cba1072)

 12. Hover your mouse over the Approval Two Activity.

![Hover your mouse over the Approval Two Activity.](sys_attachment.do?sys_id=13fc1b8193d5ba10057c7de86cba1077)

Notice that the hover status reflects both that the Approval was Restarted and the Rejected status of the Approval Activity.

13\. Close the **Workflow Context** browser tab.

14\. Scroll to the top of the **Workflow Context** form.

15\. Find the **ID** field and select the Form-Icon.

16\. Scroll down to the Approvals Related List.

17. **Right-Click > Approve** the **Requested** K14 Approval One.

18. **Right-Click > Reject** the **Requested** K14 Approval Two.

19\. Select the **Workflow Context** in the **Related Links** list.

20\. In the **Activities History** list, right-click on a **Restarted** Activity.

![In the Activities History list, right-click on a Restarted Activity.](sys_attachment.do?sys_id=17fc1b8193d5ba10057c7de86cba107b)

21\. Select **Workflow Debug > Highlight Rollback**.

![Select Workflow Debug > Highlight Rollback.](sys_attachment.do?sys_id=6ffc5b8193d5ba10057c7de86cba1000)

All the activities that were part of a single **Rollback To** execution will be colored together. Notice there is another set of Restarted Activities. These were part of a different **Rollback To** execution. This coloring is useful when debugging large workflows with multiple rollback paths. If you click on another Restarted Activity, the related records will highlight in another color.

22\. Scroll to the top of the **Workflow Context** form.

23\. Find the **ID** field and select the Form-Icon.

24\. Scroll down to the Approvals Related List.

25. **Right-Click > Approve** the **Requested** K14 Approval One.

26. **Right-Click > Approve** the **Requested** K14 Approval Two.

27\. Select the **Show Workflow** from the **Related Links** list.

28\. Hover over the Log Message **Reject Approval Two.**

![Hover over the Log Message Reject Approval Two.](sys_attachment.do?sys_id=97fc1b8193d5ba10057c7de86cba1098)

  

Notice that the Log Message is **Restarted**. This is because the final State of Approval Two went down the Approved path so the Log Message Reject Approval Two was not re-executed.

29\. Hover over the Log Message **Reject Approval Two.**

Notice that its state is **Finished.** The Workflow Context Diagram reflects the most recent state of an Activity, even if it has multiple states in the Activity History. 

![Notice that its state is Finished. The Workflow Context Diagram reflects the most recent state of an Activity, even if it has multiple states in the Activity History.](sys_attachment.do?sys_id=abfc1b8193d5ba10057c7de86cba109c)

**Use the timeline view**  
There are times in debugging when being able to see all the states graphically is useful. For that, the context has a timeline view of the Workflow.

1\. Close the browser tab of the Workflow Context.

2\. Select the **Workflow Context** from the **Related Links** list.

3\. Scroll to the bottom of the **Workflow Context**.

4\. Select the **Show Timeline**.

![Select Show Timeline](sys_attachment.do?sys_id=2ffc1b8193d5ba10057c7de86cba10b9)

In this view, it is possible to see all the occurrences of the Reject of Approval Two.
