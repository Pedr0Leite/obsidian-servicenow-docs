---
title: Configure input form screens with single and multi-scan barcode inputs
description: Configure input fields that you can use to scan a single barcode one at a time or multiple barcodes without leaving the scanning interface.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/single-multi-barcode-input-config.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Input form screen, Mobile screen types, Mobile screens, Mobile app components, Building mobile apps, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Configure input form screens with single and multi-scan barcode inputs

Configure input fields that you can use to scan a single barcode one at a time or multiple barcodes without leaving the scanning interface.

## Before you begin

You must create an [[parameter-input-screen|input form screen]] before you create inputs. For information about creating an input form screen, see [[parameter-screen-config|Configure an input form screen]].

Role required: admin

## About this task

Barcode inputs are available [[mobile-offline-mode|offline]]. [[mobile-ui-rules|Mobile UI rules]] apply to barcode inputs.

## Procedure

1.  Navigate to **All** and enter `sys_sg_parameter_screen_list.do` in the filter.

2.  Select the input form screen to which you want to add the barcode input.

3.  Select the **Inputs** tab.

4.  Double-click **Insert a new row…** and enter the following information for your barcode input as needed.

    Double-click the fields to enter values.

    |Field|Description|
    |-----|-----------|
    |Name|Name of the input.|
    |Label|Label that displays for the input.|
    |Input Type|The type of input. Select **Barcode**.|
    |Placeholder|Text that appears in an input field before users enter values.|
    |Page|Input form screen page on which the barcode input appears.|
    |Order|Order in which the barcode input appears in the input form screen.|
    |Mandatory|Option to mark the barcode input as required.|
    |Readonly|Option to mark the barcode input as read-only.|
    |Auto-fill Variable|The auto-fill variable used for this barcode input.|

5.  Right-click the input form screen banner and select **Save** to save the barcode and stay on the form.

6.  Depending on the type of barcode scan input you want to configure.

<table id="choicetable_dwz_qrl_zvb"><thead><tr><th align="left" id="d50666e249">

Option

</th><th align="left" id="d50666e252">

Description

</th></tr></thead><tbody><tr><td id="d50666e258">

**Single scan barcode inputs**

</td><td>

When you finish configuring all the fields you want, select **Update**.

</td></tr><tr><td id="d50666e270">

**Multi-scan barcode inputs**

</td><td>

1.  Select the **Name** of the barcode input you just created to configure its attributes.
2.  Scroll down to the **Attributes** section of the form and then double-click **Insert a new row…**.
3.  Enter `MaxEntries` in the **Name** field and select the check mark to save the attribute name.
4.  Double-click the **Value** field, enter the maximum number of times a user can scan in one session, and select the check mark to save the value.
5.  When you finish configuring all the fields you want, select **Update**.


</td></tr></tbody>
</table>

## Related

- [[parameter-screen-config|Configure an input form screen]]
- [[mobile-offline-mode|Offline mode]]
- [[mobile-ui-rules|Mobile UI Rules]]
- [[parameter-input-screen|Input form screen]]
