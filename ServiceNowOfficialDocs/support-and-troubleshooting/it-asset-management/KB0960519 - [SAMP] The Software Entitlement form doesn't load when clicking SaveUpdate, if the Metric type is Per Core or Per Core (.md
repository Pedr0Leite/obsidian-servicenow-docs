---
title: "[SAMP] The Software Entitlement form doesn't load when clicking \"Save/Update\", if the Metric type is \"Per Core\" or \"Per Core (with CAL)\""
aliases:
  - KB0960519
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960519
kb_number: KB0960519
last_modified: 2024-03-25
---

## \[SAMP\] The Software Entitlement form doesn't load when clicking "Save/Update", if the Metric type is "Per Core" or "Per Core (with CAL)"

  

### Issue

-   On the Software Entitlement form (alm\_license), when License Metric is of type "Per Core" or "Per Core (with CAL)", the "Save/Update" action doesn't work. i.e. the form doesn't load/respond.

### Release

-   Instance with Software Asset Management Professional for SAP (com.sn\_samp\_sap) plugin enabled.

### Cause

-   When inspecting the page via the developer tool, the below error is returned while clicking on "Save"

**ERROR: invalid field or missing message passed to g\_form.showFieldMsg('rights\_per\_license\_pack','Please enter a number greater than 0')**

-   This specific error "Please enter a number greater than 0" is triggered from the Client Script "**Check purchased rights VS upgraded right**"

https://<<instance\_name>>.service-now.com/nav\_to.do?uri=sys\_script\_client.do?sys\_id=04c71d4367522200e85a87cb5685efbf

-   Further inspecting, i.e. copying the "g\_form.getDecimalValue('rights\_per\_license\_pack')" value in developer console could see it returned value "0", though "rights\_per\_license\_pack" for the specific record is > "1".
-   If this mandatory field "Rights per license pack" is not available on the "alm\_license" form, the value that it gets assigned is "0" during "onsubmit" action and thus the form doesn't load during "Save/Update".
-   This is being validated in line #8 from the Client Script "Check purchased rights VS upgraded right".

**var rightsPerLicensePack = g\_form.getDecimalValue('rights\_per\_license\_pack');**

### Resolution

-   For this Client Script to use the "**rights\_per\_license\_pack"** available value on the Entitlement, add the "Rights per license pack" on the "alm\_license" form from the "Configure >> Form Layout" slush bucket. 

![](sys_attachment.do?sys_id=334661a81bfb2010d01143f6fe4bcb0f)
