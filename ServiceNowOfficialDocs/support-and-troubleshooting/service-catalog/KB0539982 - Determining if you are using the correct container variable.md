---
title: "Determining if you are using the correct container variable"
aliases:
  - KB0539982
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0539982
kb_number: KB0539982
last_modified: 2025-01-26
---

## Determining if you are using the correct container variable

  

### Issue

Determining if you are using the correct container variable to avoid:

-   Variables appearing in the wrong place
-   Variable not alternating as expected

  

### Release

All versions

### Resolution

To configure [container variables](https://docs.servicenow.com/csh?topicname=r_VariableTypes.html&version=latest "container variables"), navigate to the **Variables** related list on the **Catalog Item** form.

-   This list can contain a combination of container records and variable records.
-   The order of these records is important as it affects how they are rendered on the form.

This example shows an item with four variables and no containers:

  

![](sys_attachment.do?sys_id=3047a80d1bc07414f34d33bc1d4bcb48)

  

If no containers are defined, the item view shows them rendered top to bottom, in increasing order:

  

![](sys_attachment.do?sys_id=8947e80d1bc07414f34d33bc1d4bcb23)

To control the layout to use anything other than the top-to-bottom linear format, container records are needed.

  

**Using containers**

There are several methods for using containers to control layout.

**Method 1: Use the <Container Start> - <Container Split> - <Container End> Formation**

In this formation, variables appear in the first column, ordered from top to bottom until the split appears. After the split, the variables appear in the second column, ordered from top to bottom in that column.

For example, if you set up your containers as follows:

![](sys_attachment.do?sys_id=b047e80d1bc07414f34d33bc1d4bcb01)

  

The item appears as follows:

![](sys_attachment.do?sys_id=bc47e80d1bc07414f34d33bc1d4bcb03)

Having multiple splits within the same start-end formation does not make any impact. Only the first split is recognized.

To have multiple splits, set up a second start-split-end formation nested inside the first. For example:

  
  

![](sys_attachment.do?sys_id=8547e80d1bc07414f34d33bc1d4bcb26)

This helps you create three columns:

  

![](sys_attachment.do?sys_id=3847e80d1bc07414f34d33bc1d4bcb1f)

**I**t is not necessary to set up containers right at the top of the variables. Any variable outside the containers is rendered using the full width across the two columns. For example:

![](sys_attachment.do?sys_id=0d47e80d1bc07414f34d33bc1d4bcb27)

  

  

Renders as: 

  

## ![](sys_attachment.do?sys_id=8147e80d1bc07414f34d33bc1d4bcb29)  
Method 2: Use the <Container Start> - <Container End> that is using '2 column wide, alternating sides' formation 

To set this up, open the **Container Start** record, then in the **Type Specification** tab, set the **Layout** field to **2 columns wide, alternating sides**.

  

![](sys_attachment.do?sys_id=bc47e80d1bc07414f34d33bc1d4bcb20)  
  
There is no need for a split, as each variable is rendered on alternative sides. The first variable is on the left side, then the next is on the right-hand side, the next is left, and so on. For example:

  
![](sys_attachment.do?sys_id=0547e80d1bc07414f34d33bc1d4bcb22)  

  

Renders as:

  
![](sys_attachment.do?sys_id=b447a80d1bc07414f34d33bc1d4bcb49)  
  
Using an odd number of variables means the left-hand side has one more.

**Method 3: Use the <Container Start> - <Container End> that is using '2 column wide, one side, then the other' formation** 

To set this up, open the **Container Start** record, then in the **Type Specification** tab, set the **Layout** field to **2 columns wide, one side, then the other**.

  

![](sys_attachment.do?sys_id=bc47a80d1bc07414f34d33bc1d4bcbf8)  
  

  

Similar to the last formation, this type of formation does not need a <container split> because the split is done evenly halfway through. If there is an odd number of variables to render, then the right-hand side renders one more variable.  
  
For example:

![](sys_attachment.do?sys_id=3447a80d1bc07414f34d33bc1d4bcbfa)  
  
  
Renders as: 

  
![](sys_attachment.do?sys_id=b847a80d1bc07414f34d33bc1d4bcbfb)

**Containers and variable sets**

The previous descriptions assume that there are no variable sets being used. However, variable sets can also contain containers. Variable set containers offer the flexibility of defining layouts using two mechanisms:

1.  The same standard three formations as for variables. 
2.  Specifying the layout on the variable set itself, without using containers at all (also see [Defining Variable Set Layout](https://docs.servicenow.com/csh?topicname=c_DefineVariableSetLayout.html&version=latest "Defining Variable Set Layout")).

![](sys_attachment.do?sys_id=3047a80d1bc07414f34d33bc1d4bcbfd)  
  
Ensure that you specify an order both on the variable set and also on its variables to get the desired layout.

![](sys_attachment.do?sys_id=b447a80d1bc07414f34d33bc1d4bcbfe)

  

  

![](sys_attachment.do?sys_id=3c47a80d1bc07414f34d33bc1d4bcbff)  
  
The ordering fields left empty have an impact on the layout. To fully understand the impact, see [Defining Variable Set Order.](https://docs.servicenow.com/csh?topicname=c_DefineVariableSetLayout.html&version=latest "Defining Variable Set Order.")

#   

### Related Links

Possible container pitfalls are:

-   **Inactive containers:** While the containers and their ordering may appear completely correct, it may be that some of the ordered components are inactive. If all of the above is setup well and you have followed the troubleshooting steps, it is useful to bring up the active column on the variable related list. This will show if there are any inactive components that are throwing off the layouts.

-   **Poorly** **ordered containers:** For example, **Container End** with an order smaller than **Container Start** is likely to render badly. Similarly, a container split that is not ordered between the **Container Start** and **Container End** will not render as expected. You should ensure that the order of **Container Start** is less than that of **Container Split**, which is less than that of **Container End**.
