---
title: "Confirm appropriate inbound email action is created"
aliases:
  - KB0535521
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535521
kb_number: KB0535521
last_modified: 2024-04-30
---

## Confirm appropriate inbound email action is created

  

### Issue

Confirm appropriate inbound email action is created

# Summary

* * *

Many times, a desired action is not performed on an inbound email because there is not an appropriately created inbound email action.

An overview of inbound email actions and how to create them is available in the [Inbound Email Actions](https://docs.servicenow.com/csh?topicname=c_InboundEmailActions.html&version=latest "Inbound Email Actions") article in the ServiceNow product documentation. 

# Video Tutorial

* * *

# Symptoms

* * *

-   Email sent to your ServiceNow instance does not create a new incident or other record.
-   Reply email sent to your ServiceNow instance does not update the expected incident or other record.
-   Email is not processed by any inbound action and remains in the **Ready** state.
-   General problems with Inbound Email Actions.

# Troubleshooting

* * *

1.  Determine if you want the action to run on a **New**, **Reply** or **Forwarded** email. Select the appropriate type in the inbound action.
2.  Determine and select the table you want to target with the inbound email.
3.  Make sure the inbound action is **Active**.
4.  Carefully add conditions as this could block your inbound action from running.
5.  Supply a script for what action you want to perform on the target table. Some useful script examples can be found in [Inbound email action examples](https://docs.servicenow.com/csh?topicname=r_InboundEmailActionExamples.html&version=latest "Inbound email action examples").
