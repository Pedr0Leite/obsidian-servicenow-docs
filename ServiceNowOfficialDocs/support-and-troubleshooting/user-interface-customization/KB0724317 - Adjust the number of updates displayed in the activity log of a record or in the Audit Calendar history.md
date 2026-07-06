---
title: "Adjust the number of updates displayed in the activity log of a record or in the Audit Calendar history "
aliases:
  - KB0724317
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724317
kb_number: KB0724317
last_modified: 2025-09-18
---

## Adjust the number of updates displayed in the activity log of a record or in the Audit Calendar history

  

### Issue

# Description

* * *

In a standard out-of-box instance the default maximum number of updates in the activity log of a record which keeps such information is 250 updates displayed.  This same limit is also applied if a user views the calendar history view from the contextual menu of any record.  Although in an out-of-box instance this value is set at 250, this number can be adjusted to return more or fewer records if necessary.  This article describes the steps that can be used to modify this maximum number of history records which will be displayed in these views for any record that retains such a history.

![Activity Log of a record.](sys_attachment.do?sys_id=81dba0eadb42b450e515c22305961947 "Activity Log of a record")

# Procedure

* * *

The following steps can be used to modify this maximum number of history records to display:

Log into the instance with an account having admin rights to the instance.

Using the Menu Navigator, browse to the following location on the instance: **System Properties** -> **System**.

A properties page will appear.  Locate the property header that begins with the text "**Maximum number of entries retrieved for display in an activity stream.**"

Replace the value directly below this header with a numerical value of the number of records you want to appear in history lists.  If fewer than the requested number are found for a particular record, all such history records will be displayed.

![Maximum number of history records to display](sys_attachment.do?sys_id=19dba0eadb42b450e515c2230596194c "Maximum number of history records to display")

Click one of the **Save** buttons found on the properties page to record the changes.  One such Save button is at the upper right corner of the page and another is at the bottom of the page.

After making this system property change, viewing the activity log of a record or the calendar history view will display a maximum number of updates as specified in this property as set in the steps above.

Records in excess of the number selected will simply not be displayed in a activity log, with the oldest records the first to be removed from the display.

With the calendar history view, a message reading "Note: an additional XX updates to this record were omitted for easier viewing..." will be displayed, with XX representing some number of records which have been removed from the display.  

 ![Maximum history records](sys_attachment.do?sys_id=d9dba0eadb42b450e515c22305961951 "Maximum history records")

# Additional Information

* * *

Note that this property can also be directly adjusted from the sys\_properties list by locating the System Property with the  **Name** _glide.history.max\_entries_ and replacing the number in the Value field with the number of history records preferred to display in the update history and history calendar view.

Note that if the Post button is clicked to add the notes, the ticket will not actually reload, and thus all such activity log updates will remain on the ticket as well as the newest record.  However, once the ticket is Updated, Saved or reloaded the number of such activity updates will be limited by the number as found in the property as set in these steps.
