---
title: "Generate QR for Assets"
aliases:
  - Generate QR for Assets
tags:
  - servicenow-dev-program
  - code-snippet
  - generate-qr-for-assets
  - ui-actions
---

# 🧩 ServiceNow Asset QR Code Generator (UI Action)

This repository contains a **ServiceNow UI Action** script that generates and displays a QR Code for an Asset record from list view.  
When the user selects a record and clicks the UI Action, a modal window pops up showing a dynamically generated QR Code that links to asset details.


A supporting **Script Include** (server-side) is required in your ServiceNow instance but **is not included** in this repository.
At the bottom of file , a sample Script Include Code is given , check for the reference.

---

## 🚀 Features

- Generates a QR Code for the selected Asset record.
- Displays the QR Code inside a ServiceNow modal (`GlideModal`).
- Uses **QrIckit API** for quick and free QR code generation.
- Clean, modular client-side code that integrates seamlessly with UI Actions.
- Includes a `qr-code-image` file showing example QR Code generated.

---

## 🧠 How It Works

1. The `onClickQR()` function is triggered when the user clicks a UI Action button.
2. It calls `generateQRCodeForAsset(sys_id)` and passes the record’s `sys_id`.
3. A `GlideAjax` request fetches asset data from a **Script Include** on the server.
4. That data is encoded and sent to the **QrIckit** API to generate a QR Code image.
5. A ServiceNow modal (`GlideModal`) displays the generated QR Code to the user.

---


**Note :**
1) As the UI action calls a Script Include , in this folder no script include is present
2) You can modify script include part as required(i.e Which fields are to be shown when QR is scanned)
3) A sample Client Callable Script-Include is given here.

``` Script Include Code
     var GenerateAssetQR = Class.create();
GenerateAssetQR.prototype = Object.extendsObject(AbstractAjaxProcessor, {
    getAssetQRData: function() {
        var sys_id = this.getParameter('sysparm_sys_id');
        var asset = new GlideRecord('alm_asset');
        if (asset.get(sys_id)) {
            return 'Asset: ' + asset.name + ', Serial: ' + asset.serial_number;
        }
        return 'Invalid asset record.';
    }
});
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
