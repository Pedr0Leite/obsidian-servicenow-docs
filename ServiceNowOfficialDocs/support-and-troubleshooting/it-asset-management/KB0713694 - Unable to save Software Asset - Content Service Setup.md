---
title: "Unable to save Software Asset -> Content Service Setup "
aliases:
  - KB0713694
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713694
kb_number: KB0713694
last_modified: 2024-04-07
---

## Unable to save Software Asset -> Content Service Setup

  

### Issue

# Symptoms

* * *

Access "Software Asset" -> "Content Service Setup" to turn on / off for each category then click on "Save" button.

The expected behaviour after click on "Save" is showing the message:

"Selection(s) for the Software Asset Management Content Service have been successfully saved."

![](sys_attachment.do?sys_id=a8dc6ceedb42b450e515c223059619ff)

In customer's case, the page didn't return any message after click on 'Save', indicate the save function is not working

![](sys_attachment.do?sys_id=2cdcaceedb42b450e515c22305961904)

# Release

* * *

Kingston

# Cause

* * *

"glide.security.use\_csrf\_token" in 'sys\_properties' table has value set to false.

# Resolution

* * *

set "glide.security.use\_csrf\_token" value to true

# Additional Information

* * *

1\. This "Opt-In" screen (first time access "Content Service Setup") will have the same behaviour (not response after click on the button) with the property value set as false.

![](/sys_attachment.do?sys_id=6cdcaceedb42b450e515c22305961909)

2\. When you enable Chrome debug -> Console, notice following error.

ReferenceError: g\_ck is not defined

    at b.$scope.saveSelection (sn\_samp\_content\_service\_setup.do:431)

    at fn (eval at compile (angular\_includes\_1.4.jsx?v=08-29-2018\_0930:215), <anonymous>:4:230)

    at e (angular\_includes\_1.4.jsx?v=08-29-2018\_0930:256)

    at b.$eval (angular\_includes\_1.4.jsx?v=08-29-2018\_0930:135)

    at b.$apply (angular\_includes\_1.4.jsx?v=08-29-2018\_0930:136)

    at HTMLButtonElement.<anonymous> (angular\_includes\_1.4.jsx?v=08-29-2018\_0930:256)

    at HTMLButtonElement.dispatch (js\_includes\_doctype.jsx?v=08-29-2018\_0930&lp=Mon\_Sep\_24\_15\_48\_25\_PDT\_2018&c=56\_1050:24281)

    at HTMLButtonElement.r.handle (js\_includes\_doctype.jsx?v=08-29-2018\_0930&lp=Mon\_Sep\_24\_15\_48\_25\_PDT\_2018&c=56\_1050:24281)
