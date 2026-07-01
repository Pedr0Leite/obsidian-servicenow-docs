---
aliases:
  - "Dashboards"
tags:
  - knowledge-base
  - dashboards
  - update-sets
  - performance-analytics
---

# Dashboards

# How to move dashboards between instances?

## For PA Dashboards

Go to par_dashboard, find your dashboard, right click and Unload Dashboard (similar to what is being said on the “normal dashboards” KA below.

## For normal dashboards

### **Resolution**

The procedure consists of several steps each of which is comprised of several sub-steps, as follows:

**Create Source Update Set**

Log into the source instance with an account having admin rights to that instance.

Browse to the following location on that instance: **System Update Sets** -> **Local Update Sets**.

A list of update sets should appear in the frame.

Click the button titled **New** to create a new update set to be used for the purpose of transferring the Dashboard.

Fill out the New Update Set form with the following information as required:

**Name**: A descriptive name indicating the name of the Dashboard to be copied to the target instance.

**Description**: An optional field with a brief description of the purpose and objects contained in the update set.

Leave all other fields as preset.

Click the button titled **Submit and Make Current**.  This will cause this newly created update set to be the current and active update set.

[New Update Set](https://support.servicenow.com/sys_attachment.do?sys_id=238ef862db0ab450e515c22305961992)

After creating the update set, you will want to ensure not to perform any other actions other than those detailed to the end of this section in order to ensure unnecessary objects are not added to the update set.

Type the following in the Filter Navigator and press the **Enter** key.

***pa_dashboards.list***

A list of dashboards on the instance should appear.  Filter the list to locate the Dashboard you intend to move from this instance to another instance (i.e. Incident Counts).

Click the Contextual menu in the upper left corner of the dashboard record display (this menu is often called the Hamburger menu).

From the pop-up menu that appear, select the option titled **Unload Dashboard**.

This will trigger functionality to add the Dashboard and the directly related objects to be added to the current update set (which, in this case is the update set created in the steps above).

This may take a few moments, and when the operation is complete, a series of system messages will probably appear in the frame.

[Unload Dashboard](https://support.servicenow.com/sys_attachment.do?sys_id=278ef862db0ab450e515c22305961997)

Browse to the following location on the same instance: **System Update Sets** -> **Local Update Sets**.

Using the filter, locate the update set that was created in the previous steps and select it to open it.

Change the **State** field of the update set to show **Complete**.

Right click on the grey header at the top of this Update Set record and select **Save** from the pop-up menu that appears.

The update set should contain a number of objects corresponding to the objects which comprise the unloaded dashboard.

[Objects contained in Dashboard Update Set](https://support.servicenow.com/sys_attachment.do?sys_id=e78ef862db0ab450e515c2230596199c)

**Transfer Update Set to Target Instance**

After the update set has been created, the next set of steps is to transfer the update set to the target instance.  There are two standard methods which can be performed to transfer the update set, which are described here:

**Method 1 - Transfer Directly from Instance to Instance**

This method will consist of transferring the update set directly through the instance interface.  It will require that an Update Source exists on the Target instance which corresponds to the Source instance on which the Update Set was created.

To perform the transfer of the Update Set file to the target instance, perform these steps:

Log into the Target instance with an account having admin rights to that instance.

Browse to the following location on that instance: **System Update Sets** -> **Update Sources**.

Locate the name of the Update Source corresponding to the source instance of the Dashboard and the recently created update set.  Click this Update Source to open the record.

In the Related Links section of the record, click the link titled **Retrieve Completed Update Sets**.  Any new, complete update sets which have not previously been loaded to this target instance will be imported onto this instance, including the update set created in the steps above.

[Related Links](https://support.servicenow.com/sys_attachment.do?sys_id=bb8ef862db0ab450e515c223059619a1)

**Method 2 - Transfer via XML File**

This method consists of exporting the Update Set as an XML file from the source instance and then re-importing the XML file on the target instance.

The following steps briefly describe this procedure:

Ensure you are logged into the source instance with an account having admin rights to the instance.

Browse to the following location on the instance **System Update Sets** -> **Local Update Sets**.

A list of Update Sets will appear.  Locate the Update Set which contains the Dashboard you want to transfer which was created in the steps above and open this Update Set record for viewing.

Under the Related Links for this Update Set record, click the option titled **Export to XML**.

This will cause the system to download this Update Set, as an XML file to your local machine.

Log into the Target instance with an account having admin rights to that instance.

Browse to the following location on that instance: **System Update Sets** -> **Retrieved Update Sets**.

At the bottom of the list of Retrieved Update set records, click the link titled **Import Update Set from XML**.

[Import Update Set from XML](https://support.servicenow.com/sys_attachment.do?sys_id=7f8ef862db0ab450e515c223059619a6)

At the Import XML form that appears, click the **Choose File** button.

Using the File Browser window that appears, browse to and select the exported XML file from the steps above.

Once returned to the Import XML form, click the **Upload** button.

The file should upload and after a moment the list view of Retrieved Update Sets should reload, now containing the new update set.

[Imported Update Set](https://support.servicenow.com/sys_attachment.do?sys_id=338ef862db0ab450e515c223059619ac)

**Preview and Commit Update Set**

The third and final steps are to Preview and Commit the Update Set.

The steps to do this are no different than any other standard update set:

Ensure you are logged into the target instance with an account having admin rights to the instance.

Browse to the following location on the instance: **System Update Sets** -> **Retrieved Update Sets**.

A list of update sets retrieved on this instance will appear.  Locate the new update set in the list and click the record to open it for viewing.

The record will appear.  Click the **Preview Update Set** button.

The system will then preview the update set.  This process may take a few moments.

[Preview Update Set](https://support.servicenow.com/sys_attachment.do?sys_id=f38ef862db0ab450e515c223059619b1)

As with any other update set, a list of conflicts and errors may appear in the **Update Set Preview Problems** related list.  Using the normal procedure, review each of the conflicts and determine how to proceed with each object in the set.  As a general rule, since you are attempting to create an exact copy of that same dashboard from another instance, you will probably want to select "Accept remote update" for the majority of any conflicts detected.

Once all the conflicts have been resolved, click the button titled **Commit Update Set**.

[Commit Update Set](https://support.servicenow.com/sys_attachment.do?sys_id=b78ef862db0ab450e515c223059619b6)

Click the **OK** button if a dialog box that appears.

After a few moments, the update set should complete.

Browse to the following location on the same instance: **System Update Sets** -> **Local Update Sets**.

In the list of Update Sets found in the list, locate the Update Set you had imported and click the update set to open it for editing.

Change the State field to show as **Ignore**.

Click the **Update** button.

The new Dashboard has been imported into the instance.  For best results, before viewing the Dashboard, log out and back into the instance before verifying the Dashboard loaded correctly.

## Related

- [[Knowledge Base Articles]]
- [[Plataform Analytics – Metrics]]
- [[Knowledge Base Articles – Metrics]]
- [[Update sets - Full Applications]]