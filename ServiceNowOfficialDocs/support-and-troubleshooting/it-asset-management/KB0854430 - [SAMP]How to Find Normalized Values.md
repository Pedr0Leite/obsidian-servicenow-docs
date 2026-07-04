---
title: "[SAMP]How to Find Normalized Values"
aliases:
  - KB0854430
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0854430
kb_number: KB0854430
last_modified: 2024-04-08
---

## \[SAMP\]How to Find Normalized Values

  

When importing entitlement data from external systems for SAM, especially when leveraging the **Import Entitlements** capability, it is important to match the normalized values that the ServiceNow Content Services Team provides. Failure to do so would mean an entitlement brought in, and then the system not knowing what to do with it, resulting in a manual association effort of the **Software** **Entitlement** to the correct **Software Model**. While this may not be a daunting task in small or proof-of-value environments, when importing hundreds or even thousands of entitlements or more, it is important to automate the association inasmuch as possible.

One of the quickest ways to see how the Content Services Team normalizes SAM data is to look at the **Discovery Model.** This object is the link between what is found in your discovery tool(s) and how it is associated to a **Software Model**, which is the object tied to **Software Entitlements**, allowing for compliance to be calculated. The **Discovery Model** contains the raw, non-normalized data, and then next to it, the normalized fields from the ServiceNow Content Services Team. To find how ServiceNow normalizes, simply find the **Discovery Model** for the data in question.

Start by navigating to **Software Asset** > **Discovery** > **Discovery Models.** By way of warning, in a very large enterprise, there could be tens of thousands, or even hundreds of thousands, of **Discovery Models**, so searching and filtering may take a couple of seconds. The resultant pane should resemble the following:

  

![](sys_attachment.do?sys_id=2353e02adbce7450e515c22305961964)

  

Now, let’s open one of the **Discovery Models** by clicking on the **Display Name**.

Note: it is possible that some of the resultant **Discovery Models** aren’t normalized or not fully normalized. Make sure to select a model where the **Normalization status** = “Normalized”.

The areas highlighted in green illustrate the discovered data coming in from an endpoint management tool, such as SCCM, or an ITOM tool, such as ServiceNow Discovery. This is the raw data. The areas highlighted in yellow are the values as normalized by the ServiceNow Content Team.

  

![](sys_attachment.do?sys_id=a353e02adbce7450e515c2230596196a)
