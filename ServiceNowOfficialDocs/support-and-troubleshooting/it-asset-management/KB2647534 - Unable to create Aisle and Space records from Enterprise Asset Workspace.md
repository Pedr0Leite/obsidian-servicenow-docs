---
title: "Unable to create Aisle and Space records from Enterprise Asset Workspace"
aliases:
  - KB2647534
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2647534
kb_number: KB2647534
last_modified: 2025-12-10
---

## Unable to create Aisle and Space records from Enterprise Asset Workspace

  

### Issue

In the Enterprise Asset Workspace, we are attempting to create Aisle and Space, by following below steps:

Step1: Open Enterprise Asset Workspace  
Step2: Go to Inventory>All Stockroom  
Step3: Open any stockroom   
Step4: Go to Aisle and Space related list and Click Add Aisle or Add Space  
Step5: Provide Aisle name in the Popup appears on the screen and click OK to Save the record, but the record is not created.  
  

### Release

All

### Cause

We are seeing the following error in the system logs:

```
com.glide.script.RhinoEcmaError: "sn_itam_workspace" is not defined.
sys_script_include.a76f11f9779002103233b5ff9a5a99c1.script : Line(109)
```

Stack trace:

```
at sys_script_include.a76f11f9779002103233b5ff9a5a99c1.script:109
at sys_ux_data_broker_transform.faf4cef693fcc210c61e563e64891811:2 (transform)
at sys_ux_data_broker_transform.faf4cef693fcc210c61e563e64891811:3
```

This error occurs when we try to create an Aisle or Space from the Enterprise Asset Workspace. During this process, the following Data Brokers are triggered:

https://<instance>.service-now.com/sys\_ux\_data\_broker\_transform.do?sys\_id=faf4cef693fcc210c61e563e64891811

https://<instance>.service-now.com/sys\_ux\_data\_broker\_transform.do?sys\_id=4058376593b4c210c61e563e648918a5

Both of these Data Brokers call the PickTaskUtil Script Include:

https://<instance>.service-now.com/sys\_script\_include.do?sys\_id=a76f11f9779002103233b5ff9a5a99c1

When creating an Aisle, the following code in _PickTaskUtil_ is executed:

```
PickTaskUtil.createAisles = function(stockroom, aisles) {
    var locGr = new GlideRecord(ITAMCommonUtil.CMN_LOCATION_TABLE);
    var aisleSpaceGr = new GlideRecord(CommonConstants.STOCKROOM_AISLE_SPACE);
    var stockroomGr = new GlideRecord(sn_itam_workspace.AssetWorkspaceUtil.STOCKROOM_TABLE_NAME);
    stockroomGr.get(stockroom);

    for (var aisleIdx = 0; aisleIdx < aisles.length; aisleIdx++) {
        locGr.initialize();
        locGr.setValue('parent', stockroomGr.getValue('location'));
        locGr.setValue('name', aisles[aisleIdx].aisle);
        locGr.setValue('cmn_location_type', 'place');
        var locSysId = locGr.insert();

        aisleSpaceGr.initialize();
        aisleSpaceGr.setValue('stockroom', stockroom);
        aisleSpaceGr.setValue('aisle', locSysId);
        aisleSpaceGr.insert();
    }
};
```

This code references AssetWorkspaceUtil, which is not available in the instance.

The AssetWorkspaceUtil Script Include is provided by the Asset Management Workspace plugin. Since this plugin is not installed, the Script Include is missing, causing the `"sn_itam_workspace" is not defined` error.

### Resolution

Install the Asset Management Workspace plugin. Once the plugin is installed, the AssetWorkspaceUtil Script Include will be created, and you will then be able to add an Aisle without encountering the error.
