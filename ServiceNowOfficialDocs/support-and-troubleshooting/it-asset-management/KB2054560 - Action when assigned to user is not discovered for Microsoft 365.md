---
title: "Action when assigned to user is not discovered for Microsoft 365"
aliases:
  - KB2054560
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2054560
kb_number: KB2054560
last_modified: 2025-04-11
---

## Text

**Problem Statement:** 

Customer wants to understand what action to perform when there are some Microsoft 365 product installs -with missing assigned to user. 

**Logic on ServiceNow SAM Pro** 

1.  **If the product is true SaaS** 

There are some M365 products which are labelled as true SaaS (ignore installs= true), the list of true SaaS products is provided here: **[KB article](/kb?id=kb_article_view&sysparm_article=KB2019260)**.

Herein, SAM Pro will ignore the installations of the product completely and not consider them in reconciliation. Hence there is no requirement to “discover” the assigned to for these products as install does not matter for license compliance determination. 

Examples of true SaaS products include Visio Online, Microsoft 365, One Drive for business etc. 

**2\. If product is not true SaaS**  

If a product is not true SaaS (example Power Automate, End Point configuration manager client), then the install will be licensed as mentioned before 

-   -   -   ServiceNow checks the user assigned to the install (installed on) and thereby checks if the user has a subscription 

-   -   If the user has Power automate install, then the install will be licensed by the corresponding license, otherwise if the user has Enterprise E5 subscription then the install will be inferred to Enterprise E5 (as Enterprise E5 includes Power Automate as its suite component) 

-   -   If the installed on- assigned to user does not have any subscription those installs will not be inferred, as SAM Pro does not know which subscription to license the installs and will show as installs requiring action 

-   -    If the install on- assigned to user does not have any assigned user, then too the install will not be licensed as SAM Pro does not know which subscription to license the installs, and will show as installs requiring action

**Overall, Logic:** 

If the software product is a true SaaS (ignore install = true) then the discovery of assigned to would not matter, as license compliance is determined by subscriptions alone.  

However, if it is not true SaaS then assigned to discovery is important to determine which subscription this install would belong to. This would show as Separate software model result and will not infer to any suite 

**Common Questions and answers** 

**Action on MAC Machines** 

**Q:** Why are the component installs (Such as MS Outlook, One Note) of true SaaS products like Microsoft 365 showing as installs requiring action? Also, what action to take in this scenario? 

**Ans.** The primary reason is that on Mac machines, the installation of M365 Apps components—such as Microsoft Outlook, OneNote, and Word—is discovered as individual products rather than as a unified "Microsoft 365 Apps for enterprise" package. Additionally, the installed software often lacks an associated user in the discovery data. 

This behaviour is due to how discovery tools detect software on Mac systems and is not related to any limitation in SAM Pro. 

As a result, SAM Pro is unable to determine whether these individual installs (e.g., Outlook, OneNote) are part of a perpetual Microsoft Office license or a Microsoft 365 user subscription license. 

![](/sys_attachment.do?sys_id=6b931a5647f06250b7832920326d4391)

_**Figure 1** Install of Microsoft 365 apps for enterprise on MAC Machines_ 

![](/sys_attachment.do?sys_id=27931a5647f06250b7832920326d4364) 

_**Figure 2** Installs for Microsoft 365 apps for enterprise on Windows Machines_ 

These components will show on the License work bench as installation requiring action with reason as install without a software entitlement. These will be shown separately on the License work bench with its own product results and have –install requiring action. 

![](/sys_attachment.do?sys_id=f3931a5647f06250b7832920326d43a5) 

_**Figure 3** Microsoft Word showing as install requiring action_ 

![](/sys_attachment.do?sys_id=d793965647f06250b7832920326d435d) 

**What action can be taken?** 

1.  Option 1:  

If assigned to user is not found: Determined the assigned to user of the install- this will help determine if the user has a subscription or not 

2\. Option 2: If you are confident that that install belongs to a user subscription license only from M365 portal then you can create a software model for these software(s) (such as Microsoft word) and set LUM=false: this will ignore all software installs for this software 

This will then show as ignored install with reason as Installs ignored through LUM  

**Action on Server machines** 

**Q:** On Server machines, I know that there is no assigned to user discovered as these machines are not managed by a single individual. What action can I take for the same? 

![](/sys_attachment.do?sys_id=7f931a5647f06250b7832920326d432f) 

_**Figure** 4 Non true SaaS product installs on server missing assigned to user_ 

**Ans.** Installs of non-true SaaS products (such as Configuration Manager Client) of M365 may show up as installs requiring action on the license work bench, if the assigned to user is not discovered. This is by design as SAM Pro is unable to determine the eligible License of Microsoft to license these installs (user subscription license or others) as these products may have another license to license these installs 

**Action:** 

1.  Determine the assigned to user if possible so that SAM pro can determine the subscription assigned to that user 

**\[Or\]**  

2\. If you are confident that this install is only from a user subscription license, then you can create a software model for this install and make LUM=false so that the installs for this software are ignored from reconciliation. 

This will then show as ignored install with reason as Installs ignored through LUM  

![](/sys_attachment.do?sys_id=5393965647f06250b7832920326d4320)
