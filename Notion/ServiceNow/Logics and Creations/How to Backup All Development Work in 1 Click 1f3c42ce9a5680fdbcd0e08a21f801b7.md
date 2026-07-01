---
aliases:
  - "How to Backup All Development Work in 1 Click"
tags:
  - backup
  - update-sets
  - cloning
  - upgrade
  - dev-ops
---

# How to Backup All Development Work in 1 Click

Do you wish there was an easier way to keep your environments up to date?

Are you finding it time-consuming and difficult to backup and restore your development work when cloning during release cycles?

If you answered yes to any of the above, read on!

### **The Problem**

### **I want to keep my instances up to date, but it is too difficult and time-consuming to back out my Update Sets and restore them after the clone is complete.**

# **Design Pattern Matrix**

| **Version / Requirement** | **Preserve select Update Sets** | **Preserve all In Progress Update Sets (Last 90 Days)** |
| --- | --- | --- |
| **Paris** | [Update Set Batching & Export Batch](https://www.servicenow.com/community/developer-blog/how-to-backup-all-development-work-in-1-click/ba-p/2273975#batch_and_export) | [Clone Preserve Update Sets](https://www.servicenow.com/community/developer-blog/how-to-backup-all-development-work-in-1-click/ba-p/2273975#clone_preserve) |
| **Orlando** | [Update Set Batching & Export Batch](https://www.servicenow.com/community/developer-blog/how-to-backup-all-development-work-in-1-click/ba-p/2273975#batch_and_export) | [Clone Preserve Update Sets](https://www.servicenow.com/community/developer-blog/how-to-backup-all-development-work-in-1-click/ba-p/2273975#clone_preserve) |
| **New York** | [Update Set Batching & Export Batch](https://www.servicenow.com/community/developer-blog/how-to-backup-all-development-work-in-1-click/ba-p/2273975#batch_and_export) | [Update Set Batching & Export Batch](https://www.servicenow.com/community/developer-blog/how-to-backup-all-development-work-in-1-click/ba-p/2273975#batch_and_export) |

### **The Old Way**

You would wait until your environments are so out of sync, usually triggered by the Change gone wrong, causing Incidents, days of fire fighting, and late nights,  before thinking about Cloning all your environments from Production.

You have more "In Progress" Update Sets than you can poke a stick at - from Development Spikes to Enhancements put on hold indefinitely while the customer makes up their mind on the color of a button.

You filter your Update Sets by "In Progress" and painstakingly cycle each one as "Complete" and then Export them to XML. The default file name is something awful, like 1c223270dbed1fc07b337a9e0f961974.xml. You will need to remember the order in which these were created, as not to ruin some dependencies that may exist.

You might not even do any of the above and wait until there is absolutely no work in the pipeline, or have a mandatory Upgrade.

Regardless of your approach (or lack thereof), the whole process takes way too much time anyway and you wish there was an easier way.

Now there is! And it only takes 4 easy steps

![](https://www.servicenow.com/community/s/html/@2F265A353F782F27BDC48DA25BB19046/emoticons/1f642.png)

### **The New Way - Update Set Batching & Export Batch**

In case you missed the news, ServiceNow introduced a new feature called [Update Set Batching](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/hier-update-sets/concept/us-hier-overview.html) in Jakarta.

[Update Set Batching](https://docs.servicenow.com/bundle/kingston-application-development/page/build/system-update-sets/hier-update-sets/concept/us-hier-overview.html) allows Developers to relate Update Sets in Parent/Child relationships.

[](https://www.servicenow.com/community/image/serverpage/image-id/180203iCEBD7CC65C7F005D/image-size/large?v=v2&px=999)

This essentially eliminates the need to Merge Update Sets.

When a package of work is ready for deployment to the next Upstream environment, simply close the 'Update Set Parent', which in turn closes all Child Update Sets.

When retrieving Update Sets from the Upstream Environment, you only need to deploy one Update Set - the 'Update Set Parent'.

### **But how does this relate to backing up Update Sets?**

Depending on the size of your environment and rate of change, it is not uncommon to have 5-20 Update Sets "In Progress" at a time.

You would ideally like to be Cloning over DEV after every release - but this is really difficult and risky when you have a number of In Progress items, generally reflected by the number of "In Progress" Update Sets that are open.

### 

### **How to Backup Your Update Sets using Update Set Batching**

In your Development environment, prior to a clone:

1. **Create Parent Set**Create a new Update Set called "xx/yy/zz Dev Backup" (modify the name to comply with your customers naming standard)
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/180231iA4BE24F82A69E27D/image-size/large?v=v2&px=999)
    
2. **Relate all Child Update Sets**On the newly create Update Set, Navigate to 'Child Update Sets' and select 'Edit...'Using the slush bucket, the filter on 'State' is "In Progress" and 'Name' is not "Default" (Make sure you click 'Run Filter') Highlight all the Update Sets, move them across, and select 'Save'.
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/180211i3D10F956F98CC1F5/image-size/large?v=v2&px=999)
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/180215iCF9D84F5BEF45698/image-size/large?v=v2&px=999)
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/180221i7B5D718582A3B856/image-size/large?v=v2&px=999)
    
3. **Close the Parent**Set 'State' of the Parent Update Set to 'Complete'. The system will show a prompt, warning you that all Update Sets will be marked as Complete when you save (this is a good thing).Select 'OK' and save the record.ServiceNow will now close all your Update Sets for you!
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/180209i9BCCF74394F42FB5/image-size/large?v=v2&px=999)
    
4. **Export to XML**Select the Related Link 'Export Update Set Batch to XML'This has saved your Update Set Hierarchy into XML
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/180213i81A22F0C5C59E660/image-size/large?v=v2&px=999)
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/180227i04812F804282BFA3/image-size/large?v=v2&px=999)
    

