---
title: "Workflow Engine Overview"
aliases:
  - KB0538559
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538559
kb_number: KB0538559
last_modified: 2024-09-20
---

## Workflow Engine Overview

  

### Issue

**Workflow Engine Overview**

Understand Workflow within a Glide Record.  

  

  

### Resolution

**The Workflow Engine in ServiceNow**

The Workflow Engine runs part of the Glide Engine. To design applications or extend existing applications with Workflow Processes it is important to understand where the Workflow Engine is as part of the Glide record transaction.

This lab introduces the Glide Transaction and highlights the place and role of the Workflow Engine within that Transaction.

The Workflow Engine will always guarantee updates to the current record at the end of each process point.

The Glide Engine is a data drive and so reacts to **events** that signal a change in the state of some data.

Glide events are inserted, **update**, **delete** or **cancel**. These events are fired into the engine in various ways. Some examples are:

-   UI Actions:  
    -   A user clicks a **Submit** button -> an **insert** event fires into the Glide Engine.
    -   A user clicks an Update button -> an **update** event fires into the Glide Engine.
    -   A user clicks a Delete button -> a **delete** event fires into the Glide Engine.
    -   A user clicks the Cancel Transaction icon  -> a **cancel** event fires into the Glide Engine.
-   Within Scripts:  
    -   A script that initializes a GlideRecord -> an **insert** event fires into the Glide Engine.  
          
        GlideRecord gr = new GlideRecord (‘incident’);
        
        gr.initialize();
        
        gr.insert();  
          
        
    -   A Business Rule that deletes a **current**  -> a **delete** event fires into the Glide Engine.  
          
        GlideRecord gr = new GlideRecord (‘incident’);
        
        gr.get(‘specify\_sys\_id’);
        
        gr.delete();  
          
        

For each of these events fires into the Glide Engine, a series of transformations and processes begin. **One event = One Glide Transaction**. As each of these events fires into the Glide Engine, a series of transformations and processes begins.

![](sys_attachment.do?sys_id=3b77648d1bc07414f34d33bc1d4bcb5f) 

Workflow is part of both the Data Transformation layer as a **Default Workflow** and part of Post Processing as a **Deferred Workflow**. In either case, the Workflow Engine, along with other engines such as Field Normalization and Data Policy, is sandwiched between two sets of business rules.

The Order value of Business Rules determines their order of execution around the sandwiched engines. Business Rules that are ordered less than 1000 will run before the other engines, including Workflow. Business Rules that are orders greater than or equal to 1000 will run after other engines, including Workflow.

Both Business Rules and Workflow can be configured to run before data is stored (transformation) or after data is stored (post-processors).

To configure a Business Rule to run before data is stored, check the **Before** check box on the form.

By default, Workflow will run before data is stored.

To configure a Business Rule to run after data is stored, check the **After** check box on the form.

To configure a Workflow to run after data is stored, check the **Run After Business Rules** box on the Workflow Properties form.

NOTE: We will be looking at each of these specifically in just a bit.

If we were to add more detail to the graphic of a transaction, it would look like this.

![](sys_attachment.do?sys_id=b377648d1bc07414f34d33bc1d4bcb5e) 

As a Workflow Designer, it is important to understand the timing of each participant in the Glide Transaction.

A **Deferred Workflow**, which is one that runs after the database operation, will still ensure the preservation of changes to the current record, that preservation is **not** part of the same database transaction. Remember **One event = One Glide Transaction.** Since the data is already stored when a **Deferred Workflow** is called, the Workflow Engine forces a second **update** event. However, this update event will begin an independent and nested transaction, which will complete before the After Business Rules ordered greater than or equal to 1000 of the original event fire.

![](sys_attachment.do?sys_id=bf77648d1bc07414f34d33bc1d4bcb60) 

  

NOTE: Because the Default Workflow runs as part of a database event and because a **Deferred** **Workflow** performs its own nested update of current, **it is never necessary to call current.update(); anywhere within a Workflow Activity Script field**.

Keep in mind that every call to update() creates an independent **update** event. As an independent event, it will cause an unnecessary nested update that will affect the performance of your application.

### One event = One Glide Transaction

It is important as a Workflow Designer within an application to be aware of what Business Rules and Engines are also in the Application and what effect each may have on the data that drives the process.

A Workflow Designer needs to be able to predict when and how data is being transformed and by which process player. It is equally important, depending on the complexity of the application, to know when other nodes or threads will have access to that data.

![](sys_attachment.do?sys_id=3777648d1bc07414f34d33bc1d4bcb62) 

NOTE: Most business processes work very well with **Default Workflow**. If you choose to configure a Workflow to be a **Deferred Workflow**, beware of the timing of the two updates on the current record.

If there is not a **Deferred Workflow** assigned to a Glide Record in the Post Processing phase of the Glide Transition, there will be **no update to** the current record by default. The best use of the Post Processing phase of the Glide Transaction is to react to the data change not continue to change it.
