---
title: "Form Design menu item not available"
aliases:
  - KB0550083
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550083
kb_number: KB0550083
last_modified: 2024-01-28
---

## Form Design menu item not available

  

### Issue

After upgrading to Eureka (or above) or activating the Form Designer, the respective context menu item is not visible.

Steps to reproduce:  

-   In the navigation filter, enter **incident**
-   Open any incident
-   Right-click the form header
-   Select **Personalize** (**Configure** in Fuji), and observe the list of items available in the dropdown
-   Notice that the Form Design item is not available

![Form Design missing](sys_attachment.do?sys_id=1f1ce82edb42b450e515c22305961930 "Image showing that the Form Design option is not available for selection")

### Cause

The menu item that appears when right-clicking on the form header is rendered using the **context\_form\_header** UI macro (/sys\_ui\_macro.do?sys\_id=2ff1c56ca9fe3dba014340c4697b5088).

When the instance is upgraded to Eureka (or later), it tries to update the **context\_form\_header** UI macro, adding the respective logic for this plugin to get the option: _if the plugin is active, the context menu item will appear._

When an object (such as this UI macro) is customized, this is tracked in the **Customer Updates** (sys\_update\_xml) table. To prevent customizations from being overwritten during upgrades or plugin activations, the process automatically skips changes to the objects that have a version in the **Customer Updates** table.

  

### Resolution

Revert the UI macro to the base system and lose the customizations. If there are any customizations that you want to preserve, copy the changes, and revert the **context\_form\_header** UI Macro to the base system. Merge the customizations back manually.

To revert to the base system:

1.  Navigate to **System Diagnostics > Upgrade History**.
2.  Identify the record that represents your recent upgrade (for example, Fuji), and open it.
3.  Filter the **Upgrade Details** related list by \[**File name\] \[is\] \[sys\_ui\_macro\_2ff1c56ca9fe3dba014340c4697b5088\]**
4.  Select the record.
5.  Click **Revert to Out-of-box** to overwrite the UI macro with the default version.

![Return of the Form Design option](/sys_attachment.do?sys_id=571ce82edb42b450e515c22305961965 "Image showing the Form Design option is available following the steps to resolve the issue")

  

### Related Links

**Note**: For more information about Upgrade History, see [Upgrade History module](https://docs.servicenow.com/csh?topicname=c_UpgradeHistory.html&version=latest "Upgrade History module") in the product documentation. If you are unable to identify the record or revert the UI macro, export it from a demo instance and import it into the affected instance(s).  

**Warning**: When importing a UI macro, the Customer Updates table is still tracking customizations, so there is a possibility of the issue reoccurring in future upgrades. To mitigate, see [Overwrite a customization during an upgrade](https://docs.servicenow.com/csh?topicname=t_OverwriteCustomizsDuringUpgrades.html&version=latest "Overwrite a customization during upgrade").
