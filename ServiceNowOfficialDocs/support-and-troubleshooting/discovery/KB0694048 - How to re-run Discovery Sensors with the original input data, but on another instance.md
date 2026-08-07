---
title: "How to re-run Discovery Sensors  with the original input data, but on another instance"
aliases:
  - KB0694048
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694048
kb_number: KB0694048
last_modified: 2025-01-03
---

## How to re-run Discovery Sensors with the original input data, but on another instance

  

### Issue

In order to check whether known product defects or instance customisations are breaking Discovery for a particular scanned device, it is useful to see how the data is processed by the Discovery Sensors on a more recent version or clean out-of-box instance. This also allows testing with a sub-production or temporary instance, without any impact from unexpected consequences.

This procedure lets you **re-run the Sensors** for Input data from the Discovery Probes/Patterns, but on another instance.

### Release

All

### Resolution

On the Instance on which the device has already been scanned:

1.  If the device was not scanned within the last 4-5 day, **run a Quick Discovery on the IP Address**, because the ECC Queue records may have been deleted.
2.  Open the **Discovery - Discovery Status** record that included a recent scan of the device you are interested in.
3.  **Export that** discovery\_status record as XML. Make a note of the sys\_id too.
4.  Open the ECC Queue: **Discovery - ECC Queue** 
5.  Identify the ECC Queue table records by **Filtering the list**. You will expect around 2 to 30 inputs, depending on the type of device and how many Exploration Phase probes ran.  
    Your /ecc\_queue\_list.do filter conditions will need to include:
    -   Queue = Input
    -   Source = <IP Address (that the device that was scanned on)>
    -   Agent Correlator = <the sys\_id of the Discovery Status record \[discovery\_status\] that logged the run of the Schedule/Discovery Now/Quick Discovery>
6.  **Export the filtered list as XML**. 

On your Test instance:

1.  As an **admin** user with Security Admin turned on: **Import both XML files**
2.  Open the ECC Queue: **Discovery - ECC Queue** 
3.  Use the same filter conditions as above to list the same records again.
4.  **Sort records by Created time**, with the oldest first. You would expect the first to be a **Classify** sensor, followed by an **Identify** or perhaps a **Pattern Launcher** (Kingston and later), and then various others specific to device functions and properties.
5.  In created timestamp sequence, starting with the Classify input, then Identity/first Pattern input:
    -   Open the ecc\_queue record in a form
    -   Click the **'Run again'** related link
    -   You will notice a new copy of the input has been created in the ecc\_queue, which is then processed.
6.  Once the first 2 sensors have been re-run, you can start to see log messages in the **Discovery Status record** you imported. You should also see the main CI has been created. Any errors that happen can also be seen here.
7.  Continue running the other imported inputs in sequence.
8.  You could stop once you have run the input Sensor you are particularly interested in.

### Related Links

This will fail if:

-   You try and run an input without first running the ones before it.
-   Forget to also import the Discovery Status record.

New ECC Queue outputs will be created on the test instance during this process, as would be expected when additional probes are triggered by sensors, however these will not run, and don't need to be run, because you already have the inputs from running these on the original instance. The jobs will be assigned to the MID Server from the other instance, which doesn't exist on this instance. Those outputs will simply be left in ready state until the ECC Queue is cleaned after 4-5 days automatically, so ignore them.

If you already have the CI records in the instance, or are re-running the whole process a second time, you might consider deleting the existing CI records (and their related network adapter, serial number, relationships etc.) records first to avoid those effecting how it runs.
