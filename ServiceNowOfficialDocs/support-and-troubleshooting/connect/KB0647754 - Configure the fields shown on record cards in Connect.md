---
title: "Configure the fields shown on record cards in Connect"
aliases:
  - KB0647754
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0647754
kb_number: KB0647754
last_modified: 2025-01-03
---

## Configure the fields shown on record cards in Connect

  

### Issue

How to Configure the fields shown on record cards in Connect

# Description

* * *

When a record is either linked to or created from a connect conversation the details of the record are displayed as a card (see screenshot). These can be edited by following the steps below.

**Example of Record Card from Linked KB Article.**

![](sys_attachment.do?sys_id=0f0964aedb02b450e515c22305961994)

# Procedure

* * *

To configure the fields shown on record cards in Connect, create a List view with the name Connect for that record's table. This view will apply only to the full connect page ($c.do) and the end user view of support conversations.

1.  Navigate to the record’s list view, for example, **incident.list or kb\_knowledge.list**
2.  Right-click a column header and select **Configure > List Layout**.
3.  In the View name drop-down list, choose **New** to create a new view.
4.  Name the new view **Connect**.
5.  Edit the fields accordingly and then click **Save**.

# Applicable Versions

* * *

ALL

# Additional Information 

* * *

You cannot remove the **Author** or the **Updated** fields from the card regardless of whether they are on the view or not. 

The Card will always show the **Short Description** field in the top even if it is added to the list.
