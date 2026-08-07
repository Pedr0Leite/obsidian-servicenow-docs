---
aliases:
  - "Workspace for a custom app forms"
area: "Workspace"
source: notion-export
tags:
  - workspace
  - forms
  - ui-builder
  - related-lists
---

# Workspace for a custom app: forms

If you read the [first part of my blog](https://www.servicenow.com/community/next-experience-blog/workspace-for-a-custom-app-where-to-start/ba-p/2599404#:~:text=post%20is%20posted.-,Workspace%20for%20a%20custom%20app%3A%20where%20to%20start%3F,-Alisa%20Tipisova) you know how to create a workspace for you custom app and configure lists and simple record page. Now let's look into that in a little bit more details. Usually almost all work in any application is done via forms and buttons, so that what we're going to start with.

# **Views**

When you were creating workspace you probably noticed that ServiceNow created a new view for every table you specified in Workspace Builder. Of course, you can just use Default view, but I think it's a good idea to have a separate view for workspace, so let's keep it. In the custom app I'm using for this post new view was called "Workspace Home Automation 0" which is kind of ugly from my point of view, so I decided to create another one. Of course, you don't have to do it, but what if you did? How would you tell your workspace which view to use?

That's where it becomes less easy and obvious. Right now there is no easy way to set the same view for all tables in the UI. But, there is a way to do it in backend. Object you're interested in is called **UX Application**, you can access it via **Now Experience Framework -> Experiences**. To access it from UI Builder, select **Experience -> Settings -> Advanced settings**.

[Screenshot 2023-06-30 at 15.29.36 (2).png](https://www.servicenow.com/community/image/serverpage/image-id/270838i4AD5C83BCDC7688F/image-size/large?v=v2&px=999)

You'll see the configuration of you Workspace and that's where you set up the view for your tables. In the related list change the value of **view** record to the view you'd like to use in the workspace.

[Screenshot 2023-06-30 at 15.35.21 (2).png](https://www.servicenow.com/community/image/serverpage/image-id/270840iF50ADA4B22DF4BBD/image-size/large?v=v2&px=999)

The only thing you need to do now is to configure this view for all tables you're going to show in the workspace.

### 

# **Journal fields**

Before we talk about buttons there is one more topic I'd like to discuss. If you have comments or work_notes on your form, you probably noticed that the record looks like this in workspace:

[Screenshot 2023-07-03 at 13.29.03 (2).png](https://www.servicenow.com/community/image/serverpage/image-id/271166i43BB6DF1B20566FA/image-size/large?v=v2&px=999)

You can leave it be this way, but I prefer to see comments only on the right side of the screen. But if you remove journal field from the view or use UI policy to hide it, it will also be hidden in activity stream. So, the proper way of removing comments and work notes looks like this:

1. Go to **Now Experience Framework -> Configuration Settings -> UX View Rules Configurations** and create a new view rule config for your workspace.
2. On **Workspace View Rules** related list click **New** and create new view rule.
3. Select required table and view, then go to **Form Settings** and select **Hide Journal Input Fields**.
    
    [Screenshot 2023-07-03 at 13.53.02 (2).png](https://www.servicenow.com/community/image/serverpage/image-id/271175iB4F20F8BFAC78DC1/image-size/large?v=v2&px=999)
    
4. Finally, go to your **UX Application** (see previous paragraph), create new **viewRuleConfigId** page property and put sys_id of your view rule config (step 1) to value field.
    
    [Screenshot 2023-07-03 at 13.52.52 (2).png](https://www.servicenow.com/community/image/serverpage/image-id/271176i51255CDA8BDEE7FC/image-size/large?v=v2&px=999)
    

# **Related lists**

Last element that I'd like to mention in this post is related lists. Related lists are configured in old UI for your "workspace" view and they magically appear on the record. However, there is one interesting bug found by [@Shane41](https://www.servicenow.com/community/user/viewprofilepage/user-id/421565) . When you click on a related list in workspace a default "active=true" filter applies to all related lists, even if active field doesn't exist in the table. I'm not sure if this bug appears on all instances or not (so far I saw it on 2 instances), but I think it's worth mentioning.

The reason why it happens is because additionally to fixed query (preconfigured when you created related list) it's possible to filter records dynamically using **filter** field on the related list component.

[Screenshot 2023-07-03 at 14.18.42 (2).png](https://www.servicenow.com/community/image/serverpage/image-id/271184i4A292E614871C87E/image-size/large?v=v2&px=999)

By default it's empty, which looks like no additional conditions are applied, but if you open

**UX Macroponent Definition**

for your page (sys_ux_macroponent) and search for list_related component in

**Composition**

field, you'll notice "active=true" hard-coded query.

[Screenshot 2023-07-03 at 14.15.24 (2).png](https://www.servicenow.com/community/image/serverpage/image-id/271185i1805643FD1971BFB/image-size/large?v=v2&px=999)

This query will be automatically applied to all related lists on your record and cause wrong data being displayed. One way of fixing it can be adding **item.value.query** to filter field.

[Screenshot 2023-07-03 at 14.18.36 (2).png](https://www.servicenow.com/community/image/serverpage/image-id/271186iFF6DE2C383CD3262/image-size/large?v=v2&px=999)

In the [next part](https://www.servicenow.com/community/next-experience-blog/workspace-for-a-custom-app-buttons/ba-p/2603633) I'm going to talk about buttons and how to configure them for different scenarios.

- [Workspace for a custom app: buttons](https://www.servicenow.com/community/next-experience-blog/workspace-for-a-custom-app-buttons/ba-p/2603633)
- [Workspace for a custom app: headers, highlighted values, sidebar](https://www.servicenow.com/community/next-experience-blog/workspace-for-a-custom-app-headers-highlighted-values-sidebar/ba-p/2618970)
- [**UI Builder : Next Experience**](https://www.servicenow.com/community/next-experience-blog/bg-p/next-experience-blog/label-name/ui%20builder%20%3A%20next%20experience)
- [**UI Framework Next Experience**](https://www.servicenow.com/community/next-experience-blog/bg-p/next-experience-blog/label-name/ui%20framework%20next%20experience)
- [**Workspace : Next Experience**](https://www.servicenow.com/community/next-experience-blog/bg-p/next-experience-blog/label-name/workspace%20%3A%20next%20experience)

## Related
- [[Using Applicability in Next Experience Themes to s]]

- [[Workspace]]
- [[Workspace App Shell UX Page Properties]]
- [[How to use UI Actions in Workspaces]]