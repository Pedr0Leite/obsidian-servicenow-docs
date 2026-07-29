---
title: "Not all pages show up on the Service Portal Designer (/$spd.do#/page/select)"
aliases:
  - KB0656283
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656283
kb_number: KB0656283
last_modified: 2024-04-07
---

## Not all pages show up on the Service Portal Designer (/$spd.do#/page/select)

  

### Issue

Pages don't appear on the Service Portal Designer

  
  

# Problem

* * *

Not all pages show up on the Service Portal Designer (/$spd.do#/page/select).  

# Cause

* * *

The usual reason for pages not showing up is that the **Internal** field is set to true on the portal page. Internal use pages are not for public portal users but instead for administrative/designer use. For example, the sp\_config page is not a page you would want to modify and is instead used to administrate the portal itself.

To see which pages are set to internal use:

1.  Navigate to **Service Portal > Pages**.
    
    If the **Internal** field does not display by default, click the gear icon to the left of the field names and use the slushbucket to add it to the form.
    
2.  Use the filter **\[Internal\]\[is\]\[true\]** to see which pages are set to internal use.
    
    ![](/sys_attachment.do?sys_id=e409a0aedb02b450e515c22305961965)
    

# Resolution

* * *

Uncheck **Internal** for the pages you want to show in the Page Designer.