### **In Summary**

In 4 steps, you now have a single XML file containing

- Your Parent Update
- All "In Progress" Child Update Sets
- The Version Record of every change in each Update Set

[](https://www.servicenow.com/community/image/serverpage/image-id/180223i605756F21113EAB7/image-size/large?v=v2&px=999)

### **Restoration**

After you have cloned over your Development environment, restoring your In Progress Update Sets is even easier.

1. **Import the XML**Navigate to 'Retrieved Update Sets'.Scroll to the bottom and select the Related Link "Import Update Set from XML" and select your XML file containing your backup.We can see that the Retrieved Update Set contains all the Updates.
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/180219i7EEFB29926A35611/image-size/large?v=v2&px=999)
    
2. **Preview & Commit**Preview the Update Set.Action any resulting Preview Problems and click Commit.Your entire Development Pipeline has now been restored!

You will probably run into some Preview Problems when restoring, which may seem like a painful process.

This may seem annoying now, but it is better to have these come up now, rather than when you are deploying these Changes into Production!

It is always better to highlight these issues in Development before going into Production. You'll thank your future self

![](https://www.servicenow.com/community/s/html/@2F265A353F782F27BDC48DA25BB19046/emoticons/1f642.png)

### **The Newest Way - Clone Preserve Update Sets**

Use the [Clone Preserve Update Sets](https://developer.servicenow.com/blog.do?p=/post/o-admin-features/#:~:text=Clone%20Preserve%20update%20sets&text=A%20new%20setting%20for%20clones,days%20in%20the%20target%20instance.) feature - available as of Orlando

### **Other Uses**

Backing up your Development "In Progress" before a clone is only one of many uses of the new feature:

- Use to group releases instead of Merging at the last moment
- Use to map dependencies between Update Sets or show Themes

You could even write a UI Action and a Script to do the whole Backup process for you!

## Related

- [[Logics and Creations]]
- [[Upgrade]]
- [[Update sets - Full Applications]]
- [[Updating Store Apps Sucks]]
