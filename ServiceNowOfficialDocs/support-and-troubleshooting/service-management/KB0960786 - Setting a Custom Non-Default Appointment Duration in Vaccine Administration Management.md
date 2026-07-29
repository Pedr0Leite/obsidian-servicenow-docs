---
title: "Setting a Custom / Non-Default Appointment Duration in Vaccine Administration Management"
aliases:
  - KB0960786
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960786
kb_number: KB0960786
last_modified: 2024-03-27
---

## Setting a Custom / Non-Default Appointment Duration in Vaccine Administration Management

  

### Issue

You are wanting to have a **Custom Appointment Duration** within **Vaccine Administration Management**. (Example: **20 Minute Appointment Duration**)

However, by default we can see there is only the following **Duration Options:** **10 minutes, 15 minutes, 30 minutes and higher.**

### Cause

The **durations** which are listed above are the **default** ones which are provided in the **Out Of Box Product**.

Therefore it is expected for these to display. However, it is also possible to **customise** these options and add an extra **duration**.

### Resolution

Add a **Choice** to the **"appointment\_duration" Field** on the **\[sn\_vaccine\_sm\_appointment\_config\]** **Table** which contains the **Duration Value** which you are wanting to use.

  

As an example, if you want a **20 Minute Duration Option**, then you need to create the following **Choice Record:**

![](sys_attachment.do?sys_id=eebfb455db3be81014d6fb2439961991)
